# Session Archive — 2026-04-28 postwach-01

**Hive:** PostWach
**Scope:** Race-the-clock support for RTSync's DOE Genesis Mission Phase I proposal submission (DE-FOA-0003612, Topic 19-A "Trustworthy Mathematical and Symbolic Reasoning"). Paul Wach as PI on RTSync's DEVS-Enhanced Trustworthy Reasoning (DEVS-TR) proposal led by Bernard Zeigler's team. Deliverables Paul personally owed RTSync CEO DH Kim by 9 PM internal deadline: SciENcv Biosketch, SciENcv Current & Pending Other Support, DOE Collaborators List Excel for Field 12, Phase I DMSP, plus proposal-content edits to Bernie's draft and a final-form Word doc.
**Platform:** Ruflo v3.0.0, claude-opus-4-7 (1M context), Windows 11 Home, pandoc + MiKTeX, python-docx, openpyxl
**Outcome:** All four Paul-side SciENcv-and-Excel deliverables produced; proposal converted from Bernie's docx into RTSync-template-format Word doc with 4 content edits applied (NeSy framing, stoic-devs ontological grounding, IS 2026 SES-of-Queens citations, Trust Delta decision-gate metric). Topic line corrected late in session from incorrect "19-C" (lifted from template filename) to "19-A" per user's pre-existing solution-analysis Excel. Significant rework throughout; quality issues acknowledged. Submission timing as of session end was within deadline window (RTSync 9 PM internal; FOA 11:59 PM ET on Apr 28).

---

## 1. Entry state

User: "warm up ruflo." Session-start AutoMemory imported 168 entries into AgentDB. ruflo MCP stdio running (PID 11912, claude-flow v3.0.0); `system_health` reported 40/100 (memory-store legacy degraded check; AgentDB itself healthy). User declined fixes, immediately pivoted to: "I need help putting together an application on grants.gov.gov" with a path to the FOA PDF. Initial request scope was guidance on Biosketch, Current & Pending Support, Collaborators List, Data Management and Sharing Plan.

---

## 2. Method

Single-stream conversational session with frequent user iteration. No swarm orchestration; no Task subagents spawned. Tools used: Read (PDF + docx + ORCiD JSON + SERC report), Bash (pandoc, python-docx, openpyxl, Crossref/OpenAlex/PubMed lookups, file conversion), Write/Edit (markdown drafts, RIS/NBIB bulk-import files, Excel population script, docx generation script), WebFetch + WebSearch (SERC URL lookup, INCOSE-IS 2026 location), MCP `mcp__claude-flow__memory_search_unified` (STOIC + NATO neuro-symbolic context retrieval).

Phases:

