# Insurance — 10-Year Financials (clean, structured) — ⚠️ A CAUTIONARY EXAMPLE

> Pulled by `research-pipeline/scripts/financials.py` from **Screener's structured P&L + Ratios
> tables**. FY15→FY26ttm. ₹ crore. **[S: Screener.in structured tables, ~June 2026].**
> ⚠️ Verify vs filings/IRDAI before real use.

## ⛔ READ THIS FIRST — the standard P&L is the WRONG LENS for insurers

**Conventional Screener metrics — OPM%, ROCE, even Net Profit — largely MISLEAD for insurance.**
An insurer's "Sales" line is gross premium, and its "Expenses" line bundles claims, reserve
changes, and actuarial movements. The result: the standard P&L compresses or distorts the
economics that actually matter. Treat every table below as **scale/trajectory context only**, not
as a quality verdict.

| If you read… | …you'll wrongly conclude | The economics actually live in |
|---|---|---|
| **OPM% ≈ 0–3% (life)** | "terrible margins" | **VNB margin** (new-business value ÷ APE; protection-led ~26%+) |
| **ROCE declining (HDFC Life 41%→7%)** | "returns collapsing" | **EV / RoEV** (embedded value compounding mid-teens) |
| **Net Profit flat / lumpy** | "no growth" | EV growth + **persistency** (13m ~85%+, 61m ~55–65%) + **solvency >150%** |
| **General/health P&L profit** | "underwriting is fine" | **Combined ratio** (loss + expense; <100% = paid to hold float) + solvency |

➡️ **For the right framework see `examples/insurance.md` §5b "Industry Metrics Cheat Sheet."**
The life book is read on **VNB margin / EV / RoEV / persistency / solvency**; general & health on
**combined ratio + solvency**. None of these appear in a standard Screener P&L.

---

## Net Profit (₹ cr) — PAT trajectory & scale (what the P&L CAN show)

| Net Profit | FY15 | FY18 | FY20 | FY22 | FY24 | **FY25** | FY26ttm |
|---|---|---|---|---|---|---|---|
| **HDFC Life** (life) | 786 | 1,107 | 1,297 | 1,327 | 1,574 | **1,811** | 1,912 |
| **ICICI Pru Life** (life) | 1,640 | 1,619 | 1,067 | 759 | 851 | **1,186** | 1,608 |
| **LIC** (life) | – | – | 2,710 | 4,125 | 40,916 | **48,320** | 57,453 |

- **HDFC Life = steady compounder:** PAT ₹786cr (FY15) → ₹1,811cr (FY25), ~8–9%/yr, never a down
  year — the cleanest series here. Even so, *PAT understates value creation*: the EV/VNB engine
  compounds faster than reported profit. **[H]**
- **ICICI Pru's PAT actually fell** FY15→FY22 (₹1,640→₹759cr) — but this is the classic trap: the
  dip reflects ULIP/product-mix and accounting, **not** a deteriorating franchise. You'd need VNB
  margin + EV to judge it. PAT recovered to ₹1,608cr (FY26ttm). **[H]**
- **LIC = scale on a different planet:** PAT leapt ₹2,710cr (FY20) → ₹48,320cr (FY25) — a step-change
  driven by the **pre-IPO surplus-distribution / single-fund restructuring (2021–22)**, NOT organic
  margin expansion. A textbook case of why insurer PAT must be read against EV, not in isolation. **[H]**

## "Sales" = Gross Premium (₹ cr) — growth & scale

| Premium ("Sales") | FY15 | FY20 | FY25 | 10-yr CAGR (FY15→25) |
|---|---|---|---|---|
| **HDFC Life** | 27,215 | 29,380 | 92,922 | **~13%** |
| **ICICI Pru Life** | 34,453 | 21,025 | 70,778 | **~7.5%** |
| **LIC** | – | 628,043* | 889,970 | **~7.7%** (FY19→25) |

\* LIC series begins FY19 (₹571,508cr). LIC's premium base alone (~₹0.9 lakh cr) dwarfs the entire
private cohort — scale is real, but scale ≠ profitability without VNB/EV. The "Sales" line is gross
premium, **not** a revenue-quality measure: ULIP/savings premium scales fast at thin margin.

## ROCE % — shown ONLY to demonstrate why it misleads

| ROCE % | FY15 | FY18 | FY20 | FY22 | FY24 | **FY25** | FY26ttm |
|---|---|---|---|---|---|---|---|
| **HDFC Life** | 41 | 31 | 24 | 12 | 5 | **7** | 10 |
| **ICICI Pru Life** | 34 | 29 | 17 | 9 | 3 | **12** | 10 |
| **LIC** | – | – | 5 | 131† | 73 | **53** | 35 |

† LIC's ROCE swings (5% → 131% → 53%) are **artifacts of the surplus-distribution restructuring**,
not capital efficiency. **Do not rank insurers on this row.** A "declining ROCE" for HDFC Life/ICICI
Pru reflects the growing in-force balance sheet and product mix — the *opposite* of decay when EV is
compounding. ROCE is a manufacturing/asset-turn metric; it has no clean meaning for a float business.

## ⚠️ Data gaps in this pull
- **SBI Life** — `SBILIFE.json` returned **empty** (no P&L/ratios). Major omission; sourced separately.
- **ICICI Lombard** (`ICICIGI.json`) — **empty** in this pull. General insurer: read on **combined ratio**.
- **Star Health** (`STARHEALTH.json`) — **empty** in this pull. Retail health: read on **combined ratio**
  (target <100%) + solvency. Its absence here is *itself* the lesson: the general/health names'
  decisive metric (combined ratio) was never in the Screener P&L to begin with.

---

## Conclusion — this note is a cautionary example, not a scorecard

The P&L data above genuinely shows two things and **only** two things: (1) **scale** — HDFC Life and
ICICI Pru as mid-sized private compounders, LIC as a category of its own; and (2) **PAT trajectory** —
HDFC Life's steady ₹786cr→₹1,811cr compounding vs ICICI Pru's accounting-driven dip-and-recover vs
LIC's restructuring-driven step jump. Everything else a generic screen would "tell" you — that life
insurers have ~0% margins and collapsing ROCE — is an **artifact of applying manufacturing metrics to
a float/actuarial business.**

**The right lens (per `examples/insurance.md` §5b):**
- **Life** (HDFC Life, ICICI Pru, LIC): **VNB margin, Embedded Value, RoEV, persistency (13m/61m),
  solvency** — none visible in a standard P&L.
- **General / health** (ICICI Lombard, Star Health): **combined ratio (loss + expense, <100%) +
  solvency** — also absent here.

The takeaway transcends insurance: **reading the right industry-specific metrics matters more than a
generic ROCE/OPM screen.** An analyst who ranked these names on the ROCE table above would reach the
exact wrong conclusion. Tie every number here back to the VNB/EV/combined-ratio framework in
`insurance.md` before forming any view.

---

*Disclaimer: Educational illustration of a research workflow. Figures are from Screener.in structured
tables (~June 2026) and may differ from audited filings/IRDAI disclosures; several source files were
empty (see gaps). **Not investment advice.** Source JSON: `research-pipeline/data/financials/<TICKER>.json`.*
