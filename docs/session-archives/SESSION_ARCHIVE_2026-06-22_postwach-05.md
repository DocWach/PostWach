# Session Archive — 2026-06-22 postwach-05

**Hive:** PostWach. **Researcher:** Paul Wach. **Model:** Claude Opus 4.8.
**Headline:** Synthesized an updated MOACRA proposal for sponsor Tom Tenorio (TDAC), reframed from an
ontology one-pager into a standing **Live-Virtual-Constructive (LVC) Cyber Mission Engineering Proving
Ground**. Produced a comprehensive internal working document, a four-partner coalition under the UofA
umbrella, a full-$14M/year budget frame with a government-versus-performer time-charging question, a
coherent figure set, and an 8-slide dark pitch deck for Tom to integrate or show leadership.

---

## Context
Update owed to Tom (Thomas Tenorio, TDAC) on 2026-06-23 after his 2026-06-08 meeting
(`Notes_2026-06-08.docx`) and the maturation of TDAC's strategy in his 2026-06-04 briefing
(`(U) TDAC MOACRA MBCRA UNCLASSIFIED Briefing 20260604.pdf`). Prior canonical artifact was the v3
"Mission Fitness First" one-pager (sent 2026-05-06). Worked in plan mode first, then built.

## TDAC vocabulary now canonical
MOACRA = Mission Ontology of Analysis for Cyber Risk Assessment, the Authoritative Source of Truth (ASOT)
backbone; MBCRA = Mission Based Cyber Risk Assessment; MBCRA-XX = echelon toolkits (T/C/A/X/I/V, MBCRA-MA);
"Semantic Factory" = the engine that emits them; T2COM = the Training + Transformation command merger;
FCC = Futures and Concepts Center (TDAC = its brain); ATEC = the downstream test command (TDAC = upstream
sister org); CAC TID = Combined Arms Center Transformation Integration Directorates (Col Shaw, Maneuver
Air); FM 3-0 = cyber as a warfighting domain; cyber agentic triads = Human / Virtual (AI-C2) /
Cyber-Physical; the 7-layer shift-left thread; LVC = Live-Virtual-Constructive. $14M/year TRMC ask;
Maneuver Air beachhead (more than one million unmanned platforms). **Tom = Thomas Tenorio** (resolves the
old "is Tom McDermott Jr?" question: no).

## The reframe (principal-directed "far more")
UofA pitches a **standing instrumented LVC Cyber Mission Engineering Proving Ground** (extended reality +
drones + robots + DEVS digital twin), not just an ontology. It instantiates TDAC's cyber triad in hardware
and makes cyber risk empirical (effects injection + measured mission-fitness degradation). Load-bearing
bridge: WRT-2516 "Systems Engineering Beyond the Horizon" projected the 2035 SE stack (XR, agentic swarms,
continuous V&V, digital twins, ontology foundations) and named its own gap, "technology-rich but
evidence-poor," calling for benchmark/evaluation infrastructure and pilot programs. The proving ground is
that evidence engine. WRT-2406 = "Optimized Portfolio Digital Engineering" (SERC-2025-TR-005).

## What was built (all in `05 MOACRA/_workspace/`)
- `MOACRA_Working_Synthesis_2026-06-22.md` - comprehensive internal working doc (14 sections + 3
  appendices): opportunity, proving ground, evidence-gap bridge, three pillars (ontology / mathematics /
  agentic swarms, "rigor at speed"), red/blue/white operating model, year-1 Maneuver Air demonstrator,
  coalition, full-$14M budget, transition (TRAK / valley of death), team, open items, vocabulary crosswalk,
  WRT future-capability menu, and a visuals plan with a ready ChatGPT hero prompt.
- `MOACRA_Proving_Ground_Deck_2026-06-22.pptx` - 8-slide dark deck matching Tom's style, for him to
  integrate/show leadership. Built by `build_deck.py` (python-pptx).
