# Research Database — distilled primary-source notes

> Stage 2 of the workflow: every module / company becomes a research note backed by **primary
> documents** pulled by `../research-pipeline/`. This is where raw annual reports + transcripts
> get distilled into *evidence with sources*, feeding the OS assets in `../examples/<industry>-os/`.

## What's here

| File | Source depth | Feeds |
|---|---|---|
| [`SUNPHARMA-deep.md`](SUNPHARMA-deep.md) | Sun Pharma AR FY21-22 + FY20-21 + FY25 results (read in full) | Scorecards, Capital-Alloc Timeline (12b), Variant View |

*(Anchor company done end-to-end as the template; same pattern applies to the rest of the universe.)*

## The method (per company)
1. **Pull** documents via the pipeline (annual reports, transcripts, results).
2. **Extract** the long-run data: the **Ten-Year Financial Highlights** table (every Indian AR has one)
   = instant 10-yr revenue / profit / R&D / net-worth / returns trajectory for Module 12b.
3. **Read** the MD&A + risk factors for capital-allocation history and red flags.
4. **Distil** into a deep file: the trajectory, the *story the numbers tell* (Evidence→Interpretation
   →Conclusion), capital allocation, pipeline, live risks, and a steelmanned bear case.
5. **Feed** the scorecards / dashboard / memo in `../examples/pharma-os/`.

## Honest data note (what the pipeline could and couldn't reach)
- ✅ **Annual reports** downloaded + read → real **10-year financial histories** (e.g. Sun's FY18
  profit trough, the whole point).
- ⚠️ Screener's **anonymous** HTML exposes an *older snapshot* of document links — the ARs/transcripts
  it surfaced were FY22/FY21 era, not the latest. The **10-year tables are still valid history**, and
  FY23–FY25 is filled from the current results releases. For the very latest transcripts you'd log in
  to Screener (or pull from company IR / BSE directly) — a one-line change to the pipeline's source.
- The corpus (161 MB, ~40 PDFs) lives in the container (git-ignored); this distilled note is the
  durable output.
