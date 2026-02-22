---
name: indian-finance-calculations
description: Indian mutual fund financial calculations. Use when implementing
  return calculations (XIRR, CAGR, absolute), goal planning, portfolio
  analytics, or Indian number formatting.
---

# Indian MF Financial Calculations

## Return Calculations

### XIRR (for SIPs and irregular cashflows)
- Newton-Raphson method with max 100 iterations
- Cashflows: negative for investments, positive for current value
- Include current portfolio value as final positive cashflow (today's date)
- If NR doesn't converge → bisection method fallback
- Edge cases: single transaction, same-day transactions, zero cashflow

### Absolute Return
- Formula: (Current Value - Invested) / Invested × 100
- Use for: lumpsum investments < 1 year old

### CAGR
- Formula: (Current / Invested) ^ (1/years) - 1
- Use for: lumpsum investments > 1 year old
- NOT suitable for SIPs — use XIRR

## Indian Number Formatting
- Lakh/crore system: ₹1,23,45,678.00
- Regex pattern: /(\d)(?=(\d\d)+\d\.)/g → "$1,"
- Abbreviations: ₹1.5L (lakh = 1,00,000), ₹2.3Cr (crore = 1,00,00,000)
- Negative returns: red color, positive: green

## Goal Planning
- Education inflation: 10-12% per year (India)
- General inflation: 6-7%
- Equity expected return: 12% CAGR (conservative projection)
- Debt expected return: 7% CAGR
- Required SIP = FV × r / ((1+r)^n - 1), r = monthly return rate
- Show: current cost → future cost → monthly SIP needed

## Data Types
- Amounts: stored in paise (integer), display in ₹ (2 decimals)
- NAV: float with 4 decimal places
- Units: float with 3 decimal places
- Returns %: float with 2 decimal places