- Figures: `Fig2_EvidenceGapBridge_2026-06-22.png` (Mermaid), `Fig3_SevenLayerOverlay_2026-06-22.png`
  (two-row Mermaid), `Tom_Slide11_annotated_2026-06-22.png` (his seven-layer slide with layers 1-4
  highlighted, PIL), and reuse-ready extracts of Tom's slides 8/10/11/12 (pdftoppm). Hero (Fig 1) and the
  red/blue/white loop (Fig 4) are principal-generated ChatGPT renders.

## Key decisions (principal)
- Ambition ceiling: standing proving ground (year-1 demonstrator as the entry point).
- Year-1 scenario: Maneuver Air drone-swarm under contested cyber; MBCRA-T and MBCRA-A as example tools;
  explicit blue team alongside red.
- Coalition (tiered under UofA umbrella, all **existing UofA relationships**): RTSync (DEVS sim + twin;
  existing prime on SF24C-T003 and DV004), Peter Beling (UVA School of Data Science; CPS resilience;
  co-author), Bryan Watson (Embry-Riddle BID4R; bio-inspired SoS resilience), Violet Labs (digital thread
  feeding ATEC + CDAO data mesh). Framed as "potential partners."
- Budget: scope UofA + partners toward **nearly the full $14M/year as the performer** (not a minor slice);
  program ROM allocation brackets ~$14M. **Load-bearing question for Tom:** what share of the $14M is
  government time-charging (TDAC, ATEC, CAC, other federal entities) versus the UofA-plus-partners award.
- Deck: dark style, ~8 slides, audience = Tom to integrate/show leadership.

## Method / tooling notes
- Mermaid (mmdc): two-row layout needs an invisible `~~~` link between subgraphs plus SHORT subgraph titles,
  or it collapses to a single column and truncates titles. `wrappingWidth` controls node aspect.
- `pdftoppm` (from MiKTeX) extracts PDF slides to PNG; `fitz`/`pdf2image`/LibreOffice are absent here.
- PIL for the slide-11 annotation (coordinate grid to map label positions, translucent rounded-rect
  highlights + legend; verified by viewing the render).
- python-pptx for the deck; no PowerPoint/LibreOffice renderer available, so PowerPoint COM was avoided
  (would pop a window); deck verified structurally, visual review left to the principal.
- ChatGPT-browser image generation for the hero and red/blue/white renders (Codex cannot generate images);
  the hero prompt is saved in the working-doc Appendix C.

## Integration status (R016)
Proposed: the integrated physical-virtual proving ground, the MBCRA-XX cyber tools, cyber-effects injection
at scale, the MOACRA cyber ontology. Demonstrated (native domains): DEVS simulation (RTSync), agentic
swarms, ontology validation (governance ontology), resilience formalisms (Beling/Wach), TRAK, tri-model
red/blue/white review. WRT-2406/2516 = projection/roadmap authority, not a delivered physical testbed.

## Status / open
- "Good enough for now" per principal 2026-06-22. NOT yet sent to Tom.
- Condensing the working doc into a 2-page docx for Tom is an open follow-on.
- Deck not visually verified by the assistant (no renderer); principal to review in PowerPoint.
- Open for Tom: government-vs-performer budget split; real-data access (ATEC/CDAO); range/sim authorization;
  classification posture (keep year-1 unclassified); facilities; confirm Maneuver Air beachhead and a
  year-1 start; partner outreach confirmation for the coalition.

## Termination
No claude-flow swarm spawned. Work used five Explore subagents (one "prompt too long" failure, retried
compact and succeeded). `claude-flow agent list` = "No agents found." No background tasks left running.
Scratch grid/check images cleaned up. Memory updated (`project_mocra_proposal.md` + `MEMORY.md`).
Scorecard: `Papers/AI_Swarm_Productivity/data/scorecards/2026-06-22-postwach-05.yaml`.