1. **Deadline triage + FOA reading.** Caught immediately that today (Apr 28) was the FOA's Phase I deadline and that Phase II LOI window had already closed. Reframed against three feasible targets; user later confirmed Phase I tonight via RTSync internal 9 PM deadline. Read FOA pages 1-15, 63-90, 105-130 (cover, eligibility, Section IV application contents, Section IX how-to guides for Biosketch/CPS/Collaborators/DMSP).
2. **Biosketch materials.** Reviewed Paul's full + 1-page CVs and ORCiD record (only 4 works on ORCiD). Verified DOIs via Crossref for the proposal-cited papers and other candidates. Built a recommended Top 10 product list with explicit rationale per pick and discrepancy flags. Discrepancies found: full CV vs 1-page CV PhD year (resolved 2022); proposal cites INSIGHT 2023 morphism paper not in Paul's CV; book-chapter title in CV ("System Science") differs from published ("Supporting Science Areas"); Wach et al. Applied Sciences journal name in CV inconsistent with Crossref. Wrote `top10_products.md`, `sciencv_paste_blocks.md`, `appointments_outside_primary.md`, `disclosure_checklist.md`.
3. **Bulk-import files.** Generated `wach_top10_products.ris` (49→10 entries) and `.nbib` (PMID-free version on user instruction). User feedback that initial RIS was sloppy ("Why did you not take this approach? CV is canonical") prompted full rebuild using CV-as-primary-source supplemented by Crossref for missing fields (vol/issue/pages, exact title corrections). IS 2026 location looked up via WebSearch: Yokohama, Japan, June 13-18, 2026.
4. **DMSP.** Drafted Phase I-shape DMSP, ~2 pp, addressing the 5 DOE standard requirements (FOA Section IX.B.12) plus the 3 Genesis-specific additions (FAIR / SPDX Apache-2.0 / BSSW best practices). Initially over-engineered with grid-stability dataset placeholders; user pointed out Bernie's draft does not commit to a use case, so DMSP was revised to use-case-agnostic framing.
5. **Proposal-content edits to Bernie's draft.** Four edits proposed and discussed: (E1) NeSy framing in Abstract + §3.1; (E2) stoic-devs ontological grounding for DDL in §3.2 Obj 1 + §3.3 Task 2 (scoped to stoic-devs only per user direction, with mention of broader STOIC stack); (E3) cite Wach/Philipbar/Gregory IS 2026 + Philipbar/Wach IS 2026 SES-of-Queens as composition prior art in §3.3 Task 1, Task 3, §3.5; (E4) add Decision Gate Metric 6 — Trust Delta. User declined the proposed Bernie-handoff memo and chose to integrate edits directly. STOIC and NATO neuro-symbolic positioning verified via memory search and direct read of `Papers/Neuro_Symbolic_Wargaming/Research_Proposal_v2.md` + `02 Hives/05 GI-JOE/.../stoic-status.md`.
6. **Collaborators List Excel.** Read DOE template structure (`Collaborator_Template.xlsx` from Downloads); built `Wach_Collaborators_List.xlsx` with 46 collaborator entries and 2 senior/key personnel entries via openpyxl. Window April 2022 to April 2026. ~30 institutional-affiliation cells left as `[VERIFY]`; advisee section left as `[ADVISEE LAST]` placeholder for user fill. Caveat: openpyxl drops Excel data-validation dropdowns on save — text values written verbatim match the LOV anyway.
7. **Red/Blue/White team review of Final versions.** User dropped final SciENcv exports (cv-2500231.pdf, cpos-2501395.pdf) into a `Final versions/` folder along with the markdown-route DEVS-TR_Proposal_FINAL.pdf. Conducted structured review surfacing 10 red-team items (R1 PI primary-org mismatch was eligibility-critical; R2 CPS completeness; R3 person-months over-commitment; R5 typos; R6 Best Paper Award not highlighted; R7 WRT-2406 missing report ID; R8 special-issue note dropped; R9 IS 2026 not flagged accepted; R10 SERC citation format ambiguous). User then iterated SciENcv 3 times; my prior R2 over-claim that the proposal-being-submitted must appear on its own CPS was corrected by user — the "Other" in CPOS means OTHER than the proposal in question.
8. **Final Word doc in RTSync template format.** User provided template `GENESIS 19-CDEVSFM.docx`. Built python-docx generator using template's Normal + List Paragraph styles, letter / 1in margins / Calibri 11pt. Initial output had two issues caught in second R-team review: references unnumbered (auto-list-style not preserved), and Decision Gate Metrics split across 2 paragraphs each instead of merged onto one line per template format. Both fixed via post-hoc patch. Topic line was set to "19-C Composable and Modular Foundation Models" (lifted from template filename) until user surfaced their pre-existing `GENESIS FY26 DEVS Solution Analysis - Topics 11, 16, 19.xlsx` which confirmed 19-A "Trustworthy Mathematical and Symbolic Reasoning" was the correct topic; corrected.
9. **Session close.** Generated this archive + scorecard.

---

## 3. Deliverables

### New files (all in `04 Genesis/`)

**`Biosketch_Materials/`** — working materials, intended as crib sheet for SciENcv entry:
- `top10_products.md` — annotated product short-list with rationale and 5 CV/Crossref discrepancies
- `sciencv_paste_blocks.md` — manual copy-paste blocks for SciENcv fields
- `appointments_outside_primary.md` — 3-year window appointments table
- `disclosure_checklist.md` — full NSPM-33 walkthrough (sponsored research / consulting / honorary / in-kind / gifts / foreign / MFTRP / training)
- `collaborators_list_DRAFT.md` — markdown precursor to Excel
- `DMSP_DRAFT.md` — Phase I, use-case-agnostic, 5 standard + 3 Genesis-specific elements
- `wach_top10_products.ris` — RIS bulk-import for SciENcv via My Bibliography
- `wach_top10_products.nbib` — MEDLINE/NBIB fallback (PMID-free per user instruction)
- `DMSP_DRAFT.pdf` — pandoc-rendered version of DMSP

