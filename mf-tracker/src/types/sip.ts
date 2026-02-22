export type SIPStatus = 'active' | 'paused' | 'completed' | 'cancelled';

export interface SIP {
  id: string;
  client_id: string;
  scheme_code: string;
  amount: number;
  frequency: 'monthly' | 'quarterly';
  sip_date: number;
  status: SIPStatus;
  start_date: string;
  end_date: string | null;
  next_date: string | null;
  scheme_name?: string;
  fund_house?: string;
}
