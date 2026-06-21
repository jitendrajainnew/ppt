# Exchanges Company Scorecards — one rubric, every company

> Built from the **REAL 10-year financials** (`FINANCIALS-10Y.md` + the source
> `research-pipeline/data/financials/<TICKER>.json`, [S: Screener.in structured tables, ~June 2026])
> and the qualitative moat / policy reads in `../exchanges.md` (Module 11 rubric, Module 9
> policy-exposure scorecard). Scores are analyst judgment shown *with the evidence*.
> ⚠️ Cross-check vs annual reports before real use. **Not investment advice.**

## The rubric (weights) — derived from `exchanges.md` Module 11

| Factor | Weight | "5/5" looks like |
|---|---|---|
| **Moat / network durability** | 25% | Dominant, permanent liquidity/folio share; near-impossible entry; *stable* margin |
| **Take-rate resilience** | 20% | Per-unit toll holds vs SEBI/CERC; pricing power on a sticky base |
| **Regulatory risk** (5 = least exposed) | 20% | Low policy exposure; not a single-circular-away from a take-rate cut |
| **Market share %** (and trend) | 15% | #1 in its product, share rising or impregnable |
| **Operating leverage** | 10% | Fixed-cost rail; high incremental margin; mix to annuity/data |
| **Balance sheet / capital allocation** | 10% | Net cash, zero debt, disciplined high payout |
| **Total** | **100%** | |

**Scale:** 1 red flag · 3 average · 5 best-in-class. Note the **deliberate tension**: the company
with the *best* margins (IEX) carries the *worst* regulatory risk — so the weighted score, not any
single cell, decides the rank.

---

## The REAL numbers each score is grounded in  [CORE]
*₹ crore; [S: Screener.in, ~June 2026]; FY26 = TTM/est.*

| Company | OPM% (10-yr) | OPM% FY25→26t | ROCE% (10-yr) | ROCE FY25→26t | Sales FY25→26t | NP FY25→26t | Debt / payout |
|---|---|---|---|---|---|---|---|
| **IEX** | 79–84% | 84% → 84% | 50–61% | 53% → 51% | 537 → 616 | 429 → 493 | ~nil / ~62% |
| **CDSL** | 40–66% | 58% → 51% | 14→42 | 42% → **32%** ↓ | 1,082 → 1,145 | 526 → **455** ↓ | nil / ~50% |
| **CAMS** | 37–47% | 46% → 45% | 38–56% | 54% → 49% | 1,422 → 1,516 | 465 → 472 | min / ~76% |
| **BSE** | 21–64% | 58% → **64%** | 5→58 | 47% → **58%** | 3,212 → 4,834 | 1,322 → **2,487** | ~nil / ~16% |
| **MCX** | 9–71% | 60% → **71%** | 7→71 | 43% → **71%** | 1,113 → 2,302 | 560 → **1,332** | nil / ~15% |

---

## Scores (computed on the real data + Module 9/11 reads)

| Rank | Company | Moat (25) | Take-rate (20) | Reg-risk (20) | Share (15) | Op-lev (10) | Bal-sheet (10) | **Weighted /5** |
|---|---|---|---|---|---|---|---|---|
| **1** | **CDSL** | 5 | 4 | 4 | 5 | 4 | 5 | **4.50** |
| **2** | **IEX** | 5 | 4 | **2** | 5 | 5 | 5 | **4.20** |
| **3** | **CAMS** | 4 | 4 | 4 | 4 | 3 | 5 | **4.00** |
| **4** | **MCX** | 4 | 3 | 4 | 5 | 4 | 4 | **3.95** |
| **5** | **BSE** | 3 | 4 | 3 | 4 | 5 | 4 | **3.65** |

> **Weighted = 0.25·Moat + 0.20·Take-rate + 0.20·Reg-risk + 0.15·Share + 0.10·Op-lev + 0.10·Bal-sheet.**
> The order is **CDSL (4.50) > IEX (4.20) > CAMS (4.00) > MCX (3.95) > BSE (3.65)**. Note the deliberate
> tension: **IEX has the best margins in the set (84% OPM) but reg-risk 2 (CERC market coupling)** keeps it
> behind the quality-annuity CDSL — the strongest single cell does not win the rubric.

---

## Per-company reasoning — grounded in the 10-yr data

### CDSL — 4.50 · the quality compounder, with a fresh cyclicality flag  [H]
- **Moat 5 / Share 5:** retail-demat **near-monopoly** (one of a CDSL/NSDL duopoly, ~75%+ of accounts),
  per-account annuity with near-zero marginal cost. Switching cost = the installed folio base.
- **The real-data tell:** sales compounded **~26% over 10y (105→1,082cr)**, OPM expanded 43%→58% (peaked
  66% in FY22), ROCE re-rated **14%→42%** — textbook operating leverage on a fixed-cost rail, zero interest.
- **Take-rate 4 / Reg-risk 4:** depository fee caps are a *low–med* lever (Module 9 policy score 5);
  least F&O-policy-exposed of the set. **But** FY26ttm is the warning: **net profit FELL 526→455 and
  ROCE slipped 42%→32%** on softer capital-market volumes + fee pressure — the annuity is real, the
  *traffic* is sentiment-cyclical. Op-lev held at 4 (not 5) for exactly this.
- **Bal-sheet 5:** zero debt, 50–58% payout. **Verdict: highest-quality annuity in the set; the FY26 dip
  is cyclical, not structural — but it caps the score below a perfect 5.**