**`Final versions/`** — submission-bound artifacts:
- `Wach_Collaborators_List.xlsx` — DOE template populated with 46 collaborators + 2 senior/key, ~30 `[VERIFY]` cells for institutional affiliations
- `DEVS-TR_Proposal_FINAL.pdf` — markdown→pandoc→PDF route, 4 pp narrative + 3 pp bibliography
- `DEVS-TR_Proposal_FINAL.docx` — RTSync-template-format Word doc, 127 paragraphs, references numbered [1]-[49], 6 Decision Gate Metrics, Topic 19-A
- `_build_collaborators.py`, `_build_proposal_docx.py` — working scripts (delete before submission)

User-side files reviewed (Paul produced via SciENcv; reviewed by me):
- `cv-2500231.pdf` (Biosketch) — reviewed across 3 iterations
- `cpos-2501395 (1).pdf` (CPS) — reviewed across 1 iteration

### Modified files
- None in any project repo. All work is in the per-session `04 Genesis/` folder, not committed.

### Code/repo changes
- None.

---

## 4. Decisions (durable)

- **D1 (eligibility-critical).** Paul's PI primary organization on the SciENcv biosketch is RTSync Corp, Phoenix, Arizona (Senior Research Scientist 2026-present). UofA stays in Appointments-outside-primary. RTSync grant of PI status confirmed by user at session midpoint; UofA outside-employment cleared for the RTSync work.
- **D2 (Topic).** Genesis Phase I submission is under Topic 19-A — Trustworthy Mathematical and Symbolic Reasoning (ASCR), per user's pre-existing `GENESIS FY26 DEVS Solution Analysis - Topics 11, 16, 19.xlsx`. Title matches the proposal title nearly verbatim. 19-C and 16-B/16-C are positioned as separate proposals (Paul's email to DH on file).
- **D3 (DMSP).** Phase I DMSP defaults to use-case-agnostic framing (since Bernie's §3.3 Task 4 lists candidates "such as" rather than committing). Apache-2.0 + CC-BY-4.0 as default open-source licenses. Repository: GitHub for development, Zenodo for archival deposit + DataCite DOIs, OSTI for publications, arXiv for preprints. STOIC integration limited to stoic-devs module specifically (per user direction; broader stack mentioned but not relied on).
- **D4 (Proposal edits).** Four edits agreed in principle and integrated into the RTSync-template-format docx: (a) NeSy framing in Abstract + §3.1; (b) stoic-devs ontological grounding in §3.2 Obj 1 + §3.3 Task 2; (c) cite IS 2026 papers as recent prior art in §3.3 Task 1, Task 3, §3.5 (refs [48], [49]); (d) add Decision Gate Metric 6 — Trust Delta with ≥3× improvement target. R016 honesty maintained: STOIC is research-tier "in development", IS 2026 papers are "accepted".
- **D5 (CPS scope).** "Other" in Current and Pending Other Support means other than the proposal being submitted. The Genesis DEVS-TR proposal does NOT belong on its own CPS. My earlier R2 critical claim was wrong; user correctly surfaced this. Per-other-grant inclusion verified (SE Beyond the Horizon current; Adaptive PWSA pending; other actively-pending grants flagged for user verification).
- **D6 (Best Paper handling).** Best Paper Award (CSER 2024) goes as an annotation on the existing Item 6 publication entry, not a standalone product. Initial attempt to list it as Product 10 with malformed authorship ("Wach P, Taylan T, Husain M") was corrected; Item 10 restored to Wach/Esser/Topcu/Hutchison WRT-2406 SERC technical report.
- **D7 (Top 10 final).** 1. Wach/Zeigler/Salado 2021 Applied Sciences; 2. Wach/Salado 2022 IS Morphisms; 3. Wach/Salado 2022 Springer SysML chapter; 4. Wach/Topcu/Jung/Sandman/Kulkarni/Salado 2025 SE SLR; 5. Topcu/Husain/Ofsa/Wach 2025 SE Trust at Your Own Peril; 6. Husain/Wach/Topcu 2024 CSER Best Paper; 7. Wach/Beling/Zeigler/Salado 2024 Springer Study of Equivalence; 8. Philipbar/Wach 2026 IS DEVS Agentic Swarms (accepted); 9. Wach/Philipbar/Gregory 2026 IS Math-Based DEVS Data Structures (accepted); 10. Wach/Esser/Topcu/Hutchison 2025 SERC-2025-TR-005 (WRT 2406) Optimized Portfolio DE Transformation.

---

## 5. Open threads touched / opened

**Opened:** None.

**Touched:**
- **STOIC ontology stack (GI-JOE).** Used stoic-devs module (v0.4.0, 126 classes, 920 triples, 9 CQs pass) as the ontological grounding for DDL in proposal Edit 2. Honest scoping: stoic-t3sd (v0.2.0) and stoic-bridge (v0.1.0) deliberately not foregrounded in the proposal text because they're earlier-stage. T3SD-DEVS bridge paper still in draft per `02 Hives/05 GI-JOE/.../stoic-status.md`.
- **NATO Neuro-Symbolic Wargaming TAP.** Used "neural proposes, symbolic disposes" pattern from Paul's `Papers/Neuro_Symbolic_Wargaming/Research_Proposal_v2.md` to motivate DEVS-TR's NeSy framing. NATO TAP itself is unfunded; cited as motivating context, not as endorsement.

**Not touched this session:**
- HOS + Governance Composition (parent thread, planning mode pending)
- HOS Capability Freshness Subsystem (sub-thread, planning mode pending)
- DoD/DoW Policy Stack (PostWach-level reference logged 2026-04-23, per-hive ingestion deferred)
- NSA ZT Alignment, Chainguard, Fort Wachs validation, INSIGHT article, NNSA Capability Transition, PD Workbench, IGNITE
- `.claude` vs `.claude-flow` Q1/Q2 (Q3 resolved 2026-04-22)

---

## 6. Out-of-scope items user flagged

- **C&P verification of all currently-active and still-pending grants.** I flagged candidates from CV; user confirmed handling on their side.
- **Collaborators List `[VERIFY]` cells + advisees + close associates.** Drafted Excel scaffold; user fills institutional affiliations and personal-mentorship entries.
- **Bernie integration of the 4 proposal edits into Bernie's docx.** User chose to handle directly with Bernie rather than memo-handoff.
- **Submission to Grants.gov via DH Kim's RTSync sponsored research office.** All admin (SF-424, R&R Budget, Letters of Commitment, Genesis Excel template, SAM.gov, Grants.gov Workspace) is RTSync-side; not within session scope.

---

## 7. Next session entry hints

- **If submission succeeded:** schedule post-mortem session covering (a) what worked / didn't on race-the-clock proposal nights, (b) whether Topic 19-A pre-selection from solution-analysis Excel should be a documented PostWach pattern, (c) ORCiD bulk-population workflow setup for next biosketch (developer credentials user already configured but didn't use this session), (d) RTSync template-format docx generation patterns to reuse.
- **If submission slipped or held by DOE for FY27:** the FOA p. 63 explicitly contemplates this — "DOE may hold any subsequent Phase II application until FY27." DEVS-TR work is reusable verbatim; bonus time would let the use case be selected, the partner-institution lineup confirmed, and a fuller Bernie-co-authored proposal package prepared.
- **STOIC stoic-devs T3SD-DEVS bridge paper.** Currently in draft (~7000 words). If DEVS-TR is awarded, this paper becomes a high-leverage citable foundation. Worth prioritizing for publication before Phase I award negotiation.
- **Quality lessons for next race-the-clock session:** (1) at session start, survey user's existing analysis docs in the target folder before assuming context (would have caught Topic 19-A immediately); (2) for federal-form work, validate every field-format claim against the FOA before drafting; (3) prefer smaller iterations with user confirmation over larger drafts; (4) when generating docx via python-docx, preserve the source template's auto-list-numbering and inline-paragraph styles.
- **Proposal edits if Bernie wants memo form:** four edits documented in this archive's §4 D4; can be re-extracted as a standalone memo on demand.
- **Follow-on Phase II preparation.** If Phase II direct-apply path remains open via missed-LOI grace, the May 19 Phase II application requires a much fuller narrative (5-pp methods, 4-pp preliminary results, 1-pp timeline, 2-pp data sources, 4-pp performance metrics, 2-pp management plan, plus 4-pp DMSP appendix). DEVS-TR's existing Phase I narrative would need significant expansion.

