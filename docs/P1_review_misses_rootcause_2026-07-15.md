# Root-cause report: how P1 structural/formatting defects survived every review (2026-07-15)

**Author:** PostWach (CTO). **Provenance (R018):** claude-opus-4-8[1m], Anthropic, Claude Code CLI, principal-directed.
**Trigger:** After a full session of adjudication, restructuring, an RBW review, refcheck, and a PDF+DOCX build declared "done," the principal found five defects on first read. This report diagnoses why the review layers missed them. Companion to the R020 skills-first report; same failure family.

---

## Section 1 — The five misses (what the reviews should have caught and did not)

- **M1 (structural, severe).** §5 Results is organized **by question** (establish artifacts / which relationships / how mathematical / which admitted / summary). This is the exact structure co-author Alejandro **rejected**. The agreed structure is **by approach** (structural overview, text-based, SysML v2, WySE, comparison). This was even discussed mid-session ("are the results by approach?") and still shipped by-question.
- **M2 (absent asset).** The methods/protocol visual (`figures/protocol_map.png`) was created, rendered, and approved by the principal, then **never inserted** into `main.tex`. It is in neither the PDF nor the DOCX. An approved asset was orphaned.
- **M3 (content, framing).** Table 4 (`tab:gap-summary`) frames the gap only as a **practice** gap and omits the **theory** gap; the framing ("gap in current practice / where addressed") does not present it as THE single gap the paper addresses.
- **M4 (structural, redundancy).** §3.3 "The definitional gap" is thin enough that the principal would side with Alejandro and cut it; it was carried forward unquestioned.
- **M5 (formatting fidelity).** The DOCX tables do not match the PDF. The build was signed off on **content** verification (cites resolved, headings present, listing present) without **rendering the DOCX and comparing tables to the PDF**.

---

## Section 2 — Per-miss root cause

| Miss | Proximate cause | Why no gate caught it |
|---|---|---|
| M1 | The by-approach decision lived only in conversation; the draft retained the inherited by-question skeleton. | No gate encodes "agreed structure." refcheck gates cites; latexmk gates compile. Neither knows the intended section order. |
| M2 | The figure was made as a thinking aid; the "insert + caption + call out" step was never closed. | Presence-checks verify what IS in the doc; nothing checks that every created asset LANDED in the doc. Absence is invisible. |
| M3 | The gap table was written before the asserted-vs-entailed thesis fully absorbed the theory-gap point (the `mathmbse` SLR finding). | No check maps thesis claims to the tables that must carry them. |
| M4 | Section inherited from an earlier outline; never re-tested against "does this earn its place / would a reviewer cut it?" | Structural-revision checklist (research-writing skill) was not run as a gate. |
| M5 | DOCX verified by extracting text and counting elements, not by rendering. | "Verify formatting by rendering and LOOKING" was applied to the PDF and not extended to the DOCX. |

---

## Section 3 — Cross-cutting root causes (the real diagnosis)

1. **Reviews hunted errors in what was present; none checked conformance to intent.** refcheck (cites), latexmk (overfull/undefined), the RBW pass, and my DOCX check all asked "is what's here correct?" None held the **agreed design** (by-approach Results, the section intents, each co-author's specific ask) as the oracle. Error-hunting is structurally blind to "wrong structure" (M1, M4) and "required thing absent" (M2, M3).

2. **The highest-value requirement was the least instrumented.** The single most important requirement this session was "match the structure Alejandro demanded." It had **no gate at all**, while low-stakes properties (cite existence, zero overfull) had automated gates. Instrumentation was inversely proportional to importance.

3. **Absence is invisible to presence-checks.** M2 (orphaned figure) and M3 (missing theory-gap dimension) are absences. Every check run was a presence-check. Catching an absence requires a **spec of what should be there** to diff against; none existed. Same family as the DV004 sweep misses and the standing document-QA SOP TODO.

4. **Compilation success masqueraded as done.** "40 pages, 0 overfull, 0 undefined, 50/50 cites" reads as success and anchored the sign-off on *it renders* rather than *it is the right paper*. A necessary gate was treated as sufficient.

5. **Formatting fidelity verified by content, not by eye (recurring).** M5 repeats a documented recurring failure ([[feedback_formatting_verify_visually]], [[feedback_match_format_means_file_level]]): I invoked render-and-look for the PDF, then verified the DOCX by extraction and never looked at its tables.

6. **The RBW charge was wrong.** The adversarial review looked for internal defects in the prose as written (and even produced false positives on `\Cref`), never for fitness-for-purpose. An RBW whose charge is "find text defects" cannot find "this is the structure the reviewer rejected."

7. **Skills-first gap compounded (ties R020).** research-writing was applied ad hoc. Its Phase-3 structural-revision checklist ("does the structure serve the content? are sections in the right order? is anything unnecessary? is anything missing?") maps almost one-to-one onto M1/M2/M4. Skipping the skill skipped the checklist that was built to catch exactly these.

---

## Section 4 — Why each review layer specifically failed

- **refcheck / R019:** in scope only for citations. Correctly silent. Not a defect of refcheck; a misread that a green refcheck implied a clean manuscript.
- **latexmk build:** gates typesetting validity, not editorial structure. Correctly silent.
- **RBW holistic review:** wrong oracle (internal-defect hunting, not design-conformance). Produced noise (false-positive `\Cref` reds) while missing the structural miss.
- **My DOCX verification:** presence/extraction only; never rendered; never compared to the PDF.
- **The human-in-the-loop cadence:** the by-approach question was raised and answered in conversation but never written down as a requirement, so it evaporated between turns and across the context compaction.

---

## Section 5 — Preventive measures (gates, not intentions)

1. **Design-conformance checklist per manuscript (the document-QA SOP, now urgent).** Encode every agreed structural decision and every co-author ask as a checkable line (e.g., "Results ordered by approach: text / SysML / WySE / comparison — Y/N"; "every reviewer comment mapped to a disposition — Y/N"). Verify the artifact against it before "done." Conversationally-agreed structure must become a written, checkable requirement in the same turn it is agreed.
2. **Asset-placement ledger.** Every figure/table: created -> placed -> captioned -> called out in prose. An orphaned asset is a defect. Extends [[feedback_figures_label_and_callout]].
3. **Dual-format fidelity = render both and diff by eye.** For any deliverable in two formats, render BOTH and compare the same regions (tables, figures, equations). Never sign off from content extraction. Extends [[feedback_formatting_verify_visually]].
4. **Separate the build gate from the fitness gate.** "It compiles" and "it is the right paper" are different checks; a green build never stands in for design-conformance.
5. **RBW charge includes fitness-for-intent.** At least one reviewer lens must take the agreed design as the oracle and ask "does the artifact match what we decided and what the reviewer demanded," not just "find defects."
6. **Skills-first as a real gate.** Run the research-writing structural-revision checklist against the draft as an explicit step, not ad hoc.

---

## Section 6 — Disposition

Fixes for M1-M5 are planned and presented to the principal for the judgment calls (§3.3 disposition; the Results transposition and the appendix-inline moves; methods-visual placement); the DOCX formatting pass is sequenced last, after the structural edits settle. This report is the process record; the document-QA SOP (measure 1) is promoted from TODO to the next PostWach build task. Recommend routing measures 1-3 to Alpha Empress for portfolio governance, as they generalize beyond this manuscript.
