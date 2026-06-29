# Session Archive — 2026-06-13 postwach-03

> PROVENANCE: session opened under claude-fable-5[1m]; principal switched to claude-opus-4-8 (1M) mid-session (via /model, after the refverify batch). Main-thread artifacts (this archive, the 2026-06-13-postwach-03 scorecard, the new `feedback_no_overwrite_manual_edits.md` memory + MEMORY.md index entry, the enrichment to `reference_wrt2406_2516_publishable_outputs.md`, all edits to `02 My Outreach/IS 2026 - Vision for RE/_workspace/manuscript_clean.md` + `change_list.md`, the in-place build script `_build_v2_inplace.py`, the docx/PDF deliverables, `candidate.bib` + `cesun_attest.bib`, 26+2 approved.bib promotions + manifest entries, and the tri-model run packet/synthesis) produced by the main-thread model. Five Claude Task sub-agents (general-purpose): four parallel reference-verification scouts (journals; DoD/INCOSE/ISO; NIST/OASIS/OMG; self-cites) + one tri-model "Claude track" reviewer. Two external CLIs: Codex 0.133.0 and Gemini 0.46.0 (tri-model Codex/Gemini tracks). Sub-agent outputs attributed in their own files.

**Hive:** PostWach
**Scope:** Resume and finalize INCOSE IS 2026 paper #479 "Vision 2035: Exploring the Future of Requirements Specification" (Wach/Topcu/Hutchison/Sandman) toward camera-ready. Spanned 2026-06-12 into 2026-06-13.
**Platform:** ruflo v3.10.40 (warm; AgentDB sql.js+ONNX, 205 entries imported on SessionStart). pandoc 3.x, python-docx, MS Word via PowerShell COM for PDF/compare. Codex CLI 0.133.0, Gemini CLI 0.46.0. refcheck.py / refverify.py (R019 gates).
**Outcome:** #479 brought to camera-ready-quality: 4-author byline + bios (3 verified headshots), reverted Table 1, verified+attested 29-entry bibliography (R019 gate green 29/29), correct INCOSE two-column formatting via in-place docx editing, tri-model review (Claude/Codex/Gemini) + template-adherence audit, and round-3 consensus fixes applied. Final deliverable `Vision_2035_RE_Revised_2026-06-13.pdf` rendered from the principal's hand-edited docx.

---

