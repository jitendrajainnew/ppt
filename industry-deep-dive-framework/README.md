# The Industry Deep Dive Framework

> A reusable framework for studying **any** industry end-to-end — understanding its
> structure, mapping where the money is, evaluating the businesses inside it, and
> building your own investment conviction.

This framework is **reverse-engineered from four real deep dives**:

| Deep Dive | Type of industry it represents |
|-----------|--------------------------------|
| 🏗️ **Cement** | Mature, cyclical, domestic, consolidating manufacturing |
| 🚢 **Dredging** | Niche, oligopolistic, capex-heavy, policy-driven services |
| 💾 **Memory Chips** | Global, technology-led, supercycle, oligopoly |
| ⚡ **Green Energy** | Multi-sub-sector, structural-growth, value-chain heavy |

Despite covering wildly different sectors, all four follow the **same underlying spine**.
That spine — generalised and made repeatable — is this framework.

---

## How to use this folder

| File | Purpose |
|------|---------|
| `README.md` (this file) | The master framework — the 12 modules, what each is for, the questions to answer, and where to get the data |
| `TEMPLATE.md` | A blank, fill-in-the-blanks deck outline. Copy it per new industry. |
| `CHECKLIST.md` | A one-page "is my deep dive complete?" checklist + quality bar |
| `EXAMPLES.md` | How each of the four source decks maps onto the framework (proof it generalises) |
| `examples/pharma.md` | A fully worked example — the framework applied to Indian pharma, showing how 3 modules "flex" for a hard case |

**Workflow:** Copy `TEMPLATE.md` → rename to `<industry>.md` → work top to bottom →
use `CHECKLIST.md` to grade completeness before you call it done.

---

## Philosophy — what a deep dive is *for*

Every deck states the same goal up front. The Green Energy deck spelled it out as
**Learning Objectives**, and it is the best statement of the mission:

> - Understand the **dynamics** of the industry
> - **Facts > Opinions**
> - Ability to **self-research** this sector
> - Ability to **explain it to a 5-year-old**
> - Learn **where to hunt for data**
> - Build **your own conviction** in your investments

A good deep dive is therefore not a stock pitch. It is a **map of an industry** detailed
enough that (a) you can locate any company within it, (b) you can tell good economics from
bad, and (c) you can keep it up to date yourself. The stock conclusions fall out at the end.

---

## The Spine — 12 Modules

```
  FRAME                 STRUCTURE                  BUSINESSES              VERDICT
  ┌──────────┐          ┌──────────────┐           ┌───────────┐          ┌────────────┐
  │ 0 Frame  │          │ 3 How it     │           │ 8 Evaluate│          │ 10 Valuation│
  │ 1 Why now│   ──►    │   works      │   ──►     │   a biz   │   ──►    │ 11 Triggers │
  │ 2 History│          │ 4 Segments   │           │ 9 Company │          │ 12 Risks    │
  └──────────┘          │ 5 Value chain│           │   deep    │          │    Verdict  │
                        │ 6 Structure  │           │   dives   │          │    Sources  │
                        │ 7 Geography  │           └───────────┘          └────────────┘
                        │   & demand   │
                        └──────────────┘
```

Run the modules roughly in order. Not every industry needs every module at equal depth
(a tech-supercycle story leans on Module 7–8; a cyclical commodity leans on Module 5 and
10), but **every module should at least be considered**. The CHECKLIST tells you the minimum.

---

### Module 0 — Frame & Disclaimer
**Purpose:** Set scope and expectations. Who is this for, what's in/out, what it is *not*
(not investment advice). Every source deck opens with this.

**Produce:** One slide — title, scope of the industry covered, disclaimer, agenda/contents.

---

### Module 1 — Why This Industry, Why Now
**Purpose:** The hook. Why does this industry deserve attention *today*? This is the
single most important slide for a reader deciding whether to keep going.

**Key questions:**
- What changed recently that makes this timely? (a cycle turning, a technology inflection,
  a policy shift, a shortage)
- Is this a **structural growth** story, a **cyclical turn**, or a **special situation**?
- What is the one-sentence thesis?

