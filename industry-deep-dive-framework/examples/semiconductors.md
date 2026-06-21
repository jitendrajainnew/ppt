# Semiconductors (Global, with India angle) — Deep Dive (Worked Example)

> **This is a full worked example** matching the gold-standard structure — it exercises the
> framework end-to-end (Decision Summary → Research Question → … → Research Log), the 5 layers,
> archetype weighting, the CORE/APPENDIX split, confidence tags, and the
> Evidence→Interpretation→Conclusion rule.
>
> ⚠️ **All figures are ILLUSTRATIVE and directional** (approx. 2024–2025 vintage) to show the
> *shape* of a completed deep dive. **Refresh every number against primary sources (Module 17)
> before any real use.** Not investment advice.

> **Writing rules in force:** every major call shows **Evidence → Interpretation → Conclusion**;
> claims carry a **confidence tag [H/M/L]**.

**Archetype:** ☑ **Technology × Cyclical (Hybrid)** — innovation + product cycles dominate
(Technology: nodes, EUV, chiplets, design wins), but the **capital cycle** swings violently
(Cyclical: capex booms, inventory gluts, book-to-bill). Per `ARCHETYPES.md`, over-weight the
**tech roadmap inside How-it's-made (3)**, **Demand/Supply/Cycle (8)**, **Structure & Forces (6)**,
and **Geography/Regulation (7/9)** — export controls are now a first-order variable.
**Lens:** **GLOBAL primary** (this is a borderless industry) with an **India angle** (design/VLSI
talent, ATMP/OSAT, Tata Electronics + Micron Sanand, ISM/PLI incentives).
**Data vintage:** illustrative ~2024–2025 · **Version:** v1 (worked example) · **Review date:** _set on use_

---

## ★ DECISION SUMMARY — the IC Page  [CORE · read-first, written-last]

| Question | Call |
|---|---|
| **Industry attractiveness** | **Attractive (structurally), but cyclical** — secular AI/compute demand + rising silicon content, yet brutal capex/inventory cycles; the *average* chip company is mediocre, the *chokepoint owners* are extraordinary. **[M]** |
| **Best segment** | **Leading-edge foundry** (TSMC) + **lithography/EUV** (ASML) + **EDA duopoly** (Synopsys/Cadence) — true chokepoints, recurring, pricing power. **[H]** |
| **Worst segment** | **Commodity memory (DRAM/NAND)** — capital-intensive, oligopoly but still cyclical, periodic price collapses; and **trailing-edge logic** without scale. **[H]** |
| **Best-positioned company** | **TSMC** — leading-edge process + packaging chokepoint, customer trust, ~60%+ foundry share; weighted score **4.35/5** (Module 12). **[H]** |
| **Biggest risk** | **Taiwan geopolitical concentration** — a Taiwan Strait disruption is a global-economy tail risk; secondarily, **the cyclical inventory glut**. **[H]** |
| **Variant view (vs consensus)** | Consensus = "AI lifts all chips." **Variant: the durable value sits in the *chokepoints + advanced packaging + power/cooling 2nd-order chain*, not in the long tail of merchant chip vendors; and the capex super-cycle will produce a classic digestion air-pocket that consensus under-prices.** **[M]** |
| **What would change my mind** | TSMC loses a node lead (Intel 18A / Samsung ramps credibly), OR ASML EUV monopoly is broken/curbed by export rules, OR AI capex digestion proves shallow (no glut) — see falsification (Module 15). |
| **Top 3 monitoring metrics** | (1) Leading-edge **utilisation + capex guides** · (2) **Book-to-bill** + inventory days (memory + equipment) · (3) **Export-control / China-restriction** newsflow. |
| **Time horizon** | ☑ **Investment (1–3y)** for the AI/capex cycle; ☑ Structural (5–10y) for the chokepoint compounders. |

---

## ★ Research Question  [CORE]
- **Central uncertainty:** *Is the durable value of the AI/semiconductor super-cycle concentrating
  in a few process/tool/IP chokepoints (TSMC, ASML, EDA, HBM/packaging) — while the merchant-chip
  long tail commoditises — and is a cyclical digestion air-pocket being under-priced?*
- **Why it matters:** the answer decides whether you own the *chokepoint compounders* through the
  cycle, or trade the broad cohort, or wait for the glut to buy the cyclicals.