## 1. Entry state
Opened "warm up ruflo. resume work on the AI4RE paper for IS." The `Papers/AI4RE_SLR/` tree was untouched since January; the live AI4RE-line paper is "The Tale of the Broken Clock" in `02 My Outreach/IS 2026 - AI4RE/`. Principal redirected to `02 My Outreach/IS 2026 - Vision for RE/` (#479), which had a `_workspace/` from the 2026-06-09 revision (manuscript_revised.md, change_list.md, bibliography_additions.md) with one open `[PLACEHOLDER]` and an unrun R019 gate.

---

## 2. Decisions made this session (durable)
- **D1. Placeholder removed.** The Jurczyk 2025b Hume case-study `[PLACEHOLDER]` (E23) was withdrawn; the sentence reverts to the non-specific form, retaining the citation without an unverified outcome.
- **D2. References verified via 4 parallel web-research sub-agents.** Triple-check caught ~12 real bibliography errors (see §4). 26 verified entries promoted to `approved.bib` (single-model-triple-check); 2 CESUN papers (no public record) promoted via human-attested path on principal's explicit approval (attested_by paulwach@arizona.edu). Gate green 29/29.
- **D3. INCOSE docx must be built by IN-PLACE editing, not pandoc regeneration.** pandoc `--reference-doc` collapses the template's 6-section / two-column layout to one single column. Adopted the DEVS-ME #427 procedure: edit the template docx in place with python-docx (preserving sectPr/columns/styles), render PDF from it. `_build_v2_inplace.py` is the procedure record.
- **D4. Tri-model review re-run on the near-final paper + template adherence.** Independent parallel Claude/Codex/Gemini red/blue/white (not the shared-ruflo cross-review layer, deferred). Plus orchestrator deterministic format checks against the INCOSE V1.3 template.
- **D5. Round-3 held items (judgment calls):** title left in title case (accepted submission, not forced to ALL CAPS); Jurczyk 2025b reference kept "et al." (poster authorship unverifiable, would not fabricate); Table 1 caption left above the table (INCOSE's own template places it above, contradicting its prose).
- **D6. Manual-edit overwrite incident → new rule.** A round-3 rebuild regenerated the docx from template+markdown and was `cp`'d over the principal's hand-edited 06-13 file, clobbering Word-level edits (underlined emails, section spacing). Recovered via OneDrive version history. Enacted durable rule `feedback_no_overwrite_manual_edits.md`: never blind-regenerate over a deliverable touched since last build; apply deltas surgically or ask. Final PDF rendered surgically from the principal's file.

---

## 3. Artifacts produced
**#479 paper (`02 My Outreach/IS 2026 - Vision for RE/`):**
- `_workspace/manuscript_clean.md` — render-source text (heavily edited: bios, corrected 29-entry bibliography, round-3 fixes).
- `_workspace/Vision_2035_RE_Revised_2026-06-13.docx` — principal's hand-edited deliverable (round-3 content + manual email/spacing formatting).
- `Vision_2035_RE_Revised_2026-06-13.pdf` — final clean render (from principal's docx).
- `_workspace/Vision_2035_RE_TrackedChanges_2026-06-13.docx` + `.pdf` — blackline vs original submission.
- `_workspace/_build_v2_inplace.py` — in-place build script (DEVS-ME-style provenance record).
- `_photos/` — wach.png (#427), topcu.jpg + hutchison.jpg (official VT pages).
- `_workspace/change_list.md` — updated with the 2026-06-13 reference-verification pass + round-3 record.
- `_workspace/candidate.bib`, `_workspace/cesun_attest.bib` — promotion/attestation sources.

**Reference store (`04 Resource Library/00 Verified References/`):** +26 verified + 2 attested entries to `approved.bib` (105 total) + manifest entries; backup `approved.bib.bak-20260612`.

**Tri-model run (`02 My Outreach/Tri_model_review/runs/2026-06-13_is2026-479-r2/`):** briefing.md, template_requirements.md, format_check_done.md + source packet; 9 model files ({claude,codex,gemini}/{red,blue,white}.md); synthesis.md.

**Memory:** new `feedback_no_overwrite_manual_edits.md` + index; enriched `reference_wrt2406_2516_publishable_outputs.md` (Cost of Expertise verified initials Bell R / Jugan B / Longshore R + DOI/pages).

---

## 4. Bibliography errors caught (triple-check value)
- Hutchison & **See Tao** (2022) — surname was "Tao" (dual-verified CrossRef + PDF byline; fixed bib + 3 in-text).
- Peña & Valerdi (2015) — title was "software development effort," canonical "systems engineering effort."
- Cost of Expertise (2025b) — author initials Bell **R** (not G), Jugan **B** (not K), Longshore **R** (not E); added DOI 10.1002/iis2.70078, vol 35(1), pp. 1490-1507.
- Helix WRT-1004 (2020) — McDermott & Van Aken were not authors (per SERC-2020-TR-007 title page); corrected to the Hutchison/Verma/... team.
- WRT-2406 FTR (2025c) — title missing "Transformation"; author order corrected (PI/Co-PI).
- DoD DE Strategy 2018, OSLC RM 2.1, OSLC SysML 2.0 — dead URLs fixed; OSLC RM date 23→21 June; DoD issuer corrected to ODASD(SE).
- Nerayo & Wach upgraded to verified 2026 Springer chapter (DOI 10.1007/978-3-032-12309-1_43); orphan reference given an in-text cite.

## 5. Tri-model + round-3 fixes applied
Blockers: abstract citation removed; Table 1 cited before it appears; reference APA ordering (INCOSE/Jurczyk/Wach); "Concrete applied examples" → "Illustrative pilot patterns." Should-fix: in-text two-author "&"→"and"; Husain over-attribution (line 95); "authors' own benchmarking" no longer sweeps in Mahbub + duplicate sentence dropped; Helix full authors; two semicolon-as-dash artifacts; "Conclusion"→"Conclusions"; AI/APIs/RE/SERC defined at first use; ISO reference em-dashes → en-dashes. Verified format: ~4,528 words (2,000-7,000 OK), abstract 215 words, margins 0.6", 29 refs, gate green.

---

## 6. Failures / lessons
- **F1. Manual-edit clobber (D6).** Root cause: rebuild from template+markdown, not from the live deliverable. Fix: durable rule + surgical-edit posture once a file has been opened by the user. Recovered via OneDrive history.
- **F2. pandoc lost the two-column layout** before the DEVS-ME in-place procedure was adopted (D3). Several reactive renders before probing the artifact (`sectPr` count) revealed the single-section collapse.
- **F3. Gemini CLI 0.46 refuses tool calls in untrusted (OneDrive) dirs.** Needs `--skip-trust` / `GEMINI_CLI_TRUST_WORKSPACE=true` headless. New-version gotcha vs the older tri-model memory. (Record to `project_tri_model_review` next session.)
- **F4. Word COM RPC_E_CALL_REJECTED** on first call after Open; fixed by killing WINWORD, settle delays, and retry-wrapping every COM call.

---

## 7. Open items (carried forward)
1. **Title capitalization** (#479): left title case; principal may want ALL CAPS per template. Principal-owned.
2. **Jurczyk 2025b reference authorship**: kept "et al."; needs principal's correct author line (poster authorship unverifiable).
3. **`project_tri_model_review` memory**: add the Gemini `--skip-trust` gotcha (deferred this session).
4. **Cross-review / shared-ruflo layer** of the tri-model pipeline was not exercised this run (independent parallel only).
5. **STIDS MTO #479 line is distinct** — this #479 is the IS Vision paper; do not conflate.
