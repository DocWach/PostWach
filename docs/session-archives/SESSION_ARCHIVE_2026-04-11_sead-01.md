# Session Archive: 2026-04-11 SEAD-01

**Hive:** SEAD
**Date:** 2026-04-11
**Ticket:** SEAD-PD-001 (continued), POSTWACH-PD-001 (filed)

## Work Completed

### Bug Fix: LLM Suggested Rewrite Not Appearing
**Root cause identified:** The LLM prompt listed all 42 rules as sub-items, causing Claude to evaluate each rule individually (~65 evaluations) instead of 9 aggregate criteria. Responses exceeded max_tokens (1500), truncating JSON before `suggested_full_text`. Additionally, criterion_ids like "A4.R7" didn't match the expected "A4" format in the parser.

**Fixes applied (branch `sead/llm-suggested-rewrite-fix`):**
1. Restructured `_build_prompt()` to request exactly 9 evaluations (A2-A10)
2. Added per-violation green "Suggested" box in results UI
3. Increased max_tokens from 1500 to 4096 across all providers
4. Added fallback synthesis of `suggested_full_text` from per-criterion replacements
5. Added debug expander showing raw LLM responses
6. Added "Mock (test fixture)" LLM provider with canned UAV responses
7. Updated README and CHEATSHEET with Mock provider docs

### Bug Fix: Export ValueError
`_rule_iri()` crashed on criterion-level IDs ("A2") passed from LLM Tier 3 violations. Fixed to link to characteristic instead of rule when ID is not a rule.

### PostWach Ticket Filed
POSTWACH-PD-001: LLM prompt quality issues causing hallucinated values, over-rewriting, and divergence from VT React app results. Includes comparison of VT prompt vs Streamlit prompt with specific fix recommendations.

### Debugging Methodology
- Added mock LLM provider to isolate display logic from LLM response quality
- Added debug expander to capture raw LLM responses
- Compared mock (working) vs real LLM (broken) to identify the divergence point
- Found VT React app prompt at `RE_Assistant_VT/backend/ai_analyzer.py` for reference

### VT React App: Spin-Up and Delivery Fixes
Brought up the VT React app (`RE_Assistant_VT/`) locally — FastAPI backend + React/Vite frontend.

**Issues found and fixed:**
1. Vite proxy pointed to port 8002, backend runs on 8000 — all API requests failed silently
2. `LLM_MODEL=llama3.1` from `.env` leaked into Anthropic provider path, causing invalid model errors
3. README had incorrect ports (8002/3001) throughout
4. `strictPort: true` prevented fallback when port 3001 was occupied

**Branch pushed to GitHub:** `sead/delivery-fixes` on `DocWach/Requirements-Assistant`
- Includes all PostWach multi-provider work + SEAD port/model fixes + README updates

### README Updated
PostWach added an "Active Frontends" section documenting both the React app and the Streamlit PD Workbench as parallel implementations.

## Commits

### pd_workbench repo (branch `sead/llm-suggested-rewrite-fix`)
1. `316d8c4` — Fix LLM suggested rewrite not appearing after analysis
2. `24b4fe9` — Fix ValueError in report export when LLM returns criterion-level IDs

### RE_Assistant_VT repo (branch `sead/delivery-fixes`, pushed to GitHub)
3. `4b3b30b` — PostWach + SEAD delivery fixes: multi-provider, port alignment, ontology enhancements

## Files Modified

### pd_workbench
- `pd_workbench.py` — prompt restructure, mock provider, debug expander, suggestion display, fallback synthesis
- `lib/ontology_service.py` — guard `_rule_iri()` for criterion-level IDs
- `README.md` — Mock provider docs
- `CHEATSHEET.md` — Mock provider docs

### RE_Assistant_VT (28 files, 1460 insertions)
- `frontend/vite.config.js` — proxy target 8002→8000, strictPort false
- `backend/ai_analyzer.py` — multi-provider support, model name leak fix
- `backend/main.py` — provider header routing, enhanced endpoints
- `backend/set_analyzer.py` — SPARQL-backed C10/C11 analysis
- `backend/ontology_service.py` — coverage and severity methods
- `README.md` — correct ports, multi-provider docs, Windows quick start
- Plus 22 other files (see commit diff)

## Files Created
- `pd_workbench/fixtures/uav_navigation_mock_llm_responses.json` — mock LLM fixture
- `tickets/PD_Workbench_PostWach_PromptQuality_2026-04-11.md` — PostWach ticket
- `RE_Assistant_VT/backend/ontology/queries/CQ-IR10.rq` — completeness SPARQL query
- `RE_Assistant_VT/backend/ontology/queries/CQ-IR11.rq` — consistency SPARQL query
- `RE_Assistant_VT/backend/tests/` — UAV Navigation acceptance tests

## Deferred / Next Session
- PostWach: prompt quality fixes (POSTWACH-PD-001)
- React app: investigate 300s timeout on Anthropic analysis (may need request-level provider override instead of env mutation)
- SEAD: Security verification scan of pd_workbench source (carried from 2026-04-10)
- SEAD: Docker build verification (carried from 2026-04-10)
- PostWach may need to restore sub-rule descriptions in prompt once quality is tuned
