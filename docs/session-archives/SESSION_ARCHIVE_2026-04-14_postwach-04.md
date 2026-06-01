# Session Archive: 2026-04-14 PostWach-04

**Hive:** PostWach
**Project:** Outreach — Agentic Swarm Workflow Design deck (for Tom McDermott discussion)
**Date:** 2026-04-14
**Duration:** ~1 hour (paused mid-deck)
**Focus:** Iteratively build a generic deck explaining how to design agentic workflows in a swarm AI toolset, oriented to Tom McDermott's email inquiry.

---

## Session Summary

Tom McDermott emailed requesting a walkthrough of how to design an agentic workflow in a swarm AI toolset, using the NNSA PD Workbench demo as an example and comparing to the FOREST/STPA/CRRM workflow on his current project. Tom is specifically interested in user interface integration and the stages of human interaction with agents. Meeting options proposed: Monday 3pm or Tuesday 4pm.

User decision: build a **generic** deck (not NNSA-specific, not FOREST/STPA/CRRM-specific). Items 2 (generic workflow design) and 4 (UI + human-interaction staging) from the initial scoping are the keys. NNSA example and FOREST/STPA/CRRM mapping will be de-emphasized; FOREST/STPA/CRRM tailoring will appear only as a generic "if I were to" template slide.

Delivery format: Markdown deck with Mermaid diagrams (option b from format proposal). Target location: `02 My Outreach/Agentic_Swarm_Workflow_Design/deck_v0.1.md`.

Working method (user-requested): iterative bullet-debate per slide, similar to the TRAK build pattern. Draft bullets, user critiques, refine, accept, move to next slide.

