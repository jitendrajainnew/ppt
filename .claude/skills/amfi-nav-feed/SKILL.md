---
name: amfi-nav-feed
description: AMFI NAV data feed parsing and management. Use when implementing
  NAV display, scheme search, return calculations, or NAV caching.
---

# AMFI NAV Feed

## Data Source
- URL: https://www.amfiindia.com/spages/NAVAll.txt
- Updated daily by 11:30 PM IST
- Format: Semicolon-separated text
- Fields: Scheme Code;ISIN Div Payout;ISIN Growth;Scheme Name;NAV;Date

## Parsing Rules
- Lines without semicolons = fund house headers (use as category)
- Empty NAV = scheme closed/suspended
- NAV precision: 4 decimal places (float)
- Date format in feed: DD-Mon-YYYY → convert to ISO

## Caching Strategy
- Supabase cron job at 11:45 PM IST daily
- Table: nav_daily (scheme_code, isin, scheme_name, nav, nav_date, fund_house)
- Keep 1 year history for return calculations
- Client app reads from Supabase, NOT from AMFI directly
- Fallback: if cron fails, Edge Function can fetch on-demand

## Scheme Search
- Search by: scheme name (fuzzy), AMFI code, ISIN
- Show: Fund house | Scheme name | Category | Latest NAV | 1Y return
- Cache scheme master list (changes rarely)