- **Proves it:** chokepoint pricing power + share holds through a downturn; advanced-packaging/HBM
  remain supply-constrained; node leadership stays with TSMC. **Disproves it:** Intel/Samsung
  close the node gap, EUV monopoly is curbed, AI capex proves non-cyclical and broad-based.
- **Provisional thesis:** value concentrates in chokepoints + the AI 2nd-order chain
  (HBM→packaging→power→cooling); a digestion air-pocket is likely and tradeable. **Story type:**
  ☑ Structural growth + ☑ Cyclical turn.
- **⏱ Horizon:** Investment (1–3y) overlaid with Structural (5–10y).

## 0. Frame & Disclaimer  [CORE]
- **Scope:** the global chip stack — design (fabless/IDM), EDA/IP, wafer fabrication (foundry),
  lithography/equipment, materials, assembly/test (OSAT/ATMP), and memory. **Out:** end-system
  OEMs, telecom carriers, pure software.
- **For:** investors locating any semi name on the map and judging chokepoint vs commodity,
  cycle position, and geopolitical exposure.
- *Not investment advice. Do your own due diligence.*

## 1. Why Now  [CORE]
1. **AI compute boom** — accelerator demand (GPUs/ASICs) driving record data-center capex; global
   semi market ≈ **$600bn (2024)** heading toward **≈$1tn by 2030 (~8–9% CAGR)**. **[M, verify]**
2. **HBM + advanced packaging are the bottleneck** — HBM shifting from commodity DRAM to
   sold-out, allocated, high-ASP product; CoWoS/advanced-packaging capacity is the gating factor. **[M]**
3. **Geopolitics is now a first-order driver** — **US export controls** on advanced GPUs/EUV to
   China, **CHIPS Act ($52bn)**, EU/Japan/Korea/India incentives reshoring fabs. **[H]**
4. **EUV at the bleeding edge** — ASML **High-NA EUV** enabling 2nm→sub-2nm; node economics rising. **[M]**
5. **India entering hardware** — **ISM ($10bn)** + Tata Electronics (Dholera fab, Assam OSAT) +
   **Micron Sanand** ATMP; design/VLSI talent already global. **[M, verify]**

## 2. What It Is & History  [CORE — brief]
- **5-year-old test:** tiny electrical switches (transistors) printed by the billions onto silicon
  to make the "brains" inside every device; a few companies *design* them, a few *print* them, and
  almost nobody can do both at the leading edge.
- **Eras:** 1947 transistor → 1958–59 **integrated circuit** (Kilby/Noyce) → 1965 **Moore's Law**
  (transistor count doubles ~2y) → 1970s–80s **IDM era** (Intel, TI, Japan DRAM) → 1987 **TSMC =
  the foundry model** → 1990s–2000s **fabless/foundry split** (design separates from fab) →
  2010s **Moore's-Law slowdown + EUV** (few can afford leading edge) → 2020s **AI era** (compute
  scarcity, packaging, geopolitics). *History explains the structure: the foundry split created
  fabless winners (Nvidia, Apple-silicon) and concentrated manufacturing into TSMC; rising node
  cost killed all but ~3 leading-edge fabs.* **[H]**

## 3. How It's Made — *sand to system*  [CORE]
- **Pipeline flow:** **Design** (architecture + RTL) → **EDA/IP** (Synopsys/Cadence/Arm) →
  **tape-out** → **wafer fab** (deposition → **lithography** → etch → implant → CMP, ~hundreds of
  steps) → **test (wafer sort)** → **assembly/packaging (OSAT/ATMP)** → **final test** → ship.
- **Cost stack:** | Input | % of cost | Sourcing risk |
  | EUV/litho tools + fab capex | Dominant (a fab ≈ $20bn+) | **ASML monopoly (EUV)** |
  | EDA + IP licenses | High at design | Synopsys/Cadence/Arm |
  | Wafers, gases, photoresist, masks | Mid | Japan-heavy materials |
  | Assembly/test labor + substrates | Lower | OSAT (Taiwan/China) + substrate shortages |
- **Tech roadmap (where the puck goes):** node shrink **5nm → 3nm → 2nm → sub-2nm (A16/A14)**;
  transistor architecture **FinFET → GAA/nanosheet**; **backside power delivery**; **High-NA EUV**;
  and crucially **More-than-Moore = chiplets + advanced packaging (CoWoS, SoIC, hybrid bonding,
  HBM stacks)** — when shrink slows, *packaging* becomes the new performance lever. The mix-shift
  toward packaging/HBM *is* a core part of the thesis. **[H]**

