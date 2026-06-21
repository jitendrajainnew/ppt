# Auto-OEM Company Scorecards — one rubric, every company

> Built from the **real 10-year P&L + ratios** in `FINANCIALS-10Y.md` and the source JSON
> (`research-pipeline/data/financials/{MARUTI,M&M,EICHERMOT,TMPV}.json`). Scores are analyst
> judgment shown *with the evidence*. ⚠️ Cross-check vs annual reports before real use.
> [S: Screener.in structured tables, ~June 2026]. Not investment advice.

## The rubric (weights) — derived from `four-wheelers.md` Module 11  [CORE]

Module 11's six PV-OEM criteria (Scale 20 / Mix 20 / Cost-margin 15 / Distribution 15 / EV-readiness 20 /
Capital 10) are **re-cast here for a cross-cycle, financials-first scoring** of four listed names. Scale +
distribution + brand collapse into one **Franchise / market position** factor; **Margin/ROCE through the
cycle** is split out as the headline (the 10-yr data is the strongest signal); EV-transition stays
over-weighted per the archetype; mix is kept as its own premiumisation factor.

| Factor | Weight | "5/5" |
|---|---|---|
| **Franchise / market position** | 25% | Scale-leader share + deep distribution + durable brand moat |
| **Margin / ROCE through the cycle** | 20% | High *and stable* ROCE/OPM; holds up at the trough |
| **EV-transition readiness** | 20% | Credible, funded EV platform + product already selling at scale |
| **Capital allocation** | 15% | Capex into the profit-pool/EV, no value-destructive M&A, deleveraging |
| **Balance sheet** | 10% | Net cash / low leverage; self-funds the EV capex |
| **Premiumisation / mix** | 10% | Rich SUV/premium/hybrid mix; pricing power |
| **Total** | **100%** | |

**Scale:** 1 red flag · 3 average · 5 best-in-class.

## Real 10-yr financials — extracted from the source JSON [S]  [CORE]
> ₹ cr. FY26 = TTM/est. [S: Screener.in structured tables, ~June 2026]. ⚠️ Verify vs filings.

| Company | Sales FY25 | OPM% FY15→FY25 | ROCE FY18 / FY22 / FY25 | Net Profit FY18 / FY22 / FY25 | Balance sheet |
|---|---|---|---|---|---|
| **Maruti** | 152,913 | 14% → 13% (flat) | 24% / **6%** / 22% | 7,881 / **3,880** / 14,500 | **Net cash** |
| **M&M** | 159,211 | 12% → **19%** (rising) | 13% / 11% / 14% | 7,958 / 7,253 / 14,073 | Modest leverage, strong |
| **Eicher (RE)** | 18,870 | 13%* → **25%** (premium) | **49%** / 17% / 30% | 1,667 / 1,347 / 4,734 | **Net cash, debt-free** |
| **Tata Motors (TMPV)** | 439,695 | 15% → 13% (JLR) | 9% / **1%** / 20% | 9,091 / **−11,309** / 28,149 | Deleveraged (was levered) |

\* Eicher FY15 spans the Dec-2014 fiscal transition; clean RE-era OPM band is **25–31%** (FY17 on).
**Tata Motors (TMPV)** = full Tata Motors group incl. JLR through the FY2025 demerger — a JLR-driven cycle,
not an India-PV-only series.

## Factor detail — read from the 10-yr data  [CORE]

### Franchise / market position (25%)
- **Maruti → 5.** ~40% PV share, unmatched dealer + service + rural reach, largest PV exporter, net cash.
  The deepest *scale* moat in Indian autos. **[H]**
- **M&M → 4.** SUV-pure franchise (Thar/Scorpio-N/XUV) + high-return farm-equipment leadership; strong but
  narrower than Maruti's mass-market scale. **[H]**
- **Eicher (RE) → 4.** Royal Enfield is a genuine premium-brand moat (mid-size motorcycles), but it is a
  *two-wheeler* franchise adjacent to the 4W set — narrow category, niche scale. **[M]**
- **Tata Motors (TMPV) → 4.** #1 India EV-PV + JLR global-premium + scale (₹4.4 lakh-cr group revenue), but
  thinner/volatile India-PV margins and a complex multi-business group. **[M]**

### Margin / ROCE through the cycle (20%) — *the 10-yr headline*
- **Eicher → 5.** ROCE **49–53% (FY17–19)**, never below 17% even at the FY22 trough, ~30–31% now; OPM
  25–31% ≈ 2× mass-market. Highest *and most stable* returns in the set. **[H]**
- **M&M → 4.** OPM **12%→19% (+7pts, monotonic)**, ROCE 7%(FY20)→15%(ttm) with no down-years since the
  FY20 loss — *rising* returns, the premiumisation thesis in the P&L. **[H]**
- **Maruti → 3.** Textbook cyclical: ROCE **24%→6%(FY22)→22%**, OPM flat 14%→13% — never re-rated despite
  ~12% sales CAGR; classic price-taker. **[H]**
- **Tata Motors (TMPV) → 3.** Violent swing: ROCE 9%→**1%(FY22)**→20%(FY25)→3%(ttm, demerger-distorted);
  net profit **−₹28,724cr (FY19)** through a 4-yr loss streak to +₹31,807cr (FY24). Highest beta, lowest
  stability. **[H]**