Slides drafted, debated, and accepted (bullets only, not yet written to file):
- **1A — The Automation Spectrum** (scripted / single-agent / swarm).
- **1B — Anatomy: Agentic vs. Swarm** (agentic traits, swarm elevators, hive-vs-swarm distinction promoted here).
- **2 — Conceptual Building Blocks** (skill, agent, command, hook, memory as substrate). Visual: three-layer stack diagram with memory underneath.
- **3A — Anatomy of the Four Artifacts** (file, shape, trigger, mental model for each). Code snippets deferred to appendix.
- **3B — Composing Artifacts into a Hive** (hive = curated assembly; hive vs. swarm clarified).
- **3C — Memory: the Substrate** (four layers: session/project/swarm/learned; namespaces as the isolation mechanism answering Tom's question).
- **3D — Memory Durability & Drift** (accumulate vs. trim vs. curate-with-decay; drift mechanisms; governance choices).
- **4 — Topology Choices** (hierarchical / pipeline / mesh / hybrid; what topology determines; choosing heuristic).

Private backup slides drafted (user will strip before sending to Tom):
- **P1 — The Hive-of-Hives Pattern** (generic, no PostWach specifics).
- **P2 — Governance Across Hives — Open Questions** (shared-artifact ownership patterns, cross-hive ticketing, policy inheritance, memory crossing).

Slides planned but not yet drafted:
- **5 — Workflow Design Method** (five-step recipe: decompose, assign, handoffs, gates, iterate).
- **6 — Human-in-the-Loop Staging** (five interaction modes: initiate, steer, approve, correct, audit). This is the keystone slide for Tom's stated interest.
- **7 — UI Integration Patterns** (CLI, chat, dashboard, doc-in-the-loop; gate-to-affordance mapping).
- **8 — Failure Modes & Governance** (drift, cost runaway, hallucinated artifacts; gates and post-validation as mitigations).
- **9 — "If I were to" template** (generic mapping Tom can apply himself, no project specifics).
- **10 — Appendix** (glossary, artifact code-snippets, NNSA pointer, INSIGHT article pointer).

Through-line established: Tom's isolation question ("how can one step/agent pair NOT be shared with another step/agent pair?") is answered across Slides 3C (namespaces as isolation mechanism), 4 (pipeline topology with isolated namespaces is the natural fit), and anticipated in Slide 6 (humans sit at isolation boundaries reviewing handoff artifacts).

## Key Decisions

- **D1.** Format: Markdown deck with Mermaid diagrams. Render to PDF later. Location: `02 My Outreach/Agentic_Swarm_Workflow_Design/deck_v0.1.md`.
- **D2.** Scope: generic. De-emphasize NNSA PD Workbench and FOREST/STPA/CRRM specifics. FOREST/STPA/CRRM treated only as an "if I were to" template slide.
- **D3.** Slide 1 splits into 1A (Spectrum) and 1B (Anatomy) because the original single-slide draft was too dense.
- **D4.** Five building blocks: skill, agent, command, hook, memory. Memory is the substrate, not a peer artifact.
- **D5.** Creation-mechanics section splits into 3A (artifact anatomy) + 3B (hive composition) + 3C (memory substrate). Option (iii) from the three-way choice.
- **D6.** Memory Durability and Drift earns its own slide (3D). Debated vs. folding into Failure Modes; decided memory-durability is a design choice and belongs with the memory discussion, not with runtime failure modes.
- **D7.** Hive-of-hives content kept as private backup slides (P1, P2), not in the Tom-facing deck. User considers hive-of-hives a trade secret. User will delete these slides before the meeting.
- **D8.** Hive vs. swarm distinction promoted to Slide 1B (Framing), so vocabulary is clean from the start. Not on 3B.
- **D9.** Slide 2 visual: stack diagram with three layers (Entry / Execution / State). Reinforces memory-as-substrate.
- **D10.** Slide 3A uses bullet format on the slide; code snippets for each artifact go to the appendix.
- **D11.** Four topologies named in Slide 4: hierarchical, pipeline, mesh, hybrid. Pipeline is the natural fit for Tom's FOREST/STPA/CRRM mental model.
- **D12.** Blackboard accepted as a fifth topology on Slide 4. Relevant to Tom's FOREST/STPA/CRRM context where a shared analysis artifact is iteratively annotated. "Topology not equal to agent count" bullet kept but rephrased more clearly.
- **D13.** In Slide 5 (Workflow Design Method), topology choice comes before agent assignment. Topology is Step 2, not Step 3, because topology shapes the agent roles rather than the other way around.
- **D14.** Slide 8 (Failure Modes and Governance) kept lean: four failure classes plus governance-as-a-layer framing on the main slide. Detailed failure catalog pushed to backup B4; governance mechanism map pushed to backup B5; zero-trust analogy and circuit-breaker pattern pushed to backup B6.
- **D15.** STPA worked example of the Slide 9 template lives in backup B7, not the main deck. Main deck stays generic so Tom can apply the template to his own context.

## Post-Break Slides Drafted and Accepted

After the break, the session continued and the deck was completed:

- **Slide 4 refined** with fifth topology (blackboard) added; "topology not equal to agent count" bullet rephrased; Mermaid diagrams drafted for all five topologies.
- **Slide 5 — Workflow Design Method** drafted and accepted. Five-step recipe with topology as Step 2 (before agent assignment), per D13.
- **Slide 6A — Core Interaction Modes** drafted and accepted. Five modes: Initiate, Steer, Approve, Correct, Audit.
- **Slide 6B — Gate Design** drafted and accepted, including the isolation-gate connection that answers Tom's namespace-isolation question.
- **Slide 6C — Anti-Patterns** drafted and accepted.
- **Slide 7 — UI Integration Patterns** drafted and accepted. Five surfaces: CLI, chat, dashboard, doc-in-the-loop, approval inbox.
- **Slide 8 — Failure Modes and Governance** drafted as a lean core slide with most content pushed to backup (see D14).
- **Slide 9 — Generic "If I were to" template** drafted. Six-question fillable template.
- **Slide 10 — Appendix** drafted. Glossary (12 terms), four artifact code snippets (skill, agent, command, hook), pointers to NNSA PD Workbench, INSIGHT article, AI Circuit Breaker.
- **Backup slides drafted:** B4 (full failure mode catalog), B5 (governance mechanism map), B6 (zero-trust analogy and circuit breakers), B7 (STPA worked example of the Slide 9 template).

Deck file fully drafted at `02 My Outreach/Agentic_Swarm_Workflow_Design/deck_v0.1.md`, approximately 600 lines, covering all main slides 1A through 10, backups B1 through B7, and private P1 through P2.

## Open Items for Next Session

1. Draft reply to Tom proposing Monday 3pm or Tuesday 4pm.
2. Strip private backup slides P1, P2 before sending to Tom.

## Open Research Threads (raised this session)

- **SE-specific human roles.** The generic 20-role catalog used in the deck may not map cleanly to systems engineering practice. Candidate ontology task: derive an SE-specific subset or extension of the role catalog.
- **Minimum role set.** Is there a smaller set of higher-level human roles from which the 20 derive by specialization or composition? Candidate ontology and research question the user wants to revisit in a later session.

## Files Created / Modified

### Session archive (created, updated post-break)
- `docs/session-archives/SESSION_ARCHIVE_2026-04-14_postwach-04.md` (this file)

### Deck (created, fully drafted)
- `02 My Outreach/Agentic_Swarm_Workflow_Design/deck_v0.1.md` approximately 600 lines. All main slides 1A through 10, backups B1 through B7, private P1 through P2. Slide 4 updated post-break to reference the rendered PNG topology images alongside the Mermaid source blocks.

### Rendered deliverables (created post-break)
- `02 My Outreach/Agentic_Swarm_Workflow_Design/Agentic_Swarm_Workflow_Design_Deck_v0.1.pdf` (214 KB final, rendered via pandoc + xelatex; initial render was 171 KB before image embedding)
- `02 My Outreach/Agentic_Swarm_Workflow_Design/Agentic_Swarm_Workflow_Design_Deck_v0.1.docx` (70 KB final; initial render was 31 KB)
- `02 My Outreach/Agentic_Swarm_Workflow_Design/Agentic_Swarm_Workflow_Design_Deck_v0.1.pptx` (generated via pandoc with `--slide-level=2`)

### Topology diagram images (created post-break)
Rendered via mermaid-cli (mmdc v11.12.0) to `02 My Outreach/Agentic_Swarm_Workflow_Design/images/`:
- `topology_hierarchical.png` (6.3 KB)
- `topology_pipeline.png` (3.0 KB)
- `topology_mesh.png` (4.7 KB)
- `topology_blackboard.png` (14.1 KB)
- `topology_hybrid.png` (11.2 KB)

## Session Completion

After the post-break archive update, the session continued with rendering work:

1. Deck rendered to PDF via pandoc + xelatex (171 KB initial, text-only).
2. Deck rendered to DOCX (31 KB initial).
3. Five topology Mermaid diagrams rendered to PNG via mermaid-cli (mmdc v11.12.0) and saved to the `images/` subfolder.
4. Deck file Slide 4 amended to reference the PNG images alongside the existing Mermaid source blocks.
5. PDF regenerated with embedded images (214 KB final).
6. DOCX regenerated (70 KB final).
7. PPTX generated via pandoc with `--slide-level=2` as the primary delivery format. PDF and PPTX opened for user review.
8. Session terminated by user.

### Additional Decisions

- **D16.** PPTX generated via `pandoc --slide-level=2` is the primary delivery format for Tom. PDF and DOCX retained as backups.

## Tom McDermott Email (for context)

Tom requested: discussion of how to design an agentic workflow in a swarm AI toolset, using the NNSA demo as an example, comparing to the FOREST/STPA/CRRM workflow on his current project. Primary interest: user interface integration and stages of human interaction. Proposed meeting: Monday 3pm or Tuesday 4pm (small-team meeting already on calendar).

User note: Tom is detailed and will not be the last to make this inquiry. User also wants to understand these concepts better for communication and funding purposes.
