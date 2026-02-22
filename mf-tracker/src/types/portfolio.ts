import { SchemeMaster } from './scheme';

export interface Portfolio {
  id: string;
  client_id: string;
  scheme_code: string;
  units: number;
  avg_nav: number;
  invested_amount: number;
}

export interface PortfolioWithScheme extends Portfolio {
  scheme: SchemeMaster;
  current_nav: number;
  current_value: number;
  returns_absolute: number;
  returns_pct: number;
}