### CAMS — 4.00 · the steadiest demand driver (AUM-linked, not trade-linked)  [H]
- **Moat 4 / Share 4:** RTA duopoly (with KFin) servicing ~two-thirds of Indian MF AUM — an entrenched,
  switching-cost-heavy back office earning a basis-point toll on a *structurally rising* AUM pool.
- **Real-data tell:** ROCE held **38–56%** across FY19–26 (54% FY25); OPM rose 37%→46–47%; sales
  659→1,516cr with profit 146→472cr — the **least dramatic** series in the universe.
- **Op-lev 3:** lower than the pure exchanges — more people-/operations-intensive (OPM 45–47% vs IEX 84%).
- **Take-rate 4 / Reg-risk 4 / Bal-sheet 5:** AUM-linked revenue is the steadiest driver; minimal debt;
  payout 65–76% (FY25). **Verdict: the "picks-and-shovels" compounder — arguably the most durable *demand*,
  even if margins sit below the pure exchanges.**

### IEX — 4.20 · best margins in India, single live regulatory threat  [H]
- **Moat 5 / Share 5 / Op-lev 5:** ~90%+ monopoly in short-term power exchange; the matching engine is
  built once and scaled at ~zero marginal cost. **OPM 84% held flat FIVE straight years (FY22→FY26ttm)**,
  ROCE 50–61% — the **highest and most STABLE margin in the set**; sales 254→616cr while expenses crept
  only 51→96cr. The cleanest proof of the toll-road thesis.
- **Reg-risk 2 — the deliberate penalty:** **CERC market coupling** is a live, IEX-specific thesis-killer
  that can redistribute share and compress the take rate (Module 9 policy score 2, the worst in the set).
  This single cell is why the strongest-margin company is *not* ranked #1.
- **Take-rate 4 / Bal-sheet 5:** per-unit fee resilient so far; ~nil debt, ~62% payout. **Verdict: own the
  margin, respect the single-product/single-regulator concentration — the fattest toll-road carries the
  thinnest diversification.**

### MCX — 3.95 · recovering commodity monopoly, highest beta  [M]
- **Moat 4 / Share 5:** ~90%+ near-monopoly in commodity derivatives.
- **Real-data tell — operating leverage BOTH ways:** FY24 was a one-off **tech-platform (TCS) migration**
  trough — OPM cratered to **9%, ROCE 7%, NP ₹83cr** (expenses 514→621cr on flat sales) — then snapped to
  **60→71% OPM, 43→71% ROCE, NP 560→1,332cr** once the new platform went live and options volume arrived.
- **Take-rate 3:** commodity options mix still maturing; per-contract toll less proven than equities.
- **Reg-risk 4 / Bal-sheet 4:** commodity product/position limits are a *med* lever; nil debt.
  **Verdict: the cleanest recovery story, but the FY24 trough is the standing reminder that the same
  fixed-cost rail works violently in reverse.**

### BSE — 3.65 · best re-rate, highest policy exposure  [M]
- **Op-lev 5 / Take-rate 4 / Share 4:** the **violent operating-leverage upside** is the whole story —
  ROCE swung **5% (FY20) → 47% (FY25) → 58% (ttm)** and OPM 21%→64% as Sensex/Bankex weekly options gave
  BSE a *separate* liquidity pool NSE didn't own; **NP 121→1,322→2,487cr**; index-options premium share
  mid-teens% and rising. Owns CDSL + ICCL (more of the stack).
- **Moat 3 — capped:** still the #2 venue in NSE's liquidity shadow; the moat is real only in the
  *adjacent* contract it invented, not in NSE's Nifty franchise.
- **Reg-risk 3 — the swing both ways:** **highest F&O-curb / expiry / charge-cap exposure** (Module 9
  score 3). SEBI's one-weekly-expiry rule *helped* BSE — policy giveth and taketh.
- **Bal-sheet 4:** ~nil debt, but payout cut to ~16% as it reinvests/retains through the re-rate.
  **Verdict: the best growth/re-rate and the highest beta to a single SEBI circular — a cyclical/
  special-situation, not a buy-and-forget compounder.**

---

## What the REAL data CHANGED vs the illustrative `exchanges.md` ranking
1. **CDSL clearly #1 on the real numbers** (4.50) — 26% 10-yr sales CAGR, ROCE 14→42%, zero debt — but the
   **FY26ttm profit fall (526→455) and ROCE slip (42→32%)** is a genuine, freshly-printed cyclicality flag
   that the illustrative table didn't carry. Quality annuity, sentiment-cyclical traffic. **[H]**
2. **IEX is the margin king but the rank-capped name** — 84% OPM × 5 years is unmatched, yet CERC market
   coupling (reg-risk 2) keeps it behind the duopoly compounders on weighted score. The strongest cell
   does not win the rubric. **[H]**
3. **BSE/MCX upside is now *proven in the P&L*, not just narrative** — BSE NP nearly doubled, MCX 6-7×ed
   off the FY24 trough — confirming the "violent operating leverage" thesis with hard numbers, while the
   MCX FY24 trough proves the downside is equally real. **[M]**

## Re-grade triggers
- **CDSL** FY27 net-profit / ROCE re-acceleration (volumes recover) → op-lev 4→5 → score → ~4.60.
- **IEX** CERC market-coupling order *clarified favourably* → reg-risk 2→3/4 → score → ~4.30–4.50 (could top the table).
- **BSE** sustained index-options share gain + resumed payout → moat 3→4 / bal-sheet 4→5 → score → ~3.95.
- **MCX** options-volume durability over 4+ quarters → take-rate 3→4 → score → ~4.05.
- Any **hard transaction-charge cap** → take-rate 4→2 across BSE/MCX/IEX (sector-wide de-rate).
