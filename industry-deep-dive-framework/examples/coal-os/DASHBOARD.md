# Coal Industry Dashboard — Live KPIs

> The "is the report alive?" asset. Each metric: current reading + direction + source + date.
> **Refresh monthly.** Status as of ~June 2026 research sprint. ⚠️ Verify vs primary before use.
> Cells tagged **[verify]** are live market reads that must be refreshed against primary sources
> (Ministry of Coal / CEA / seaborne benchmarks) before any real use. **Not investment advice.**

## A. Industry cycle "tell" metrics (the auction-premium / power-demand cycle)

| KPI | Current reading | Direction | What it signals | Source |
|---|---|---|---|---|
| **CIL e-auction premium** (over notified) | **Moderating off the 2022 spike, still a premium** [verify] | ↓ normalising | The cyclical margin lever — easing from peak | CIL/MSTC notifications [verify, ~2026] |
| **Seaborne thermal (Newcastle / API)** | **Off 2022 highs, above pre-2020 base** [verify] | → / ↓ | Import-parity ceiling lower | Newcastle/API2 benchmark [verify] |
| **Seaborne coking (prime hard)** | **Volatile, cyclically elevated** [verify] | → | Coking-import cost / steel margins | Platts/seaborne [verify] |
| **India power demand growth** | **~6–8% YoY** [verify] | ↑ | Underlying thermal demand strong | CEA / Grid-India [verify, ~2026] |
| **Thermal PLF** | **~68–72%, recovering off ~55–58% lows** [verify] | ↑ | Baseload still needed despite RE adds | CEA [verify] |
| **Coal stock-days at power plants** | **~normalising (~15–25 days)** [verify] | ↑ easing | <7 = crisis tightness; normalising = supply caught up | CEA daily coal-stock report [verify] |
| **CIL production (MT, FY)** | **~770–800 Mt/yr toward ~1bn-t target** [verify] | ↑ | Scale / volume base | Ministry of Coal / CIL [verify] |
| **CIL offtake (MT, FY)** | **≈ production, low stock build** [verify] | → | Offtake ≈ production = healthy dispatch | CIL monthly [verify] |
| **CIL dividend yield** | **~6–8%** [verify] | → | Cash return — among large-cap highest | Screener / market price [verify] |

> *Reading it:* this is **not a GDP-driven cyclical** — domestic demand is near-baseload. What moves
> the names is the **e-auction premium + dividend + policy/transition headlines**. Trade the
> auction-premium / yield / policy cycle, not the offtake line. **[H]**

## B. The two structural swing variables (where the terminal-value debate lives)

| KPI | Current reading | Direction | Source |
|---|---|---|---|
| **Coal share of India power generation** | **~70–75%** [verify] | → (slow decline) | CEA [verify, ~2026] |
| **India coal consumption** | **~1.1–1.2 bn t/yr, rising ~5–7%** [verify] | ↑ | Ministry of Coal / IEA [verify] |
| **Coking-coal import dependence** | **~85%+ imported** [verify] | → | Import-substitution runway intact | Ministry of Coal [verify] |
| **Commercial-mining ramp (post-2020 auctions)** | **Private output ramping off a low base** [verify] | ↑ | Adds national supply / erodes CIL share | Ministry of Coal auction data [verify] |
| **Net-zero / NDC RE glide path** | **Net-zero-2070 ceiling; RE+storage cost the swing** [verify] | structural risk | The long-dated terminal-value input | Govt NDC / IEA [verify] |

## C. Company KPI table — from the REAL 10-year financials [S: Screener.in structured tables, ~June 2026]

> Hard numbers below are from the structured P&L/ratios JSON (`research-pipeline/data/financials/`),
> **not** live cells — no [verify] tag needed. ⚠️ Third-party tables; cross-check vs filings.

| Company | OPM% FY24 (peak) | OPM% FY26ttm | ROCE% FY24 | ROCE% FY26ttm | Net profit FY24 (₹cr) | Net profit FY26ttm (₹cr) | Payout% FY26ttm | Read |
|---|---|---|---|---|---|---|---|---|
| **Coal India** | **33%** | **24%** | **64%** | **35%** | **37,369** | **31,071** | **53%** | Cash machine **softening** off the top |
| **NLC India** | 26% | 32% | 7% | 10% | 1,868 | 3,769 | 15% | Lower-return lignite+power hybrid; profit improving |
| **NTPC** | 29% | 28% | 10% | 8% | 21,332 | 27,546 | 32% | Steady regulated utility, compounding quietly |

**The headline tell — Coal India's franchise-monopoly returns and the FY25→FY26ttm crack:**

| Coal India | FY15 | FY18 (trough) | FY19 (peak) | FY23 | FY24 (peak NP) | FY25 | FY26ttm |
|---|---|---|---|---|---|---|---|
| **ROCE %** | 52 | 45 | **107** | 78 | 64 | **48** | **35** |
| **OPM %** | 23 | 11 | 25 | 32 | 33 | 33 | **24** |
| **Net profit (₹cr)** | 13,727 | 7,038 | 17,464 | 31,723 | **37,369** | 35,302 | 31,071 |
| **Payout %** | 95 | 146 | 46 | 47 | 42 | 46 | 53 |

> *Reading it:* Coal India ran **ROCE 35–107% for a decade** — franchise-monopoly, not utility,
> returns on a low-capex, near-net-cash base. **But FY25→FY26ttm is the first real crack:** ROCE
> **48%→35%**, OPM **33%→24%**, net profit **35,302→31,071cr**. That is exactly the melting-ice-cube
> *shape* the bears predicted. Early, possibly cyclical (e-auction premia, wage revision) — but
> **directionally the terminal-decline signature, now "watch closely."** **[M]**
>
> NTPC is the bond-like anchor — **ROCE pinned ~8–11% every year FY15–26**, profit compounding
> ₹9,992cr→₹27,546cr. NLC is the lower-return outlier — **ROCE ~7–13%**, lumpy (FY16 net profit
> collapsed to ₹68cr on tax) — *not a Coal India proxy.* **[H]**

## What to watch next month
1. **CIL e-auction premium** at each MSTC notification — re-accelerating or compressing toward zero?
2. **CEA plant coal-stock-days + thermal PLF** — tightness easing or re-tightening?
3. **India power-demand growth** — still ~6–8%, or any sign of back-to-back declines (falsification)?
4. **CIL FY26 full-year ROCE/OPM print** — does the 48%→35% / 33%→24% rollover deepen or stabilise?
5. **Dividend declaration / payout guidance** (CIL) — maintained, or the first cut?
6. Commercial-mining output ramp + any cess/carbon-levy budget move (policy event-driven).

---
*Sources: hard financials [S: Screener.in structured tables, ~June 2026]; live cells [verify] vs
Ministry of Coal / CEA / Grid-India / seaborne benchmarks. **Not investment advice** — do your own
due diligence.*
