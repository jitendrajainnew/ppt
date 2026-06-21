# Worked Examples — Industry Deep Dive Library

Completed deep dives built with the framework (see `../README.md`, `../TEMPLATE.md`).
Each runs the full v1.0 spine end-to-end: **Decision Summary → Research Question → … →
Research Log**, with the 5 quality layers, archetype weighting, CORE/APPENDIX split,
confidence tags [H/M/L], and the v1.0 modules (5c Red Flag Checklist, 12b Management &
Capital-Allocation Timeline, 17b Source Quality Table — present in reports built after the v1.0 freeze).

> ⚠️ **All figures in every example are ILLUSTRATIVE / directional** (to show the *shape* of a
> completed deep dive). Refresh against primary sources before any real use. **Not investment advice.**

## The library, by archetype

| Report | Archetype proven | Anchor company (scored end-to-end) | What it stress-tests |
|---|---|---|---|
| [`pharma.md`](pharma.md) | Regulated × Technology | Sun Pharma | Regulation + science + patents + compliance (hardest industry) |
| [`semiconductors.md`](semiconductors.md) | Technology × Cyclical | TSMC | Innovation/product cycles, foundry oligopoly, capital cycle |
| [`solar.md`](solar.md) | Technology × Infrastructure × Regulated | Waaree | Value-chain margin migration, commoditisation |
| [`four-wheelers.md`](four-wheelers.md) | Consumer/Cyclical × Technology | Maruti Suzuki | Demand cycle + EV-disruption moat erosion |
| [`coal.md`](coal.md) | Commodity/Cyclical × Regulated | Coal India | Cost curve, ESG/terminal-decline vs cash-cow |
| [`reits.md`](reits.md) | Infrastructure × Regulated | Embassy | Yield instrument, NAV, rate sensitivity |
| [`insurance.md`](insurance.md) | Regulated × Financials (Float) | HDFC Life | Float economics, combined ratio, VNB/EV |
| [`exchanges.md`](exchanges.md) | **Network/Platform** × Regulated | BSE | Liquidity network effects, winner-take-most, take-rate |
| [`invits.md`](invits.md) | Infrastructure × Regulated (yield) | IndiGrid | Concession-asset yield, accretive-acquisition spread |
| [`holding-companies.md`](holding-companies.md) | Capital-Allocation / Special-Situation | Bajaj Holdings | **Holdco discount** — framework flexing on a non-standard category |
| [`steel.md`](steel.md) | Commodity/Cyclical × Capital-intensive | JSW Steel | The capital-cycle classic — cost curve, China, leverage |

## From report → operating system

`pharma.md` is the **encyclopedia**; [`pharma-os/`](pharma-os/) is what the OS *generates* from
it — a **live-sourced** (deep-research, ~June 2026) set of working assets:
- [`pharma-os/DASHBOARD.md`](pharma-os/DASHBOARD.md) — live KPIs (IPM growth, US erosion, FDA status, GLP-1, CDMO)
- [`pharma-os/COMPANY-SCORECARDS.md`](pharma-os/COMPANY-SCORECARDS.md) — 6 companies scored on one rubric, ranked, with FY25 evidence
- [`pharma-os/QUESTION-BANK.md`](pharma-os/QUESTION-BANK.md) — the unanswered question per module (Q→Evidence→Answer)
- [`pharma-os/INVESTMENT-MEMO.md`](pharma-os/INVESTMENT-MEMO.md) — 1-page IC summary + the 4 variant views (the alpha)

This is the difference between an *industry study* and an *investment process*: the report is the
map; the OS is the live thesis generated from it.

**Every Indian-listed industry now has an `<industry>-os/` folder with real 10-year financials**
pulled by the pipeline (`../research-pipeline/scripts/financials.py`) from Screener's structured
tables — `FINANCIALS-10Y.md` in each:

| OS folder | Real-data highlight (10-yr) |
|---|---|
| `pharma-os/` | Full OS (dashboard, scorecards, question bank, memo) + Sun FY18 ROCE trough 32%→10% |
| `steel-os/` | The capital cycle laid bare — Tata Steel −₹4,169cr→+₹41,749cr→−₹4,910cr |
| `exchanges-os/` | Toll-road thesis proven — IEX OPM ~84%, ROCE 50-61%; CDSL/CAMS 40-56% |
| `coal-os/` | Coal India ROCE 35-107% cash machine + the recent softening (bear's first evidence) |
| `four-wheelers-os/` | Cyclical Maruti (ROCE 24%→6%→24%) vs compounders M&M/Eicher |
| `solar-os/` | Manufacturing up-cycle (Waaree ROCE 16%→39%) vs IPP leverage (Adani Green ROCE ~8%) |
| `holding-companies-os/` | Holdco discount in data — Bajaj Holdings profit ₹2,029→₹9,789cr, ROCE understated |
| `invits-os/` | Yield-instrument signature — IndiGrid OPM ~90%, ROCE ~8%; PGInvIT GAAP swings |
| `insurance-os/` | Cautionary: OPM/ROCE are the *wrong* lens (use VNB/EV/combined ratio) |

In each case the **real long-run data either validated or sharpened the report's thesis** — the
point of reading the source, not summarising it.

## Archetype coverage

✅ Technology · ✅ Commodity/Cyclical · ✅ Regulated · ✅ Infrastructure · ✅ Network/Platform
· ✅ plus hybrids and the non-standard **Capital-Allocation/Special-Situation** (holdcos).

The framework architecture has held across all of these **without structural change** — which
is the real proof it generalises. The bottleneck now is *data completeness* in each report
(every figure is illustrative until refreshed from primary sources), not the framework.

## How to read one

Start at the **Decision Summary (IC page)** — if a PM reads one page, it's that. Then the
**Research Question** frames the investigation; the CORE modules carry the argument; the
APPENDIX (dashboards, graveyard, scoring tables, research log) holds the evidence.

## How to build a new one

1. Copy `../TEMPLATE.md` → `<industry>.md`.
2. Tag the **archetype** (`../ARCHETYPES.md`) — it sets module weighting + mandatory deliverables.
3. Work top to bottom; keep the CORE narrative tight (~15–20 pp), push machinery to APPENDIX.
4. Grade against `../CHECKLIST.md` (Gate 0 layers → Gate 1 modules → Gate 2 craft) before calling it done.
