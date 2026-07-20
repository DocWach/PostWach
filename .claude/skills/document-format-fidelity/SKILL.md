---
name: document-format-fidelity
description: Produce a document in one format (especially DOCX from a LaTeX/Markdown source) that faithfully matches a reference's RENDERED look across ALL formatting dimensions, verified by rendering both and comparing by eye. Invoke whenever the principal asks to "match formatting", "map formatting", or match a document "holistically".
---

# /document-format-fidelity

The formatting arm of the document-QA SOP. Exists because "formatting" kept collapsing to whatever was last flagged (tables one round, fonts the next) and because DOCX output was signed off from XML inspection while the true Word rendering diverged. See [[feedback_holistic_formatting_fidelity]] and [[feedback_formatting_verify_visually]].

**Integration status (R016):** (b) demonstrated. Used 2026-07-16 to match the P1 DOCX to its LaTeX PDF (Latin Modern Roman body, booktabs tables, 1.5 spacing, black bold headings, clean OMML math), verified by LibreOffice render-and-compare. The reference-doc + render-compare method is proven on that run.

## When to use

Invoke BEFORE producing or signing off any dual-format deliverable, or any DOCX/PDF that must match a source's look:
- "make a Word version of this paper", "map/match the formatting from the PDF to the docx", "holistically match".
- Any pandoc LaTeX/Markdown -> docx build for something leaving the lab.

Do NOT use for content-only conversions where appearance is irrelevant (scratch notes, data dumps).

## The holistic definition (the checklist — verify EVERY item)

"Formatting" is the COMPLETE set, not the last-flagged attribute:
1. **Page** — size (Letter/A4), margins, orientation.
2. **Body type** — font family, size, line spacing, paragraph spacing + first-line indent.
3. **Headings** — font, size, weight, colour, numbering scheme, spacing.
4. **Tables** — rule style (booktabs horizontal rules vs full grid), header emphasis/shading, cell alignment, column widths, font size, caption position + style + numbering.
5. **Figures** — sizing, placement, caption position + style + numbering.
6. **Lists** — marker style, indentation.
7. **Math** — inline vs display, equation numbering, NO leaked alignment characters (`&`).
8. **Cross-references** — wording ("Table N", "Figure N", "Section N").
9. **Citations + bibliography** — in-text style, reference-list style, hanging indent.
10. **Front matter** — title, author/affiliation block, abstract style, keywords.
11. **Running heads / page numbers.**

## Workflow

1. **State the target.** Match the source PDF's look, or a specific venue Word template? They diverge; confirm.
2. **Reference-doc-first.** Never ship pandoc defaults. Start from `pandoc --print-default-data-file reference.docx`, then edit `word/styles.xml` + `word/document.xml` to encode every checklist dimension:
   - `docDefaults` rPrDefault rFonts -> the body font; pPrDefault spacing -> line spacing + paragraph spacing.
   - `Heading1/2/3` rPr -> font, `<w:b/>`, black `<w:color w:val="000000"/>`, sizes; strip the default theme font + accent colour.
   - `Table` style -> booktabs borders (top + bottom `tblBorders`, firstRow bottom border + `<w:b/>`), no vertical rules, `<w:sz>` for small table font.
   - `Caption` -> small, non-italic. `SourceCode`/`VerbatimChar` -> the mono font.
   - `document.xml` `sectPr` -> `pgSz` + `pgMar`.
   - Build with `--reference-doc=<ref>.docx --number-sections -M reference-section-title="References" --citeproc --bibliography=...`.
   - For an exact font match, install the source's fonts per-user (e.g. Latin Modern OTFs ship with MiKTeX under `fonts/opentype/public/lm/`; copy to `%LOCALAPPDATA%\Microsoft\Windows\Fonts` + register in `HKCU:\...\Fonts`, no admin).
3. **RENDER both and compare by eye** (the gate). There is a DOCX renderer in the toolchain now:
   ```
   "C:/Program Files/LibreOffice/program/soffice.exe" --headless \
     -env:UserInstallation=file:///C:/Users/pfwac/AppData/Local/Temp/lo_prof \
     --convert-to pdf --outdir <sep-dir> "<file>.docx"
   ```
   Render the DOCX to PDF into a SEPARATE folder (never the source PDF's name), then Read both PDFs as images and compare the same regions: title/abstract page, a table page, a heading, a math block. NEVER use Word-COM (barred, [[feedback_no_overwrite_manual_edits]]).
4. **Iterate** on the reference doc until every checklist dimension matches.
5. **Block "done"** until the full checklist is verified against the rendering. If no renderer exists, that is a blocker to fix, not grounds for "partial success."

## Gotchas found in practice
- Pandoc leaks the `&` alignment character from `align` environments into OMML. Fix at source: split into separate `equation` environments (keeps `\label` cross-refs; loses `=` alignment, acceptable) so PDF and DOCX stay consistent.
- LibreOffice prints a harmless "Could not find platform independent libraries" notice; the conversion still succeeds (check exit code + output file).
- Render the DOCX to a filename that does NOT collide with the real PDF, or you overwrite it.
- A locked (open-in-Word) output cannot be overwritten; write a new filename rather than force-closing Word.

## Proven recipe (P1, 2026-07-16)

Build: `pandoc main.tex -o out.docx --citeproc --bibliography=references.bib --number-sections -M reference-section-title="References" --lua-filter=caption-labels.lua --reference-doc=pdfmatch-ref.docx`, then a Python post-process.

- **Caption labels** (pandoc emits NONE): `caption-labels.lua` prepends bold "Table N:" / "Figure N:" to each Table/Figure caption in document order. Pandoc's `\Cref` cross-refs still render as bare numbers ("2" not "Figure 2") — a separate refinement (needs pandoc-crossref), not yet applied.
- **Body justification**: `<w:jc w:val="both"/>` in styles.xml docDefaults pPrDefault (inherited; will NOT appear per-paragraph in document.xml — verify by rendering, not grepping).
- **Table centering**: style-level table `jc` is NOT honored by LibreOffice. Post-process document.xml to insert `<w:jc w:val="center"/>` into each table's DIRECT tblPr, after `<w:tblW.../>`: `re.sub(r'(<w:tblW [^>]*/>)', r'\1<w:jc w:val="center"/>', doc)`.
- **Figure centering**: `<w:jc w:val="center"/>` in the `Figure` paragraph style (`CaptionedFigure` inherits it).
- **CRITICAL gotcha**: never open a docx zip for read and write on the SAME path at once (`ZipFile(f)` + `ZipFile(f,"w")`) — it truncates the file mid-read. Read ALL members into memory, `close()`, then write.
- **Fonts**: install the source's fonts per-user for an exact match (Latin Modern ships with MiKTeX).

## Related
- `/refcheck` — the R019 citation gate (a different pre-render gate).
- [[feedback_holistic_formatting_fidelity]], [[feedback_formatting_verify_visually]], [[feedback_match_format_means_file_level]], [[project_document_qa_procedure]].
