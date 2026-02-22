---
name: mfu-bse-star
description: MFU and BSE Star API integration for mutual fund transactions.
  Use when implementing portfolio data, transactions, SIP registration,
  or any MFU/BSE Star API interaction.
---

# MFU / BSE Star Integration

## MFU (Mutual Fund Utilities)
- Unified platform for MF transactions across all AMCs
- Uses CAN (Common Account Number) for client identification
- MFD authenticates with ARN number + EUIN
- Base URL: https://www.mfuonline.com/api/
- Auth: Token-based, refresh every 24 hours

## Key Endpoints
- /portfolio — client holdings with current value
- /transactions — transaction history
- /sip — active SIP list with dates and amounts
- /cart — place new transactions

## BSE Star MF
- BSE's mutual fund transaction platform
- Uses Client ID + Member ID for authentication
- Requires L1 (order entry) and L2 (payment) steps
- Supports: order placement, SIP registration, mandate management

## Implementation Rules
- ALL API calls through Supabase Edge Functions (never from client app)
- Store API credentials in Supabase Vault/secrets
- Map MFU/BSE scheme codes to AMFI codes for NAV matching
- Transaction types: P (Purchase), R (Redemption), SI (SIP), SW (Switch)
- Validate: amount >= minimum investment, SIP date (1-28 only)
- Log every API call for SEBI audit trail
- Handle token expiry with auto-refresh + retry

## Data Mapping
- MFU scheme code → AMFI scheme code (use mapping table)
- CAN → internal client_id in Supabase
- BSE client code → internal client_id
