# Session Archive — 2026-05-04 postwach-01

**Hive:** PostWach
**Scope:** INSIGHT 2026 article "From Rules to Agentic Swarms" — full revision cycle from reviewer-comment receipt through v3 sent to co-authors. Spans 2026-04-29 (reviewer comments received) through 2026-05-04 (v3 + change log delivered to Alejandro and Brad). Single continuous conversation across multiple days.
**Platform:** Ruflo v3.5.80 → v3.6.27, claude-opus-4-7 (1M context), Windows 11.
**Outcome:** v3 manuscript delivered to co-authors with comprehensive change log. All 23 reviewer comments and 17 author-review comments addressed (one figure regeneration pending Word re-render after co-author edits). Article spine refactored from 5 authors-built case studies to 4 + SERC literature treatment. New L2 persistence framing established as central thesis. Companion adjudication artifacts (YAML + MD + CSV + XLSX) and tooling scripts produced.

---

## 1. Entry state

User opened the session by asking PostWach to extract reviewer comments from `Review copy - Wach_Salado_INSIGHT_2026_AI_History_v1.docx` (received 2026-04-29). The original article (v1) had been submitted earlier in the year and was in hold pattern per memory. Two reviewers returned 23 comments: Tom McDermott Jr (R1, 8 comments) and Zoe Szajnfarber (R2, 15 comments). User wanted a spreadsheet for adjudication; surfaced standing convention (YAML primary + MD companion per `feedback_reviewer_feedback_cataloging.md`); resolved with YAML + MD + derived CSV/XLSX.

---

## 2. Method

Direct tool use with one background literature-scan agent. Approximately 30 user turns over 5 days. Each substantive change discussed before execution per "Discuss before executing" rule.

