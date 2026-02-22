export type AlertType = 'nav_above' | 'nav_below' | 'return_target' | 'sip_reminder';

export interface Alert {
  id: string;
  client_id: string;
  type: AlertType;
  scheme_code: string | null;
  threshold: number | null;
  is_active: boolean;
  created_at: string;
}
