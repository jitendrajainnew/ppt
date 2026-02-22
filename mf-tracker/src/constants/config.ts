export const SUPABASE_URL = process.env.EXPO_PUBLIC_SUPABASE_URL ?? '';
export const SUPABASE_ANON_KEY = process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY ?? '';

export const AMFI_NAV_URL = 'https://www.amfiindia.com/spages/NAVAll.txt';

export const SIP_DATES = Array.from({ length: 28 }, (_, i) => i + 1);

export const GOAL_TYPES = [
  'child_education',
  'retirement',
  'house',
  'car',
  'emergency_fund',
  'wealth_creation',
  'custom',
] as const;

export const TRANSACTION_TYPES = {
  P: 'Purchase',
  R: 'Redemption',
  SI: 'SIP',
  SW: 'Switch',
} as const;

export const FUND_CATEGORIES = [
  'Equity',
  'Debt',
  'Hybrid',
  'Solution Oriented',
  'Other',
] as const;
