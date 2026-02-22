export interface SchemeMaster {
  scheme_code: string;
  isin: string | null;
  name: string;
  fund_house: string;
  category: string;
  sub_category: string | null;
}

export interface NAVDaily {
  scheme_code: string;
  nav: number;
  nav_date: string;
}
