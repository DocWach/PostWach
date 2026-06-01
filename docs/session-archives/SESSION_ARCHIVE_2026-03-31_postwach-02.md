# Session Archive: 2026-03-31 PostWach-02

**Date:** 2026-03-31
**Hive:** PostWach
**Focus:** VT ISE Senior Design -- bug fixes + v2.0.0 feature release (student meeting)

---

## Session Summary

Met with VT ISE Senior Design students (Team 4). Fixed two bugs reported during the meeting, then implemented five prioritized feature requests from the student feedback session. Shipped as v2.0.0.

## Phase 1: Bug Fixes (during meeting)

### Bug 1: LLM recommendation bias
The system prompt (`SYSTEM_PROMPT_ANALYST` in `llm_analyst.py`) was cost-biased. Small local models (Llama 3.1 8B via Ollama) default to cheapest. Fixed by updating prompt to require cost AND time comparison and to respect user-stated priorities.

### Bug 2: Min-time solver math error (two sub-bugs)
- **MILP (ortools):** Delivery time modeled as `max(lead, production)` instead of additive `lead + production - 1`. Fixed constraint linearization.
- **LP (scipy):** No real min-time formulation existed. Added `_solve_scipy_min_time()` with auxiliary variable T.
- **Result:** Min Time (RU disrupted, 5000kg) went from 1 supplier/9.2 wk to 3 suppliers/6.1 wk.

**Commit:** `bf1b34a`

## Phase 2: v2.0.0 Feature Release (post-meeting)

Five prioritized items from student feedback, implemented with 3 parallel agents + main thread integration.

### Item 1: Persistent scenario history
- CSV-backed `scenario_store.py` (replaced SQLite after thread-safety error in Streamlit)
- New "Scenario History" tab: browse, review, delete past runs
- Past run context available to LLM for learning

### Item 2: Dual disruption classification (cause + effect)
- 6 causes: Geopolitical, Raw Material Shortage, Natural Disaster, Pandemic, IT Disruption, Other
- 4 effects: Supplier Failure, Logistics Delay, Demand Spike, Quality Issue (unchanged)
- LLM classifier now detects ALL affected suppliers from text (multi-supplier)

### Item 3: Severity scale 1-10
- Replaces word-based severity (low/medium/high/critical)
- Display as X/10 in UI

### Item 4: Graduated disruptions (A+B hybrid)
- Severity-to-multiplier preset table: severity 1-10 maps to capacity % (95%-0%) and lead time multiplier (1.05x-3.0x)
- Full Pipeline: severity auto-maps via lookup table
- Manual Tab: per-supplier radio (Full offline / Graduated) with capacity % and lead time multiplier sliders
- Backward compatible: legacy disruptions without multipliers default to fully offline

### Item 5: Multiple supplier disruptions
- `disruptions: dict[str, dict]` parameter added to sim, optimizer, and compare_strategies
- Manual Tab: per-supplier expandable panels with independent duration/mode/params
- LLM Pipeline: classifier identifies all affected suppliers; keyword fallback catches all matches
- Each supplier can have different severity in the same scenario

**Commit:** `306a873`

## Agent Coordination

| Agent | Task | Duration | Files |
|---|---|---|---|
| classifier-agent | Cause/effect types + severity 1-10 | 34s | `llm_analyst.py` |
| persistence-agent | CSV scenario storage module | 58s | new `scenario_store.py` |
| multi-supplier-agent | Multi-supplier disruption support | 209s | `supply_chain_sim.py`, `supply_chain_optimizer.py` |
| Main thread | App.py integration, graduated disruptions, CSS fixes, README | -- | `app.py`, `README.md`, `.gitignore` |

## Files Modified

| File | Change |
|---|---|
| `src/app.py` | Complete rewrite: 5 tabs, multi-supplier UI, graduated controls, severity display, history tab, CSS fixes |
| `src/llm_analyst.py` | Dual classifier prompt, severity 1-10, multi-supplier detection, updated analysis prompts |
| `src/supply_chain_sim.py` | Graduated disruption support, severity preset table, multi-supplier filtering |
| `src/supply_chain_optimizer.py` | Min-time LP fix, graduated disruption support, multi-supplier filtering |
| `src/scenario_store.py` | New file: CSV-backed persistent storage |
| `README.md` | Updated: v2.0.0 notes, new Mermaid architecture diagram, severity table, 5-tab description |
| `.gitignore` | Added scenarios.csv and scenarios.db |

## Verification

- 24/24 existing tests pass throughout all changes
- Multi-supplier disruption tested (RU + CN simultaneously)
- Graduated disruption tested (severity 5: 50% cap, 1.5x lead time)
- CSV store: save/retrieve/delete round-trip verified
- Streamlit app launched and functional after each change set

## Git

| Commit | Description |
|---|---|
| `bf1b34a` | Fix min-time optimizer and LLM recommendation bias |
| `306a873` | v2.0.0: Multi-supplier disruptions, graduated severity, persistent history |

Both pushed to `DocWach/Supplychain-Analysis-VT-ISE-Senior-Design` (main).

## Deferred Items

- Containerization (Docker + Ollama sidecar) -- raised by students, not yet scoped
- Evaluation harness update for new classifier fields (cause/effect/severity)
- Green text CSS bug -- partially addressed but root cause in `st.metric` dollar rendering not fully isolated

---

## Session Status: COMPLETE