## 4. Segments  [CORE]
| Segment | Economics | **Tell metric** | Trajectory |
|---|---|---|---|
| **Leading-edge foundry** | Very high capex, high margin, chokepoint | Node lead + utilisation | **Growing, defensible** |
| **Lithography/equipment** | Oligopoly→monopoly (EUV), recurring service | Book-to-bill, EUV backlog | **Growing** |
| **EDA / IP** | Software margins, sticky duopoly | Renewal/ACV growth | **Growing, defensible** |
| Fabless (logic/GPU) | High margin, design-win driven, cyclical | Design wins, ASP | AI-led growth, cyclical |
| **Memory (DRAM/NAND)** | Capital-heavy oligopoly, price-cyclical | Bit growth, contract price | **Cyclical**; HBM = upside |
| Analog/Power/MCU | Diverse, sticky, trailing-edge, long-life | Content $/system | Steady, auto/industrial cyclical |
| Materials/gases | Specialty, Japan-heavy | Share of consumable spend | Steady |
| **OSAT / ATMP (incl. India)** | Lower margin, scale + packaging tech rising | Advanced-packaging mix | **Growing (packaging)** |

## 5. Value Chain & Margin Map ⭐  [CORE]
**Chain:** EDA/IP → **Design (fabless/IDM)** → **Foundry (wafer fab)** → **OSAT/packaging** →
**Test** → System OEM → End customer.

| Stage | Margin | Capex | Competition | Recurring? | **Who captures it** | Margin ↑/↓ |
|---|---|---|---|---|---|---|
| EDA / IP | **Very high** | Low | Duopoly | **Yes** | Synopsys, Cadence, Arm | ↑ |
| Litho/equipment | High | Med | **Monopoly (EUV)** | Service yes | **ASML**, AMAT, LRCX, TEL | ↑ |
| Fabless design | High | Low–Med | Design-win | Semi | Nvidia, AMD, Apple, Qualcomm | ↑ (AI) |
| **Leading-edge foundry** | High | **Extreme** | ~3 players | Sticky | **TSMC** (>60% share) | → high |
| Memory | Cyclical | Extreme | Oligopoly (3–4) | No | Samsung, SK Hynix, Micron | ↕ (HBM ↑) |
| OSAT/ATMP | Low–Mid | Med | Fragmented | Semi | ASE, Amkor; (Tata, Micron India) | ↑ (packaging) |
- **Max value:** EDA/IP + EUV + leading-edge foundry (chokepoints). **Value destroyed:** subscale
  trailing-edge logic + mistimed memory capex. **[H]**
- **Integrating:** foundries forward into **advanced packaging**; fabless firms (Nvidia/Apple) deepen
  ties to TSMC; IDMs (Intel) split design vs foundry; hyperscalers (Google/Amazon/MS) integrate
  **back into custom silicon (ASICs)** to escape merchant pricing. **[H]**

## 5b. Industry Metrics Cheat Sheet ⭐  [CORE — read this if nothing else after the value chain]
| Metric | What it means | Calculated | What "good" looks like |
|---|---|---|---|
| **Process node (nm)** | Leading-edge capability | Smallest in volume prod. | At/ahead of leading edge |
| **Wafer starts / capacity util** | Volume + cycle health | Wafers out ÷ capacity | High util (>90%) at leading edge |
| **Book-to-bill** | Forward demand (equipment) | Orders ÷ billings | >1.0 = expansion |
| **Capex / sales** | Reinvestment intensity | Capex ÷ revenue | High but disciplined; watch the cycle |
| **Gross margin** | Pricing power | std. | Foundry >50%, EDA >75%, memory swings |
| **Design wins / ASP** | Fabless momentum | wins, $/unit | Rising in AI/HPC |
| **Inventory days** | Glut/restock signal | DIO | Lean = healthy; spiking = glut |
| **HBM / advanced-packaging mix** | AI exposure | % of revenue/capacity | Rising = AI leverage |

## 6. Structure & Forces  [CORE]
- **Concentration:** ☑ **Oligopoly hardening to monopoly at the chokepoints.** Leading-edge foundry
  ≈ **3 credible players (TSMC, Samsung, Intel), TSMC >60% share**; **EUV = ASML monopoly**; **EDA
  = Synopsys + Cadence duopoly**; memory = **3–4 firms**. *The moat is capital + know-how + an
  ecosystem of trust, and at the very edge it is a near-monopoly on the tools and the process.* **[H]**
