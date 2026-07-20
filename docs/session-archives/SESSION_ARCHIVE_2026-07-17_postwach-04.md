# Session Archive: Remove co-author (Nicole Hutchison) from IS 2026 Vision-for-RE paper + regenerate PDF
**Date:** 2026-07-17
**Hive:** PostWach (CTO / Chief Scientist)
**Type:** Deliverable edit (manuscript authorship change) + render
**Provenance (R018):** claude-opus-4-8[1m], Anthropic, Claude Code CLI, principal-directed.
**Status:** DONE. Edited docx + regenerated PDF delivered; visually verified.

## Objective
Remove Nicole Hutchison from the INCOSE IS 2026 paper ("Vision 2035: Exploring the Future of
Requirements Specification"), in
`02 My Outreach/IS 2026 - Vision for RE`, and regenerate the PDF.

## What was done

### 1. Located her three roles in the current deliverable
Current deliverable = `_workspace/Vision_2035_RE_Revised_2026-06-14.docx` -> `Vision_2035_RE_Revised_2026-06-14.pdf`
(Word-produced, 12 pp). The author block and bios are in **tables** (not `doc.paragraphs`), found via
python-docx table inspection:
- **Author block** (Table 0, 2x3): r0c2 = Nicole Hutchison, National Security Institute, Virginia Tech, `nlong@vt.edu`.
- **Bio** (Table 2): r2c1 = her end-of-paper biography.
- **Citations** (7 paragraph mentions): body + reference list -- Helix/WRT-1004 (2020), DECF INSIGHT (2022),
  CESUN 2025 (Jurczyk et al.), WRT-2406 (2025c). These are references to her PUBLISHED works, not authorship.

### 2. Scoping decision
Principal's instruction ("author info upfront and her bio at the end") = the two authorship locations only.
**Kept the citations** -- removing legitimate scholarly references would break the bibliography and misrepresent
the record. Surfaced this decision explicitly rather than asking.

### 3. Surgical edit (python-docx, on a dated copy -- never overwrote the live 06-14 file)
Copy -> `_workspace/Vision_2035_RE_Revised_2026-07-17.docx`.
- Author block: deleted Nicole's cell content; **reflowed** Karson Sandman (was r1c0) into r0c2 so three authors
  sit cleanly across the 3-column row (Paul Wach / Taylan G. Topcu / Karson Sandman); cleared the now-empty row 1.
  Moved paragraph XML with `copy.deepcopy` to preserve run/cell formatting; kept each cell's `tcPr` (widths intact).
- Bios: deleted Nicole's table row (`t2._tbl.remove(row._tr)`), leaving Paul / Taylan / Karson.

### 4. Regenerated + verified
Rendered with **LibreOffice headless** (`soffice --headless --convert-to pdf`) ->
`Vision_2035_RE_Revised_2026-07-17.pdf` (main folder, alongside the other Revised PDFs).
Verified by extracting text AND rendering page 1 + the bio page to PNG and LOOKING
([[feedback_formatting_verify_visually]]): author row is a clean 3-column layout with no gap; Biography ends
with the three remaining authors; Hutchison reference-list citations preserved.

## Fidelity caveat (flagged to principal)
The official 06-14 PDF was **Microsoft Word**-produced (12 pp). I cannot drive Word here (COM barred per
[[feedback_no_overwrite_manual_edits]]), so this PDF is **LibreOffice**-rendered (10 pp) -- content/structure
identical, only line/page breaks differ. For a page-exact Word match, principal can open the edited
`...2026-07-17.docx` and export from Word.

## Artifacts
- `_workspace/Vision_2035_RE_Revised_2026-07-17.docx` (edited source)
- `Vision_2035_RE_Revised_2026-07-17.pdf` (regenerated, main folder)

## Files touched
Created: edited docx, regenerated PDF, this archive, scorecard `2026-07-17-postwach-04.yaml`. Modified: none
(worked on a copy; the 06-14 originals untouched).
