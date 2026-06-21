# Insurance Company Scorecards — one rubric, every company (split LIFE vs GENERAL/HEALTH)

> Derived from the **Module 11 weighted rubric** in `examples/insurance.md`, scored on **FY25
> primary metrics** (web-sourced VNB margin / RoEV / persistency / solvency for life; combined
> ratio / loss ratio / solvency for general-health). ⚠️ Cross-check vs IRDAI / annual reports
> before real use. Not investment advice.

## ⛔ The metric that drives every score — and the one we REFUSE to use

**OPM% and ROCE are the WRONG inputs and we do not score on them.** Per `FINANCIALS-10Y.md`, an
insurer's ROCE "declining 41%→7%" is a balance-sheet artifact, not decay; OPM ≈ 1% is gross-premium
accounting. **The primary scoring input is VNB margin (life) / combined ratio (general-health)** —
the actual profit engines. Anyone who ranked these names on the ROCE table would reach the *exact
wrong* conclusion. **[H]**

## The rubric (Module 11 weights)

| # | Factor | Weight | Primary metric | "5/5" |
|---|---|---|---|---|
| C1 | **Underwriting discipline** | 25% | **VNB margin** (life) / **combined ratio** (gen-health) | VNB margin high-20s%+ / combined ratio <100% |
| C2 | **Distribution moat** | 20% | Banca / agency / digital reach + cost | Captive bank channel or dominant agency at low cost |
| C3 | **Persistency / retention** | 15% | 13th / 61st-month persistency, renewals | 13m ~87%+, 61m ~60%+ |
| C4 | **Solvency / balance sheet** | 15% | Solvency ratio, float quality | >200%, conservative liability-matched book |
| C5 | **Growth runway** | 15% | Segment penetration, product mix | Long under-penetration runway, margin-rich mix |
| C6 | **Management / float quality** | 10% | Capital allocation, ALM, EV/VNB compounding | Disciplined float deployment, RoEV mid-teens+ |
| | **Total** | **100%** | | |
**Scale:** 1 red flag · 3 average · 5 best-in-class. **Good = underwriting discipline + distribution moat + high persistency + strong solvency + long runway + quality float.**

---

## SUB-SEGMENT 1 — LIFE (scored on VNB margin / RoEV / persistency / solvency)

### FY25 primary inputs [S]

| Company | VNB margin | RoEV | Persistency 13m / 61m | Solvency | EV (₹cr) | Distribution |
|---|---|---|---|---|---|---|
| **HDFC Life** | 26.1% | 16.0% | **87% / 61%** | 188% | 53,246 (+18%) | HDFC Bank banca + agency + Exide |
| **SBI Life** | **27.8%** | **20.2%** | 86.6% / 61.5% | 196% | 70,250 (+21%) | **SBI branch network (captive bank)** |
| **ICICI Pru Life** | 22.8% | 13.1% | 85.1% / ~55% | **212.2%** | ~47,000 [verify] | ICICI Bank + multi-channel |
| **LIC** | 17.6% | ~11.4% | 74.8% / [verify] | 211% | ~8,13,200 | **Dominant agent army (~60%+ share)** |

**Sources:** [S: HDFC Life FY25 press release/investor presentation; SBI Life Q4FY25 (Groww/Business Standard); ICICI Pru Life Q4FY25 (Business Standard/icra); LIC FY25 press release 27-May-2025 & ICICI Sec note], ~Jan–Jun 2025. PAT/premium scale anchors from `{HDFCLIFE,ICICIPRULI,LICI}.json`. `SBILIFE.json` was empty.

### Life scores

| Rank | Company | C1 Underwriting (VNB margin) 25 | C2 Distribution 20 | C3 Persistency 15 | C4 Solvency 15 | C5 Runway 15 | C6 Mgmt/Float 10 | **Weighted /5** |
|---|---|---|---|---|---|---|---|---|
| **1** | **SBI Life** | 5 | 5 | 4 | 4 | 4 | 5 | **4.55** |
| **2** | **HDFC Life** | 4 | 5 | 5 | 4 | 4 | 4 | **4.35** |
| **3** | **ICICI Pru Life** | 3 | 4 | 4 | 5 | 4 | 4 | **3.90** |
| **4** | **LIC** | 2 | 5 | 2 | 4 | 5 | 3 | **3.45** |