- **Porter's 5:** Rivalry **Low at the edge / High in commodity (memory, trailing logic)** ·
  Entrants **Very Low** (a leading-edge fab ≈ $20bn+; EUV unavailable to new entrants) · Substitutes
  **Low** (no substitute for advanced compute) · **Supplier power Very High** (ASML, EDA, materials)
  · Buyer power **Mixed** (hyperscalers concentrating, but they need TSMC).
- **Know-how/IP:** process recipes + yield learning (TSMC), litho physics (ASML), EDA algorithms +
  IP libraries (Synopsys/Cadence/Arm). India's edge = **design/VLSI engineering talent** and an
  emerging **ATMP/packaging** base.

## 7. Geography  [CORE — brief]
| Region | Role | Policy | Producer/Consumer |
|---|---|---|---|
| **Taiwan** | Leading-edge foundry (TSMC) — the chokepoint | Strategic; concentration risk | **Producer (critical)** |
| **South Korea** | Memory (Samsung, SK Hynix) + logic | K-incentives | Producer |
| **United States** | Design/EDA/IP leadership; fabs returning | **CHIPS Act; export controls** | Designer + consumer |
| **China** | Largest consumer; building self-sufficiency under sanctions | SMIC; subsidies | Consumer + (curbed) producer |
| **Japan** | Materials, equipment, Rapidus 2nm bet | Subsidies | Producer (tools/materials) |
| **Netherlands** | **ASML = EUV monopoly** | Export-control aligned with US | Producer (critical tool) |
| **India** | **Design talent; emerging ATMP/OSAT + first fabs** | **ISM/PLI** | Consumer → emerging producer |
- **India position:** ☑ **Emerging producer** — strong in *design/VLSI*; entering *packaging/ATMP*
  (Micron Sanand, Tata Assam) and *fabs* (Tata–PSMC Dholera). Largely *importer* of finished chips
  today, with an explicit policy push up the value chain. **[M]**

## 8. Demand, Supply & Cycle  [CORE]
- **Demand:** AI/data-center compute (structural), plus cyclical end-markets (PC, smartphone, auto,
  industrial). Rising **silicon content per system** is the secular tailwind.
- **Supply:** **constrained** at leading-edge + HBM + advanced packaging (CoWoS); **ample-to-glut**
  in commodity memory and mature logic when the cycle rolls.
- **Cycle position:** **AI/leading-edge in expansion-to-peak capex [M]**; **memory recovering off a
  2023 trough [M]**; broad analog/auto **digesting inventory [M]**.
- **Demand vs STOCK cycle:** *Evidence:* end-demand for compute trends up, but chip *stocks* swing
  with **capex guides, book-to-bill, and inventory days**. *Interpretation:* what moves the equities
  is the **inventory + capex cycle and the export-control headline**, not the secular trend line.
  *Conclusion:* respect the cycle — own chokepoints through it, trade cyclicals around the glut. **[H]**
- **★ Second-Order Effects:** **AI → more GPUs → more HBM → more advanced packaging (CoWoS) →
  more power draw → data-center build-out → grid/transformers → cooling (liquid) → utilities →
  nuclear/gas.** *The best opportunities often sit 2–3 steps down:* HBM (memory makers),
  **packaging/substrates**, power semis (SiC/GaN), thermal/cooling, and electrical equipment. **[M]**
- **Key numbers [illustrative ~2024, verify]:** global semi ≈ **$600bn → ~$1tn by 2030 (~8–9%
  CAGR)**; AI accelerators a fast-growing slice (tens → >$100bn run-rate); TSMC leading-edge foundry
  share ≈ **>60%**; ASML EUV ≈ **~100% of EUV tools**; a leading-edge fab ≈ **$20bn+**; HBM a small
  but explosively growing share of DRAM. **[M, verify]**

