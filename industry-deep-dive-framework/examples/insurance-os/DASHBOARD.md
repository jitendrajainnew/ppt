# Insurance Industry Dashboard — Live KPIs

> The "is the report alive?" asset. Each metric: current reading + direction + source + date.
> **Refresh quarterly** (life: VNB/EV each result; general/health: combined ratio each result).
> Status as of ~June 2026 research sprint. ⚠️ Verify vs IRDAI / company filings before use. Not investment advice.

## ⛔ READ THIS FIRST — the RIGHT metrics, not OPM/ROCE

**Generic P&L metrics (OPM%, ROCE, Net-Profit margin) MISLEAD for insurers** — see
`FINANCIALS-10Y.md`. An insurer's "Sales" = gross premium and "Expenses" bundles claims + reserve
movements, so OPM ≈ 0–3% and "ROCE collapsing 41%→7%" are *artifacts*, not decay. The economics
live in **VNB margin / EV / RoEV / persistency / solvency** (life) and **combined ratio + solvency**
(general/health). This dashboard tracks **those**. PAT/premium below are **scale context only**. **[H]**

| Wrong lens (ignore) | Right lens — LIFE | Right lens — GENERAL/HEALTH |
|---|---|---|
| OPM% ≈ 0–3% | **VNB margin** (VNB ÷ APE) | **Combined ratio** (loss + expense; <100% = paid to hold float) |
| ROCE "declining" | **EV / RoEV** (compounding mid-teens) | **Loss ratio** + **solvency** |
| Net-Profit lumpiness | **Persistency** (13m/61m) + **solvency** | RoE anchored to combined ratio |

---

## A. Industry cycle "tell" metrics

| KPI | Current reading | Direction | What it signals | Source |
|---|---|---|---|---|
| **Life penetration** | **~3% of GDP** (non-life ~1%) vs global ~7% combined | low / runway | Multi-decade under-penetration tailwind | IRDAI / insurance.md §1 [verify] |
| **Private-life VNB margin band** | **~22.8%–27.8%** (ICICI Pru → SBI Life, FY25) | → (watch price war) | New-business profitability; the life "margin" | Company FY25 [S, below] |
| **Retail-health growth** | **~20%+** premium CAGR post-COVID | ↑ | Best non-life segment economics, sticky renewals | GI Council / insurance.md [verify] |
| **General/health combined ratio** | Sector **~100–105%**; retail-health repricing | → / ↑ | Underwriting still loss-making pre-float | IRDAI / co. FY25 [S, below] |
| **Health-claims inflation** | **Double-digit**; loss ratios drifting up | ↑ | Forces premium repricing (Star LR 65%→69.8% FY23→25) | [S: Star Health FY25] |
| **10Y G-sec / bond yields** | ~6.5–7.0% range | → | Float income + non-par life spread | Market [verify] |
| **Sector solvency** | **>150% min; leaders 188%–269%** | → stable | Balance-sheet cushion intact | Company FY25 [S] |

## B. LIFE scorecard — the metrics that MATTER (FY25)

> Read **VNB margin → RoEV → persistency → solvency**. PAT/premium are scale only (from JSON).

| KPI | **HDFC Life** | **SBI Life** | **ICICI Pru Life** | **LIC** | Why it signals winning |
|---|---|---|---|---|---|
| **VNB margin** | **26.1%** | **27.8%** | **22.8%** | **17.6%** | New-business profitability (VNB÷APE) |
| **VNB (₹cr)** | 2,586 (+14%) | 5,954 (+7%) | 2,370 | 10,011 (+4.5%) | Absolute new-business value |
| **APE (₹cr)** | ~9,900 [verify] | 21,417 (+9%) | 10,407 | ~36,400 [verify] | New-business volume |
| **RoEV (operating)** | **16.0%** | **20.2%** | **13.1%** | **~11.4%** | EV compounding — the real return | 
| **Embedded Value (₹cr)** | 53,246 (+18%) | 70,250 (+21%) | ~47,000 [verify] | ~8,13,200 | In-force + adj. net worth |
| **Persistency 13m** | **87%** | **86.6%** | 85.1% | 74.8% | Renewal stickiness |
| **Persistency 61m** | **61%** | **61.5%** | ~55% [verify] | [verify] | Long-tail book quality |
| **Solvency ratio** | 188% | 196% | **212.2%** | **211%** | Capital cushion (>150% min) |
| **PAT FY25 (₹cr)** ⚠️scale | 1,811 | 2,413 | 1,186 | 48,320† | *Scale only — not quality* (from JSON) |
| **Premium FY25 (₹cr)** ⚠️scale | 92,922 | ~84,000 [verify] | 70,778 | 889,970 | *Scale only* (from JSON) |

