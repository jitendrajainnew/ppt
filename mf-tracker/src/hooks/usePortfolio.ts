import { useQuery } from '@tanstack/react-query';
import { useAuthStore } from '@/store/authStore';
import { fetchPortfolioSummary } from '@/services/portfolio';

export function usePortfolio() {
  const user = useAuthStore((s) => s.user);

  return useQuery({
    queryKey: ['portfolio', user?.id],
    queryFn: () => fetchPortfolioSummary(user!.id),
    enabled: !!user?.id,
  });
}
