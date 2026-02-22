import { useQuery } from '@tanstack/react-query';
import { useAuthStore } from '@/store/authStore';
import { fetchSIPs } from '@/services/sips';

export function useSIPs() {
  const user = useAuthStore((s) => s.user);

  return useQuery({
    queryKey: ['sips', user?.id],
    queryFn: () => fetchSIPs(user!.id),
    enabled: !!user?.id,
  });
}
