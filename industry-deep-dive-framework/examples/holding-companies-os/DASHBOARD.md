# Holding Companies (HOLDCO) Dashboard — Live KPIs

> The "is the report alive?" asset. The KEY metric here is the **HOLDCO DISCOUNT** (market cap vs
> NAV), **not ROCE** — reported ROCE (~1–13%) is a cost/equity-method *artifact* and the wrong lens
> (see `FINANCIALS-10Y.md`). Track: discount %, dividend yield + payout, and **look-through earnings
> growth** (the NAV compounding engine). Each metric: reading + direction + source + date.
> **Refresh weekly on the discount mark; monthly on the rest.** Status ~June 2026.
> [S: Screener.in structured tables, ~June 2026] + live web checks. ⚠️ Verify vs primary before use.
> **Not investment advice.**

## A. The look-through earnings engine — what NAV is actually compounding at  [CORE]

> This is the **real** "tell" — for a holdco the P&L is share-of-associate / investment income, so
> Net Profit ≈ **look-through earnings** = a clean proxy for underlying NAV compounding. ₹ crore.

| KPI | Bajaj Holdings (BAJAJHLDNG) | Tata Investment (TATAINVEST) | What it signals |
|---|---|---|---|
| **Look-through Net Profit FY15** | **₹2,029cr** | **₹186cr** | Starting NAV-earnings base |
| **Look-through Net Profit FY18** (break) | ₹2,655cr | ₹131cr | Bajaj FY18 = Other-Income jump (₹8→₹2,390cr) |
| **Look-through Net Profit FY24** | ₹7,365cr | ₹385cr | Underlying compounding visible |
| **Look-through Net Profit FY25** | ₹6,626cr | ₹312cr | Both dipped FY25 (mkt/realisation timing) |
| **Look-through Net Profit FY26ttm** | **₹9,789cr** | **₹434cr** | Re-accelerated to record |
| **FY15→FY26ttm multiple** | **≈4.8×** | **≈2.3×** | NAV-earnings growth (the discounted-compounder leg) |
| **≈ Look-through CAGR (11y)** | **≈15.4%** [H] | **≈8.0%** [H] | Bajaj's Auto+Finserv >> Tata's diversified book |
| **Other Income (FY26ttm)** | ₹9,182cr | ₹118cr | = share of associates / investment income = the engine |
| **Reported ROCE (FY26ttm)** | 11% — **IGNORE** | 2% — **IGNORE** | Artifact of cost-basis accounting; NOT a quality read |

*Evidence → Interpretation → Conclusion:* both names' Net Profit rises while "Sales" stays tiny →
the profit is **look-through**, not operating → **NAV is compounding (Bajaj ~15%, Tata ~8%) even if
the discount never moves**; that compounding, bought at a discount, is the base-case return. **[H]**

## B. THE KEY METRIC — Holdco discount to NAV  [CORE · the swing variable]

> The discount is a *price-vs-NAV* measure and is **NOT** in the P&L tables — it must be sourced live.
> Marked **[verify]** because NAV requires marking each listed holding to today's price (stake% × mcap)
> + net cash − holdco debt. Directional ranges below from the framework + web checks; refresh weekly.

| KPI | Bajaj Holdings | Tata Investment | Direction | Source |
|---|---|---|---|---|
| **Discount to NAV %** | **≈50–55%** `[verify — live]` | **≈55–65%** `[verify — live]` | → wide | holding-companies.md [M]; web ~Jun-2026 |
| **≈ Look-through NAV (₹cr)** | ≈1,30,000+ `[verify]` | ≈30,000–40,000 `[verify]` | ↑ (NAV compounding) | holding-companies.md [M, verify] |
| **5Y discount context** | range ≈45–70% | "unusual discount" debated | → deep end | ValuePickr / brokerage SOTP [L] |
| **Cash as % of mcap** | High (net cash) `[verify]` | Moderate `[verify]` | → | filings [M, verify] |
| **Substitute check** | Buy Bajaj Auto/Finserv directly | Buy underlying Tatas/MF | — | the holdco's core problem |

## C. Dividend yield + payout — "paid to wait"  [CORE]

| KPI | Bajaj Holdings | Tata Investment | What it signals | Source |
|---|---|---|---|---|
| **Dividend yield** | **≈1.8–3%** `[verify]` | **≈0.4–1%** `[verify]` | Bajaj pays you more to hold | Trendlyne / Investing.com, ~Jun-2026 |
| **Latest declared DPS** | ₹130 (ex-date 30-Jun-2026) `[verify]` | annual payer `[verify]` | Rising-ish at Bajaj | Simply Wall St / web, Jun-2026 |
| **Payout ratio (holdco)** | Moderate-rising | Low–moderate | Willingness to share cash | filings [M] |
| **Upstreaming health** | High (Auto+Finserv pay well) | Mixed (diversified book) | Un-starved vs starved | [M, verify] |

## D. Buyback activity — the single best unlock, and it is MISSING  [CORE · the whole thesis in one row]

| KPI | Bajaj Holdings | Tata Investment | Why it matters | Source |
|---|---|---|---|---|
| **Buyback-at-discount record** | **None notable** `[verify]` | **None notable** `[verify]` | A buyback at 50% off NAV is ≈**2× accretive/₹**; its absence = run-for-control | holding-companies.md [M] |
| **Demerger / structure-collapse** | None live `[verify]` | None live `[verify]` | The cleanest unlock (hands shares to holders) | [M, verify] |
| **Stated intent to close discount** | "considering disclosures / sub-buybacks" `[verify]` | none stated `[verify]` | Weak/absent = base case "stays cheap" | web, ~Jun-2026 [L] |

> *Reading it:* both names have a **compounding NAV** (Section A) bought at a **deep discount**
> (Section B) and pay you a **dividend to wait** (Section C) — but **neither has run the buyback**
> that would convert the discount into per-share NAV accretion (Section D). That empty row is exactly
> why both still trade at deep discounts. **The discount is the swing variable; the catalyst is absent.**

## E. The MAHSCOOTER data gap  [APPENDIX]

| Holdco | Status |
|---|---|
| **Maharashtra Scooters (MAHSCOOTER)** | ⚠️ **DATA GAP** — `MAHSCOOTER.json` returned empty; **excluded** from all KPI/score tables. Framework (holding-companies.md) treats it as a Bajaj-group, Auto/Finserv-heavy, **deepest-discount control vehicle** (≈45–55% discount, low payout, hoarder) — but **no real financials available here**, so it is flagged, not scored. |

## What to watch (weekly / monthly)  [CORE]
1. **Discount mark-to-market** — recompute NAV (stake% × live mcap of each holding) + net cash − debt; is the gap narrowing or widening?
2. **Any buyback / demerger / delisting announcement** at either name (or any group peer) — the class re-rates on one proof point (second-order effect).
3. **Payout step-up** — rising DPS / payout ratio = governance signal the promoter is willing to share.
4. **Underlying NAV compounding** — Bajaj Auto + Bajaj Finserv earnings (Bajaj); Tata-group + market book (Tata Inv) — is the look-through engine still running?
5. **Tax/SEBI catalyst news** — buyback-tax (Oct-2024 shift), DDT, LTCG-on-unlocking, NCLT scheme rules — these are the broadest class-wide levers.