**Score rationale (evidence → interpretation):**
- **SBI Life #1 [M]:** highest VNB margin (27.8%) → C1=5; captive SBI branch reach → C2=5; best RoEV (20.2%) → C6=5. *The VNB-margin + bank-distribution leader.* Ceiling: solvency (196%) trails ICICI Pru; 13m persistency just behind HDFC.
- **HDFC Life #2 [M]:** best persistency (87%/61%) → C3=5; HDFC Bank banca + Exide agency → C2=5; VNB margin 26.1% strong but below SBI → C1=4. *Balanced-mix compounder with the stickiest book.*
- **ICICI Pru Life #3 [M]:** VNB margin 22.8% is the **FY25 miss** (stock -10% on the print) → C1=3; fortress solvency 212.2% → C4=5; RoEV 13.1% lags → C6=4. *Cheapest of the privates for a reason — margin recovery is the swing.*
- **LIC #4 [M]:** lowest VNB margin (17.6%) → C1=2; weakest persistency (74.8% 13m) → C3=2; but unmatched scale/runway + agent army → C5=5, C2=5. *Scale ≠ quality: dominant share, sub-par new-business economics, policy-exposed.*

---

## SUB-SEGMENT 2 — GENERAL / HEALTH (scored on COMBINED RATIO / loss ratio / solvency)

> ⚠️ **Do NOT compare these scores cross-segment to the life table** — different rubric inputs
> (combined ratio replaces VNB margin in C1; no VNB/RoEV). Rank only *within* sub-segment.

### FY25 primary inputs [S]

| Company | Combined ratio | Loss ratio | Solvency | RoE | Segment |
|---|---|---|---|---|---|
| **ICICI Lombard** | **103.8%** | ~70% [verify] | **269%** | 19.1% | Multi-line general |
| **Star Health** | 101.1% (97.3% FY24 ↑) | 69.8% (65.0%→66.5%→69.8%) | 221% | teens [verify] | Standalone retail health |

**Sources:** [S: ICICI Lombard FY25 Annual Report & Q4FY25 press release; Star Health FY25 results / earnings call & loss-ratio series], ~Apr–Oct 2025. ⚠️ `ICICIGI.json` & `STARHEALTH.json` **empty** in Screener — no JSON scale anchor; the missing combined ratio *is* the lesson.

### General/Health scores

| Rank | Company | C1 Underwriting (combined ratio) 25 | C2 Distribution 20 | C3 Retention 15 | C4 Solvency 15 | C5 Runway 15 | C6 Mgmt/Float 10 | **Weighted /5** |
|---|---|---|---|---|---|---|---|---|
| **1** | **ICICI Lombard** | 4 | 4 | 3 | 5 | 4 | 4 | **3.95** |
| **2** | **Star Health** | 3 | 4 | 3 | 4 | 5 | 3 | **3.55** |

**Score rationale (evidence → interpretation):**
- **ICICI Lombard #1 [M]:** combined ratio 103.8% — disciplined for a multi-line general book → C1=4; fortress solvency 269% → C4=5; RoE 19.1% rising → C6=4. *The general-underwriting + capital benchmark; profit despite >100% CR via float income.*
- **Star Health #2 [M]:** combined ratio **deteriorating 97.3%→101.1%**, loss ratio climbing 65%→69.8% as claims inflation outruns repricing → C1=3, C6=3; but best-in-segment retail-health runway + pricing power → C5=5. *Structural volume + pricing power vs the live claims-inflation test; PAT fell ₹1,103cr→₹787cr.*

---

## ⚠️ What scoring on the RIGHT metrics CHANGED (vs an OPM/ROCE screen)

1. **LIC ranks LAST in life despite the biggest PAT (₹48,320cr) and ROCE swings to 131%.** On VNB
   margin (17.6%, lowest) + persistency (74.8%, weakest), it is the *quality laggard*. An OPM/ROCE
   screen would have crowned it. **[H]**
2. **ICICI Pru Life screens cheap-for-a-reason, not cheap-and-good.** Its FY25 VNB-margin miss
   (22.8%, stock -10%) — invisible in PAT (which *recovered* to ₹1,186cr) — drops C1 to 3. **[H]**
3. **SBI Life edges HDFC Life on VNB margin + RoEV**, not on profit scale. The margin/return lens,
   not the P&L, separates #1 from #2. **[M]**
4. **Both general/health names "look profitable" on PAT but run combined ratios >100%** — i.e. they
   *lose* on underwriting and are rescued by float income. Star Health's worsening CR (the metric
   absent from its empty JSON) is the real signal, not its positive PAT. **[H]**

## Re-grade triggers
- **SBI Life / HDFC Life VNB margin compression** (price war) → C1 down → could flip the #1/#2 order.
- **ICICI Pru VNB-margin recovery** above ~25% → C1 3→4 → score → ~4.10, closes gap to HDFC.
- **Star Health combined ratio back <100%** (repricing catches claims inflation) → C1 3→4 → score → ~3.80.
- **LIC persistency / non-par-mix improvement** lifting VNB margin → C1/C3 up from a low base.