1. **Reviewer-comment extraction.** Wrote `scripts/extract_docx_comments.py` to parse `word/comments.xml`, `commentsExtended.xml`, and `document.xml` from the .docx zip. Extracted 23 comments with anchored quotes, paragraph context, author identities, dates. Produced `reviewer_feedback.{yaml,md,csv,xlsx}` per the cross-paper convention.
2. **Adjudication round 1.** User adjudicated three comments inline: Q1=C (Topcu citation single-use; resolved to "use once for NLP bridge"), Q2 (DoW with single explanatory footnote), confirmation that NLP folds into DL section. Logged adjudications into the YAML; regenerated CSV/XLSX.
3. **Adjudication round 2 (proposed).** Wrote `scripts/apply_insight_adjudications.py` to bulk-add proposed adjudications for the remaining 17 comments. Each adjudication carried a `decided_by: "Claude (proposed for Wach review)"` flag for spot-check.
4. **SERC spine debate.** User raised the question of restating the article as "examples from SERC researchers, much of which is our own work." Multi-turn debate covering five sub-options (C-1 through C-5c with alpha/beta/gamma sub-paths). Resolved to: remove PHM Case Study (uncitable); reframe spine; cite SERC researchers for ML/DL/NLP. User confirmed SERC affiliation (UA and VT are SERC member institutions).
5. **Background literature scan.** Spawned general-purpose agent for SERC ML/DL/NLP literature search. Strategy: SERC AI4SE workshop reports first, then technical reports. Two named-researcher leads injected via SendMessage during the agent's run: Mark Blackburn (Stevens, NLP) and Daniel Selva (Texas A&M, Daphne). Agent returned 9 candidates per paradigm with verified author/title/venue/SERC-tie.
6. **Persistence framing debate.** L1 (parallel threads) vs L2 (unified thesis) vs L3 (architectural reorganization). User chose L2: "each new paradigm has become a durable substrate." User pushed back on overly tidy lineage claims (the L1 history is more adversarial than smooth-substrate). Refined framing: substrate accumulates *despite* tribal rejection, not because of smooth integration.
7. **V3 markdown generation.** Single Write of `Wach_Salado_INSIGHT_2026_AI_History_v3_draft1.md` (~7,450 words body) integrating all adjudicated comments + L2 framing + locked SERC citations + spine refactor.
8. **V3 Word and PDF rendering.** Pandoc with v1.docx as `--reference-doc` for style template. Word: 26 MB. PDF: xelatex via MiKTeX, 11 MB.
9. **Author review.** User reviewed v3 (in Word) and provided 17 comments (A1–A17) plus 1 side note (S1). Logged in `author_review_v2.md`. Topics included: tone-down absolutes, citations at first mention, page numbers, Figure 1 not actually fixed (caption claim removed), Topcu sharper LLM-ceiling framing, Expert Systems "the prior" wording, figure cross-references, Daphne case-study label, SVMs and other acronym audit (broader sweep needed), "heir to Houston" overclaim removal, agentic-AI tool-calling overhaul, NASA/DL spell-out, Table 1 cross-reference, misplaced citation chain, CSER 2026 + IS 2026 citation additions, STOIC paragraph rewrite, and call-to-action third-opening replacement.
10. **V3 regeneration with author comments.** Single full-rewrite pass applying all adjudicated changes. New Word doc + PDF.
11. **Bibliography verification.** Wrote `scripts/verify_bibliography.py`. Found one orphaned reference (Hamilton and Ali 2026, leftover from v1's PHM section). Removed.
12. **Figure 1 regeneration.** Wrote `scripts/generate_insight_figure1.py` (matplotlib). Three iterations: v5 initial (top + bottom rows, white text), v5 refined (transparent bg, larger bold), v6.1 final (compact top + larger bottom info box, three rows per paradigm: method/character/limitation, black bold 11pt on pale paradigm tint, transparent bg, no overflow on Swarms column).
13. **Ruflo citation.** User asked for the proper citation. Verified GitHub metadata via `gh repo view ruvnet/ruflo` and `gh api users/ruvnet`: author display name is "rUv", project is "ruflo", latest version v3.6.27, MIT license. Constructed: `rUv. 2026. *ruflo* (Version 3.6.27). Agent orchestration platform for Claude. https://github.com/ruvnet/ruflo.`
14. **Final verification.** Cross-checked user-edited v3.docx against all 23 reviewer comments and all 17 author comments. 22/23 reviewer comments fully applied; 15/17 author comments fully applied; 1 partial (Figure 1 image regeneration awaiting Word re-render); 1 deferred (S1 portfolio decision).
15. **Change log.** Wrote `ChangeLog_v3.md` with two tables (reviewer + author) and rendered to `ChangeLog_v3.docx` using v1.docx as style template.
16. **V3 sent to co-authors.** User sent v3 + change log to Alejandro Salado and Brad Philipbar 2026-05-04.

---

## 3. Deliverables

### New files in `02 My Outreach/INSIGHT 2026 AI History/`

**Manuscript (current canonical):**
- `Wach_Salado_INSIGHT_2026_AI_History_v3.docx` (Word)
- `Wach_Salado_INSIGHT_2026_AI_History_v3_draft1.md` (markdown source)
- `Wach_Salado_INSIGHT_2026_AI_History_v3_draft1.pdf` (PDF rendering)

**Figure assets:**
- `AI_history_overview_v5.png` (v6.1 figure: regenerated Figure 1 with prominent date row, three info rows per paradigm)

**Adjudication and change-log artifacts:**
- `reviewer_feedback.yaml` (canonical, queryable per cataloging convention)
- `reviewer_feedback.md` (human-readable companion)
- `reviewer_feedback.csv` and `reviewer_feedback.xlsx` (flat adjudication grid)
- `author_review_v2.md` (per-comment author-review log)
- `ChangeLog_v3.md` and `ChangeLog_v3.docx` (revision summary by reviewer + author tables)

**Background agent output:**
- `.serc_lit_scan.md` (literature-search agent's candidate citations)

### New files in `01 PostWach/scripts/`

- `extract_docx_comments.py` (reusable: parse Word comments)
- `reviewer_feedback_to_csv.py` (reusable: derive CSV/XLSX from canonical YAML)
- `apply_insight_adjudications.py` (one-off: bulk-add adjudication blocks)
- `verify_bibliography.py` (reusable: cross-check body cites against references list)
- `generate_insight_figure1.py` (matplotlib figure generator)

### Modified files

- `MEMORY.md` — INSIGHT entry updated to "v3 sent to co-authors 2026-05-04"; author count corrected to 3 (Wach, Salado, Philipbar); v3 status and artifact paths recorded.

---

## 4. Headline outcomes

**Spine refactor.** v1's PHM Testbed Case Study removed (uncitable Virginia Tech testbed; user's prior work without published reference). Article spine reframed as "examples from SERC researchers, much of which is our own work." Authors' Case Studies retained: Houston (ES), TurboArch (LLM), GenGroves (Agentic), MACQ (Swarm). ML/DL/NLP paradigms covered through SERC-community literature (Daphne, Blackburn digital-twin DL, Vierlboeck NLP4RE, Topcu LLM ceiling).

**L2 persistence framing.** Article's central thesis became "each new paradigm has become a durable substrate." Subsumes the cumulative-not-substitutional argument and the hybrid-systems point under one unified persistence thesis. Threaded through introduction, every paradigm section's persistence sentence, and the conclusion punchline ("the durable investment is at the layers, not the frontier").

**Capability + limitation symmetry.** Two-bullet template applied to every paradigm section per R2 #15 meta-theme: italic pair "What this paradigm enabled..." + "Where this paradigm reached its ceiling." Section 2 (Expert Systems) variant: "What this paradigm enabled that manual practice alone could not" (no prior paradigm to compare).

**Tool-calling section overhaul.** Section 6 (Agentic AI) rewritten with three named pillars in separate paragraphs: Tool calling, Persistent memory, Goal-directed control loops. GenGroves workflow rewritten using explicit tool-call language and observe-and-correct framing. MCP positioned as the structured tool-call protocol.

**Citation set locked.** ML: Viros Martin and Selva 2019 (Daphne, IEEE J-STARS). DL primary: Blackburn and Austin 2021 (SERC-2021-TR-007). DL secondary: Hagedorn et al. 2020 (INSIGHT, same venue as article). NLP statistical: Vierlboeck, Lipizzi, and Blackburn 2025. NLP→LLM bridge: Topcu, Husain, Ofsa, and Wach 2025 (single self-cite). NN surrogate: Forrester, Sobester, and Keane 2008. CSER 2026: Wach, Sandman, and Iyer 2026. IS 2026: Philipbar and Wach 2026 + Wach, Philipbar, and Gregory 2026. Ruflo: rUv 2026.

**Figure 1 regenerated.** Programmatic generation via matplotlib. Top half: paradigm header, prominent bold date row, timeline arrow. Bottom half (~1.55× top): three info rows per paradigm (method/character/limitation) in pale paradigm tint with black bold 11pt text. Transparent background. No overflow on the Swarms column. Source script reusable for further iteration.

---

## 5. Open threads touched

- **Reviewer feedback cataloging convention.** Exercised: YAML primary + MD companion in source folder; canonical schema for cross-paper queries. INSIGHT cohort added to the reference cohort list.
- **Paper status discipline rule.** Exercised: status changed only on user assertion (received reviewer comments → in revision → v3 to co-authors).
- **Auto-spawn background agents rule.** Exercised: SERC literature scan run as background agent without blocking main thread.
- **Discuss before executing rule.** Exercised throughout: every substantive change debated and confirmed before execution. Multiple multi-option debates resolved by user: SERC sub-options (C-1/C-2/C-3/C-4/C-5a/C-5b/C-5c), persistence framing (L1/L2/L3), call-to-action third opening (alpha/beta/gamma), Figure 4 reframe (alpha/beta/gamma plus i/ii/iii disposition), figure 1 styling (multiple iterations).
- **Address intent not literal phrasing rule.** Exercised: user's "spreadsheet" request answered literally (CSV/XLSX) plus surfaced the canonical YAML+MD format; user chose all three.

---

## 6. Out-of-scope items

1. **Co-author feedback.** Pending from Alejandro and Brad. No further user action expected until co-author edits return.
2. **Final Word re-render with v6.1 Figure 1.** Word doc currently embeds the older Figure 1; needs re-render once co-author edits land. Image asset `AI_history_overview_v5.png` ready.
3. **Hamilton 2026 reference removal in user's docx.** User's edited v3.docx still has the orphaned Hamilton reference; user needs to remove from Word manually (or re-render from current markdown).
4. **Page numbers.** A3 unverifiable from markdown; user needs to add via Word UI Insert → Page Numbers, or modify reference template and re-render.
5. **Bibliographic verification (4 items).** Vierlboeck author order (Wiley page); Topcu in-press details; CSER 2026 page numbers when proceedings publish; IS 2026 page numbers when proceedings publish.
6. **Side note S1 (COSYSMO/MACQ retire).** Out of scope for this article; flag for future PostWach CTO portfolio session.

---

## 7. Next session entry hints

- **If co-author edits return:** open `Wach_Salado_INSIGHT_2026_AI_History_v3.docx`; extract via pandoc; diff against current v3.md to identify co-author changes; integrate into v4 markdown; re-render.
- **If editor responds:** check whether revisions are required vs. accept-as-is; reuse `reviewer_feedback.yaml` schema for any new comment cohort.
- **If re-rendering v3 with v6.1 Figure 1:** ensure `AI_history_overview_v5.png` is in source folder and v3 markdown references it; re-run `pandoc --reference-doc=Wach_Salado_INSIGHT_2026_AI_History_v1.docx`.
- **Bibliographic verification:** Vierlboeck check via `https://onlinelibrary.wiley.com/journal/15206858`; Topcu via Wiley DOI 10.1002/sys.21810; CSER and IS 2026 page numbers track conference proceedings publication schedule.
- **Reusable scripts:** all five scripts in `01 PostWach/scripts/` are venue-agnostic and can be applied to future paper revisions.