## 8a. CYCLE DASHBOARD  [APPENDIX] — *where are we in the cycle?*  (illustrative — verify)
| Indicator | Current (~2024–25) | 5Y context | Direction | What it signals |
|---|---|---|---|---|
| Leading-edge utilisation | High (sold out at AI nodes) | rose with AI | ↑ | Tight chokepoint, pricing power |
| Equipment book-to-bill | ~>1 (litho), softer broad | volatile | → | Selective expansion |
| Memory contract prices | Recovering off 2023 trough | deep down-cycle | ↑ | Memory up-cycle early |
| Capex/sales (industry) | Elevated (AI build) | high | → | Risk of future digestion |
| Inventory days (broad logic) | Normalising from glut | spiked 2022–23 | ↓ | Restock underway |
| Export-control intensity | High / tightening | escalating since 2022 | ↑ | Persistent geopolitical drag |

## 8b. INDUSTRY KPI DASHBOARD  [APPENDIX] — *who is winning?*  (illustrative ~2024 — verify)
| KPI | TSMC | Samsung | Intel | ASML | Nvidia | Why it signals winning |
|---|---|---|---|---|---|---|
| Revenue (~$bn) | ~90 | ~200 (group) | ~55 | ~28 | ~60→130 (surging) | Scale / momentum |
| Gross margin | **~53–56%** | mixed (memory swings) | ~35–40% (pressured) | **~51%** | **~73%+** | Pricing power |
| Node leadership | **3nm→2nm leader** | close 2nd | 18A catching up | enables all | (fabless on TSMC) | Process edge |
| Foundry share | **>60%** | ~10–12% | rebuilding | n/a | n/a | Manufacturing dominance |
| Chokepoint | leading-edge + CoWoS | memory/HBM | x86 + fab turnaround | **EUV monopoly** | **AI GPU + CUDA** | Defensibility |
| Capex (~$bn) | ~30+ | very high | very high (strained) | (customer of fabs) | low (fabless) | Reinvestment / strain |
| R&D intensity | high | high | high | very high | very high | Innovation engine |
> *Reading it:* TSMC wins on **node + packaging + share**; ASML on **EUV monopoly**; Nvidia on
> **GPU + CUDA software moat**; SK Hynix/Micron/Samsung fight over **HBM**; Intel is the **turnaround
> wildcard** (18A node + foundry ambition).

## 9. Regulation, Policy & Government — *now lead actor*  [CORE]  (over-weighted per archetype)
| Policy / body | Effect | Tailwind/Risk |
|---|---|---|
| **US export controls** (advanced GPU/EUV to China) | Cuts China leading-edge access | Risk (China rev) / moat (incumbents) |
| **US CHIPS Act ($52bn)** | Subsidises US fabs (TSMC AZ, Intel, Micron) | Tailwind (reshoring), execution risk |
| **Dutch/Japan export alignment** | Restricts EUV/DUV + tools to China | Risk to equipment China sales |
| **China subsidies / SMIC** | Domestic self-sufficiency drive | Long-run competitive risk |
| **EU Chips Act** | EU fab incentives | Tailwind (Europe) |
| **India ISM ($10bn) + PLI/DLI** | Funds fabs, ATMP, design | Tailwind (India entry) |
| **Entity List / license rules** | Gates who can buy/sell what | Episodic shock risk |

**★ GEOPOLITICAL EXPOSURE SCORECARD [CORE — a top ranking input for this archetype; illustrative, verify]:**
| Company | Geographic concentration | China-revenue / export-control exposure | Geo score /5 |
|---|---|---|---|
| ASML | Netherlands HQ, global install base | China DUV sales curbed | **4** |
| TSMC | **Taiwan-concentrated** (mitigating via AZ/Japan/Germany) | Taiwan Strait tail risk | **3** |
| Nvidia | US-design, TSMC-built | China-GPU bans cut a revenue slice | **3** |
| Intel | US/global fabs, CHIPS-backed | lower China dependence | **4** |
| SMIC | China-only, sanctioned | **Cut off from EUV/leading edge** | **2** |
> This column feeds **C4 (15% weight)** of the Module 11 rubric — geopolitics is now a core input.

## 10. Management & Capital Allocation ⭐  [CORE summary + APPENDIX detail]  (over-weighted per archetype)
> *Same industry, same cycle → different management → different outcome.* The clearest divider in
> semis is **who timed the capital cycle and node bets right vs who over-built into a glut, missed a
> node, or torched cash on overpriced M&A.**