### EV-transition readiness (20%) — *over-weighted per archetype*
- **Tata Motors (TMPV) → 5.** **#1 India EV-PV** (Nexon/Punch/Curvv EV), dedicated EV architecture, Agratas
  backward cell integration — clearest EV lead among listed names. **[H]**
- **M&M → 4.** Born-electric INGLO/BE platform launching on its strongest (SUV) segment. **[M]**
- **Maruti → 3.** **First BEV (eVX) arrived late**; hedged into hybrid/CNG — the hybrid bridge buys time but
  is not an EV lead. Its single clearest structural vulnerability. **[M]**
- **Eicher (RE) → 3.** RE electric motorcycle (Flying Flea) is nascent; premium-ICE brand exposed to 2W
  electrification long-term. **[M]**

### Capital allocation (15%)
- **Eicher → 4.** Disciplined, debt-free, capex into RE capacity; rising payout (~41%). **[H]**
- **M&M → 4.** Went solo on SUVs (good), funded farm + EV from cash; SsangYong was the past sin, since
  exited. **[M]**
- **Maruti → 4.** Funded scale + hybrid + EV from net cash, no value-destructive M&A; EV-launch *timing* is
  the only critique. **[M]**
- **Tata Motors (TMPV) → 3.** JLR (2008) *eventually* created value and became the cash engine, but the path
  ran through huge write-downs (FY19) and a 4-yr loss streak; **deleveraging is real** (interest ₹8,097cr
  FY21 → ₹2,827cr ttm) — improving, but volatile track record. **[M]**

### Balance sheet (10%)
- **Maruti → 5** (net cash) · **Eicher → 5** (net cash, debt-free) · **M&M → 4** (modest leverage, strong)
  · **Tata Motors (TMPV) → 3** (materially deleveraged but historically levered; group complexity). **[H]**

### Premiumisation / mix (10%)
- **M&M → 5** (SUV-pure, richest mix) · **Eicher → 5** (pure premium) · **Tata Motors → 4** (JLR luxury +
  Nexon SUV) · **Maruti → 3** (catching up via Brezza/Grand Vitara/Fronx + hybrid). **[H]**

## Scores (computed on the real 10-yr data)  [CORE]

| Rank | Company | Franchise (25) | Margin/ROCE (20) | EV-ready (20) | Cap-Alloc (15) | Bal. Sheet (10) | Mix (10) | **Weighted /5** |
|---|---|---|---|---|---|---|---|---|
| **1** | **Eicher (RE)** | 4 | 5 | 3 | 4 | 5 | 5 | **4.20** |
| **2** | **M&M** | 4 | 4 | 4 | 4 | 4 | 5 | **4.10** |
| **3** | **Maruti Suzuki** | 5 | 3 | 3 | 4 | 5 | 3 | **3.85** |
| **4** | **Tata Motors (TMPV)** | 4 | 3 | 5 | 3 | 3 | 4 | **3.75** |

*Weighted = Σ(score × weight). E.g. M&M = 4(.25)+4(.20)+4(.20)+4(.15)+4(.10)+5(.10) = **4.10**.*

## What the real data CHANGED (vs the illustrative Module-12 ranking)  [CORE]

1. **Eicher tops on cross-cycle returns, not scale.** Once **Margin/ROCE through the cycle** is weighted at
   20% on real data, Eicher's **30–53% ROCE / 25–31% OPM** moat outranks Maruti's flat 13% OPM. The
   illustrative `four-wheelers.md` table (Maruti & M&M tie at 3.85) didn't include Eicher; the financials
   put the premium-brand moat first. **[H]**
2. **M&M is the compounder, confirmed.** **OPM 12%→19% (+7pts) + ROCE 7%→15% with no down-years + ~6× profit
   off the FY20 trough** = the decade's standout four-wheeler. Edges into #2 on rising-margin evidence. **[H]**
3. **Maruti is great-but-cyclical, not a compounder.** ROCE **24%→6%→22%** and flat OPM = buy-at-trough, not
   own-through-cycle. Franchise (5) is unmatched; the margin line (3) is the honest ceiling. **[H]**
4. **Tata Motors (TMPV) earns the EV-ready 5 *and* the volatility 3.** Including it (per the brief) adds the
   listed EV-PV leader the old `FINANCIALS-10Y.md` flagged as missing — but its **−₹28,724cr → +₹82,645cr**
   swing and ROCE 1%→20%→3% make it the **highest-beta turnaround**, not a stability pick. FY26ttm ROCE 3%
   / OPM 6% are **demerger-distorted** (₹86,113cr other income) — FY24–25 ROCE ~20% is the clean read. **[M]**

## Re-grade triggers  [CORE]
- **Maruti eVX/EV success at scale** → EV-readiness 3→4 → score → ~4.05 (challenges M&M for #2).
- **Tata Motors clean post-demerger series settling near FY24–25 ROCE ~20%** → Margin 3→4 + Bal-sheet 3→4 →
  score → ~4.05.
- **M&M sustains 19% OPM + EV traction through a down-cycle** → Margin 4→5 → score → ~4.30 (takes #1).
- **Eicher RE-electric flop or premium-2W EV disruption** → EV-readiness 3→2 → score → ~4.00.