**Patterns from the decks:**
- Cement → *"Why Study Cement Now?"*: long consolidation, pricing power returning, scale
  economies, cheap valuations, out-of-favour.
- Memory → the **AI capex cycle** as the master driver; "the capex cycle has just started."
- Green Energy → the **flywheel** (cheaper than coal, scale manufacturing, regulation,
  net-zero pledges, climate change).
- Dredging → govt focus on port-led development + inland waterways.

**Produce:** A "Why Now" slide with 3–5 reasons, ideally one chart showing the inflection.

---

### Module 2 — What It Is & History
**Purpose:** Ground the reader. Define the thing simply, then show how the industry got to
where it is. History reveals the *structure* — who consolidated whom, what regulation shaped
it, which eras of boom/bust set today's competitive map.

**Key questions:**
- In one plain sentence (5-year-old test), what is this industry?
- What are the **eras**? (e.g., Cement India: Government Control → License Raj →
  Nationalisation → Privatisation → M&A / Regional-to-National)
- What invention or event kicked it off? (Solar: photovoltaic effect 1839 → first cell 1883
  → … → China mass production 2011)

**Produce:** A definition slide + a **timeline** of eras/milestones.

---

### Module 3 — How It Works / How It's Made (Technology 101)
**Purpose:** Explain the actual physical or technical process. You cannot judge a business
in a sector you don't mechanically understand. Keep it "explain to a 5-year-old" simple.

**Key questions:**
- What is the production process or service delivery, step by step?
- What are the **raw material inputs** and what do they cost (as % of total)?
- What is the core technology, and where is it heading (next-gen)?

**Patterns from the decks:**
- Cement → *"How is Cement Made?"* + Raw Materials & Costs.
- Solar → *"How a Solar Cell is Made"*: Polysilicon → Ingots → Wafers → Cells → Modules.
- Memory → *"Memory Chips 101"*, HBM vs DRAM vs NAND, even *KV Cache explained*.
- Dredging → the dredging process and why depth/soil type matters.

**Produce:** A process-flow diagram + an inputs/cost-stack slide + a "tech 101" explainer.

---

### Module 4 — Types / Segments / Classifications
**Purpose:** Break the industry into its sub-parts. Different segments have different
economics, customers, and growth — lumping them together hides the opportunity.

**Key questions:**
- What are the product/technology types? (Types of Dredgers; Types of Cement; Lithium-ion
  vs Solid-state batteries; HBM vs NAND vs HDD; Onshore vs Offshore vs Floating wind;
  Grey/Blue/Green hydrogen)
- Which segment is growing, which is declining, which is the future?
- What use-case does each segment serve?

**Produce:** A segmentation table — for each type: what it is, who uses it, cost/performance,
trajectory (growing/declining).

---

### Module 5 — Value Chain & Margin Map  ⭐
**Purpose:** *The most important analytical module.* Lay out the chain from raw input to end
customer and mark **where the profit pool actually sits**. Two businesses in the same
industry can have opposite economics depending on which link they occupy.

**Key questions:**
- What are the stages from "ground to grid" (raw material → … → end user)?
- At each stage: margin profile, capital intensity, competition, room to innovate,
  recurring vs one-off revenue?
- **Where is maximum value captured? Where is value destroyed?**
- Who is **integrating** (backward/forward) to capture more of the chain?

**Pattern — the Green Energy "Where is maximum value?" slide is the gold standard.** It rated
each stage:
| Stage | Verdict |
|-------|---------|
| Raw material (silica → ingots) | Low margin, high capex, limited innovation |
| Cell/module manufacturing | Stable margin, scale economies, high competition |
| Parts suppliers (glass, EVA, junction box) | Good margin, scale, low competition |
| EPC (engineering/procurement/construction) | Razor-thin, contract work, no innovation |
| Plant & grid operators | Very high margin (80%+), very high capex, recurring, only giants survive |

**Produce:** A horizontal value-chain diagram + a margin/capex/competition rating per stage +
a note on who is integrating.

---

