# Pharma — 10-Year Financials (clean, structured)

> Pulled by `research-pipeline/scripts/financials.py` from **Screener's structured P&L + Ratios
> tables** (sourced from filings) — reliable long-run series, not OCR'd PDFs. Mar-2026 = TTM/est.
> ₹ crore. [S: Screener.in, ~June 2026]. ⚠️ Verify vs filings before real use.

## ROCE % — the capital-efficiency trajectory (the headline)

| ROCE % | FY15 | FY17 | **FY18** | FY20 | FY22 | FY24 | **FY25** | FY26ttm |
|---|---|---|---|---|---|---|---|---|
| **Sun** | 23 | 20 | **10** | 10 | 17 | 17 | **20** | 21 |
| **Cipla** | 15 | 7 | 9 | 12 | 17 | 23 | **23** | 15* |
| **Divi's** | 33 | 29 | 22 | 25 | 35 | 16 | **20** | 22 |
| **Dr Reddy's** | 22 | 9 | 8 | 11 | 14 | 27 | **23** | 14* |
| **Mankind** | – | – | – | – | 32 | 26 | **16** | 14 |
| **Torrent** | 27 | 19 | 13 | 15 | 19 | 23 | **27** | 15* |

\* FY26ttm dips partly reflect TTM/working-capital timing and recent debt-funded M&A.

## Net Profit (₹ cr) — the cycle in profits

| Net Profit | FY15 | **FY17** | **FY18** | FY21 | FY23 | FY24 | **FY25** |
|---|---|---|---|---|---|---|---|
| **Sun** | 5,476 | **7,846** | **2,542** | 2,272 | 8,513 | 9,610 | **10,965** |
| **Cipla** | 1,229 | 1,035 | 1,417 | 2,389 | 2,833 | 4,154 | **5,269** |
| **Divi's** | 852 | 1,060 | 877 | 1,984 | 1,823 | 1,600 | **2,191** |
| **Dr Reddy's** | 2,336 | 1,292 | **947** | 1,952 | 4,507 | 5,578 | **5,725** |
| **Mankind** | 445 | – | – | 1,293 | 1,310 | 1,942 | **2,011** |
| **Torrent** | 751 | 934 | 678 | 1,252 | 1,245 | 1,656 | **1,911** |

## Sales (₹ cr) & operating margin (FY25)

| | Sales FY25 | OPM% FY25 | Sales 10-yr CAGR (FY15→25) |
|---|---|---|---|
| **Sun** | 52,578 | 29% | ~6.7% |
| **Cipla** | 27,548 | 26% | ~9.3% |
| **Divi's** | 9,360 | 32% | ~11.6% |
| **Dr Reddy's** | 32,644 | 26% | ~8.1% |
| **Mankind** | 12,207 | 25% | ~13.9% (FY15 base small) |
| **Torrent** | 11,516 | 32% | ~9.5% |

## What the long-run data reveals (and how it updates the scorecards)

1. **Sun's FY18 ROCE trough (32%→10%) is unmistakable** — the Ranbaxy + Halol + US-erosion crisis,
   profits ₹7,846cr→₹2,542cr. Recovery to 20%+ ROCE by FY25 was *built on specialty*. The whole sector
   thesis, in one company's curve. **[H]**
2. **Cipla = the steady compounder** — ROCE 7% (FY17) → 23% (FY24-25), profit 4×'d FY17→FY25 with
   *rising* margins. Reinforces its #1 rubric rank (quality + consistency, not a single good year). **[H]**
3. **Divi's runs the highest structural ROCE (29-35% pre-COVID)**, dipped to 16% (FY24) on a capex +
   post-COVID-API unwind, now recovering (20-22%). → its capital-allocation score is *understated* if you
   only look at FY24; the franchise earns 30%+ in good years. **Upgrade conviction. [H]**
4. **Mankind's ROCE is in visible DECLINE — 37% (FY21) → 16% (FY25) → 14% (TTM)** — the BSV (₹13,768cr)
   debt-funded deal is dragging returns. This *confirms* the capital-allocation red flag the rubric flagged
   (Mankind cap-alloc 3 / balance-sheet 3). **The data validates the concern. [H]**
5. **Dr Reddy's & Torrent are the cyclicals** — ROCE swung 8% (FY18) → 27% (FY23-24); great when the US
   cycle is up, exposed when it turns. Buy-at-trough names, not steady compounders.

## Cross-check vs the rubric (COMPANY-SCORECARDS.md)
- **Cipla #1 (4.40)** — validated: best *consistency* of ROCE improvement + pristine compliance.
- **Sun #2 (4.30)** — validated: the FY18 scar explains the compliance caution; specialty drives the recovery.
- **Divi's #3 (4.20)** — arguably *light*; the 30%+ historical ROCE + debt-free balance sheet support a higher cap-alloc score once CDMO capacity absorbs.
- **Mankind #6 (3.65)** — validated by the declining-ROCE trend; watch BSV payback.

*Source JSON: `research-pipeline/data/financials/<TICKER>.json` (full 12-year P&L + ratios).*