---

## 8. Honest session retrospective

User explicitly flagged frustration with quality and pacing on multiple occasions during this session ("very low quality work in creating the source files", "your estimates seem to always be off", "very frustrating", "the references are no longer label[ed]"). Specific failures:

1. **Topic line.** Used "19-C Composable and Modular Foundation Models" as the proposal topic by lifting from the RTSync template filename (`GENESIS 19-CDEVSFM.docx`) without verifying. The actual selected topic was 19-A "Trustworthy Mathematical and Symbolic Reasoning", documented in user's pre-existing `GENESIS FY26 DEVS Solution Analysis - Topics 11, 16, 19.xlsx` which I did not survey at session start. User caught this near the end of the session; correction took an additional ~5 minutes.
2. **Reference numbering.** Generated the docx via python-docx using the template's "List Paragraph" style assuming auto-numbering would carry through; it did not. Lost all `[1]`-`[49]` reference labels, orphaning the in-text citations. Fixed via post-hoc text patch but should have been caught in initial generation.
3. **Best Paper Award.** Initial fix to highlight the CSER 2024 Best Paper was malformed — created a standalone Item 10 product entry titled "Best Paper Award" with author error ("Wach P, Taylan T, Husain M" — Taylan is Topcu's first name). Should have been an annotation on the existing Item 6 publication. Two iterations to resolve, displacing the WRT-2406 SERC technical report which had to be restored.
4. **CPS scope.** Asserted in initial R2 review that the Genesis DEVS-TR proposal must appear on its own CPS as pending. User correctly pointed out the "Other" in CPOS means other-than-the-proposal-being-submitted. Walked back the claim.
5. **Collaborators / RIS source pivot.** Initially built RIS file from Crossref + proposal references, ignoring Paul's CV which is the canonical source. User pushed back ("the content can mostly be copied directly from my CV"); rebuilt from CV.
6. **Time estimation.** Consistently over-estimated task durations across SciENcv edits, Excel population, and proposal generation. Lost user trust on pacing claims.
7. **Frictions added by tool-chain.** pandoc on Windows drops U+2011 non-breaking-hyphen in input filenames (required `shutil.copy2` workaround); python-docx cannot write to docx files open in Word (required user close-and-reopen); bash heredoc with embedded apostrophes parses incorrectly (required Write-to-file-then-execute pattern). These cost ~25 minutes cumulatively.

What worked: parallel reading of FOA + ORCiD + CV at session open built fast context; Crossref DOI verification produced clean bibliographic data for the SciENcv product list; the FOA-extraction work (Sections IV.C and IX.B.9-12) is reusable for any future DOE proposal in this PI's portfolio; the RTSync template-format docx generation pattern is reusable; the DOE Collaborators Excel scaffold reduced what would have been ~1 hour of manual Excel work to ~15 minutes of `[VERIFY]` cell fills. Net for the user: AI accelerated the bookkeeping but introduced enough errors to require near-continuous QC.

Lessons for future race-the-clock proposal sessions, captured for memory:
- (a) survey user's existing analysis docs in the target folder at session start before drafting
- (b) for federal forms, validate every field-format claim against the FOA's exact instructions before drafting
- (c) prefer smaller iterations with user confirmation over larger drafts
- (d) for docx generation, preserve source template's list-numbering and inline-paragraph styles
- (e) honest time estimates: race-the-clock proposal work compresses poorly; budget more user-side iteration than expected
