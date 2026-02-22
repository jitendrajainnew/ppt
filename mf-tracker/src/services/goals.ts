import { supabase } from './supabase';
import type { Goal } from '@/types/goals';

export async function fetchGoals(clientId: string): Promise<Goal[]> {
  const { data, error } = await supabase
    .from('goals')
    .select('*')
    .eq('client_id', clientId)
    .order('target_date', { ascending: true });

  if (error) throw new Error(error.message);
  return data ?? [];
}

export async function createGoal(
  goal: Omit<Goal, 'id' | 'created_at' | 'current_value'>
): Promise<Goal> {
  const { data, error } = await supabase
    .from('goals')
    .insert({ ...goal, current_value: 0 })
    .select()
    .single();

  if (error) throw new Error(error.message);
  return data;
}