### Module 6 — Industry Structure & Competitive Forces
**Purpose:** Is this a cosy oligopoly or a brutal commodity scrum? Structure determines
whether *anyone* in the industry can earn good returns.

**Key questions:**
- **Porter's Five Forces**: rivalry, new entrants, substitutes, supplier power, buyer power.
- Concentrated or fragmented? (Dredging & Memory = oligopoly; Cement India = consolidating)
- Where is the **know-how / IP** concentrated? (Dredging tech in Netherlands & Belgium;
  90%+ of solar supply chain in China)
- What are the **entry barriers**? (capital, technology, licences, scale)

**Produce:** A Porter's Five Forces slide + a "key global players" map + a note on barriers
to entry and where technical know-how sits.

---

### Module 7 — Geography & Markets
**Purpose:** Industries are not global monoliths. Demand, policy, and production are
distributed unevenly across countries. Map them.

**Key questions:**
- Which regions **produce**, which **consume**? (China produces 90% of solar; EU/LatAm/US
  consume differently)
- Per key region: market size, growth rate, policy stance, a representative case study.
- Where does **your home market (India)** fit — importer, emerging producer, future exporter?

**Pattern:** Green Energy did region-by-region (EU, LatAm w/ Chile & Poland case studies,
US, China, India). Cement did Global vs India.

**Produce:** A region-by-region set of slides (size, growth, policy, case study) + a
"production vs consumption" geographic split.

---

### Module 8 — Demand Drivers & Supply Dynamics (Cycle Position)
**Purpose:** Quantify what pulls demand and what constrains supply — and locate where we
are in the cycle. This is where shortages, gluts, and pricing power live.

**Key questions:**
- What are the structural **demand drivers**? (govt capex, AI inference, net-zero, urbanisation)
- What is the **supply situation**? Booked out / over-supplied? Lead times to add capacity?
- Where in the **cycle** are we — bottom, expansion, peak, glut?
- Is **pricing power** rising or falling?

**Patterns:**
- Memory → *"Demand is rising multifold times than supply"*, capacities booked to 2028,
  new capacity not online until late 2027 → supercycle.
- Dredging → India demand drivers (ports, inland waterways) vs limited fleet supply.
- Cement → "Pricing Power Returning" after "Long Consolidation of Cycle."

**Produce:** A demand-drivers slide + a supply/capacity slide + an explicit "where are we in
the cycle" call.

---

### Module 9 — Regulation, Policy & Government
**Purpose:** In most of these industries, government *is* the swing factor. Subsidies,
duties, mining rights, and local-content rules make or break the economics.

**Key questions:**
- What policies drive or throttle the industry? (PLI schemes, import duties, net-zero targets)
- What licences / resource rights are required? (Cement: Limestone Mining Act changes; Dredging
  govt ownership; US Jones Act forcing local build/operate)
- Is policy a **tailwind or a risk** right now?

**Produce:** A policy-landscape slide listing the key schemes/rules and their direction.

---

### Module 10 — How to Evaluate a Business in This Sector ⭐
**Purpose:** The reusable **scorecard**. Before looking at any single company, define what a
*good* business in this industry looks like. Then you can score every player consistently.

**The Cement deck's checklist is the template** — adapt the questions per industry:
1. Ability to **grow capacity**?
2. Does it have **captive raw-material inputs**?
3. Does it have **scale** to drive efficiencies?
4. Can it **brand** itself / reach the end consumer?
5. Is it selling to **industry or non-industry** use?
6. Is it a **strategic asset** (e.g., enables entry into a geography)?

The Solar deck gave the complement — characteristics of **successful companies** in the
toughest (raw-material) link: *sturdy balance sheet, economies of scale, limited competition*,
and differentiation via *efficiency improvements / more robust product*.

**Produce:** A 5–8 question scorecard tailored to this industry's economics, plus the
"what good looks like" profile. **This becomes the lens for Module 9.**

---

### Module 11 — Company Deep Dives
**Purpose:** Apply the Module 8 scorecard to the actual players. Group them, then dissect
the ones that matter.

**Key questions per company:**
- **Capabilities & positioning** — where on the value chain (Module 5), which segments
  (Module 4), scale vs peers.
