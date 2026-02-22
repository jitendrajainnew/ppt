import { supabase } from './supabase';
import type { SIP } from '@/types/sip';

export async function fetchSIPs(clientId: string): Promise<SIP[]> {
  const { data, error } = await supabase
    .from('sips')
    .select(`
      *,
      scheme:scheme_master(name, fund_house)
    `)
    .eq('client_id', clientId)
    .order('sip_date', { ascending: true });

  if (error) throw new Error(error.message);

  return (data ?? []).map((sip: SIP & { scheme?: { name: string; fund_house: string } }) => ({
    ...sip,
    scheme_name: sip.scheme?.name,
    fund_house: sip.scheme?.fund_house,
  }));
}

export async function fetchActiveSIPCount(clientId: string): Promise<number> {
  const { count, error } = await supabase
    .from('sips')
    .select('*', { count: 'exact', head: true })
    .eq('client_id', clientId)
    .eq('status', 'active');

  if (error) throw new Error(error.message);
  return count ?? 0;
}
