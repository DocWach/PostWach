# Session Archive: 2026-03-17 PostWach-03

**Date:** 2026-03-17
**Hive:** PostWach
**Session:** postwach-03
**Focus:** VT Supply Chain -- Student Feedback Triage + Bug Fixes

---

## Context

Boleslav Econa (VT ISE Senior Design Team 4) emailed 2026-03-14 reporting three issues with the Titanium Supply Chain Disruption Analyzer. This session triaged the feedback, diagnosed root causes, debated fix approaches, and implemented all four fixes.

## Student Issues (from email)

1. **Optimal (Min Time) not producing shortest delivery time.** Screenshot showed Min Time at 10 wk while Fastest First achieved 8 wk. Root cause: the LP objective `minimize sum(lead_time * x)` drives all allocation to a single fast supplier, but actual delivery time is `max(lead_time_i + ceil(x_i/cap_i) - 1)` across suppliers. Concentrating on one supplier overloads it.

2. **"Send results to AI for analysis" button broken in Manual Scenario tab.** Button and results were inside `if run_manual:` block; clicking the button triggered a Streamlit rerun where `run_manual=False`, losing both button and data.

3. **Example selector overwrites `user_input` without updating text box.** Python variable overwritten but text_area widget not refreshed. Confusing UX.

4. **LLM outputs raw identifiers ("min_cost") instead of display names ("Optimal (Min Cost)").** Student asked "how do we train the model?" -- revealing a conceptual gap about prompt engineering vs. model training.

## Approach Debate

### Min Time LP (Issue 1)
- **Option A (chosen): Minimax LP reformulation.** Introduce auxiliary variable T, constrain T >= delivery_time_i for each supplier, minimize T. Standard LP technique, directly teachable to ISE students.
- **Option B: Iterative LP.** Run LP, check delivery, add constraints, repeat. Ugly but functional.
- **Option C: Rename and document.** Honest but doesn't fix the bug.

### UI Bugs (Issues 2-3)
- Both are classic Streamlit state management problems. Fixed with `st.session_state` persistence.
- Boleslav attached a modified app.py with an `on_click` approach (attachment stripped by Outlook). Our fix uses session_state which is cleaner and handles both bugs consistently.

### Display Names (Issue 4)
- Dual fix: (a) `format_result_summary()` emits display names in the text sent to the LLM, (b) system prompt includes explicit name mapping. Belt and suspenders.

## Deliverables

### Files Modified (canonical location: `05 Service/04 Senior Design/AY 25-26 VT Supply Chain/src/`)

| File | Changes |
|------|---------|
| `supply_chain_optimizer.py` | Added `_solve_ortools_minimax()` and `_solve_scipy_minimax()` (~120 lines). Updated `optimize_allocation()` and `optimal_allocate()` to route min_time to minimax solvers. |
| `supply_chain_sim.py` | Added `_STRATEGY_DISPLAY` dict. Updated `format_result_summary()` to emit display names. |
| `llm_analyst.py` | Added strategy name guidance (6 mappings) to `SYSTEM_PROMPT_ANALYST`. |
| `app.py` | Fixed example selector with `st.session_state` + `st.rerun()`. Fixed Manual Scenario tab: results persist in session_state, AI response persists across reruns. Fixed About tab Llama version 3.1 -> 3.3 70B. |

### Verification

- **24/24 existing tests pass** (no regressions)
- **Minimax LP verified:** US-disrupted scenario: Min Time delivery dropped from 10 wk to 8 wk (matches Fastest First heuristic). Allocation correctly spreads across JP (2652 kg), AU (1926 kg), RU (421 kg).
- **All 4 source files compile clean**

### Minimax LP Formulation (for reference)

```
minimize  T
subject to:
  T >= lead_time_i - 1 + x_i / capacity_i    for each supplier i
  sum(x_i) = demand
  0 <= x_i <= capacity_i * usable_weeks_i
  T >= 0
```

Continuous approximation of `delivery = lead_time + max(0, ceil(x/cap) - 1)`. The ceiling function makes the exact problem nonlinear, but the LP continuous relaxation produces near-optimal allocations. Post-solve delivery times are computed with ceiling for accuracy.

## LLM Modularity Assessment (Requested Investigation)

### Architecture
- Multi-provider registry (`PROVIDERS` dict) with OpenAI-compatible shim
- 4 providers configured: Groq, Cerebras, Ollama, OpenAI
- Auto-detection scans env vars + Ollama health check
- Single chokepoint `_call_llm()` for all LLM calls

### Gaps Found
1. **Anthropic SDK in requirements.txt but not integrated** -- dead dependency (Anthropic uses different API format)
2. **No provider interface/protocol** for non-OpenAI-compatible APIs
3. **Hardcoded temperature (0.3) and max_tokens (1024)** -- no per-call override
4. **JSON parsing duplicated** between `full_pipeline()` and `app.py`

### Assessment
Modularity is sufficient for the senior design scope (all target providers are OpenAI-compatible). The Anthropic gap is the only concrete issue.

## Not Done / Next Steps

- [ ] Push changes to GitHub (`DocWach/Supplychain-Analysis-VT-ISE-Senior-Design`)
- [ ] Reply to Boleslav's email explaining fixes and reframing "model training" as prompt engineering
- [ ] Have students experiment with system prompt refinements (bounded learning task)
- [ ] Wire `suppliers_research.csv` into app (dropdown to switch datasets)
- [ ] Remove or integrate the dead `anthropic` dependency
