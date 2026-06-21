# Holding Companies — 10-Year Financials (clean, structured)

> Pulled from **Screener's structured P&L + Ratios tables** (sourced from filings) — reliable
> long-run series, not OCR'd PDFs. Mar-2026 = TTM/est. ₹ crore.
> [S: Screener.in structured tables, ~June 2026]. ⚠️ Verify vs filings before real use.
>
> **Read this note differently from an operating company.** For holdcos, the P&L and ROCE are the
> *wrong lens* — most of the "profit" is share-of-associate / investment income, and the balance
> sheet carries holdings at cost / equity-method, not market value. The metric that matters is
> **NAV and the holdco discount**, not reported ROCE. The tables below are shown precisely to
> demonstrate *why* (see "What the long-run data reveals").

## Coverage & data gaps

| Holdco | Type | Status |
|---|---|---|
| **Bajaj Holdings (BAJAJHLDNG)** | Operating-cum-investment holdco (Bajaj Auto + Bajaj Finserv) | ✓ full 12-yr series |
| **Tata Investment (TATAINVEST)** | Pure investment holdco | ✓ full 12-yr series |
| **Maharashtra Scooters (MAHSCOOTER)** | Bajaj-group investment holdco | ⚠️ **DATA GAP** — JSON returned empty; excluded |

## Net Profit (₹ cr) — note it *rises* even as "Sales" stays tiny

| Net Profit | FY15 | FY17 | **FY18** | FY20 | FY22 | FY24 | **FY25** | FY26ttm |
|---|---|---|---|---|---|---|---|---|
| **Bajaj Holdings** | 2,029 | 2,473 | **2,655** | 3,080 | 4,126 | 7,365 | **6,626** | 9,789 |
| **Tata Investment** | 186 | 200 | **131** | 90 | 214 | 385 | **312** | 434 |

*FY18 is the structural break for Bajaj Holdings — see the Other-Income jump below.*

## Income mix & reported ROCE (₹ cr, FY15 → FY26ttm) — the holdco "tell"

The crucial column is **Other Income** (= share of associates / dividend & investment income).
For a holdco it *dwarfs* operating Sales, and it — not the business — drives Net Profit.

### Bajaj Holdings

| | FY15 | FY16 | FY17 | **FY18** | FY19 | FY20 | FY21 | FY22 | FY23 | FY24 | FY25 | FY26ttm |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Sales** | 524 | 470 | 842 | 420 | 431 | 435 | 457 | 484 | 522 | 1,702 | 739 | 1,070 |
| **Other Income** | 35 | 7 | 8 | **2,390** | 2,827 | 3,058 | 3,451 | 3,896 | 4,673 | 5,967 | 6,224 | 9,182 |
| **Net Profit** | 2,029 | 2,265 | 2,473 | 2,655 | 3,048 | 3,080 | 3,654 | 4,126 | 4,946 | 7,365 | 6,626 | 9,789 |
| **EPS (₹)** | 182 | 204 | 222 | 239 | 274 | 269 | 328 | 364 | 436 | 653 | 586 | 866 |
| **ROCE %** | 4 | 3 | 4 | **13** | 12 | 11 | 10 | 9 | 10 | 13 | 10 | 11 |

### Tata Investment

| | FY15 | FY16 | FY17 | FY18 | FY19 | FY20 | FY21 | FY22 | FY23 | FY24 | FY25 | FY26ttm |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Sales** | 229 | 247 | 270 | 158 | 177 | 144 | 163 | 254 | 277 | 385 | 306 | 403 |
| **Other Income** | 0 | 0 | 0 | 8 | 0 | 0 | 25 | 18 | 36 | 65 | 103 | 118 |
| **Net Profit** | 186 | 194 | 200 | 131 | 134 | 90 | 155 | 214 | 252 | 385 | 312 | 434 |
| **EPS (₹)** | 3.4 | 3.5 | 3.6 | 2.4 | 2.6 | 1.8 | 3.0 | 4.2 | 5.0 | 7.6 | 6.2 | 8.6 |
| **ROCE %** | 10 | 10 | 10 | 3 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

> For Tata Investment, "Sales" *is* dividend + investment income (a pure investment book), and
> reported ROCE collapses to ~1-2% from FY18 — not because the franchise deteriorated, but because
> the **capital employed balloons with the carrying value of the investment portfolio while only the
> realised income flows through the P&L.** The NAV gain sits on the balance sheet, unrecognised.

## What the long-run data reveals

### 1. Bajaj Holdings: tiny Sales, huge Profit — the look-through engine

