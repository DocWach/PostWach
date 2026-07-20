# Session Archive — PostWach 2026-07-20-postwach-02

> PROVENANCE: authored by Claude (Anthropic, Opus 4.8, claude-opus-4-8[1m]) via Claude Code CLI, at Paul Wach's direction. 2026-07-20.

## Objective
Support a live discussion with an external collaborator (Taylan, who knows the product best, could
not join). Provide (1) an overview of the "WRT-2516 requirements co-pilot," (2) its architecture, and
(3) a speakable articulation aid (what it is / what it isn't / components / how it works / product
trajectory), plus a shareable architecture figure.

## What was established (grounding, from the actual source, not the PostWach-side derivative)
- **Naming reconciliation:** no artifact is literally labeled "requirements co-pilot." Under **WRT-2516**
  (SERC-AIRC, NNSA sponsor) there are two lines: the **technical report** (3D->4D SE assessment/
  transformation framework, TRAK Bayesian evidence aggregation) and **RE_Assistant_VT**, the
  requirements-engineering tool. The co-pilot = **RE_Assistant_VT**.
- Read the real backend at `03 Projects/01 NNSA/01 Deliverables/RE_Assistant_VT/` (FastAPI + React,
  Render single-service deploy), not the governance-revector extract. Ties to
  [[feedback_probe_artifact_not_narrative]]: running code defines the system; the derivative describes it.

## Architecture (as read from source)
Full-stack, ontology-grounded, human-in-the-loop pipeline:
1. **Ingest/parse** (`requirements_parser.py`) via `/api/upload`.
2. **AI analyzer** (`ai_analyzer.py`): per-requirement A-criteria (A2-A10) classification, ontology-first
   (SPARQL) with `incose_rules.json` fallback. Anti-hallucination by design: the AI only classifies
   (satisfied, explanation, exact `affected_text` substring, scoped `suggested_replacement`); it does
   NOT rewrite requirements. Parallel (ThreadPoolExecutor). Provider-agnostic (Anthropic default
   `claude-sonnet-4-20250514`; OpenAI-compatible/Ollama local). BYO key via `X-API-Key`.
3. **Ontology + validation** (`ontology_loader.py`, `ontology_service.py`, `ontology/*.ttl`): 42 rules,
   15 quality characteristics, 14 categories, BFO-aligned; mints assessments as RDF; computes coverage +
   quality profile; validates against SHACL shapes (non-blocking `shacl_conforms`). 9 competency-question
   queries (CQ-IR01..09).
4. **Set-level analysis** (`set_analyzer.py`, `set_analysis_prompt.py`): B-criteria (consistency,
   completeness, glossary, conflicts); programmatic SPARQL report + optional Claude semantic pass.
5. **Multi-reviewer consensus** (`reviewer_manager.py`, `consensus_engine.py`): roles lead/senior/junior
   = weights 3/2/1; weighted vote per violation; unanimous->1.0, majority>0.6->resolved, else conflict;
   lead-only override; builds `final_text`.
6. **Output** (`document_generator.py`): corrected DOCX + JSON.
7. **RAG/calibration** (`knowledge_store.py`): ingests reviewer decisions; per-rule acceptance rates.
   Plus an offline eval harness (`run_analysis.py`, `tests/`): confusion matrix / precision / recall /
   F1 / FNR / FPR vs human ground truth over 10 runs.

## Integration status flags (R016)
- **As-built = (c) integrated deliverable**: ontology -> analyzer -> SHACL -> consensus -> DOCX wired into
  one deployable product. Caveat: verified by static read, not by running it (user said no test needed).
- **RAG "learning" is half-wired**: ingestion runs on every submit, but `analyze_all_requirements` hard-sets
  `rag_enhanced=False`; retrieval-back-into-prompt is not active in the main path. The *learning* sub-feature
  is **(b) demonstrated/uncoupled**, not (c). Classic [[feedback_uncoupled_vs_untested]]. Do not claim "it
  learns" externally.
- **Stale model id**: pins `claude-sonnet-4-20250514`; current guidance Sonnet 4.6 (`claude-sonnet-4-6`).

## Deliverables produced
- Articulation aid (in-conversation): what it is / isn't / components / how it works / trajectory, framed
  for an external audience ([[feedback_internal_external]] team-progress framing;
  [[feedback_artifact_ip_protection]] "contact the authors" if availability is asked).
- **Architecture figure** rendered to PNG (Mermaid + mmdc), color-coded ANALYZE/DECIDE/IO/calibration
  layers, dashed "roadmap" feedback loop distinguishing today's flow (solid) from the learning loop (dashed):
  - `docs/figures/RE_Assistant_CoPilot_Architecture.mmd`
  - `docs/figures/mermaid-config.json`
  - `docs/figures/RE_Assistant_INCOSE_Requirements_CoPilot_Architecture_v1.png`
  Verified by rendering and looking ([[feedback_formatting_verify_visually]]); bold labels, no lines over
  text ([[feedback_diagram_formatting]]); descriptive PNG name ([[feedback_pdf_naming]]).

## Next steps (offered, not done)
- Trace the RAG retrieval gap to confirm dead-code vs disabled.
- Side-legend variant (INCOSE criteria spelled out) or a 16:9 slide crop.
- One-line model-id bump to Sonnet 4.6.

## Housekeeping
- Files created: 3 figure files (mmd/config/png) + this archive + the scorecard.
- No code modified; no commits made.
- ruflo warmed (bridge connected, 767 AgentDB entries); memory recall used, no memory writes.
- No background agents/swarms/workflows spawned; agent_list active = 0, none to terminate.