**Acquisition track record [APPENDIX — illustrative, verify; capital allocation is destiny in a capex industry]:**
| Acquirer → Target | ~Value | Verdict | Why |
|---|---|---|---|
| AMD → **Xilinx** (2022) | ~$49bn (stock) | **Created** | Stock-funded at peak; broadened DC/FPGA franchise |
| Nvidia → **Mellanox** (2020) | ~$7bn | **Created** | Networking became core to AI systems |
| Nvidia → **Arm** (attempted, 2020–22) | ~$40bn | Blocked | Regulators killed it; avoided overhang |
| SoftBank/Arm | ~$32bn (2016) | Mixed→OK | Later IPO'd; strategic IP toll-booth |
| Intel → **Altera** (2015) | ~$16.7bn | **Destroyed→spun** | Synergies failed; later divested |
| Intel → **Mobileye** (2017) | ~$15bn | Mixed | IPO'd a stake; auto-AI optionality |
| Broadcom → **VMware** (2023) | ~$69bn | Jury out | Debt-funded software pivot, margin extraction play |
| ADI → **Maxim / Linear** | ~$21bn / ~$15bn | **Created** | Disciplined analog roll-up, sticky franchises |

- **Node/capex-timing lens:** judge management by *cycle timing + execution*, not spend. TSMC's
  disciplined leading-edge bets compounded; Intel's repeated **node delays (10nm/7nm)** ceded
  leadership and value. **[H]**
- **Pattern [H]:** value-destroyers share traits — **a missed node, over-build into a glut, or
  debt-funded peak M&A.** Compounders **timed capex, held node leadership, and returned cash with
  discipline** (TSMC, ASML, analog roll-ups).

## 11. Evaluate-a-Semi-Business — weighted rubric ⭐  [CORE]
| # | Criterion | Weight | Why |
|---|---|---|---|
| 1 | **Chokepoint / moat strength** (node, EUV, EDA, packaging, software) | 25% | Determines durability of pricing power |
| 2 | **Cycle/capex discipline** (timing, inventory, ROIC through cycle) | 20% | Avoids glut value-destruction |
| 3 | **Technology roadmap execution** (node/packaging on time) | 20% | A missed node halves a franchise |
| 4 | **Geopolitical exposure** (concentration, China, export controls) | 15% | Now a first-order risk |
| 5 | **Customer/ecosystem lock-in** (trust, design wins, software) | 10% | Stickiness of demand |
| 6 | **Capital allocation / balance sheet** | 10% | Funds capex without distress |
|   | **Total** | **100%** | |
**Scale:** 1 red flag · 3 average · 5 best-in-class. **Good = chokepoint + cycle-disciplined + on-roadmap + geo-diversified + locked-in customers + funded.**

## 12. Company Deep Dives  [CORE: TSMC · APPENDIX: full table]
**Tiers:** *Chokepoint leaders* TSMC, ASML, Synopsys/Cadence · *Fabless winners* Nvidia, AMD, Apple
(captive), Broadcom, Qualcomm · *Memory* SK Hynix, Micron, Samsung · *Equipment* AMAT, Lam, TEL ·
*Challengers/turnarounds* Intel, Samsung-foundry, Rapidus · *Laggards/at-risk* SMIC (sanctioned),
subscale trailing-edge.

**Scored ranking [APPENDIX] (illustrative — verify):**
| Company | C1 Moat | C2 Cycle | C3 Roadmap | C4 Geo | C5 Lock-in | C6 Capital | **Weighted /5** | Rank |
|---|---|---|---|---|---|---|---|---|
| **TSMC** | 5 | 4 | 5 | 3 | 5 | 4 | **4.35** | 1 |
| ASML | 5 | 4 | 5 | 4 | 5 | 4 | **4.50** | 1 |
| Nvidia | 5 | 3 | 5 | 3 | 5 | 5 | **4.20** | 3 |
| Synopsys | 5 | 4 | 4 | 4 | 5 | 4 | **4.35** | 1 |
| SK Hynix | 3 | 3 | 4 | 3 | 3 | 3 | **3.20** | 5 |
| Intel | 3 | 2 | 3 | 4 | 3 | 3 | **2.90** | 6 |
> *(ASML and Synopsys score at/above TSMC on pure defensibility; TSMC ranked the worked example as
> the manufacturing chokepoint with the broadest leverage to the AI build.)*

### Company: TSMC  [CORE — best-positioned, scored end-to-end]
- **Positioning:** the world's leading-edge foundry; **>60% foundry share**, node leadership
  (3nm→2nm), and the **CoWoS advanced-packaging** chokepoint for AI accelerators. Sits at the
  *highest-value, most-defensible* manufacturing node of the chain — Nvidia, Apple, AMD all depend on it.
