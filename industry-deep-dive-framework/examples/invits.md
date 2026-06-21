# InvITs / Infrastructure Investment Trusts (India) — Deep Dive (Worked Example)

> **A worked example for a yield-instrument, asset-heavy × Regulated archetype** — it exercises the
> full framework (Decision Summary → Research Question → … → Research Log), the 5 layers, archetype
> weighting, the CORE/APPENDIX split, confidence tags, and Evidence→Interpretation→Conclusion.
>
> ⚠️ **All figures are ILLUSTRATIVE and directional** (approx. FY24–FY25 vintage) to show the
> *shape* of a completed deep dive — they use **"≈"** and carry **[M, verify]**. **Refresh every
> number against primary sources (Module 17) before any real use.** Not investment advice.

> **Writing rules in force:** every major call shows **Evidence → Interpretation → Conclusion**;
> claims carry a **confidence tag [H] strong · [M] some · [L] speculative**.

> **Note — InvITs are not operating companies, and they are the infra *sibling* of REITs, not a copy.**
> Modules are adapted: *"How it's made" = how an InvIT is **structured*** (sponsor → project SPVs →
> trust → unitholders; NDCF → distribution mechanics). *"Segments" = infra asset types* (power
> transmission, toll roads, gas pipelines, telecom towers, renewables). *"Company deep dives" =
> individual InvITs.* **Capital allocation is CENTRAL.** **The key difference vs REITs:** REITs hold
> *perpetual* real estate with rising rents; **InvITs hold *finite-life concession* assets** (a 30–35yr
> transmission licence, a 20–30yr toll concession) that **amortise toward zero residual value** — so a
> chunk of the "yield" is actually *return of capital*, and **accretive acquisitions are not optional
> growth, they are survival** (you must keep replacing decaying concession life). **[H]**

**Archetype:** ☑ **Infrastructure / Asset-heavy × Regulated** — a **yield instrument** where
**asset utilisation (availability/traffic/demand)**, **capital allocation (accretive acquisitions/
leverage)**, and **regulation (SEBI InvIT mandates, taxation)** dominate. Per `ARCHETYPES.md`,
over-weight **Capital Allocation (10)**, **Asset utilisation / Demand-supply-cycle (8)**, **Regulation
(9)**, and **Valuation (16, NDCF/DPU yield-spread)**. Innovation/tech (3) is de-emphasised.
**Data vintage:** illustrative ~FY24–FY25 · **Version:** v1.0 (worked example) · **Review date:** _set on use_

---

## ★ DECISION SUMMARY — the IC Page  [CORE · read-first, written-LAST]

| Question | Call |
|---|---|
| **Industry attractiveness** | **Neutral-to-Attractive** — a bond-plus instrument: ≈9–13% distribution yield + accretive-acquisition growth = low-teens total-return *potential*, but **asset-type-dependent** and rate-sensitive. The *average* InvIT is a depreciating-asset yield trap; the *right* one (availability-based, low-traffic-risk, disciplined acquirer) is a total-return compounder. **[M]** |
| **Best segment** | **Power transmission** (availability-based, ≈99% availability → near-zero demand risk, perpetual-ish via re-acquisition) and **annuity/HAM roads** (govt pays, no traffic risk). **[H]** |
| **Worst segment** | **Pure traffic-risk toll roads** (revenue rides on volume + a fixed concession clock ticking to zero) and **single-asset/short-residual-life** trusts. **[H]** |
| **Best-positioned company** | **IndiGrid (India Grid Trust)** — AAA-rated power-transmission pure-play, deep PowerGrid/sponsor + third-party pipeline, availability-based cash flows; weighted score **≈4.0/5** (Module 12). **[M]** |
| **Biggest risk** | **Rate / G-sec move + DPU sustainability** — InvITs are duration assets; a 10Y back-up compresses the spread and de-rates NAV, *and* on finite-life concessions a DPU "held flat" by debt or by returning capital can mask underlying decay. **[H]** |
| **Variant view (vs consensus)** | Consensus lumps all InvITs together as high-yield bond-proxies on "risky infra." **Variant: the asset *type* is everything — availability-based transmission InvITs (IndiGrid, PowerGrid InvIT) are mispriced as if they carried toll-road traffic risk, while accretive acquisitions off the NMP/asset-monetisation pipeline convert the depreciating-asset problem into a compounding-DPU engine.** **[M]** |
| **What would change my mind** | DPU sustained only by rising leverage or return-of-capital (not cash), OR an acquisition spree at sub-cost-of-capital yields, OR a sponsor governance/pledge event, OR traffic shortfalls at the road trusts (falsification triggers, Module 15). |
| **Top 3 monitoring metrics** | (1) NDCF coverage of DPU + cash vs return-of-capital mix · (2) 10Y G-sec vs distribution-yield **spread** · (3) Net debt/AUM + accretion spread on new acquisitions. |
| **Time horizon** | ☑ **Investment (1–3y)** for the rate-cut + monetisation-pipeline turn; ☑ Structural (5–10y) for the NMP-driven asset-monetisation supply + power-grid capex super-cycle. |

---

## ★ Research Question  [CORE] — do this BEFORE anything else
- **Central uncertainty:** *Are InvITs mispriced bond-proxies offering equity-like total return via
  accretive acquisitions + (in transmission) inflation/availability-linked cash flows — or are they
  yield traps on depreciating finite-life concession assets where the "yield" is partly return of
  your own capital?*
- **Why it matters (the payoff):** decides whether you size InvITs as a fixed-income substitute (clip
  the ≈9–13% "coupon", accept that some is amortisation) or an equity-like compounder you underwrite
  on accretion + asset-type quality.
- **PROVES it:** rising NDCF, DPU growth funded by *cash* (not debt/return-of-capital), accretive
  acquisitions (yield-on-cost > cost of capital), low/zero demand risk (transmission availability,
  annuity roads). **DISPROVES it:** flat/declining NDCF, DPU propped by leverage or capital return,
  dilutive deals, traffic shortfalls, short residual concession life with no replacement pipeline.
- **One-line thesis (provisional):** *asset type is destiny* — own availability-based transmission +
  annuity/HAM InvITs run by disciplined accretive acquirers; avoid pure traffic-risk toll and
  single-asset/short-life trusts.
- **Story type:** ☑ Cyclical turn (rates) + ☑ Structural growth (NMP / asset-monetisation pipeline).
- **⏱ Horizon:** Investment (1–3y) overlaid with Structural (5–10y) _(most disagreements here are horizon mismatches)_.

