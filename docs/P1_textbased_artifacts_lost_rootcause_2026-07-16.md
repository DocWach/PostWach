# Root-cause report: the text-based artifact rendering was lost from the Results (2026-07-16)

**Author:** PostWach (CTO). **Provenance (R018):** claude-opus-4-8[1m], Anthropic, Claude Code CLI, principal-directed.
**Trigger:** The principal noticed that §5.1 Text-based practice no longer shows the artifacts. The text-based rendering of the four artifacts (natural-language SR, SD, VR, VM) is the basis the descriptive-based and science-based approaches formalize, and it has disappeared from the Results. This is the THIRD consecutive root-cause report; it is the same meta-pattern as `P1_review_misses_rootcause_2026-07-15.md` and `P1_results_misalignment_rootcause_2026-07-16.md`.

## Section 1 — What was lost

The text-based approach's distinctive contribution is that it *renders* the stakeholder needs as the four verification artifacts in natural language; the descriptive-based (SysML v2) and science-based (WySE) approaches then formalize those same artifacts. That rendering is foundational: it is what the other two build on. In the current draft:
- §5.1 Text-based practice contains only the relationship analysis (existence, characterization, admission). It shows no artifacts.
- The SR table (`tab:sr`) and the natural-language descriptions of the system design, verification requirements, and verification models now sit in Methods §4.2.4 "The notional case," introduced as "From these needs *we derive* five system requirements" — an approach-neutral derivation, not attributed to text-based practice.
- The original framing sentence, "the text-based approach renders the stakeholder needs as the four verification artifacts, and the descriptive-based and science-based approaches formalize the same artifacts," is gone.

The result is an asymmetry: §5.2 shows the SysML rendering (the listing) and §5.3 the WySE apparatus, but §5.1 shows no text-based rendering, even though the text-based rendering is the input to the other two.

## Section 2 — Where it went, and how it happened

On the earlier turn the principal directed that §5.1 "Structural overview" was misaligned and its content should go to Methods. I dissolved §5.1 and, in `_new423.tex`, moved the SR table plus the SD/VR/VM descriptions into Methods §4.2.4, reframing them as "the notional case" and "the requirements we derive." In doing so I dropped the sentence that attributed the natural-language rendering to text-based practice.

So the content moved wholesale by its surface (a table and some descriptions) and I collapsed its meaning to a single role: "the fixed case." But `tab:sr` and the artifact descriptions carry TWO roles: (a) the common specification the comparison runs against, and (b) the text-based approach's natural-language rendering of the artifacts, which the other approaches formalize. I preserved role (a) and erased role (b).

## Section 3 — Root cause

I move content by LOCATION, not by ROLE. I had no map of what each piece of the manuscript *means* and where its meaning belongs, only a view of where it currently sits. When the instruction was "move §5.1 to Methods," I moved everything in §5.1 to Methods, including an element (the text-based rendering) whose semantic home is the Results, under text-based practice. I also failed to flag the consequence at the time: it is my responsibility to notice that relocating the text-based rendering out of the Results would erase the "text-based is the basis for the other two" relationship, and to raise it before executing. I did neither.

This is the same failure family as the two prior reports: I satisfy the literal instruction while losing a semantic relationship, because my checks are structural (does it compile, do refs resolve, is content present somewhere) and never ask "does each element still play the role it needs to, in the place that role belongs."

## Section 4 — Recurrence

Three reports, one meta-pattern: local/mechanical execution that loses meaning.
- 2026-07-15: wrong Results structure survived review because I checked correctness, not design-conformance.
- 2026-07-16 (misalignment): a Methods restructure duplicated §5.1 because I did not check the downstream section.
- 2026-07-16 (this): a directed content move erased a semantic role because I moved by location, not by role.

The through-line is the absence of a content-role discipline. The document-QA SOP, flagged as unbuilt in both prior reports, is now flagged a third time; it must include a content-role map, not just a section-boundary check.

## Section 5 — Preventive measures

1. **Content-role map for the paper.** Enumerate each element and its role: common inputs (Methods) vs. approach outputs (Results). The text-based rendering of the artifacts is an *approach output* and belongs in §5.1; the stakeholder needs and the fixed SD/VM selection are *common inputs* and belong in Methods. Any move consults this map.
2. **Move by role, and flag role changes.** When relocating content, state its role explicitly and confirm the target section is where that role belongs. If a move would change or erase a role (e.g., "this is the text-based rendering, not just the case"), surface it before executing rather than after.
3. **Symmetry check across parallel sections.** In a by-approach Results, each approach subsection should carry the same kinds of element (its rendering, then its analysis). A missing element in one subsection (here, no rendering in §5.1) is a defect a symmetry pass would catch.

## Section 6 — Proposed fix (for principal confirmation)

Restore the text-based rendering to §5.1 as the foundation the other approaches build on:
- **Move to §5.1 Text-based practice:** the SR table (`tab:sr`) and the natural-language renderings of the SD, VR, and VM, introduced as "text-based practice renders the artifacts as follows; the descriptive-based and science-based approaches formalize these same artifacts (§5.2, §5.3)." Then the existing relationship/characterization/admission analysis follows.
- **Keep in Methods §4.2.4 "The notional case":** the stakeholder needs (`tab:notional-case`) and the fixed selection of one system design (SD4) and two verification models (VM-A/VM-B = VM8/VM6), as the common test setup. The requirements themselves are then rendered by each approach in the Results.
- **Restore symmetry:** §5.1 shows the text-based rendering, §5.2 the SysML listing, §5.3 the WySE apparatus, each followed by its analysis and its In-sum summary.

Open question for the principal: whether the SR table should live in §5.1 (as the text-based rendering, my recommendation) or stay in Methods with §5.1 showing the rendering in prose and referencing it. I recommend the former.
