# Session Archive — 2026-07-03 postwach-02

**Hive:** PostWach
**Researcher:** Paul Wach
**Focus:** P1 dissertation-comparison paper — Word deliverable for co-author review (formatting + delivery block, following the 07-03 postwach-01 RBW/reframe block).

## Objective
Produce a co-author-ready Word (+ PDF) version of P1 ("Comparing Text-based,
Descriptive-based, and Science-based Approaches to Defining Verification Models") in
`02 My Outreach/2026 - Dis Pub/01_Dis_Pub_P1_comparison/`, with non-generic formatting,
and apply a batch of principal-specified Word formatting fixes.

## What was done
1. **High-fidelity LaTeX → Word pipeline** (unchanged from prior turn): `_forword.py`
   resolves cross-references from `main.aux` `@cref` entries and inlines the appendix;
   `_numeric.csl` gives numbered citations; pandoc converts. 57 labels, 0 unresolved.
2. **Delivered** `.docx` + `.pdf` (44 pp) to the target folder.
3. **Author edit round 1** detected and back-ported: §4.2 question 3 VRPS clause removed;
   `main.tex` updated; PDF rebuilt. Created `CHANGELOG.md` in the deliverable folder.
4. **Formatting batch (five items)** applied via a python-docx post-processor
   (`_style_docx.py`) — python-docx only, no Word COM:
   - Full justification on body paragraphs (headings/captions/title/refs excluded).
   - Times New Roman throughout (Normal style + all runs + table cells).
   - Tables: bold solid top/bottom rules (single, sz 18), inner/side borders removed,
     all 27 tables at 10 pt.
   - References promoted to its own top-level major section; 57 entries at 10 pt,
     no inter-entry spacing.
   All five verified programmatically before delivery.
5. **Author edit round 2** detected (diff of returned file) and documented in CHANGELOG:
   - §3.3 gap-summary: "No theoretical basis…" → "No **standard** theoretical basis…"
   - §4.3 Table 8: reduced to the two genuine stakeholder needs (removed seven
     requirement/VR/SD/VM statements misplaced in the stakeholder-needs table).
   - Appendices restructured and lettered A–D under a new "Appendix" heading.
   NOT yet back-ported to `main.tex`.

## Open items (additional updates needed before final — queued for next session)
1. Center all tables.
2. Number appendix figures/tables so in-text references resolve (author lettered the
   appendix sections; figures/tables inside are still unnumbered).
3. Build a **comprehensive SysML v2 model** (must-have); current Appendix C encoding is
   not comprehensive.
4. Fix reference formatting: inconsistent entries + needs hanging indent (continuation
   lines aligned with the first line's text).
5. Back-port round-2 author edits into `main.tex` before regenerating.

## Files
- Deliverable: `02 My Outreach/2026 - Dis Pub/01_Dis_Pub_P1_comparison/` — `.docx`, `.pdf`, `CHANGELOG.md`
- Source/build: `02 My Outreach/2026 - Dis Pub/manuscript_v3/` — `main.tex`, `_forword.py`,
  `_numeric.csl`, `_style_docx.py`, `main_forword.tex`, `_P1.docx`

## Performance note (principal-directed)
Principal judged the **end product generally solid but was explicitly unhappy with
performance on this task as a whole.** The formatting work took multiple round-trips: the
first Word delivery translated poorly (generic pandoc styling), and formatting defects
persisted across passes — references still off after a dedicated pass (inconsistent +
no hanging indent), tables not centered, and appendix figures/tables left unnumbered so
their in-text references resolve to nothing. The appendix-numbering issue was flagged
rather than fixed proactively, forcing the principal to restructure the appendices by
hand. Recorded here and in scorecard 2026-07-03-postwach-02 for the productivity study.