## 0. Frame & Disclaimer  [CORE]
- **Scope (in):** Indian-listed & large private InvITs — power transmission (IndiGrid, PowerGrid
  InvIT), roads/toll & annuity (IRB InvIT, IRB Infrastructure Trust, NHIT/National Highways Infra
  Trust, Cube Highways Trust, Bharat Highways), telecom towers (Data Infrastructure Trust), gas
  pipelines, renewables. REITs as the adjacent sibling; global infra-fund / yieldco framing for context.
  **(out):** listed infra *developers/EPC* (L&T, IRB Infra Developers as operating cos), pure REIT
  (office/retail) detail, unlisted PE infra funds.
- **Who it's for:** investors locating any InvIT on the map and judging asset-type risk + leverage +
  distribution sustainability + accretion + yield-spread.
- **Agenda:** asset-type economics → structure → value chain (the accretion spread) → regulation (the
  instrument's DNA) → capital allocation (CENTRAL) → scored company ranking → verdict.
- *Not investment advice. Do your own due diligence.*

## 1. Why This Industry, Why Now  [CORE]
1. **High absolute yields + spread** — InvIT distribution yields ≈ **9–13%** vs 10Y G-sec ≈ **~6.5–7%**;
   a **~250–600 bps spread**, far wider than REITs (a real cushion if cash is sustainable). **[M, verify]**
2. **Rate-cut cycle** — a falling-rate environment compresses the discount rate → **NAV uplift** +
   **cheaper acquisition funding** for these duration/leveraged vehicles. **[M]**
3. **Asset-monetisation super-pipeline** — the **National Monetisation Pipeline (NMP, ≈₹6 lakh cr
   target)** + PowerGrid / NHAI (via NHIT) recycling brownfield assets *creates the acquisition supply*
   InvITs feed on. **[M, verify]**
4. **Power-grid capex super-cycle** — renewable-evacuation + grid build-out expands the transmission
   asset pool IndiGrid/PowerGrid InvIT can acquire. **[M]**
5. **Institutionalisation** — sovereign/pension/insurance buyers (GIC, KKR, Ontario Teachers', etc.)
   anchoring InvITs deepens the market and lowers cost of capital. **[M]**

## 2. What It Is & History  [CORE — keep brief]
- **5-year-old test:** an InvIT is like a REIT but instead of buildings it owns **roads, power lines,
  pipelines or towers** that earn money for a *fixed number of years* (the concession), then hand back
  to the government. You're **forced by law to be paid out** most of the cash — but because the asset
  *runs out*, part of what you get back is your own money returning.
- **Origin event:** **SEBI InvIT Regulations, 2014** — created the legal wrapper to let infra
  developers monetise operating (de-risked) assets and recycle capital into new builds.

| Era / Year | What happened | Why it matters today |
|---|---|---|
| Pre-2014 | Infra funded on developer balance sheets → over-leverage (IL&FS-style) | Set the "before": stranded, over-levered infra |
| **2014 SEBI InvIT Regs** | Legal framework for the trust wrapper | **Created the asset class** |
| **2017** | **IRB InvIT** (first, roads/toll) + **IndiGrid** (transmission) list publicly | Proved the model; two opposite risk archetypes from day one |
| 2018–19 | Reg tweaks (leverage to ≤70% w/ conditions; private placement route) | Enabled **private InvITs** (PowerGrid InvIT IPO 2021; many large private trusts) |
| 2020 → | **Asset-monetisation era** — NHIT (NHAI), PowerGrid InvIT, Cube, Data Infra Trust, Bharat Highways | Govt + sponsors recycle brownfield → acquisition supply |
| 2023 → | SEBI tightens governance/valuation/related-party + unit-holder rights | Maturing instrument; institutional anchoring |

*Evidence:* the timeline. *Interpretation:* InvITs were born to fix India's over-levered-infra problem
by moving *operating* assets into a payout wrapper. *Conclusion:* **the structure exists to recycle
capital — so capital allocation (accretion) isn't a side-show, it's the reason the vehicle exists.** **[H]**

## 3. How an InvIT Works — *structure & distribution mechanics*  [CORE]
- **Structure (the cascade):** **Sponsor** (infra developer/PE, e.g. Sterlite/KKR for IndiGrid,
  PowerGrid, NHAI, IRB) seeds operating assets → assets held in **project SPVs / Holdco** (one per
  concession) → SPVs owned by the **InvIT Trust** → Trust managed by an **Investment Manager** +
  overseen by a **Trustee** → Trust issues **units** to **unitholders**. Cash flows *up* the cascade
  (SPV → trust) and *down* to investors.
- **Structure diagram (the cascade):**
  ```
        Sponsor (developer/PE)  ──seeds/ drops-down assets, retains ROFO──┐
                                                                          ▼
   Unitholders ──own units──►  InvIT TRUST  ◄── Trustee (oversight)  ◄── Investment Manager (runs it)
        ▲                          │  holds equity + lends to ──►  Project SPV 1 (e.g. transmission line)
        │   DPU = interest +        │                              Project SPV 2 (e.g. toll road)
        └── dividend +              │                              Project SPV 3 (e.g. pipeline)
            capital-return  ◄───────┘  NDCF flows UP from SPVs (tariff/toll/annuity revenue)
  ```
- **SEBI mandates (the rules that define the instrument):** ≥**80%** of value in **completed,
  revenue-generating** infra (≤20% under-construction/other); ≥**90% of net distributable cash flow
  (NDCF)** must be **distributed**; distributions **≥quarterly** (public InvITs); leverage capped at
  **≤49%** of AUM **baseline**, extendable to **≤70%** subject to **AAA rating + 6-yr distribution
  track record + unitholder approval**. **[H, verify exact thresholds]**
- **Distribution waterfall (revenue → unitholder):**
  `Tariff / toll / annuity revenue → less SPV opex, O&M, taxes → **SPV cash** → up to trust as
  **interest on shareholder loans + dividend + return of capital** → less trust expenses → **NDCF**
  → ≥90% distributed as → **DPU**, split into **(a) interest** (taxed at slab in unitholder hands),
  **(b) dividend** (taxable/exempt per SPV regime), **(c) return of capital / amortisation** (not
  income — reduces cost base) — see Module 9.`
- **The crucial REIT difference:** in a REIT the building lasts forever and rent rises; in an InvIT
  the **concession is finite** — so the **return-of-capital component is structural, not incidental**,
  and a headline 11% "yield" might be (say) ≈7% true cash income + ≈4% your own capital coming back.
  **You MUST decompose the DPU.** **[H]**

## 4. Types / Segments — *each a different risk*  [CORE]
| Segment | What it is / economics | **Tell metric** | Trajectory |
|---|---|---|---|
| **Power transmission** | Availability-based tariff (paid for *being available*, not for power flow); ≈99% availability → near-zero demand risk; 35-yr licences, re-acquirable | Availability % + tariff stability | **Best / growing (grid capex)** |
| **Annuity / HAM roads** | Govt (NHAI) pays a fixed annuity regardless of traffic; no volume risk, counterparty = sovereign | Annuity coverage / NHAI receivables | **Growing, low-risk** |
| **Toll roads (traffic-risk)** | Revenue = traffic × toll; **volume risk + fixed concession clock**; WPI-linked toll hikes | Traffic growth % + toll realisation | **Riskier, cyclical** |
| **Gas pipelines** | Transmission tariff (PNGRB-regulated), volume + tariff risk | Utilisation % + tariff order | **Steady, regulated** |
| **Telecom towers** | Long master-lease rentals from telcos; tenancy-ratio upside | Tenancy ratio + telco credit | **Growing (data/5G)** |
| **Renewables** | PPA-based generation; resource (wind/solar) risk + offtaker credit | PLF % + PPA tenor / offtaker | **Structural, offtaker-risk** |
- **Key insight:** the spectrum runs from **availability/annuity (bond-like, no demand risk)** →
  **regulated-tariff (utilisation risk)** → **traffic-risk toll (full demand risk + a clock)**. The
  first group suits the InvIT wrapper beautifully; **pure traffic-risk toll strains it** because you're
  layering volume uncertainty on top of a depreciating concession. **[H]**

## 5. Value Chain & Margin Map ⭐  [CORE]
**Chain:** Land/RoW + EPC (build) → **Operating asset (de-risked concession)** → **Drop-down into InvIT**
→ **Asset management (NDCF ops)** → **Capital markets (recycling/accretion)** → Unitholder.

| Stage | Margin | Capex | Competition | Recurring? | **Who captures it** | Margin ↑/↓ |
|---|---|---|---|---|---|---|
| EPC / construction | Project margin | Very High | High | No | Developer/sponsor | → |
| Operating concession | **High, stable (post-build)** | Low (O&M) | Low | **Yes (concession life)** | Asset owner (InvIT) | → (decays w/ life) |
| Drop-down into trust | Sponsor exit at fair value | n/a | Med | Episodic | Sponsor (ROFO) | ↑ if priced for sponsor |
| **Asset management (NDCF)** | **High (stable cash)** | Low | Low | **Yes** | **InvIT / unitholders** | → high |
| Capital markets / accretion | **Accretion spread** = asset yield − cost of capital | n/a | Med | Episodic | **Unitholders (if disciplined)** | ↑ if accretive |
- **Max value captured:** the **accretion spread** — *acquire a concession at, say, ≈10–11% asset
  yield, fund it at a blended ≈8–9% cost of capital → the ≈150–250 bps spread accretes to DPU.* That
  spread is the entire growth engine on a finite-life asset base. **Value destroyed:** over-paying for
  drop-downs (sponsor extracting value), debt-funded acquisitions below cost of capital, or letting
  concession life run down without replacement. **[H]**
- **Who is integrating / internalising:** the live debate (mirrors REITs) is **external vs internalised
  management** + **sponsor conflict on drop-down pricing**. IndiGrid (KKR-managed) and others are
  externally managed; the value question is whether the Investment Manager prices ROFO drop-downs for
  the *sponsor* or the *unitholder*. **[M]**

## 5b. Industry Metrics Cheat Sheet ⭐  [CORE — read this if nothing else after the value chain]
| Metric | What it means | How it's calculated | What "good" looks like |
|---|---|---|---|
| **NDCF** | Net distributable cash flow (the payout pool) | SPV cash up to trust − trust expenses | Growing, cash-backed |
| **DPU** | Distribution per unit | NDCF distributed ÷ units | Growing via accretion, *cash*-funded |
| **DPU composition** | Interest / dividend / **return-of-capital** split | per-component disclosure | **Low return-of-capital share** (= real income) |
| **Distribution yield** | Cash return to holder | DPU ÷ unit price | ≈9–13%, **spread over G-sec** |
| **AUM** | Asset base under the trust | Σ enterprise value of SPVs | Growing via accretive M&A |
| **Net debt / AUM (LTV)** | Gearing vs 49%/70% caps | Net debt ÷ AUM | **≈55–70% transmission OK if AAA; lower better** |
| **Accretion spread** | The growth engine | Asset acquisition yield − cost of capital | **Positive (≈+150–250 bps)** |
| **EV / asset (per ckm / per km / per MW)** | Acquisition price discipline | EV ÷ physical unit | In line/below replacement, not inflated |
| **Concession residual life** | Years of cash left | Weighted-avg remaining concession yrs | **Long + replenished by pipeline** |
| **Availability % / Traffic growth** | Demand-risk gauge | Operational | **Transmission ≈99% / toll traffic +ve** |
| **Interest coverage / DSCR** | Debt safety | Cash ÷ debt service | Comfortable, AAA-consistent |

## 5c. Red Flag Checklist ⭐  [CORE — the one-page kill-criteria sheet]
> The *inverse* of the scorecard — InvIT-specific signs of a trap. If any fire, dig before you buy.

| # | Red flag (InvIT-specific) | Why it kills value | Where to check |
|---|---|---|---|
| 1 | **Traffic-risk concentration** (toll volume = revenue) on long concessions | Volume miss → DPU miss; no floor | Segment mix; traffic disclosures |
| 2 | **DPU funded by debt or return-of-capital, not cash** | "Yield" is your own capital / leverage, not income | NDCF bridge; DPU composition |
| 3 | **Rising leverage toward the 70% cap** to sustain DPU/M&A | Refinancing + rate shock risk; AAA at risk | Net debt/AUM trend; rating actions |
| 4 | **Related-party drop-downs at inflated valuation** | Sponsor extracts value from unitholders | Valuer reports; EV/asset vs peers |
| 5 | **Short residual concession life + no replacement pipeline** | Cash literally runs out; NAV → 0 | Weighted residual life; ROFO depth |
| 6 | **Sponsor pledge / governance event / single-asset trust** | Sponsor distress or one-asset fragility | Promoter pledge; asset count; rating |
- **Concentration:** ☐ Oligopoly ☑ **Consolidating** (sponsor-led, few large platforms) ☐ Fragmented
- **Porter's 5:** Rivalry **Low–Med** · Entrants **Low** (need large de-risked operating assets) ·
  Substitutes **High** (G-secs, REITs, bonds, dividend equity — same yield buyer) · Supplier (sponsor/
  govt pipeline) **Med–High** · Buyer (govt/grid offtaker) **Low–Med**.
- **Where know-how/barriers sit:** access to large, de-risked, rated operating concessions + a credible
  ROFO pipeline + a low cost of capital. The moat is **the asset + the pipeline + the rating**, not tech. **[H]**

## 6. Industry Structure & Forces  [CORE]
- **Concentration:** **Consolidating, sponsor-led oligopoly** — a handful of sponsors/managers (KKR/
  IndiGrid, PowerGrid, NHAI/NHIT, IRB, Brookfield/Data Infra, Cube/I Squared) control the de-risked
  asset pipeline; **the barrier is *access to large rated operating infra*, not capital.** **[H]**
- **Porter's 5:** Rivalry **Low–Med** (few trusts, differentiated by asset type) · Entrants **Low**
  (need a large stabilised, rated concession portfolio to list) · Substitutes **High** (bonds, G-secs,
  REITs, dividend equities compete for the same yield buyer) · **Supplier (sponsor/govt ROFO) Med–High**
  (trust depends on pipeline + Manager fees) · **Buyer (offtaker — grid/NHAI/telco) Low–Med** (often
  sovereign-ish counterparties = low credit risk but price-taker dynamics).
- **Where know-how/IP sits / key players:** the moat is the **asset + rating + pipeline**. Key Indian
  players by type — *transmission:* IndiGrid, PowerGrid InvIT · *roads:* IRB InvIT, IRB Infra Trust,
  NHIT, Cube Highways, Bharat Highways · *towers:* Data Infrastructure Trust · *global infra-fund
  context:* Macquarie/MIRA, Brookfield Infra, KKR, GIP. **[H]**

## 7. Geography & Markets  [CORE — keep brief]
| Region | Size + growth (dated) | Policy | Producer/Consumer | Case study |
|---|---|---|---|---|
| **India (transmission)** | Grid capex super-cycle (renewable evacuation) | TBCB bids; availability tariff | **Producer + consumer** | IndiGrid AAA availability-based cash flows |
| **India (roads)** | Large NHAI network; NMP monetisation | HAM/annuity vs toll BOT | Producer + consumer | NHIT/IRB — annuity vs traffic-risk split |
| **India (towers/pipelines)** | 5G/data + gas-grid build | TRAI / PNGRB | Producer + consumer | Data Infra Trust tenancy upside |
| **US/Global (context)** | Mature listed-infra + yieldco market | Sector framing | Benchmark/cautionary | **Yieldco busts (SunEdison/TerraForm)** |
- **Home market (India) position:** ☑ **Emerging, asset-monetisation-led** — a young instrument riding
  the NMP/grid-capex wave; the *global* context (yieldco busts, over-levered infra) is the cautionary tale.

## 8. Demand, Supply & Cycle  [CORE]
- **Demand drivers:** yield-hungry institutional/retail capital seeking **G-sec-plus** income; rate-cut
  cycle improving relative appeal of duration assets. **Supply situation:** the **NMP / sponsor
  drop-down pipeline** *creates* the asset supply InvITs acquire — more brownfield monetisation =
  more accretion runway.
- **Cycle position:** ☑ **Expansion / early-recovery** — *rate cycle turning toward cuts* **[M]** +
  *monetisation pipeline ramping* **[M]**; both supportive for InvIT NAV and acquisition economics.
- **Demand cycle vs STOCK cycle (what really moves the stocks):** *Evidence:* InvIT operating cash
  flows are contractual (availability tariff / annuity) and move slowly. *Interpretation:* what moves
  the *units* is the **10Y G-sec / rate cycle** (duration) far more than quarterly operations.
  *Conclusion:* **trade the rate + yield-spread + accretion cycle; the operating cash is the slow
  layer underneath.** **[H]**
- **★ Second-Order Effects (chase the chain):** **rate cuts → discount-rate compression → NAV uplift +
  cheaper acquisition funding → wider accretion spread → DPU growth → re-rating.** Separately: **renewable
  build-out → grid-evacuation capex → new transmission lines → more InvIT-able assets → IndiGrid/PowerGrid
  InvIT acquisition pipeline → 2–3 steps down, the *transmission* InvIT is the underpriced node** (vs the
  headline solar developer). Counter-chain: **rate hikes + traffic shortfall (toll) + leverage at the
  cap → DPU cut + NAV de-rate.** **[M]**
- **Key numbers [illustrative ~FY24, verify]:** combined InvIT AUM ≈ **~₹5–6 lakh cr** across listed +
  large private; distribution yields ≈ **~9–13%**; 10Y G-sec ≈ **~6.5–7%**; spread ≈ **~250–600 bps**;
  leverage (net debt/AUM) ≈ **~55–70%** for transmission (AAA) vs lower for some roads; NMP target ≈
  **~₹6 lakh cr**; IndiGrid availability ≈ **~99%**. **[M, verify]**

## 8a. CYCLE DASHBOARD  [APPENDIX] — *where are we in the cycle?*  (illustrative — verify)
| Indicator | Current (~FY24) | 5Y context | Direction ↑/→/↓ | What it signals |
|---|---|---|---|---|
| 10Y G-sec yield | ~6.5–7% | fell from ~7.5% peak | ↓ (cuts) | Tailwind for duration/NAV + funding |
| Distribution-yield vs G-sec spread | ~250–600 bps | wide vs REITs | → | Real cushion *if* cash-backed |
| Transmission availability | ~99% | stable high | → | Near-zero demand risk |
| Toll traffic growth | mid-single-digit (asset-specific) | recovered post-COVID | ↑ | Supports traffic-risk trusts |
| Asset-monetisation pipeline (NMP/drop-downs) | Ramping | building since 2020 | ↑ | Accretion runway expanding |
| Cost of capital (InvIT bond spreads) | Easing | spiked in rate-up shocks | ↓ | Cheaper accretive M&A |

## 8b. INDUSTRY KPI DASHBOARD  [APPENDIX] — *who is winning?*  (illustrative ~FY24 — verify, [M])
| KPI | IndiGrid | PowerGrid InvIT | IRB InvIT | NHIT | Why it signals winning |
|---|---|---|---|---|---|
| Asset type | **Transmission (availability)** | Transmission (availability) | **Roads (toll, traffic-risk)** | Roads (toll + TOT) | Demand-risk profile |
| AUM (≈₹cr) | ~30,000+ | ~12,000–15,000 | ~8,000–10,000 | ~30,000+ | Scale |
| Distribution yield | ~9–10% | ~10–12% | ~11–13% | ~na (private/varied) | Yield to holder |
| Net debt / AUM | ~60–65% | low (lightly levered) | moderate | varies | Leverage headroom |
| Rating | **AAA** | AAA | AA+/AAA | AAA | Cost-of-capital & 70% cap eligibility |
| AUM growth (accretion) | **Strong (active acquirer)** | Limited (PGCIL drop-downs) | Asset-specific | Strong (NHAI TOT) | Inorganic runway |
| Mgmt model | External (KKR) | External (PGCIL) | External (IRB) | External (NHAI/Govt) | Alignment / fee leakage |
> *Reading it:* **IndiGrid** wins on **active accretive acquisition + AAA + availability cash flows**;
> **PowerGrid InvIT** on **low leverage + pristine sponsor** but thinner growth; **IRB InvIT** offers the
> **highest headline yield but carries traffic risk + finite toll concessions** (yield ≠ income); **NHIT**
> on **scale + sovereign (NHAI) pipeline**. The dashboard *visually separates* the availability-based
> compounders from the traffic-risk, return-of-capital-heavy yield plays.

## 9. Regulation, Policy & Government — *defines the instrument*  [CORE]  (over-weighted per archetype)
| Policy / rule / body | Effect | Tailwind or risk? |
|---|---|---|
| **SEBI InvIT Regulations 2014 (+ amendments)** | Legal framework; mandatory structure | **Enables the asset class** |
| **≥80% in completed revenue-generating infra** | Caps construction risk | De-risks (limits greenfield optionality) |
| **≥90% NDCF distribution** | Forces payout (the yield) | Tailwind for income; limits retained reinvestment |
| **Leverage cap: 49% baseline → 70%** (AAA + 6-yr track + unitholder nod) | Caps gearing | Risk-control + growth lever; **70% = a watch-item** |
| **Distribution taxation** (interest = slab; dividend per SPV regime; **return-of-capital = not income, reduces cost base**) | Each component taxed differently | Complexity; **budget tax-rule changes are a recurring risk** |
| **Related-party / valuation rules** (independent valuer for drop-downs; unitholder voting) | Curbs sponsor self-dealing | Governance tailwind (tightening) |
| **TBCB / NHAI-TOT / PNGRB tariff regimes** | Set the underlying asset cash flows | Sector-specific tailwind/risk |

**★ DISTRIBUTION & LEVERAGE SCORECARD [CORE — the yield-instrument's #1 ranking input; illustrative, [M, verify]]:**
| InvIT | NDCF coverage of DPU | Net debt/AUM (vs 70% cap) | Return-of-capital share of DPU | **Yield-quality score /5** |
|---|---|---|---|---|
| PowerGrid InvIT | Comfortable | Low | Low (availability cash) | **5** |
| IndiGrid | Comfortable | ~60–65% | Low–Med | **4** |
| NHIT | Adequate | varies | Med (TOT amortisation) | **4** |
| IRB InvIT | Adequate | Moderate | **High (toll amortisation + traffic risk)** | **3** |
> *Evidence:* the coverage + return-of-capital columns. *Interpretation:* a high return-of-capital share
> means the "yield" is partly *your* money back, not income. *Conclusion:* **this column feeds C3
> (distribution sustainability) + C2 (leverage) of the Module 11 rubric — the core yield-instrument inputs;
> the same headline 12% yield is *not* the same quality across these trusts.** **[H]**

## 10. Management & Capital Allocation ⭐  [CORE summary + APPENDIX detail]  (over-weighted — CENTRAL for an InvIT)
> *An InvIT is a capital-recycling machine on a depreciating asset base — accretion isn't optional, it's
> survival.* Same cycle → different capital allocation → different DPU outcome. The clearest divider is
> **who acquired accretively (asset yield > cost of capital) with leverage + valuation discipline vs who
> diluted unitholders / over-paid sponsors / propped DPU with debt or return of capital.**

| Dimension | Evidence (illustrative, dated) | Score 1–5 |
|---|---|---|
| Acquisition record (accretive vs dilutive) | IndiGrid: serial third-party + sponsor transmission buys at positive accretion spread | 4 |
| Dilution / equity-raise history | Periodic unit issuance/InvIT-bond to fund deals — watch DPU accretion vs dilution | 3 |
| Leverage discipline (net debt/AUM vs caps) | Transmission runs ~60–65% (AAA-consistent); roads vary | 4 |
| Distribution growth (DPU CAGR, *cash*-funded) | Steady DPU growth at the transmission names | 4 |
| Management alignment (internal vs external) | **All externally managed** (KKR/PGCIL/NHAI/IRB) — fee + sponsor-conflict risk | 3 |
| Sponsor skin-in-game & ROFO pipeline | Strong (KKR/PowerGrid/NHAI/Brookfield backing + ROFO) | 4 |
| **Capital Allocation Score** | | **3.7/5** |

**Acquisition / capital-allocation track record [APPENDIX — illustrative, [M, verify]; the heart of an InvIT]:**
| InvIT → Action (year) | ~Value | Verdict: accretive / dilutive / mixed | Why |
|---|---|---|---|
| IndiGrid → **Sterlite/sponsor transmission drop-downs** (2017–19) | ~₹ several thousand cr | **Accretive** | De-risked availability assets at positive spread |
| IndiGrid → **third-party transmission acquisitions** (2020–22) | ~varies | **Accretive** | Bought outside the sponsor at attractive yields, broadened pipeline |
| IndiGrid → **solar/renewables foray** | ~varies | Mixed → watch | Adds offtaker/resource risk to a clean transmission book |
| PowerGrid InvIT → **PGCIL asset drop-downs** | ~₹ large | **Accretive but slow** | Pristine sponsor; limited pace of further drops |
| IRB InvIT → **toll concession portfolio** | ~₹ large | **Mixed** | High yield but traffic risk + finite life = return-of-capital heavy |
| NHIT → **NHAI TOT bundles** | ~₹30,000cr+ | Mixed→OK | Sovereign pipeline scale; toll/TOT amortisation profile |
| _Sector-wide_ → **internalisation / sponsor-conflict on drop-down pricing** | — | **Pending — would create value** | Removes fee leakage / related-party pricing risk |

- **Accretion lens:** judge every acquisition by **asset yield-on-cost vs cost of capital** and **DPU
  accretion per unit**, *and* by whether it **lengthens weighted residual concession life**. A
  debt-funded buy that lifts DPU *and* replenishes asset life = good; an over-priced sponsor drop-down
  that dilutes or just returns capital = value destruction even if AUM rises. **[H]**
- **Pattern [M]:** *Evidence:* the durable names (IndiGrid, PowerGrid InvIT) buy **availability/annuity
  assets accretively, keep ratings AAA, and grow cash DPU.** *Interpretation:* the risk cases lever up,
  over-pay the sponsor, or live off traffic-risk toll with heavy return-of-capital. *Conclusion:* **screen
  capital allocation by *asset type bought + accretion spread + residual-life replenishment*, not headline AUM.**

## 11. How to Evaluate an InvIT — weighted rubric ⭐  [CORE]
| # | Criterion (industry-specific) | Weight % | Why it matters |
|---|---|---|---|
| 1 | **Asset quality + risk type** (availability/annuity > regulated > traffic-risk) | 25% | Demand-risk profile is destiny on a finite-life asset |
| 2 | **Leverage discipline** (net debt/AUM vs 49/70% caps, rating) | 20% | Over-leverage kills a yield instrument when rates rise |
| 3 | **Distribution sustainability / coverage** (NDCF coverage, *cash* vs return-of-capital) | 20% | Separates real income from capital-return / debt-funded yield |
| 4 | **Sponsor pipeline + alignment** (ROFO depth, conflict, internal/external) | 15% | Inorganic runway + governance |
| 5 | **Accretion track record** (asset yield − cost of capital, DPU accretion) | 12% | The growth engine on a decaying base |
| 6 | **Governance** (related-party/valuation discipline, unitholder rights) | 8% | Curbs sponsor value-extraction |
|   | **Total** | **100%** | |
**Scale:** 1 = red flag · 3 = average · 5 = best-in-class. **What "good" looks like: availability/annuity
assets + disciplined leverage (AAA) + cash-backed growing DPU + deep accretive pipeline + clean governance.**

## 12. Company Deep Dives  [CORE: IndiGrid · APPENDIX: full table]
**Tiers:** *Leaders (availability/annuity)* IndiGrid, PowerGrid InvIT, NHIT · *Roads/traffic* IRB InvIT,
IRB Infra Trust, Cube Highways, Bharat Highways · *Towers/other* Data Infrastructure Trust ·
*Adjacent context* REITs (Embassy, Mindspace — different, perpetual asset class).

**Scored ranking [APPENDIX] (≥4 names scored end-to-end; illustrative — [M, verify]):**
| InvIT | C1 Asset/Risk | C2 Leverage | C3 Distrib. sustain | C4 Pipeline/align | C5 Accretion | C6 Governance | **Weighted /5** | Rank |
|---|---|---|---|---|---|---|---|---|
| **IndiGrid** | 5 | 4 | 4 | 4 | 4 | 3 | **4.07** | 1 |
| PowerGrid InvIT | 5 | 5 | 5 | 3 | 2 | 4 | **4.20** | — (low growth)* |
| NHIT | 4 | 3 | 4 | 5 | 3 | 4 | 3.85 | 2 |
| IRB InvIT | 2 | 3 | 3 | 3 | 3 | 3 | 2.71 | 4 |
> *Weighting:* C1 25% · C2 20% · C3 20% · C4 15% · C5 12% · C6 8%. *Note:* PowerGrid InvIT scores
> highest on *quality/safety* but is a **low-growth** drop-down-limited vehicle (thin accretion); among
> **active compounders**, **IndiGrid** leads on accretive growth + AAA availability cash flows. We
> deep-dive **IndiGrid** as the bellwether of the *good* InvIT archetype.

### Company: IndiGrid (India Grid Trust)  [CORE — bellwether, scored end-to-end]
- **Positioning:** India's first and largest **power-transmission InvIT pure-play** (~₹30,000cr+ AUM),
  managed by **KKR** (acquired sponsor/manager from Sterlite). **Availability-based** tariffs (~99%
  availability → near-zero demand risk), **AAA**-rated, with both **sponsor ROFO and active third-party**
  acquisition pipeline. Sits at the *core, low-risk* centre of the asset class.
- **Scorecard 4.07/5:** strong on asset-risk(5)/leverage(4)/distribution-sustainability(4)/pipeline(4)/
  accretion(4); weaker on governance(3, externally managed + sponsor-conflict watch).
- **Financials / metrics [illustrative, [M, verify]]:** availability ≈ **~99%**, distribution yield ≈
  **~9–10%**, **net debt/AUM ≈ ~60–65%** (AAA-consistent, within the 70% cap), DPU growing low-single-
  to mid-single-digit, **return-of-capital share moderate** (transmission is largely income, not
  amortisation), 35-yr licences with re-acquisition optionality. **[M, verify]**
- **Capital allocation:** serial accretive acquirer — sponsor drop-downs *and* third-party transmission
  buys at a positive accretion spread; *the* swing factor is **accretive growth without over-leverage,
  dilution, or drifting into riskier (renewables/offtaker) assets.** **[M]**
- **★ Moat analysis [CORE — not all yield is equally durable; rate each]:**
  | Moat type | Strength | Evidence |
  |---|---|---|
  | Scale | Strong | Largest transmission InvIT (~₹30,000cr+); cost-of-capital + acquisition reach |
  | Brand (asset) | Strong | AAA-rated, availability-based marquee transmission lines |
  | Regulatory | **Strong** | Availability tariff = near-zero demand risk; AAA unlocks the 70% leverage lever |
  | Distribution (pipeline) | Strong | Sponsor ROFO **+** active third-party transmission deal flow |
  | Pipeline (accretion) | Strong | Grid-capex super-cycle expands the acquirable asset pool |
  | Switching costs | Med–Strong | Monopoly transmission corridor; tariff locked over the licence |
- **Triggers:** rate cuts (NAV uplift + cheaper funding), accretive transmission acquisitions, grid-capex
  pipeline, possible internalisation/governance upgrade.
- **Risks:** leverage at the higher end (~60–65%), rate back-up (duration), external-management/sponsor
  conflict on drop-down pricing, **drift into renewables/offtaker risk diluting the clean transmission book.**

### 12b. Management & Capital-Allocation Timeline ⭐  [CORE for the anchor company]
> Company analysis is where most reports stay shallow. Go deep on IndiGrid: dated capital-allocation
> decisions + a return/DPU trend + a real bear case. **(Illustrative/directional — [M, verify dates & values].)**

- **Capital-allocation timeline (dated key decisions — drop-downs, acquisitions, leverage, sponsor change):**
  | Year | Decision | Capital | Outcome (created / destroyed / TBD) |
  |---|---|---|---|
  | 2017 | **IPO as first transmission InvIT** (Sterlite-sponsored) | listing | Created — proved availability-asset InvIT model |
  | 2017–19 | **Sponsor transmission drop-downs** (de-risked lines) | ~several thousand cr | Created — accretive availability assets |
  | 2019 | **KKR acquires sponsor/Investment Manager** from Sterlite | control deal | Created — institutional manager + lower cost of capital |
  | 2020–22 | **Third-party transmission acquisitions** (beyond sponsor) | ~varies | Created — broadened pipeline, accretive |
  | 2021–23 | **Leverage to ~60–65% via InvIT bonds** to fund accretion | debt | TBD — accretive but raises duration/refinance risk |
  | 2022 → | **Solar/renewables foray** | ~varies | TBD — adds offtaker/resource risk to a clean book (the bear's exhibit) |
  | ongoing | **Steady DPU growth, AAA maintained** | — | Created — cash-backed DPU compounding |
- **Multi-year return/DPU trend:** distribution yield held ≈9–10% with **DPU grinding up via accretion**;
  AUM compounded from drop-downs + third-party buys; the inflection was **KKR's 2019 takeover** lowering
  cost of capital and professionalising acquisitions. **[M]**
- **Management quality & mistakes:** record of **delivering accretive growth + AAA discipline**; the
  governance flag is the **external-manager/sponsor-conflict** structure and **drop-down pricing**; the
  most debatable call is the **renewables diversification** (does it dilute the clean availability story?). **[M]**
- **The BEAR CASE (steelman it — what the bulls ignore):** IndiGrid is a **leveraged (~60–65%) duration
  asset** — a 10Y back-up de-rates it regardless of availability; growth depends on a **continuous supply
  of accretive transmission assets** that may compress in yield as competition (and cheaper bidders) crowd
  the TBCB pipeline; **renewables drift** imports offtaker/resource risk the clean-transmission thesis was
  built to avoid; and as an **externally KKR-managed** vehicle, drop-down pricing and fees can leak value
  to the sponsor. If accretion spreads compress *and* rates rise, you're left holding a high-leverage
  bond-proxy. **[M]**

## 13. Failure Modes — Historical Graveyard  [APPENDIX]
- **Who died / which sub-sectors destroyed value + cause:** **IL&FS (2018)** — India's marquee
  *pre-InvIT* over-levered infra group collapsed under hidden leverage + asset-liability mismatch, the
  cautionary "why the InvIT wrapper exists" story. **Traffic-risk toll-road defaults** — numerous BOT
  toll concessions globally and in India missed traffic forecasts → debt defaults / lender losses
  (the structural hazard inside any pure-toll InvIT). **Over-levered infra developers** broadly (the
  pre-2014 model). **Global yieldco busts** — **SunEdison/TerraForm Power** (2016): a US renewables
  yieldco that levered up to fund "drop-downs" from a distressed sponsor, promised ever-rising
  distributions, and **imploded when the growth/acquisition machine stalled and the sponsor went
  bankrupt** — the *direct* InvIT cautionary tale (yieldco = InvIT's foreign cousin).
- **Recurring failure pattern:** *high leverage + demand-risk (traffic) assets + a finite concession
  clock + a rising-rate shock + DPU promises funded by acquisitions/debt rather than cash* = the classic
  yield-vehicle value-destruction recipe; **and** *related-party drop-downs that leak value to a
  distressed sponsor.* **[H]**
- **Base rate:** in rate-up shocks, **leveraged yield instruments de-rate first and most**; survival
  depends on (a) **demand-risk-free cash** (availability/annuity) and (b) **cash-backed, not
  acquisition-/debt-funded, distributions** — the SunEdison/TerraForm pattern shows how fast a
  "growing-distribution" yieldco unwinds when the acquisition engine jams. **[M]**

## 14. Live Risk Dashboard — what can kill the thesis TODAY  [APPENDIX]
| Thesis-killer | Current status | Tripwire (early tell) | Severity |
|---|---|---|---|
| 10Y G-sec / rates back up | Watch (rate cycle) | 50–75 bps rise in 10Y; spread compresses | **Very High** |
| DPU funded by debt / return-of-capital | Watch | NDCF coverage <1x; rising return-of-capital share | **Very High** |
| Leverage creeps to the 70% cap | Stable-ish | Net debt/AUM toward 70%; rating watch/downgrade | High |
| Traffic shortfall (toll trusts) | Asset-specific | 2 qtrs of negative traffic growth vs forecast | High |
| Accretion spread compresses | Latent | New deals at sub-cost-of-capital yields | High |
| Sponsor governance / pledge / conflict event | Latent | Related-party drop-down at rich valuation | Medium |
| Adverse distribution-tax change (budget) | Latent | Change to interest/return-of-capital taxation | Medium |
| Short residual concession life | Latent | Weighted residual life falling, thin pipeline | Medium |

## 15. Consensus vs Variant View ⭐  [CORE] — where alpha lives
| What consensus believes | Your variant view | Confidence [H/M/L] |
|---|---|---|
| "InvITs = high-yield bond-proxies on risky infra; the ≈9–13% yield is the whole story (and it's risky)" | **Asset *type* is everything: availability-based transmission (IndiGrid, PowerGrid InvIT) is mispriced as if it carried toll-road traffic risk; accretive acquisitions off the NMP/grid-capex pipeline convert the depreciating-asset problem into a compounding cash-DPU engine — these are total-return compounders, not just yield traps** | **[M]** |
- **Supporting:** ~99% availability (no demand risk), AAA ratings, wide ~250–600 bps spread, active
  accretive third-party transmission deal flow, rate-cut-driven NAV uplift + cheaper funding.
- **Contradicting (steelman the bears):** InvITs *are* leveraged duration — a rate back-up de-rates them
  regardless of cash; on **toll trusts the yield is partly return of your own capital**; accretion spreads
  can compress as the pipeline gets competitive; external management + sponsor drop-down pricing leak value;
  the **SunEdison/TerraForm** pattern shows acquisition-fed "growing distributions" unwind fast.
- **★ FALSIFICATION TEST — proven WRONG if:** (a) **DPU is sustained only by rising leverage or
  return-of-capital** (NDCF coverage falls below 1x), **or** (b) **acquisitions are done at sub-cost-of-
  capital yields** (accretion spread turns negative), **or** (c) **a sponsor governance/pledge event or
  related-party over-priced drop-down** hits, **or** (d) **toll-trust traffic shortfalls / a transmission
  availability breach** materialise, **or** (e) total return collapses to **just the yield minus rate
  de-rating** with no accretive growth.

## 16. Valuation, Verdict & Investment Fit  [CORE]
- **Valuation method & why:** *not* P/E. **NAV / NDCF** (DCF of remaining concession cash flows − net
  debt; price vs NAV = discount/premium) + **distribution-yield vs G-sec spread** (the duration anchor)
  + **total-return build:** *cash distribution yield (decomposed — strip out return-of-capital) +
  DPU growth via accretion − any rate de-rating.* **Margin-of-safety check:** buy when the
  **distribution-yield − G-sec spread is wide**, the **DPU is cash-backed (low return-of-capital)**, and
  price is **at/below NAV**; *avoid mistaking return-of-capital for income.*
- **Read:** asset-type- and rate-dependent — availability/annuity InvITs with AAA, cash-backed growing
  DPU and an accretive pipeline deserve a total-return premium; pure traffic-risk toll / short-life /
  high-return-of-capital trusts are **high-headline-yield-for-a-reason.** **[M]**
- **Triggers (specific, time-bound):** | Trigger | Timing | Impact | | Rate cuts (discount-rate compression) | event-driven | NAV uplift + cheaper M&A | | Accretive transmission acquisition | 1–2y | DPU growth | | NMP/TOT pipeline drop-downs | ongoing | accretion runway |
- **Conclusion — answers the Research Question, at the declared horizon:** the better Indian InvITs are
  **not pure depreciating-asset yield traps** — **availability-based transmission run by disciplined
  accretive acquirers (IndiGrid, PowerGrid InvIT) are total-return compounders** mispriced as if they
  carried toll-road risk; but they **remain leveraged, rate-sensitive duration assets on finite
  concessions**, so entry on a **wide, cash-backed yield-spread + at/below NAV** matters, and you must
  **decompose the DPU.** **Own availability/annuity, AAA, accretive, low-return-of-capital InvITs; avoid
  pure traffic-risk toll, short-residual-life, and high-leverage single-asset trusts.** **[M]**
- **INVESTMENT FIT** _(a great instrument can still be a bad investment — fit depends on cycle + valuation)_:
  | Fit | Yes/No | At what price / cycle point? |
  |---|---|---|
  | Compounder | **Yes** (availability/annuity, AAA, cash-DPU growth — IndiGrid, PowerGrid InvIT) | Buy at/below NAV with a wide, cash-backed yield-spread |
  | Cyclical | **Yes** (rate-cycle play) | Buy when 10Y is peaking / cuts approaching |
  | Turnaround | Selective (de-levering / re-rated toll trust) | Only on visible coverage/traffic inflection |
  | Special situation | Selective (internalisation / NMP drop-down) | Event-driven (governance/accretion re-rate), sized small |

## 17. Data Sources & How to Track  [APPENDIX]
- **Regulatory (primary):** **SEBI** InvIT Regulations + circulars, InvIT offer documents/trust deeds,
  leverage/valuation/related-party disclosures; sector regulators (CERC/TBCB for transmission, NHAI/MoRTH
  for roads, PNGRB for pipelines, TRAI for towers).
- **Market / ratings (primary-ish):** **CRISIL / ICRA / India Ratings** rating rationales (AAA/leverage/
  coverage), RBI 10Y G-sec / rates; BSE/NSE InvIT data; **NMP / DIPAM** monetisation pipeline.
- **Company filings:** InvIT **quarterly distribution announcements (DPU + composition)**, NDCF
  statements, investor presentations, NAV/valuer reports, annual reports, acquisition disclosures.
- **Monitoring cadence:** **quarterly** NDCF coverage + DPU composition (cash vs return-of-capital) +
  net debt/AUM + availability/traffic; **ongoing** 10Y G-sec vs distribution-yield spread + rating
  actions; **event-driven** acquisition accretion-spread checks; **annual** capital-allocation review.

### 17b. Source Quality Table  [APPENDIX] — weight evidence by reliability
| Tier | Source type | Weight | Notes |
|---|---|---|---|
| 1 | InvIT annual report / NDCF & valuer statements / offer document | 5 | Primary, audited |
| 1 | SEBI / sector-regulator (CERC, NHAI, PNGRB) data | 5 | Primary, official |
| 2 | Rating-agency rationales (CRISIL/ICRA/India Ratings) | 4 | Independent but issuer-paid |
| 2 | Earnings-call / Investment-Manager commentary | 4 | Primary but self-interested |
| 3 | Industry / pipeline reports (NMP, infra consultants) | 3 | Secondary, methodology matters |
| 4 | Expert / channel-check (traffic, tariff) interviews | 2 | Useful, unverifiable, sample-biased |
| 5 | Social media / forums / yield-chasing tips | 1 | Opinion — corroborate before using |
- **Key claims, by source tier:** the load-bearing claims (availability ~99%, AAA rating, NDCF coverage,
  leverage caps) rest on **tier 1–2** (filings, regulator, ratings) → confidence earned; the *accretion-
  spread* and *pipeline-runway* claims lean tier 2–3 → tagged **[M]**; yield-trap-vs-compounder framing
  is interpretive → **[M]**.

## 18. Research Log  [APPENDIX] — living document (seed entries; append on each new data point). Review date: _set on use_
| Date | Observation (fact, dated + sourced) | Impact on thesis (+/−/neutral) | Confidence |
|---|---|---|---|
| _illustrative_ | 10Y G-sec easing as rate-cut cycle begins | + (discount-rate compression → NAV uplift + cheaper M&A) | [M] |
| _illustrative_ | IndiGrid availability sustained ≈99%, AAA maintained | + (supports demand-risk-free compounder thesis) | [M] |
| _illustrative_ | IndiGrid net debt/AUM at ~60–65% (toward higher end) | − (leverage / duration watch) | [M] |
| _illustrative_ | IRB InvIT DPU carries high return-of-capital share | − (headline yield ≠ income; traffic-risk trust) | [M] |
| _illustrative_ | NMP / NHAI-TOT drop-down pipeline ramping | + (accretion runway expanding) | [M] |
| _illustrative_ | IndiGrid renewables foray adds offtaker risk | neutral/− (tests clean-transmission discipline) | [L] |
| _illustrative_ | All listed InvITs still externally managed; drop-down pricing debated | − (governance / fee-leakage overhang) | [M] |
| _<add next>_ | | | |
