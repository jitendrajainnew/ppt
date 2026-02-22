import { GOAL_TYPES } from '@/constants/config';

export type GoalType = (typeof GOAL_TYPES)[number];

export interface Goal {
  id: string;
  client_id: string;
  name: string;
  type: GoalType;
  target_amount: number;
  target_date: string;
  current_value: number;
  linked_sip_ids: string[];
  created_at: string;
}

export interface GoalProjection {
  futureValue: number;
  monthlySIPNeeded: number;
  progressPct: number;
  yearsRemaining: number;
  inflationAdjustedTarget: number;
}