- **Evidence.** Standalone "Sales" sits at ₹400-740cr for most of the decade, yet Net Profit runs
  ₹2,029cr (FY15) → ₹9,789cr (FY26ttm), a ~4.8× rise. The bridge is **Other Income**, which jumps
  from ₹8cr (FY17) to ₹2,390cr (FY18) and ₹9,182cr (FY26ttm).
- **Interpretation.** That FY18 step-change is an accounting/structure event, not an operating one:
  the bulk of profit is **share of associates' earnings (Bajaj Auto + Bajaj Finserv look-through)**,
  not revenue Bajaj Holdings itself generates. Net Profit therefore tracks the *underlying
  associates compounding*, while the holdco's own "operations" are immaterial.
- **Conclusion.** Reading Bajaj Holdings as an operating company (Sales → margin → profit) is
  category-error: ~90%+ of earnings are look-through. The profit line is real; the "Sales" line is
  noise. **[H]**

### 2. Reported ROCE (~10-13%) *understates* true returns — it's an artifact, not a verdict

- **Evidence.** Bajaj Holdings' ROCE never clears 13% and mostly sits 9-13%; Tata Investment's sits
  at **1-2%** post-FY18.
- **Interpretation.** ROCE = EBIT / capital employed. The numerator captures only *recognised* P&L
  income (dividends + equity-method share), while the denominator (capital employed) carries the
  investment book **at cost / equity value, not market value** — and excludes all unrealised NAV
  appreciation. A portfolio that has compounded 15-18% in market value can still report a 1-2%
  "ROCE" because the gains are unrecognised and the cost base is stale. The ratio is mechanically
  depressed.
- **Conclusion.** For a holdco, low reported ROCE is *expected and meaningless* — it is the
  signature of cost/equity-method accounting, not poor capital efficiency. Anyone screening holdcos
  on ROCE will (wrongly) reject the entire category. **[H]**

### 3. The metric that actually matters: NAV and the holdco discount

- **Evidence.** Net Profit (look-through earnings) rises steadily for both names — Bajaj Holdings
  ~4.8× and Tata Investment ~2.3× over FY15→FY26ttm — i.e. the **underlying NAV is compounding**.
  Yet holdcos of this type persistently trade well below NAV (the "holdco discount").
- **Interpretation.** Since reported P&L/ROCE can't capture portfolio value, the real variables are
  (a) **NAV per share** (the look-through value of the holdings) and (b) the **discount** of market
  cap to that NAV. Rising look-through earnings = NAV compounding *even if the discount never
  narrows* — the holder still earns the underlying's return on the NAV they bought at a discount.
- **Conclusion.** This is the data backing for `holding-companies.md`'s core point: **value the NAV,
  watch the discount; ignore ROCE.** The discount is the swing variable, and any discount narrowing
  is pure upside on top of NAV compounding. **[H]**

### 4. Falsification test — does the discount ever narrow?

- **Evidence.** The series shown is P&L only; it confirms NAV compounding but is **silent on the
  discount**, which is a price-vs-NAV measure not present in these tables.
- **Interpretation.** The holdco thesis is falsifiable on exactly one axis: if look-through earnings
  keep rising (NAV up) **and** the discount stays stuck or widens *indefinitely*, the holder only
  ever earns the underlying return and never the re-rating — the discount becomes a permanent tax,
  not a temporary opportunity. The thesis "buy NAV at a discount" requires the discount to *at least
  not widen*, ideally to occasionally narrow (buybacks, special dividends, regulatory change,
  group restructuring).
- **Conclusion.** These financials **support** the NAV-compounding leg of the thesis but **cannot
  confirm or reject** the discount-narrowing leg — that requires market-cap-vs-NAV time series,
  which is the explicit falsification test to run next. Flagged as the key open question. **[M]**

## Cross-check vs the framework (holding-companies.md)
- **Core claim validated:** conventional P&L/ROCE is the wrong lens — the data shows profit driven
  by look-through income and ROCE mechanically suppressed by cost-basis accounting. **[H]**
- **NAV compounding visible:** rising look-through Net Profit at both names is direct evidence the
  underlying value compounds even while the discount persists. **[H]**
- **Open question (falsification):** the discount's behaviour over time is *not* in these tables and
  must be sourced separately before the "buy at a discount" leg can be confirmed. **[M]**

---

*Source JSON: `research-pipeline/data/financials/<TICKER>.json` (full 12-year P&L + ratios).*
*MAHSCOOTER.json returned empty — excluded as a data gap.*

---

**Disclaimer.** This note is a data-structuring exercise built from third-party (Screener.in)
structured tables, ~June 2026, and may contain errors; figures should be verified against primary
filings before any use. NAV and holdco-discount figures referenced are *not* contained in these P&L
tables and must be sourced separately. **This is not investment advice** — it is not a
recommendation to buy, sell, or hold any security. Do your own research and consult a
SEBI-registered adviser.
