---
name: mf-tracker-schema
description: Database schema knowledge for the MF tracker app. Use when
  creating tables, writing queries, or implementing RLS policies.
---

# MF Tracker Database Schema

## Core Tables
- clients (id, phone, name, pan_masked, can_number, created_at)
- portfolios (id, client_id, scheme_code, units, avg_nav, invested_amount)
- transactions (id, client_id, scheme_code, type, amount, units, nav, date)
- sips (id, client_id, scheme_code, amount, frequency, sip_date, status)
- goals (id, client_id, name, type, target_amount, target_date, linked_sips)
- nav_daily (scheme_code, nav, nav_date) — partitioned by month
- scheme_master (scheme_code, isin, name, fund_house, category, sub_category)
- alerts (id, client_id, type, scheme_code, threshold, is_active)

## RLS (Row Level Security) — CRITICAL
- Every table with client data: RLS enabled
- Policy: client can only see rows WHERE client_id = auth.uid()
- Service role bypasses RLS (for Edge Functions / admin)
- nav_daily and scheme_master: public read, no RLS needed

## Indexes
- portfolios: (client_id, scheme_code) unique
- transactions: (client_id, date DESC)
- nav_daily: (scheme_code, nav_date DESC)
- sips: (client_id, status)