**Sources:** VNB margin / RoEV / EV / persistency / solvency — **[S: HDFC Life 9M/12M-FY25 press release & investor presentation; SBI Life Q4FY25 results (Groww/Business Standard); ICICI Pru Life Q4FY25 (Business Standard / icra); LIC FY25 press release 27-May-2025 & ICICI Sec note], all ~Jan–Jun 2025.** PAT & Premium — **[S: Screener.in structured P&L via `research-pipeline/data/financials/{HDFCLIFE,ICICIPRULI,LICI}.json`, ~Jun 2026].** † LIC PAT step-up is a **2021–22 surplus-distribution restructuring artifact**, not organic — see `FINANCIALS-10Y.md`. **[H]**

> *Reading it:* **SBI Life leads on VNB margin (27.8%) + RoEV (20.2%) + SBI bank distribution**;
> **HDFC Life best persistency (87%/61%) + balanced mix**; **ICICI Pru lower VNB margin (22.8%) —
> the FY25 margin miss that sent the stock -10%**; **LIC = scale on another planet but lowest VNB
> margin (17.6%), weakest persistency (74.8%), policy-exposed.** RoEV — not ROCE — is the return metric.

## C. GENERAL / HEALTH scorecard — combined ratio is king (FY25)

> Read **combined ratio (<100% = paid to hold float) → loss ratio → solvency**. RoE only *anchored to* combined ratio.

| KPI | **ICICI Lombard** (Gen) | **Star Health** (Health) | Why it signals winning |
|---|---|---|---|
| **Combined ratio** | **103.8%** | **101.1%** (97.3% FY24 → worsening) | Underwriting profitability; <100% = paid to hold float |
| **Loss ratio** | ~70% [verify] | **69.8%** (65.0%→66.5%→69.8% FY23→25) | Claims severity vs pricing |
| **Expense ratio** | ~34% [verify] | 30.4% (30.7% FY24) | Cost discipline |
| **Solvency ratio** | **269%** | 221% | Capital cushion (>150% min) |
| **RoE** | **19.1%** (17.2% FY24) | teens [verify] | Return *anchored to* combined ratio |
| **GDPI / GWP (₹cr)** ⚠️scale | 26,833 (+8.3%) | 16,781 | *Scale only* — not quality |
| **PAT FY25 (₹cr)** ⚠️scale | [verify] | 787 (vs 1,103 FY24, ↓) | *Scale only* — note the drop tracks combined-ratio worsening |

**Sources:** **[S: ICICI Lombard FY25 Annual Report & Q4FY25 press release; Star Health FY25 results / earnings call & Nikhil Jha loss-ratio series], ~Apr–Oct 2025.** ⚠️ `ICICIGI.json` and `STARHEALTH.json` were **EMPTY** in the Screener pull (see `FINANCIALS-10Y.md` gaps) — *which is itself the lesson*: the decisive metric (combined ratio) was never in a P&L screen. **[H]**

> *Reading it:* **Both run combined ratios >100%** — pre-float underwriting losses rescued by
> investment income. **ICICI Lombard (103.8%)** is the disciplined-general benchmark with fortress
> solvency (269%) + rising RoE (19.1%). **Star Health (101.1%, deteriorating from 97.3%)** is the
> repricing-cycle test: loss ratio climbing 65%→69.8% as claims inflation outruns price hikes; PAT
> fell ₹1,103cr→₹787cr. Retail-health pricing power is the thesis; claims inflation is the risk.

## D. Data gaps & verification queue [verify]
- **SBI Life premium, ICICI Pru EV/61m persistency, LIC APE/61m persistency** — interpolated/[verify] vs filings.
- **ICICI Lombard loss/expense split, PAT** and **Star Health RoE/PAT** — [verify] vs FY25 annual reports.
- **`SBILIFE.json`, `ICICIGI.json`, `STARHEALTH.json` all empty** in Screener pull — no JSON scale anchor; web-sourced only.

## What to watch next quarter
1. **VNB margin** at the life leaders — any compression = protection price-war tell (falsification trigger).
2. **Combined ratio** trend at Star Health / ICICI Lombard — is health repricing catching claims inflation (<100%)?
3. **Persistency 13m/61m** — book-quality direction (LIC's 74.8% the laggard to watch).
4. **Solvency** each result — cushion vs the 150% floor; any draw-down on growth.
5. **IRDAI / Budget circulars** — surrender-value norms, EoM caps, composite licence, GST-on-premium (event-driven).
