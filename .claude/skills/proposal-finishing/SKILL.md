---
name: proposal-finishing
description: The end-to-end procedure for taking an SBIR/technical-volume proposal (or a review of one) from draft to submission-ready, derived from the DLA DTO (NV011) work. A composition/orchestrator of existing skills, run the phases in order, each gated. Use when finishing, reviewing, or camera-readying a proposal or technical volume, or when a principal says "follow the procedure used for the DLA proposal." NOT for one-off content edits (just edit) or for matching an external template's look (use document-format-fidelity directly).
metadata:
  type: reference
  integration_status: (b) demonstrated — DLA NV011 V7->V8, 2026-07-19/20
---

# /proposal-finishing

The repeatable SOP behind the DLA DTO (NV011) finishing pass. It exists because proposal finishing kept being improvised, and improvisation missed simple things (duplicate captions, unnumbered tables, orphan refs, oversized figures, boilerplate from other proposals). This procedure is a **fixed sequence of gated phases, each backed by a skill**. Run them in order; do not skip the gates.

## Governing rules (always on)
- **Copies only.** Never edit the master. Work on a versioned copy; integer version = the one actually sent. [[feedback_no_overwrite_manual_edits]]
- **Cyan = the reviewer's changes.** Every insertion/rewrite is highlighted turquoise so the recipient sees exactly what changed.
- **Render is truth; attributes lie.** No formatting item is "done" from XML/attributes, only from rendering to PDF and LOOKING. [[feedback_formatting_verify_visually]]
- **Necessary ≠ sufficient.** A clean automated scan does not mean done; the render-and-look gate is separate and also required. [[feedback_holistic_formatting_fidelity]]
- **No fabrication.** No invented citations, expansions, dates, or program details; use `[PLACEHOLDER]` or flag. [[feedback_references_triple_check]]

## The phases (each maps to a skill)

| # | Phase | What it does | Skill |
|---|---|---|---|
| 0 | **Baseline & safety** | Copy the master to a working version; extract to text (pandoc) for analysis; set version discipline. | — |
| 1 | **Requirements & needs (problem-first)** | Inventory the solicitation's explicit requirements; capture stated + web-inferred stakeholder needs; do NOT jump to a solution. | **stakeholder-analysis**; **deep-research** (or research agents) for inferred needs |
| 2 | **Reassess** | Trace requirement/need → draft coverage → gap → recommendation (coverage claimed only with a draft quote). Catalog defects. | — (analysis) |
| 3 | **Content edits (cyan)** | Fix defects; add needs-responses (bio, DE perspective, etc.) positioned as answers to named needs; de-boilerplate. | **research-writing** / **grant-writing** |
| 4 | **References (triple-check)** | Determine cited-vs-listed; delete orphans; resolve dangling cites with NO fabrication; reconcile in-text↔bib; renumber/remap; verify each resolves. | **reflookup**, **refverify**, **refcheck** (R019) |
| 5 | **Figures** | Reproduce as legible, compact, editable diagrams (Mermaid/mmdc); bold labels, no lines over text; embed INLINE with caption paired + keep-with-next. | mmdc + [[feedback_diagram_formatting]] |
| 6 | **Tables** | Unify style (borders/shading/alignment/font); numbered caption above each; in-text callout for each. | [[feedback_figures_label_and_callout]] |
| 7 | **Headings / typography** | Uniform heading hierarchy and sizes; fix outliers and nested-numbering collisions; consistent body font. | — |
| 8 | **QA gate + render-and-look (BOTH)** | Run the scan; resolve every FAIL, review every WARN. THEN render to PDF and view every figure/table/heading region. | **document-qa** (check.py) + **document-format-fidelity** |
| 9 | **Page limit** | Measure by rendering (don't estimate); consolidate to the cap (figures/tables count). Confirm the cap from the BAA if not in the topic. | — |
| 10 | **Close-out** | Cover note (every change + accept/decline checklist); if a lab session, session archive + R014 scorecard; promote the send version. | — |

## Running it
1. Announce which phase you are in. 2. Invoke that phase's skill (Skill tool) or cite its named framework, per turn (R020 bright line). 3. Do NOT advance past a gate (Phase 4, 8) until it passes. 4. When reviewing someone else's master (e.g., an RTSync draft), do Phases 1–4/8 as **cyan-marked copies + a cover note**, and FLAG (with locations) any owner-content defect you won't surgically rewrite (their figures, their malformed tables), rather than editing their master.

## Adaptation for a review (vs. owning the doc)
When the deliverable is *your review/feedback* on another team's master: still run Phases 1–2 fully; in Phase 3 mark changes cyan on a copy; in Phases 5–7 FLAG owner-content issues with exact locations instead of rewriting; always run Phase 8 (the scan catches their defects too) and deliver the Phase 10 cover note.

## Related
- **document-qa** (Phase 8 scan), **document-format-fidelity** (Phase 8 look + external-template match), **stakeholder-analysis** (Phase 1), **reflookup/refverify/refcheck** (Phase 4), **research-writing/grant-writing** (Phase 3), **deep-research** (Phase 1 inferred needs).
