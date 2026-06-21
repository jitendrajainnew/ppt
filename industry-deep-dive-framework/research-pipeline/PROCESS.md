# Research Pipeline — the framework for *doing* the research

> The deep-dive framework (`../README.md`) is the **map**. This is the **machine** that fills it
> with real, primary-source data: download → extract → organize → read → synthesize.
> It operationalises the 7-stage workflow ("pharma.md is the operating system, not the report").

## The pipeline

```
  TICKERS ──► [1] LINKS ──► [2] FETCH ──► [3] EXTRACT ──► [4] ORGANISE ──► [5] READ ──► [6] SYNTHESISE
  (NSE/BSE)   Screener      curl bulk     pdfminer        per-module       extract      OS assets
              doc lists     download      PDF→text        research DB       claims+      (dashboard,
                                                                            evidence     scorecards,
                                                                                         memo)
```

| Stage | Tool | Output |
|---|---|---|
| **1. Links** | `pipeline.py links` | Scrapes Screener for each ticker's annual reports, concall transcripts, investor presentations → `data/raw/<TICKER>/_links.json` |
| **2. Fetch** | `pipeline.py fetch` | Bulk-downloads a prioritised subset (newest-first) via `curl` → `data/raw/<TICKER>/*.pdf` + `_manifest.json` |
| **3. Extract** | `pipeline.py extract` | `pdfminer` → `data/text/<TICKER>/*.txt` (readable plain text) |
| **4. Organise** | manual / `research-db/` | Map extracted text to the 12 framework modules (the per-module research folders) |
| **5. Read** | the analyst (you/agent) | Read transcripts + MD&A; pull **claims with evidence + source + date** |
| **6. Synthesise** | the OS assets | Update Dashboard, Company Scorecards, Question Bank, Investment Memo |

## Quickstart

```bash
cd research-pipeline
python3 scripts/pipeline.py all SUNPHARMA CIPLA DIVISLAB DRREDDY TORNTPHARM
# tune volume:  MAX_AR=2 MAX_CALL=6 MAX_PPT=1 python3 scripts/pipeline.py all <tickers>
```

Then read `data/text/<TICKER>/*.txt` and feed findings into `../examples/<industry>-os/`.

## What to read, and what to pull from each doc type

| Document | Read for | Feeds module |
|---|---|---|
| **Concall transcript** | Management's *own framing*, guidance, what they're worried about, Q&A tells → **variant-view signals** | 8 Demand, 15 Variant View |
| **Annual report (MD&A)** | 10-yr financials, **capital-allocation history**, segment detail, risk factors | 10 Capital Alloc, 12b Timeline, 16 Valuation |
| **Investor presentation** | Current KPIs, pipeline, capacity, guidance slides → **dashboard** | 8b KPI Dashboard |
| **Results press release** | Hard FY numbers (revenue, margin, ROCE, mix, R&D) | 11/12 Scorecards |
| **Ratings rationale / regulator** | Leverage, compliance status, independent view | 5c Red Flags, 9 Regulation |

## Source-quality discipline (per `../TEMPLATE.md` 17b)
Tag every extracted claim **[S: source, date]** and weight by tier: filing/regulator = 5,
transcript = 4, industry report = 3, expert = 2, social = 1. Primary documents (this pipeline)
are tier 1–2 — the highest-confidence inputs.

## Storage policy
- `data/raw/` (PDFs) and `data/text/` (extracted text) are **git-ignored** — they're large and
  reproducible. Re-run the pipeline to regenerate.
- **Committed:** the scripts, `PROCESS.md`, the `_manifest.json` (what was downloaded), and the
  **synthesised notes** in `research-db/` + `../examples/<industry>-os/`.
- The raw corpus lives in the working container; the *distilled knowledge* lives in git.

## Limitations / notes
- Screener exposes clean URLs for established names; recently-listed companies (e.g. Mankind)
  may only show opaque BSE `AnnPdfOpen` links that need anchor-text parsing to categorise.
- Some hosts (NSE, a few IR sites) rate-limit or 403 anonymous `curl`; the downloader records
  failures in the manifest and continues.
- Annual reports are large (10–60 MB) and OCR-quality varies; extraction is best-effort.
