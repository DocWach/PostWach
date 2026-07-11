# Session Archive — 2026-07-09 postwach-03

**Hive:** PostWach (CTO / Chief Scientist). **Researcher:** Paul Wach. **Model:** Claude Opus 4.8 [1m] (main-loop; no subagents, no swarm).
**Focus:** Capability recon: assess whether Graphify and InfraNodus fit the hive-of-hives, and to what extent/how; document findings in `00 Planning and Execution`.
> PROVENANCE: run by Claude (Anthropic, Opus 4.8, claude-opus-4-8[1m], Claude Code main-loop) at Paul Wach's direction. Web review via WebFetch/WebSearch; no code installed or executed; no store writes; no commits; no agents spawned.

## Headline
Delivered a dual-lens, R016-tagged fit assessment. Central finding: the five links resolve to **two distinct tools**, and the recommendation splits accordingly: **adopt Graphify's code** (MIT, native skill+MCP fit, local-first) on a scoped pilot; **adopt InfraNodus's ideas** (AGPL + paid SaaS + data egress + Obsidian lock-in makes the code a poor fit for governed private hives). Principal confirmed the framing and **deferred the pilot to post-2026-07-12** (after the Fable cutoff).

## What was assessed
- **Graphify** (`Graphify-Labs/graphify`, `graphify.net`, `graphifylabs.ai` = one product, three fronts): MIT Python CLI + Claude Code skill + MCP server; tree-sitter AST (local, no LLM for code) + your-own-key LLM for docs/media; Leiden/NetworkX; outputs `graph.json`/`graph.html`/`GRAPH_REPORT.md`; per-edge EXTRACTED/INFERRED/AMBIGUOUS tags; local-first (only outbound call is the configured model).
- **InfraNodus** (Nodus Labs / Ways Ltd; `infranodus.com` + Obsidian plugin): AGPL-3.0 + paid SaaS text-network tool; differentiator is structural gap detection (betweenness/modularity) to research-question generation; NestJS/Prisma/PostgreSQL/Sigma.js/Textexture; sends graph conversions + prompts to their servers + OpenAI.

## Fit judgment (CTO lens)
- Graphify fills a real gap: **automated structural extraction from raw heterogeneous files**, which neither AgentDB (semantic recall) nor the GI-JOE portfolio ontology (hand-curated, 119 individuals) does. Complementary, not duplicative; its `graph.json`/Neo4j export could feed candidate individuals into the GI-JOE ABox. Best uses: portfolio navigation (registry/index duty), cross-paper concept map over `Papers/`.
- InfraNodus's gap-detection-to-question loop is genuinely new vs our stack and maps onto `morphism-research-frontier` / `research-portfolio-optimizer` needs, but should be **built native** (AgentDB embeddings + network metrics), not licensed.
- Aligned to the 2026-05-27 ontology-tooling recon frame (dual lens, R016 ranking, competitive map, R018 provenance).

## Decision
- Framing confirmed by principal. Pilot (assessment action item 1) **deferred to post-2026-07-12**; no justifiable reason to install/access before the Fable cutoff. Early-trigger exception logged: pull forward if a concrete navigation/mapping task starts burning noticeable token/context budget on raw-repo grepping before July 12.

## Files
- Deliverable: `00 Planning and Execution/Graphify_InfraNodus_Hive_Empire_Fit_Assessment_2026-07-09.md` (created; edited to add the deferral status note under Recommended Next Actions).
- Record: this archive; scorecard `2026-07-09-postwach-03.yaml`.

## Still open (post-2026-07-12)
- Graphify pilot: install (`uv tool install graphifyy`), index PostWach repo or the isomorphism-library paper folder (scratch OUTSIDE OneDrive), measure query utility + token cost vs raw-file reading; promote R016 (a)->(b) only after the run.
- Bridge study (Graphify export -> GI-JOE ABox, co-own with GI-JOE); native gap-detection method build; Fort Wachs pre-adoption security gate; `capability-index.md` entry if the pilot passes.

## Hygiene
No commits. No agents spawned; no swarm started (ruflo warmed to v3.14.4 for status only, then idle). No orphaned agents. No store writes, so no R018 store attribution beyond this archive's provenance line. Nothing installed or executed.
