# Session Archive: 2026-04-15 PostWach-01

**Hive:** PostWach
**Project:** Outreach — Agentic Swarm Workflow Design deck (Tom McDermott meeting prep)
**Date:** 2026-04-15
**Duration:** ~30 minutes (time-boxed, meeting at T+12)
**Focus:** Rebuild the Tom-facing PPTX as a genuine slide deck rather than an outline dump; add missing Mermaid diagrams; add a "training" clarification slide.

---

## Session Summary

Immediately prior to Tom McDermott's meeting, the user opened the v0.1 deliverables (PDF + PPTX) from the previous session and found that the PPTX did not feel like actual slides — the DOCX/PDF read as design notes, and pandoc had rendered those notes verbatim as bullet-heavy slides. With ~12 minutes before the meeting, the user requested a rebuild.

Three paths were debated (rewrite markdown for slide-shape; pandoc + reference.pptx template; python-pptx hand-build). Recommendation was a hybrid, but time forced option 1 only. v0.2 was written as a new clean slide-shape markdown file, rendered to PPTX, and iterated.

After initial render, the user flagged two gaps:

1. Mermaid diagrams were critical and several were missing (the v0.1 ASCII three-layer stack, automation spectrum, memory layers, gate, workflow method, and HIL modes had no renders — only the 5 topology PNGs from yesterday existed).
2. The topology slide stacked 5 images side-by-side using pandoc width hints that PPTX does not honor, so the images rendered at inconsistent sizes.

Both were addressed: six new Mermaid diagrams authored and rendered via mmdc; the topology slide split into five separate slides (one per topology); a new "What 'Training' Actually Means" slide added to answer a recurring concept-level question (the base model is frozen, hives are *configured and equipped* rather than trained).

Final deliverable: `Agentic_Swarm_Workflow_Design_Deck_v0.2c.pptx` with all 11 PNGs embedded (5 topologies + spectrum, stack, memory-layers, gate, workflow-method, hil-modes). Private slides P1/P2 omitted from v0.2 from the start.

## Key Decisions

- **D1.** Build v0.2 as a *new* slide-shape markdown file (`deck_v0.2_slides.md`), keeping v0.1 as design notes / speaker reference. Do not edit v0.1 content in place.
- **D2.** PPTX is the only delivery format for Tom. Skip PDF and DOCX renders to save time.
- **D3.** Omit private slides P1 and P2 from v0.2 entirely — avoid the strip-before-sending step.
- **D4.** Split the five-topology slide into one slide per topology. Pandoc PPTX does not honor side-by-side width hints, so single-image slides render more consistently.
- **D5.** Add a new slide "What 'Training' Actually Means" — positioned after *Memory: The Substrate* and before *Memory Durability and Drift*. Frames the hive as *expert with a well-organized notebook*, not *student who took classes*. Answers a recurring audience question (Tom-class, but general).
- **D6.** Six new Mermaid source files authored under `images/`: `spectrum.mmd`, `stack.mmd`, `memory_layers.mmd`, `gate.mmd`, `workflow_method.mmd`, `hil_modes.mmd`. All rendered to PNG via mmdc at 1600px wide.
- **D7.** File versioning: v0.2a/b/c reflect successive rebuilds after pandoc permission errors (PPTX held open in PowerPoint). Use a new suffix letter per rebuild rather than closing the file during live meeting prep.

## Files Created / Modified

### Created
- `02 My Outreach/Agentic_Swarm_Workflow_Design/deck_v0.2_slides.md` — clean slide-shape markdown, ~23 main slides, no P1/P2
- `02 My Outreach/Agentic_Swarm_Workflow_Design/Agentic_Swarm_Workflow_Design_Deck_v0.2.pptx` — initial render (locked, superseded)
- `02 My Outreach/Agentic_Swarm_Workflow_Design/Agentic_Swarm_Workflow_Design_Deck_v0.2b.pptx` — post-diagram render (superseded)
- `02 My Outreach/Agentic_Swarm_Workflow_Design/Agentic_Swarm_Workflow_Design_Deck_v0.2c.pptx` — final render with training slide + split topology slides
- `images/spectrum.mmd` / `.png` — 3-box automation spectrum
- `images/stack.mmd` / `.png` — three-layer stack replacing v0.1 ASCII art
- `images/memory_layers.mmd` / `.png` — four memory layers + namespace callout
- `images/gate.mmd` / `.png` — gate as isolation boundary between phases
- `images/workflow_method.mmd` / `.png` — 5-step recipe flow with iterate arrow
- `images/hil_modes.mmd` / `.png` — five interaction modes placed across a workflow
- `docs/session-archives/SESSION_ARCHIVE_2026-04-15_postwach-01.md` (this file)

### Modified
- `02 My Outreach/Agentic_Swarm_Workflow_Design/deck_v0.1.md` — status section updated with v0.2 change log

## Open Items for Next Session

1. Debrief what actually worked and didn't in the Tom meeting; record which slides carried the conversation and which were skipped.
2. If v0.2 becomes a reusable template for future walkthroughs (Tom said "not the last to make this inquiry"), consider the hybrid approach originally proposed: pandoc + reference.pptx template for styling, python-pptx hand-build for the 3–4 structural slides that most benefit from custom layout.
3. Decide whether private slides P1 (Hive-of-Hives Pattern) and P2 (Governance Across Hives) should become a separate internal-only deck rather than backup slides in the Tom deck.
4. SE-specific human role catalog (flagged in the 2026-04-14 session) still open.
5. Minimum role set question (are the 20 modes derivable from fewer primitives?) still open.

## Context Carried Forward

- Meeting format preference (per 2026-04-14 session): walkthrough conversation, not formal presentation. PDF/DOCX had been judged suitable for screen-share at one point; user disagreed, triggered the v0.2 rebuild.
- Terminology discipline: *hive* vs. *swarm* (persistent workshop vs. runtime crew), *agent* vs. *skill* (perspective vs. procedure), *command* vs. *hook* (pull vs. push). v0.2 keeps these clean from Slide 2 onward.
- Training clarification (new this session): hives accumulate and curate; they do not update weights. Use this framing whenever a collaborator asks how the hive "learned" something.
