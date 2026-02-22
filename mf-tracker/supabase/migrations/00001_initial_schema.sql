-- MF Tracker Initial Schema
-- All client data tables have RLS enabled

-- Clients table
CREATE TABLE IF NOT EXISTS clients (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  phone TEXT NOT NULL UNIQUE,
  name TEXT,
  pan_masked TEXT,
  can_number TEXT,
  created_at TIMESTAMPTZ DEFAULT now()
);

ALTER TABLE clients ENABLE ROW LEVEL SECURITY;
CREATE POLICY "clients_own_data" ON clients
  FOR ALL USING (id = auth.uid());

-- Scheme master (public data, no RLS needed)
CREATE TABLE IF NOT EXISTS scheme_master (
  scheme_code TEXT PRIMARY KEY,
  isin TEXT,
  name TEXT NOT NULL,
  fund_house TEXT NOT NULL,
  category TEXT NOT NULL,
  sub_category TEXT
);

-- NAV daily data (public data, no RLS needed)
CREATE TABLE IF NOT EXISTS nav_daily (
  scheme_code TEXT NOT NULL REFERENCES scheme_master(scheme_code),
  nav NUMERIC(12,4) NOT NULL,
  nav_date DATE NOT NULL,
  PRIMARY KEY (scheme_code, nav_date)
);

CREATE INDEX idx_nav_daily_lookup ON nav_daily (scheme_code, nav_date DESC);

-- Portfolios
CREATE TABLE IF NOT EXISTS portfolios (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  client_id UUID NOT NULL REFERENCES clients(id),
  scheme_code TEXT NOT NULL REFERENCES scheme_master(scheme_code),
  units NUMERIC(15,3) NOT NULL DEFAULT 0,
  avg_nav NUMERIC(12,4) NOT NULL DEFAULT 0,
  invested_amount BIGINT NOT NULL DEFAULT 0,
  UNIQUE (client_id, scheme_code)
);

ALTER TABLE portfolios ENABLE ROW LEVEL SECURITY;
CREATE POLICY "portfolios_own_data" ON portfolios
  FOR ALL USING (client_id = auth.uid());

-- Transactions
CREATE TABLE IF NOT EXISTS transactions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  client_id UUID NOT NULL REFERENCES clients(id),
  scheme_code TEXT NOT NULL REFERENCES scheme_master(scheme_code),
  type TEXT NOT NULL CHECK (type IN ('P', 'R', 'SI', 'SW')),
  amount BIGINT NOT NULL,
  units NUMERIC(15,3) NOT NULL,
  nav NUMERIC(12,4) NOT NULL,
  date DATE NOT NULL
);

ALTER TABLE transactions ENABLE ROW LEVEL SECURITY;
CREATE POLICY "transactions_own_data" ON transactions
  FOR ALL USING (client_id = auth.uid());

CREATE INDEX idx_transactions_client_date ON transactions (client_id, date DESC);

-- SIPs
CREATE TABLE IF NOT EXISTS sips (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  client_id UUID NOT NULL REFERENCES clients(id),
  scheme_code TEXT NOT NULL REFERENCES scheme_master(scheme_code),
  amount BIGINT NOT NULL,
  frequency TEXT NOT NULL DEFAULT 'monthly' CHECK (frequency IN ('monthly', 'quarterly')),
  sip_date INTEGER NOT NULL CHECK (sip_date BETWEEN 1 AND 28),
  status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'paused', 'completed', 'cancelled')),
  start_date DATE NOT NULL,
  end_date DATE,
  next_date DATE
);

ALTER TABLE sips ENABLE ROW LEVEL SECURITY;
CREATE POLICY "sips_own_data" ON sips
  FOR ALL USING (client_id = auth.uid());

CREATE INDEX idx_sips_client_status ON sips (client_id, status);

-- Goals
CREATE TABLE IF NOT EXISTS goals (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  client_id UUID NOT NULL REFERENCES clients(id),
  name TEXT NOT NULL,
  type TEXT NOT NULL CHECK (type IN ('child_education', 'retirement', 'house', 'car', 'emergency_fund', 'wealth_creation', 'custom')),
  target_amount BIGINT NOT NULL,
  target_date DATE NOT NULL,
  current_value BIGINT NOT NULL DEFAULT 0,
  linked_sip_ids UUID[] DEFAULT '{}',
  created_at TIMESTAMPTZ DEFAULT now()
);

ALTER TABLE goals ENABLE ROW LEVEL SECURITY;
CREATE POLICY "goals_own_data" ON goals
  FOR ALL USING (client_id = auth.uid());

-- Alerts
CREATE TABLE IF NOT EXISTS alerts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  client_id UUID NOT NULL REFERENCES clients(id),
  type TEXT NOT NULL CHECK (type IN ('nav_above', 'nav_below', 'return_target', 'sip_reminder')),
  scheme_code TEXT REFERENCES scheme_master(scheme_code),
  threshold NUMERIC(12,4),
  is_active BOOLEAN NOT NULL DEFAULT true,
  created_at TIMESTAMPTZ DEFAULT now()
);

ALTER TABLE alerts ENABLE ROW LEVEL SECURITY;
CREATE POLICY "alerts_own_data" ON alerts
  FOR ALL USING (client_id = auth.uid());
