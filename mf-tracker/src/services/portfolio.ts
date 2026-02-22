import { supabase } from './supabase';
import type { Portfolio, PortfolioWithScheme } from '@/types/portfolio';

export async function fetchPortfolio(clientId: string): Promise<PortfolioWithScheme[]> {
  const { data: holdings, error } = await supabase
    .from('portfolios')
    .select(`
      *,
      scheme:scheme_master(*)
    `)
    .eq('client_id', clientId);

  if (error) throw new Error(error.message);
  if (!holdings) return [];

  // Get latest NAVs for all scheme codes
  const schemeCodes = holdings.map((h: Portfolio) => h.scheme_code);
  const { data: navData } = await supabase
    .from('nav_daily')
    .select('scheme_code, nav')
    .in('scheme_code', schemeCodes)
    .order('nav_date', { ascending: false });

  const latestNavMap = new Map<string, number>();
  navData?.forEach((n: { scheme_code: string; nav: number }) => {
    if (!latestNavMap.has(n.scheme_code)) {
      latestNavMap.set(n.scheme_code, n.nav);
    }
  });

  return holdings.map((h: Portfolio & { scheme: PortfolioWithScheme['scheme'] }) => {
    const currentNav = latestNavMap.get(h.scheme_code) ?? h.avg_nav;
    const currentValue = Math.round(h.units * currentNav * 100);
    const returnsAbsolute = currentValue - h.invested_amount;
    const returnsPct =
      h.invested_amount > 0
        ? ((currentValue - h.invested_amount) / h.invested_amount) * 100
        : 0;

    return {
      ...h,
      current_nav: currentNav,
      current_value: currentValue,
      returns_absolute: returnsAbsolute,
      returns_pct: returnsPct,
    };
  });
}

export async function fetchPortfolioSummary(clientId: string) {
  const holdings = await fetchPortfolio(clientId);

  const totalInvested = holdings.reduce((sum, h) => sum + h.invested_amount, 0);
  const totalCurrent = holdings.reduce((sum, h) => sum + h.current_value, 0);
  const totalReturns = totalCurrent - totalInvested;
  const returnsPct = totalInvested > 0 ? (totalReturns / totalInvested) * 100 : 0;

  return {
    holdings,
    totalInvested,
    totalCurrent,
    totalReturns,
    returnsPct,
    holdingsCount: holdings.length,
  };
}