- **Scorecard 4.35/5:** elite on moat(5)/roadmap(5)/lock-in(5); strong capital(4)/cycle(4); the
  one knock is **geographic concentration (3)** — Taiwan tail risk, mitigated by Arizona/Japan/Germany fabs.
- **Financials [illustrative]:** revenue ≈ **$90bn**, **gross margin ~53–56%**, **net cash**, **ROE
  high-20s%**, capex ≈ **$30bn+/yr**, R&D high. **[M, verify]**
- **Geopolitics:** Taiwan concentration is *the* swing factor; track fab-diversification progress
  and Strait risk. **[M]**
- **★ Moat analysis [CORE — not all growth is equally durable]:**
  | Moat type | Strength | Evidence |
  |---|---|---|
  | Scale | **Strong** | >60% foundry share; cost + yield-learning lead |
  | Brand/Trust | **Strong** | "Pure-play, no-compete" — fabless trust it with crown-jewel designs |
  | Regulatory/Geo | Medium | CHIPS-backed AZ fabs **but** Taiwan concentration caps it |
  | Distribution/Ecosystem | **Strong** | Deep IP/EDA/OSAT ecosystem + reference flows |
  | Pipeline (roadmap) | **Strong** | Node lead (2nm) + CoWoS packaging = durable, hard to replicate |
  | Switching costs | **Strong** | Re-taping a leading design to another foundry is costly + risky |
- **Triggers:** 2nm ramp, CoWoS capacity expansion, AI-accelerator demand, fab-diversification milestones.
- **Risks:** Taiwan geopolitics, AI capex digestion, a credible Intel-18A/Samsung node challenge, capex over-build.

## 13. Failure Modes — Historical Graveyard  [APPENDIX]
- **Who died / why:** **Intel** — missed **10nm/7nm** nodes, ceded leadership to TSMC, **foundry
  stumbles**, massive value erosion (the canonical "missed-node" failure). **GlobalFoundries** —
  **exited the 7nm race (2018)**, conceded the leading edge, retreated to specialty. **Elpida**
  (bankrupt 2012, absorbed by Micron) and **Qimonda** (bankrupt 2009) — **memory price-war deaths**
  in a brutal DRAM glut. Japan's once-dominant DRAM makers largely **exited**; **AMD nearly died**
  before going fabless. **SMIC** — capped out, **cut off from EUV/leading edge** by sanctions.
- **Recurring pattern:** *missing a node + over-building into a commodity glut + capital intensity
  with no pricing power* = the value-destruction recipe. **[H]**
- **Base rate:** the leading edge has gone from **~20+ players to ~3** in two decades — Moore's-Law
  economics is a serial killer; **recovery from a missed node is rare and slow (years), sometimes never.** **[H]**

## 14. Live Risk Dashboard — thesis-killers TODAY  [APPENDIX]
| Thesis-killer | Status | Tripwire (early tell) | Severity |
|---|---|---|---|
| Taiwan Strait disruption | Latent tail | Military/political escalation | **Very High** |
| AI capex digestion / glut | Watch | Hyperscaler capex cuts; rising inventory days | **High** |
| TSMC loses node lead | Low now | Intel 18A / Samsung 2nm credible ramp | High |
| EUV monopoly curbed | Low | Export rules curb ASML; new entrant (none near) | Medium |
| Memory price collapse | Cyclical | HBM oversupply; contract-price drop | Medium–High |
| Export-control escalation | Active | New Entity-List / tool bans | Medium–High |
| CHIPS/fab execution slips | Watch | Cost overruns, delays at AZ/Ohio/Dholera | Medium |

## 15. Consensus vs Variant View ⭐  [CORE]
| Consensus | Variant view | Conf |
|---|---|---|
| "AI lifts all chips; semis go up and to the right" | **Durable value concentrates in chokepoints (TSMC/ASML/EDA) + the AI 2nd-order chain (HBM→packaging→power→cooling); the merchant long-tail commoditises; and a cyclical digestion air-pocket is under-priced** | **[M]** |
- **Supporting:** TSMC/ASML pricing power through cycles, EDA duopoly renewals, HBM/CoWoS sold out,
  hyperscaler custom-silicon shift squeezing merchant vendors, history of post-build gluts.
