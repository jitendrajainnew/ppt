import { useQuery } from '@tanstack/react-query';
import { useAuthStore } from '@/store/authStore';
import { fetchGoals } from '@/services/goals';

export function useGoals() {
  const user = useAuthStore((s) => s.user);

  return useQuery({
    queryKey: ['goals', user?.id],
    queryFn: () => fetchGoals(user!.id),
    enabled: !!user?.id,
  });
}