- **Financials** — Balance Sheet (leverage, capex, asset base) and P&L (revenue growth,
  operating margin). Every company deep dive in the decks showed both BS and P&L.
- **Triggers** — specific upcoming catalysts (new fleet, capacity doubling, duty changes).
- **Risks** — company-specific (the Dredging DCI risks slide: ECB loan, no management, broken
  balance sheet).

**Pattern — group the field first.** Cement split players into:
**Group A (Leaders) / Group B (Challengers + Targets) / Group C (Lost the Race)**. Then it
deep-dived the names that matter. Memory grouped by segment (giants, ancillaries).

**Produce:** A grouping/tiering slide → then per-company: positioning, BS, P&L, margins,
triggers, risks. Use the same layout for every company so they're comparable.

---

### Module 12 — Valuation, Triggers, Risks & Verdict

**12a — Valuation.** Use the method that fits the sector:
- Replacement-cost / EV-per-tonne for capacity businesses (Cement: *"EV by Replacement Cost"*).
- Growth-adjusted multiples for tech (Memory: PE vs growth, margin crossover vs TSMC).
- Payback period & EPS bridge for capacity-doubling stories (Borosil: "3.8 years payback,
  EPS > Rs 50 by FY24").
- Always include a **"are we in a bubble / margin of safety"** sanity check (Memory:
  *"Are we in a Bubble? No, but not cheap either."*).

**12b — Triggers / Catalysts.** What will re-rate these names? (new orders, capacity online,
duty imposition, cycle turn, M&A). Be specific and time-bound.

**12c — Risks.** Always a dedicated section. Recurring risk taxonomy from the decks:
- **Capital intensity** (can't fund growth)
- **Policy dependence** (subsidy/duty reversal)
- **Customer/order concentration** (Dredging: dependence on DCI order overflow)
- **Balance-sheet fragility** (leverage, FX-denominated loans — EUR/INR)
- **Management/governance** (no accountable owner, govt-run)
- **Rivalry / price war** among leaders
- **Demand shock** (economic slowdown)
- **Elevated valuations**

**12d — Conclusion / Thesis.** Synthesise into a clear view (the Dredging conclusion is a
good model: oligopoly, turnaround candidate, emerging small-cap, captive-to-contract shift).

**Produce:** Valuation slide(s) + triggers list + risks list + a crisp conclusion.

---

### Module 13 (appendix) — Data Sources & How to Track
**Purpose:** Deliver on "learn where to hunt for data" and "ability to self-research."
A deep dive that can't be maintained is a snapshot, not a map.

**Produce:** A **"How to Track This Sector"** slide — the channels, analysts, agencies,
reports, X/Twitter handles, and primary sources to follow. (Green Energy listed IEA, BNEF,
McKinsey/BCG/Bain, Tony Seba, Akshat Rathi, GWEC, etc.; Cement listed source videos.)

See `CHECKLIST.md` for the generic source list to start from.

---

## The "altitude" rule

The recurring craft lesson across all four decks: **constantly move between altitudes.**
- **30,000 ft** — macro driver / why now (Module 1, 8)
- **10,000 ft** — industry structure, value chain, geography (Modules 5–7)
- **Ground level** — the actual process, single companies, single triggers (Modules 3, 11)

A complete deep dive touches all three. A weak one gets stuck at one altitude (all macro
hand-waving, or all company minutiae with no structure).

---

## TL;DR — what it takes to make a complete deep dive

1. **Frame it** (scope, why now).
2. **Explain it** (history, how it's made, segments) — pass the 5-year-old test.
3. **Map the money** (value chain + margin map + industry structure + geography).
4. **Locate the cycle** (demand drivers vs supply, pricing power).
5. **Define "good"** (an evaluation scorecard) *before* looking at companies.
6. **Score the players** (group them, then deep-dive financials/triggers/risks).
7. **Value, catalyse, caveat, conclude** (valuation + triggers + risks + verdict).
8. **Make it maintainable** (data sources + how to track).

Facts > opinions. Always end with *your own* conviction, not someone else's tip.
