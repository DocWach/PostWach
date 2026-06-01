# Session Archive: 2026-04-12 PostWach-02

**Hive:** PostWach
**Date:** 2026-04-12
**Duration:** ~6 hours (afternoon/evening)
**Focus:** TRAK Practitioner Guide v9 → v10: reviewer feedback, WRT-2516 citation, Appendix C (9-category taxonomy), SERC template conversion, figure/table captioning (Option C), build infrastructure

---

## Session Summary

Received reviewer feedback on v8 PDF identifying six formatting and content issues (items a-f): missing Roadmap framework figure, WRT-2516 citation style, §3.4 title revision, missing 9-category evidence labels, §3 vs §4 title intent, duplicate evidence-quality table at §4.6. Addressed all six in v9.

Debated treatment of the 9-category condition-based evidence taxonomy (from Roadmap Report WRT-2516 §8.2, Table 3). Decided Option C: reproduce the full 9-category table in a new Appendix C for reference, fold §9.4 "Evidence Taxonomy Consolidation" into §9.8 "Empirical Validation" as a calibration objective.

Converted v9 markdown into sponsor-ready Word docx using the WRT-2516 template as a style reference. Built a reusable Python merge pipeline (`build_trak_docx.py`) that runs pandoc with `--reference-doc`, preserves template front matter (cover page, disclaimer, Research Team table, TOC field), updates cover-page text, strips cover-page author lines for TRAK primary authors while keeping all six in the Research Team table, and appends the pandoc-generated body via docxcompose. Fixed heading duplication bug (removed `--number-sections` from pandoc; template's Heading styles already handle numbering).

Received second round of feedback on TRAK guide:
1. Figures and Tables not referenced in text — initially proposed Option B (figures + main-body tables only), user pushed back that Option C (full captioning) is the professional standard. Conceded. Executed Option C.
2. PD outcomes bulleted list in §2.1 should be a table with ID/Title/Description columns — executed as Table 1.
3. After implementing, realized Appendix B's 49 data tables would clutter the List of Tables. Removed Appendix B captions, kept informal bold labels (§B.5) and section headers (elsewhere).

Final artifacts:
- `TRAK_Practitioner_Guide_v9_2026-04-12.pdf` (60 pages, 1 MB) - addressed reviewer items a-f
- `TRAK_Practitioner_Guide_v9_2026-04-12.docx` (3.6 MB) - SERC template conversion
- `TRAK_Practitioner_Guide_v10_2026-04-12.pdf` (~70 pages, 1 MB) - full captioning + cross-refs
- `TRAK_Practitioner_Guide_v10_2026-04-12.docx` (3.6 MB) - Word Caption style applied + Lists of Figures and Tables inserted after ToC

Raised two inter-hive policy items for future discussion: (a) shared doc-merge tooling (the pattern we built), (b) artifact storage policy (NNSA Deliverables folder has 66+ items).

## Key Decisions

- **D62:** WRT-2516 cited as `[WRT-2516] P. Wach, A. Salado, T. G. Topcu, T. McDermott, J. Gregory, and K. Sandman, "Systems Engineering Beyond the Horizon..."` in new References section. Public release, approved for unlimited distribution.
- **D63:** 9-category evidence taxonomy treatment: full table reproduced in new Appendix C (from WRT-2516 Table 3). Naming bridge added: Roadmap Report calls it "maturity taxonomy (condition-based)"; TRAK calls it "9-category evidence quality taxonomy" — same set.
- **D64:** §9.4 Evidence Taxonomy Consolidation folded into §9.8 Empirical Validation as a calibration objective (measuring inter-rater consistency between 6-level and 9-category scales).
- **D65:** §3.4 title changed to "Evidence Quality is a Property of Every Claim" (was "Evidence Quality Is Not a Dimension").
- **D66:** §4 title changed to "Three (Underlying) Practitioner Questions" (was "The Assessment Instrument (Q1-Q3)").
- **D67:** §4.6 "Evidence Quality on Every Cell" duplicate table collapsed to ~3-sentence pointer back to §3.4 and Appendix C.
- **D68:** §9.10 "8.x Organizational Constraint Modeling" legacy numbering bug fixed: retitled "Conway's Law and Organizational Constraint Prototype" (now renumbered §9.9 after §9.4 fold).
- **D69:** Cover page of docx shows TRAK primary authors (Wach, Salado); Research Team table on page 2 lists all six WRT-2516 contributors with roles preserved.
- **D70:** Report number on cover highlighted as `[REPORT NUMBER TBD]` in yellow per user note that formal numbering is not yet assigned.
- **D71:** TRAK docx uses WRT-2516 Feb 15 2026 public release template (working copy at `WRT-2516_template.docx`). Original Vision_and_Roadmap docx untouched.
- **D72:** Full figure/table captioning (Option C) adopted over B. Rationale: template includes Lists of Figures and Tables, sponsor format expects it, user pushback identified B as "less than professional."
- **D73:** Appendix B tables (49 data matrices) use informal labels (bold `**Table B.5.N:**` for Bayesian; section ### headers for 9-cell matrices), NOT numbered captions. Avoids List of Tables clutter.

## Work Completed

### TRAK v9 edits (content, addressing reviewer items a-f)
- `Section_1_2.md`: Roadmap framework figure inserted at §2 intro; WRT-2516 citation at GRL reference; §3.4 retitled; 9-category pointer updated to reference Appendix C.
- `Section_3_4.md`: §4 retitled "Three (Underlying) Practitioner Questions"; §4.6 duplicate evidence table collapsed to pointer.
- `Section_7_8.md`: §9.4 Evidence Taxonomy Consolidation deleted, calibration objective appended to §9.8 Empirical Validation.
- `Section_8_Conway_Insert.md`: "8.x" legacy heading renamed; 3 of 6 Conway figures embedded as real images (scenario config, org topology, decision impact); 3 remain textual (no screenshots).
- `Appendix_C_Evidence_Taxonomy.md`: new file, 23 lines, reproduces 9-category table verbatim from WRT-2516 Table 3 with maturity-taxonomy naming bridge and usage guidance.
- `References.md`: new file, 7 IEEE-style citations (WRT-2516, WRT-2406, DoDI 5000.89, INCOSE GWR, IEEE 29148, ISO 25000, ISO 15288).

### TRAK v10 edits (full captioning, Option C)
- `Section_1_2.md`: Tables 1-7 captioned (PD outcomes, Executional levels, GRL phases, 6-level evidence, 3 cross-dimension quadrants) with in-text cross-references.
- `Section_7_8.md`: Tables 8-12 captioned (outcomes-priority, trajectory, cell counts, binding constraint, Q3 trust).
- `Section_8_Conway_Insert.md`: Table 13 captioned (dimension mapping); Figures 2-4 cross-referenced in prose.
- `Section_1_2.md`: Figure 1 cross-referenced in §2 intro.
- `Appendix_A_Templates.md`: 10 table captions (Tables A.1-A.8 including A.4.1-3 sub-tables).
- `Appendix_C_Evidence_Taxonomy.md`: Table C.1 caption.
- `Appendix_B_Full_Assessment.md`: attempted captions, then reverted after user feedback about List of Tables clutter. B.5 restored to bold-label format `**Table B.5.N:**`.
- PD outcomes in §2.1 converted from bulleted list to Table 1 with ID | Title | Description columns per user request.

### Build infrastructure
- `build_trak_docx.py`: consolidated single-command build (markdown concat → pandoc → front-matter merge → caption style → Lists of F/T insertion).
- `build_trak_v10.sh`: PDF build via pandoc+xelatex (renamed from v9).
- Post-processing logic: walks paragraphs, applies Word's built-in `Caption` style to any paragraph matching `^(Figure|Table) [A-Za-z0-9.]+\.`. Collects entries, injects a "Lists of Figures and Tables" section immediately after the TOC field.
- Heading duplication bug root-caused: `--number-sections` pandoc flag inserts literal numbers into heading text while template's Heading styles also auto-number — doubles the prefix. Fix: omit flag, let template handle numbering.

### Reviewer feedback addressed (first round, v8 → v9)
- (a) Missing Roadmap framework image — added at §2 (Figure 1).
- (b) WRT-2516 citation — full IEEE reference in new §13 References; Roadmap Report designation used in prose.
- (c) §3.4 title off-putting — changed to "Evidence Quality is a Property of Every Claim."
- (d) 9-category labels missing — full taxonomy reproduced as Appendix C.
- (e) §3 vs §4 title/intent confusion — §4 renamed "Three (Underlying) Practitioner Questions."
- (f) §4.6 duplicate table — collapsed to pointer back to §3.4 / Appendix C.

### Reviewer feedback addressed (second round, v9 → v10)
- (1) Figure/Table references not in text — executed Option C: all figures and body/appendix-A/appendix-C tables captioned and cross-referenced.
- (2) PD outcomes as table — executed as Table 1 with ID/Title/Description columns.
- (3) Report number is placeholder — highlighted as `[REPORT NUMBER TBD]` yellow on cover page.

## Files Modified or Created

### Guide content (`01 NNSA/01 Deliverables/Practitioner_Guide_Prose/`)
- `Section_1_2.md` — tables 1-7 captioned, figure 1 xref, WRT-2516 citation, §3.4 retitle
- `Section_3_4.md` — §4 retitle, §4.6 collapse
- `Section_7_8.md` — tables 8-12 captioned, §9.4 folded into §9.8
- `Section_8_Conway_Insert.md` — §9.10 rename, figures embedded, table 13 caption
- `Appendix_A_Templates.md` — 10 table captions
- `Appendix_B_Full_Assessment.md` — B.5 bold labels restored, no formal captions
- `Appendix_C_Evidence_Taxonomy.md` — new, 9-category taxonomy + table caption
- `References.md` — new, 7 IEEE citations

### Build tooling (`01 NNSA/01 Deliverables/`)
- `build_trak_docx.py` — self-contained docx build (pandoc + front-matter merge + caption style + Lists F/T)
- `build_trak_v10.sh` — PDF build (renamed from v9.sh)
- `WRT-2516_template.docx` — working copy of template for pandoc reference-doc

### Deliverables
- `TRAK_Practitioner_Guide_v9_2026-04-12.pdf` (60 pages, 980 KB)
- `TRAK_Practitioner_Guide_v9_2026-04-12.docx` (3.6 MB)
- `TRAK_Practitioner_Guide_v10_2026-04-12.pdf` (~70 pages, 1 MB)
- `TRAK_Practitioner_Guide_v10_2026-04-12.docx` (3.6 MB)

## Memory Updates

Added two open-thread entries to `memory/MEMORY.md` and dedicated detail files:
- `memory/project_shared_doc_tooling.md` — inter-hive doc-merge tooling policy discussion
- `memory/project_nnsa_deliverables_cleanup.md` — NNSA folder cleanup deferred pending inter-hive artifact storage policy

## Open Items

1. Formal report number for TRAK (currently `[REPORT NUMBER TBD]` placeholder). Sponsor-assigned; user flagged as likely to change.
2. Inter-hive policy session: doc-merge tooling ownership + artifact storage policy (paired). Candidates for ownership: PostWach (CTO, authored), Alpha Empress (COO, standardizing), SEAD (build engineering), or standalone `DocWach/doc-merge` repo.
3. In Word, open v10 docx and F9-refresh the TOC field. Lists of Figures and Tables are inserted as static text (not a field) — they'll be accurate on first open but won't auto-update if captions change. Acceptable because rebuild regenerates them.
4. Verify v10 end-to-end in Word: check Figure 1 renders, Conway Figures 2-4 render, all 34 Table captions styled correctly, Lists of F/T section appears between ToC and body, numbering correct throughout.
5. Appendix B informal labels: may want to decide at some point whether to use SEQ fields to make them count-aware or leave fully static.

## Tier 1 Revisions (v10 → v11, from ChatGPT reviewer feedback)

Received external reviewer (ChatGPT red/blue/white team) feedback on v10. Executed Tier 1 (professional polish, low-cost, high-signal):

- **D74:** Section numbering bug root-caused and fixed with single change: `{.unnumbered}` attribute on Executive Summary heading. PDF numbering now starts at §1 Layered Framework, matching all existing internal "Section N" cross-references and the Executive Summary's own section claims. No inline edits needed to the dozens of references throughout the guide.
- **D75:** AI capability-inversion finding narrowed in Executive Summary. New wording emphasizes unvalidated AI with prompt-inlined rules on informal representation is the demonstrated failure; other AI architectures (Iterations 3-4) restore and extend trust.
- **D76:** Added "Scope of Validation" callout at end of Executive Summary (unnumbered subsection). Distinguishes validated framework elements (4-layer architecture, D1-D3, Q1-Q3, gap taxonomy, evidence taxonomies) from illustrative/exploratory elements (Bayesian priors in B.5, Conway prototype, ETV computation).
- **D77:** Added "Status: Exploratory Prototype" disclaimer box at top of §8.9 Conway's Law subsection. Notes all parameters are author-specified, barrier-to-scenario mapping is qualitative, no decision-grade conclusions.
- **D78:** Added "Multi-Assessor Adjudication" subsection to §6.2 (How to Apply, Assessment phase). Minimal protocol: independent scoring, lower-score convention on disagreement, minimum evidence level, published team composition and session protocol, adjudication count preserved.

**Tier 2 (deferred, acknowledge in any reviewer response):** Empirical validation across additional capabilities/organizations, inter-rater reliability study, Bayesian calibration. All already in §8 as future work.

**Tier 3 (declined/deferred):** Full scoring/adjudication protocol, broader validation before quantitative layer is presented as decision-supportive. Declined as out of scope for this revision; minimal adjudication (D78) addresses the cheapest version of the ask.

**Artifacts:**
- `TRAK_Practitioner_Guide_v11_2026-04-12.pdf` (~70 pages, 1 MB) - Tier 1 reviewer revisions
- `TRAK_Practitioner_Guide_v11_2026-04-12.docx` (3.6 MB) - Tier 1 + justification + table borders + SEQ-field captions + dynamic List of Figures/Tables + baked-in layout preferences

## Tier 1 Revisions Continued (v10 -> v11, completing reviewer round)

Continuing from D74-D78 above, closed out additional polish and build-pipeline enhancements:

- **D79:** All paragraph text set to fully justified via `apply_justified_alignment()` in build script. 486-487 body paragraphs affected; headings, captions, titles, and ToC entries excluded.
- **D80:** All 74 tables given top/bottom/header-row borders (booktabs-style; no vertical lines) via `add_table_bottom_borders()`.
- **D81:** Title on cover page split into two paragraphs: "Transformation Roadmap Assessment Kit (TRAK):" on line 1 and "A Practitioner Guide for Systems Engineering Capability Transformation" on line 2. Baked into build script via `split_title_into_two_paragraphs()`.
- **D82:** Page break added before Disclaimer (pushes disclaimer off title page) and before Executive Summary (gives it its own page). Baked into `apply_user_layout_preferences()` in build script. Idempotent: detects existing page breaks and skips duplication.
- **D83:** Figure and table captions converted to Word native SEQ fields (`{ SEQ Figure \\* ARABIC \\* MERGEFORMAT }` and `{ SEQ Table \\* ARABIC \\* MERGEFORMAT }`) for main-body captions. This is the XML format Word's "Insert Caption" produces natively; enables native cross-referencing. Cached numbers pre-populated (1-4 for Figures, 1-13 for Tables) so display is correct immediately without requiring F9.
- **D84:** Appendix captions (A.1 through A.8, A.4.1-3, B.5.1 through B.5.6c, C.1) kept as literal labels instead of SEQ fields, because SEQ cannot produce hierarchical labels. These 21 Appendix tables are intentionally NOT included in the List of Tables (matches earlier D73 decision to avoid clutter).
- **D85:** Dynamic List of Figures and List of Tables implemented via Word TOC fields with `\c "Figure"` and `\c "Table"` SEQ-identifier filters. These now refresh correctly with F9 (or Ctrl+A F9 for all fields). Replaced the prior static text lists.
- **D86:** Separate paragraph styles `Figure Caption` and `Table Caption` created (inheriting from built-in Caption). Not required for the SEQ-based TOC filters but useful for future style-based queries and cross-references.

**Known behavior:** On first open, Word shows a security prompt about external-link data in the Lists. This is a template-inherited prompt, not related to the TOC fields, and can be dismissed. After dismissing and pressing F9 (or Ctrl+A, F9), all three field types refresh: Table of Contents, List of Figures, List of Tables.

## Open Questions for Next Session

Logged by user 2026-04-12 for tomorrow's continuation:

1. **Scope of Validation section.** Do we need it at all? User promoted it to Section 1 (removed from Executive Summary as subsection) and unnumbered. Re-evaluate whether the content justifies a dedicated section, whether it should fold back into the Executive Summary, or whether pieces should distribute to §8 (Framework Extensions).
2. **NNSA package composition.** Decide exactly what deliverables ship to NNSA. Candidates: (a) TRAK Practitioner Guide (final v11 or later), (b) TRAK Streamlit app (the Python tool PostWach built; GI-JOE has ontology handoff open), (c) any Excel-based tool. Need a deliverable manifest.
3. **IGNITE figures (Conway Insert).** §8.9 currently uses three Conway prototype figures sourced from IGNITE '26 demonstration with NNSA-specific context. Question: should these be replaced with generic DoD imagery to make the guide more broadly applicable, or kept as NNSA-specific since NNSA is the sponsor? Trade-off: broader applicability vs. direct sponsor relevance.
4. **User documentation for Excel app and/or Streamlit app.** Do either or both ship with a user manual? Scope of each manual.
5. **VT PD Workbench review.** Virginia Tech team (Taylan) is expected to upload their portion of the PD Workbench. Review content when available and integrate with the SEAD handoff already issued (PD_Workbench_SEAD_Handoff_2026-04-10.md).

## Next Session Priorities

1. Answer the 5 open questions above.
2. Replace `[REPORT NUMBER TBD]` when sponsor-assigned number is known.
3. End-to-end review of v11 docx in Word (user task).
4. Begin inter-hive policy session for doc-merge tooling + artifact storage.
5. PD Workbench: SEAD handoff still pending (D1-D3 execution on PD_Workbench_SEAD_Handoff_2026-04-10.md) + VT upload integration.

## Agent Activity

| Agent | Type | Duration | Purpose |
|-------|------|----------|---------|
| write-appendix-c | write | ~40s | Appendix C evidence taxonomy from WRT-2516 Table 3 |

Balance of work performed in main session via direct edits, Python scripts, and pandoc/docxcompose orchestration.

Total: 1 agent spawned, many direct edits + script-driven batch operations.
