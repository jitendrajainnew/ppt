export type TransactionType = 'P' | 'R' | 'SI' | 'SW';

export interface Transaction {
  id: string;
  client_id: string;
  scheme_code: string;
  type: TransactionType;
  amount: number;
  units: number;
  nav: number;
  date: string;
}