- **Contradicting (steelman the bears):** AI demand may be more durable/less cyclical than past
  cycles; Intel-18A or Samsung could break TSMC's lead; export controls could fragment the chokepoints;
  power/cooling 2nd-order names may already be priced.
- **★ FALSIFICATION TEST — proven WRONG if:** (a) **TSMC loses the node lead** (Intel 18A/Samsung 2nm
  ramp in volume with major wins), **or** (b) the **EUV monopoly is broken or hard-curbed**, **or**
  (c) **AI capex proves non-cyclical** — no inventory glut, no digestion air-pocket over 4–6 quarters,
  **or** (d) **HBM/advanced-packaging oversupplies fast**, collapsing that premium.

## 16. Valuation, Verdict & Investment Fit  [CORE]
- **Method:** *not* one multiple for all. **Chokepoints (TSMC/ASML/EDA):** premium P/E + DCF on
  durable FCF, accept higher multiples for moats. **Memory:** **EV/EBITDA through-cycle + replacement
  cost / book**, buy near trough. **Fabless (Nvidia/AMD):** P/E vs design-win-driven growth, watch the
  cycle. **Equipment:** book-to-bill + backlog. Always apply an explicit **geopolitical discount** to
  Taiwan-concentrated names and a **cyclicality discount** to capex-heavy commodity segments.
- **Read:** segment-dependent — chokepoints deserve premiums; commodity memory and trailing logic are
  cheap-for-a-reason mid-cycle. **[M]**
- **Triggers:** 2nm/CoWoS ramps, memory price recovery, capex-guide inflections, export-control headlines,
  India fab/ATMP milestones.
- **Conclusion (answers the Research Question):** durable value **is** concentrating in chokepoints +
  the AI 2nd-order chain; a cyclical digestion air-pocket is likely. **Own the chokepoint compounders
  (TSMC, ASML, EDA) through the cycle; play HBM/packaging/power as 2nd-order; trade the cyclicals
  (memory, broad logic) around the glut; avoid subscale trailing-edge.** **[M]**
- **INVESTMENT FIT:**
  | Fit | Yes/No | At what price/cycle |
  |---|---|---|
  | Compounder | **Yes** (TSMC, ASML, Synopsys/Cadence) | Pay up only with node lead + clean roadmap |
  | Cyclical | **Yes** (memory, equipment) | Buy near the inventory/capex trough, not the peak |
  | Turnaround | Selective (Intel) | Only on credible 18A/foundry proof points |
  | Special situation | Selective (India ATMP/fab, M&A breaks) | Event-driven, sized small |

## 17. Data Sources & How to Track  [APPENDIX]
- **Industry data:** **SIA / WSTS** (market + book-to-bill), **SEMI** (equipment, fab capacity),
  **TrendForce / Yole** (memory, packaging), **Gartner/IDC**.
- **Company:** TSMC monthly sales + quarterly calls; ASML/AMAT/Lam orders + backlog; Nvidia/AMD/Intel
  earnings; SK Hynix/Micron/Samsung memory guides; 10-Ks / investor decks.
- **Policy:** US BIS export-control rules / Entity List, CHIPS Act awards, EU/Japan/Korea incentives,
  **India ISM/MeitY** announcements (Tata, Micron, ISM scheme).
- **Monitoring cadence:** TSMC monthly sales; quarterly capex guides + book-to-bill + inventory days;
  memory contract prices (TrendForce); export-control newsflow (event-driven); India fab/ATMP milestones.

## 18. Research Log  [APPENDIX] — living document (seed entries; append on each new data point)
| Date | Observation (fact, sourced) | Impact on thesis | Conf |
|---|---|---|---|
| _illustrative_ | TSMC leading-edge sold out; CoWoS capacity allocated | + (chokepoint thesis) | [M] |
| _illustrative_ | Memory contract prices recovering off 2023 trough; HBM tight | + (cycle turn + 2nd-order) | [M] |
| _illustrative_ | New US export-control tightening on advanced GPUs/tools to China | − (China rev) / + (incumbent moat) | [M] |
| _illustrative_ | Intel 18A milestones progressing | − (node-lead falsification watch) | [L] |
| _illustrative_ | Micron Sanand ATMP + Tata Dholera fab progressing (India) | + (India angle) | [L] |
| _<add next>_ | | | |
