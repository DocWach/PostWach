# Session Archive — 2026-07-15 postwach-04

**Hive:** PostWach (CTO / Chief Scientist)
**Topic:** P1 "Asserted or Entailed?" — five review-miss corrections + root-cause report, by-approach Results restructure, PDF/DOCX rebuild
**PROVENANCE:** Opus 4.8 (claude-opus-4-8[1m]), Anthropic, Claude Code CLI, principal-directed.
**Status:** CLOSED. Continuation after postwach-03; opened when the principal found five defects on first read of the postwach-03 "done" deliverables.

## Charge

On first read of the postwach-03 PDF/DOCX the principal flagged five items every prior review had missed, and asked for the corrections plus an extensive root-cause report on how they survived.

## What happened

1. **Root-cause report (item 5).** `docs/P1_review_misses_rootcause_2026-07-15.md`. Core diagnosis: every review checked correctness of what was present (cites, overfull, undefined, content-present); none held the agreed design as the oracle, so a wrong structure, an orphaned figure, a missing table dimension, and unrendered DOCX tables were all invisible. The highest-value requirement (match Alejandro's structure) was the only one with no gate. Six preventive gates proposed; the document-QA SOP promoted from TODO to next build task.

2. **The definitional gap / Table 4 (item 1).** Debated three options; proposed and applied cutting §3.3 (Alejandro's stance) and folding THE gap into Related Work as one gap with two faces, practice (standards/SysML assess or trace but cannot make adequacy checkable) and theory (no mathematical foundation for the definitional question, per the mathmbse SLR). Dropped the gap-summary table, which duplicated the Results comparison (Table 11).

3. **Methods visual (item 3).** The protocol figure (`figures/protocol_map.png`) was created and approved in a prior session but never inserted; it was in neither the PDF nor the DOCX. Inserted into Methods Overview (§4.1) with a numbered caption and an in-text callout. **Caught by render-and-look:** the figure content was itself stale, hard-coding "one subsection per question" (the rejected structure); regenerated the Mermaid source to by-approach and rebuilt the PNG via mmdc.

4. **Results by-approach (item 4).** Transposed §5 from by-question (establish / relationships / how-mathematical / admitted / summary, the form Alejandro rejected) to by-approach: 5.1 Structural overview, 5.2 Text-based, 5.3 Descriptive-based (SysML listing moved inline), 5.4 Science-based (identity-isomorphism worked example moved inline), 5.5 Comparison. The two shared assessment axes were consolidated into the overview; the appendix reduced to the complete SD-to-VM-A proof only. Fixed three dangling `\Cref{how-mathematical}` in `appendix_proof.tex`, and one duplicate `fig:sysmlv2` label.

5. **DOCX formatting fidelity (item 2).** Built a custom pandoc reference document whose Table style matches the PDF booktabs (top rule, bold header + mid rule, bottom rule, no vertical grid) and rebuilt the DOCX against it (23 Table-style references applied, 0 unresolved citations, References heading, protocol + WySE figures, listing present). Limitation recorded: no DOCX renderer in this environment, so visual table confirmation is the principal's in Word.

6. **Rebuild + verify.** PDF via latexmk: 40 pages, 0 overfull (h+v), 0 undefined, 0 multiply-defined. Verified by rendering and looking at page 1, the protocol figure (page 12), the SysML listing (page 21), and the by-approach Results (page 19). R019 gate re-run on the restructured source: 50/50, 0 missing. New filenames carry a `_restructured` tag because the postwach-03-named files were locked open in Word (Word not force-closed, per the hazard rule).

## Key result

P1 now matches the agreed by-approach Results structure that Alejandro required; the orphaned protocol figure is placed and corrected; the gap is stated once with both faces; and the DOCX tables carry a booktabs-matching style. The build is clean and the R019 gate holds.

## Decisions / status

- §3.3 cut and folded (principal asked for a debated proposal; Option A proposed and applied). **Confirmed by principal 2026-07-16** ("much closer to what was agreed and expected"); no gap table. Decision closed.
- Results order 5.1-5.5 (LaTeX 1-indexed) = the principal's 5.0-5.4 by-approach request.
- DOCX citations remain author-date (no IEEE CSL); PDF is citation-style-authoritative.
- Deliverables: `Asserted_or_Entailed_Verification_Models_P1_restructured_2026-07-15.{pdf,docx}`. The postwach-03 files are superseded (safe to close in Word).
- Open: the document-QA SOP (root-cause measure 1) is the next PostWach build task; measures 1-3 recommended to Alpha Empress for portfolio governance.

## Artifacts produced / modified

- `manuscript_v3/main.tex` (Results restructure, gap fold, protocol figure, author/appendix edits), `appendix_proof.tex` (ref fixes), `figures/protocol_map.mmd` + regenerated `.png`
- `manuscript_v3/custom-ref.docx` (booktabs table style), `..._restructured_2026-07-15.pdf` (40 pp) + `.docx`
- `01 PostWach/docs/P1_review_misses_rootcause_2026-07-15.md`
