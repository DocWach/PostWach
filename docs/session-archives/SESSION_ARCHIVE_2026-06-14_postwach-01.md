# Session Archive — 2026-06-14 postwach-01

> PROVENANCE: claude-opus-4-8 (1M) main thread. Artifacts (this archive, the 2026-06-14-postwach-01 scorecard, new memory `feedback_formatting_verify_visually.md` + MEMORY.md index, all edits to `Vision_2035_RE_Revised_2026-06-14.docx` + its PDF, the surgical edit scripts `_apply_0614.py`/`_polish_0614.py`, and the tri-model run packet/synthesis) produced by the main-thread model. One Claude Task sub-agent (general-purpose, tri-model "Claude track"). Two external CLIs: Codex 0.133.0 and Gemini 0.46.0 (Codex/Gemini tracks).

**Hive:** PostWach
**Scope:** Continue finalizing INCOSE IS 2026 #479 "VISION 2035: EXPLORING THE FUTURE OF REQUIREMENTS SPECIFICATION" toward camera-ready: apply principal's review directives, run a third tri-model review, apply consensus polish, and correct Table 1 to true INCOSE format.
**Platform:** ruflo v3.10.40 (warm). python-docx for surgical docx edits; MS Word via PowerShell COM for PDF render. Codex 0.133.0, Gemini 0.46.0.
**Outcome:** #479 advanced to camera-ready quality. Title set to ALL CAPS; Karson Sandman affiliation corrected; WRT-2406 citations added then de-stuttered; tri-model r3 verdict "substantively camera-ready"; consensus polish applied; **Table 1 corrected to INCOSE format (borderless with gray header, caption below, kept together on one page)**. Deliverable `Vision_2035_RE_Revised_2026-06-14.pdf`. All edits surgical; principal's manual formatting (underlined emails) preserved throughout.

---

## 1. Entry state
Resumed #479 from postwach-03 (2026-06-13). Working file = principal's hand-edited `_workspace/Vision_2035_RE_Revised_2026-06-13.docx` (round-3 content + manual email underline/spacing). A stale Word lock file was present (no live Word process). Held items from 06-13: title capitalization, Jurczyk 2025b authorship, Gemini --skip-trust note.

## 2. Decisions made this session (durable)
- **D1. Title -> ALL CAPS** per the INCOSE template ("VISION 2035: EXPLORING THE FUTURE OF REQUIREMENTS SPECIFICATION").
- **D2. Jurczyk 2025b reference left "et al."** (principal: "that's fine").
- **D3. Karson Sandman affiliation.** Byline shows University of Arizona / Systems & Industrial Engineering (consistent with Wach, Aerospace removed from byline); his end bio retains "System Director with The Aerospace Corporation and a part-time researcher at the University of Arizona." (Department mirrored from Wach; principal to confirm if his unit differs.)
- **D4. WRT-2406 (Wach et al., 2025c) citation placement.** Added at the first body mention of Vision 2035 (Pareto paragraph) and the next paragraph's first sentence per principal. Tri-model flagged the pair as a back-to-back stutter; principal chose the consensus de-stutter: keep the first-mention cite, reword the next paragraph's opening ("They build on...") to drop the echo + second parenthetical. Tradespace cite later in that paragraph retained.
- **D5. Table 1 INCOSE format (the headline correction).** Correct INCOSE table = borderless (white/invisible borders, single sz4 FFFFFF), gray header band (D0CECE), caption BELOW the table, kept together on one page (top of page preferred). Our table had black "Table Grid" box lines and was splitting across pages with the header row orphaned. Both corrected.
- **D6. Gemini --skip-trust required.** Gemini CLI 0.46 refuses tool calls in untrusted (OneDrive) dirs; set GEMINI_CLI_TRUST_WORKSPACE=true + --skip-trust upfront this run -> worked first try.

## 3. Work / artifacts
- `_workspace/Vision_2035_RE_Revised_2026-06-14.docx` + `Vision_2035_RE_Revised_2026-06-14.pdf` — current deliverable (surgical edits on the 06-13 base; manual formatting preserved). 06-13 retained as fallback.
- `_workspace/_apply_0614.py` (title caps, Karson byline, WRT-2406 cites, table caption-below + shading), `_workspace/_polish_0614.py` (de-stutter, intro transition, backward-table sentence, cite standardization, NIST, caption rewording) — surgical edit records.
- Table 1 border + keep-together fixes applied directly (white borders matching INCOSE; cantSplit on 4 rows + keep_with_next on 16 cell paragraphs).
- Tri-model r3: `02 My Outreach/Tri_model_review/runs/2026-06-14_is2026-479-r3/` (briefing + template_requirements + format_check_done + packet; 9 model files; synthesis.md).
- New memory `feedback_formatting_verify_visually.md` + MEMORY.md index entry.

## 4. Tri-model review r3 (consensus)
Verdict: substantively camera-ready, no blockers. All three flagged the WRT-2406 over-citation (de-stuttered, D4). Applied polish: intro "remainder of this article" transition refactor + "current-state" -> "current state"; reworded the now-backward "A summary of the roadmap is provided in Table 1" sentence; standardized the fine-tuning-degradation cite to (Wach et al., 2025b); spelled out NIST at first use; crisper Table 1 caption. Karson byline-vs-bio and caption-below both judged clean by all three.

## 5. Failures / lessons — FORMATTING (recurring; principal flagged)
- **F1. Recurring formatting miscommunication.** Principal: "We seem to continue to miscommunicate on the subject of formatting." Pattern across sessions: pandoc two-column collapse (06-13), manual-edit overwrite (06-13), and this session's Table 1 defects. Root cause: I verify formatting at the XML/attribute level or assert completion, instead of rendering and visually comparing to the template's RENDERED appearance.
  - This session's concrete miss: I "verified" Table 1 by checking caption position and shading in the docx XML and called it INCOSE-correct. The rendered PDF showed two real defects I had not looked for: (a) black "Table Grid" box lines, where the INCOSE template uses white/invisible borders (its borders ARE present in XML but colored FFFFFF — attributes mislead); (b) the table split across pages with the header row stranded at the bottom of page 6.
  - Fix adopted: for ANY formatting task, render to PDF, view the affected region, and compare to the template's rendered output, not its attributes. Captured as `feedback_formatting_verify_visually.md`; reinforces [[feedback_probe_artifact_not_narrative]] and [[feedback_match_format_means_file_level]].
- **F2. Word COM RPC_E_CALL_REJECTED** recurred on first call after Open; handled by kill-WINWORD + settle + retry wrapper (as before).

## 6. Open items (carried forward)
1. **Karson Sandman department** assumed to be Systems & Industrial Engineering (mirrors Wach); principal to confirm his actual UofA unit.
2. **Gemini --skip-trust** now used inline; still worth a one-line addition to `project_tri_model_review` memory.
3. **R1/R3.2/R3.4 scoped-out posture** (applied examples with outcomes, quantified ROI cited to WRT-2406 rather than in-paper) — deliberate "vision paper" framing, not a defect; would require verifiable outcome data to harden.
4. Persistent 4 idle ruflo worker stubs in the registry (no exposed IDs; not targetable; clear on ruflo restart).
