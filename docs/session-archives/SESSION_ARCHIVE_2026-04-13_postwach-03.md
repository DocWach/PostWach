# Session Archive: 2026-04-13 PostWach-03

**Hive:** PostWach (faculty advisor role)
**Project:** VT Supply Chain Analysis (Virginia Tech ISE Senior Design Team 4)
**Date:** 2026-04-13
**Duration:** ~90 minutes
**Focus:** Review VT-delivered test artifacts; fix 6 flagged model/LLM bugs; stress test (IN PROGRESS — to resume tomorrow)

---

## Session Summary

Started a new session on the VT Supply Chain project. Moved two student deliverables from `Downloads/` to `VT Supply Chain/VT Test Runs/`: the April 7 meeting agenda (`2026-04-07_Meeting_Agenda.docx`) and the Streamlit scenarios export (`2026-04-13_scenarios.csv`, 3 LLM-driven runs from Apr 6-7 using Ollama/llama3.1).

Reviewed both artifacts and identified bugs. The meeting notes corroborated most of what the CSV review surfaced: `fastest_first` returns empty when infeasible, `proportional` always flags feasible even when delivery overruns the disruption window, and the "full pipeline doesn't evaluate full disruptions" symptom (my B2 — short disruption windows cap capacity incorrectly). Students additionally reported that editing `suppliers.csv` has no effect on the model — confirmed: `app.py` imports `load_suppliers` but never calls it and uses `DEFAULT_SUPPLIERS` throughout.

Began implementing all 6 fixes in place. Five are complete; one (optimal_* collapse) is complete as a byproduct but needs verification. Stress test harness not yet written. Existing pytest has 8 failures that are pinning the old buggy behavior and need rewriting.

## Work Completed (code changes, UNCOMMITTED)

Files modified in `VT Supply Chain/src-repo/src/`:
- `app.py`
- `supply_chain_sim.py`
- `supply_chain_optimizer.py`
- `llm_analyst.py`

### Fix #1 — `suppliers.csv` wiring (DONE)
`app.py` now calls `load_suppliers("suppliers.csv")` at module import with `DEFAULT_SUPPLIERS` fallback. Module-level `SUPPLIERS` and `SUPPLIER_SOURCE` replace every downstream `DEFAULT_SUPPLIERS` reference in tabs, the pipeline, manual scenario, and supplier database views. Supplier database tab now shows whether data came from the CSV or from built-in defaults.

### Fix #2 — `fastest_first` empty allocation / B1 (DONE)
Rewrote the `fastest_first` branch in `supply_chain_sim._allocate_order`. The old per-week loop with condition `week > (planning_horizon - s.lead_time_weeks)` excluded every supplier whose lead time equaled or exceeded the planning horizon, producing empty allocations whenever `disruption_weeks` was small. New implementation is a pure greedy fill (sorted by lead time ascending, take up to `capacity × usable_weeks` per supplier). Never returns empty if any supplier has positive capacity.

### Fix #3 — Planning horizon conflation / B2 (DONE)
Extracted a helper `_delivery_planning_horizon` in `supply_chain_sim.py`. Horizon = min(52, max_lead + ceil(order / total_cap) + 2). Decouples from `disruption_weeks`, which is now only an event-duration parameter (degradation multipliers are already baked into each supplier's degraded attributes). Applied the same change in both `supply_chain_optimizer.optimize_allocation` and `optimal_allocate`. Added `MAX_PLANNING_HORIZON_WEEKS = 52` as a business ceiling so genuinely oversize orders remain infeasible.

### Fix #4 — `proportional` feasibility flag / B5 (DONE)
Added a second feasibility gate in `run_disruption_scenario`. Feasibility now requires (a) total allocation >= 0.95 * demand AND (b) every supplier's allocated kg fits within its horizon-capacity envelope (`capacity_kg_per_week × usable_weeks`). The proportional strategy previously passed gate (a) by construction but could silently oversubscribe individual suppliers; gate (b) catches that. Per-supplier overages are emitted as warning notes.

### Fix #5 — LLM recommends infeasible / B3 (DONE)
`llm_analyst.py`:
- Tightened `SYSTEM_PROMPT_ANALYST` with a "HARD RULE — FEASIBILITY FIRST" block prohibiting recommending any strategy marked "Feasible: NO" when feasible alternatives exist.
- Added `_feasibility_preamble()` that computes a loud "FEASIBLE: ..." / "INFEASIBLE: ..." block and prepends it to the user message in `analyze_with_comparison`.
- Added `validate_recommendation()` as a post-check that appends a "SYSTEM OVERRIDE" warning if the LLM response text names only an infeasible strategy.

`app.py` pipeline step 3 now calls `analyze_with_comparison(sim_results, question=...)` instead of plain `analyze(sim_context, question=...)`, routing every production recommendation through the preamble + validator.

### Fix #6 — optimal_* strategy collapse / B4 (DONE as byproduct of Fix #3)
Root cause was `demand = min(order, total_capacity)` with `sum(upper_bounds) == total_capacity`, collapsing the LP feasible region to a single point so every objective returned the same allocation. With Fix #3 removing the artificial capacity cap, total_capacity now far exceeds demand for typical cases, so the three objectives differentiate naturally. Needs explicit verification in tomorrow's stress test before closing the task.

## Work In Progress — RESUME HERE TOMORROW

### Regression tests (8 existing failures — diagnosed, not yet rewritten)
`pytest tests/test_model_fixes.py -v` after the fixes → **16 passed, 8 failed**. Inspection shows the 8 failing tests were pinning the OLD (buggy) behavior:
- `TestTimeBoundedCapacity::test_normal_gap`, `::test_large_lead_time`, `::test_lt_equals_horizon`, `::test_lt_exceeds_horizon` — all assumed `planning_horizon = disruption_weeks`. With Fix #3 this no longer holds. Tests need rewriting to assert correct new semantics (planning horizon independent of disruption duration).
- `TestScenarioRegression::test_baseline_fastest_first`, `::test_ru_disrupted_fastest_first` — assumed a per-week round-robin fastest_first distributing across 3+ suppliers. New greedy fastest_first packs suppliers in lead-time order (Titan-US: 5000 alone in baseline). Decision needed (see Open Questions).
- `TestScenarioRegression::test_us_disrupted_cheapest_non_qualified` — expected RU + CN both used; with generous horizon RU alone satisfies the order. Rewrite the assertion or reduce order_qty.
- `TestEdgeCases::test_order_exceeds_capacity` — 50,000 kg with RU disrupted is now feasible (28-week delivery). Rewrite to use a genuinely infeasible size (e.g., 10,000,000 kg) OR to assert the "delivery > disruption window" warning.

### Delivery-vs-disruption-window warning (NOT yet added)
Students' exact complaint on proportional was "evaluates as feasible even if it goes over disruption length". My Fix #4 addresses the tautology but not the window-overrun signal. Next session: add a note on every ScenarioResult when `total_delivery_weeks > disruption_weeks` (when disruption_weeks > 0), without changing `feasible`. Keeps physical-capacity feasibility separate from window-compliance.

### Stress test harness (Task #7 — NOT STARTED)
Parameter sweep to write: severity 1-10, disruption_weeks {1,2,4,8,16,24,52}, qty {1k, 5k, 20k, 50k, 500k, 10M}, qualified_only {T,F}, disrupted_supplier sets (none / JP+US / RU / all-qualified). Invariants to assert:
1. `fastest_first` never returns empty when any supplier has capacity.
2. For fixed demand, feasibility should NOT invert with disruption duration (original B2 symptom).
3. `optimal_cost` <= `optimal_balanced` <= `optimal_time` on cost axis for feasible runs (locks B4 fix).
4. Mock LLM: `validate_recommendation` never passes an infeasible pick when feasible alternatives exist.
5. Changing `suppliers.csv` (adding/removing a supplier, changing capacity) changes the simulation output (locks #1 fix).

## Key Files Touched (uncommitted — check `git status` to resume)

In `VT Supply Chain/src-repo/`:
- `src/supply_chain_sim.py` — `_allocate_order` rewrite, `_delivery_planning_horizon` helper, feasibility gate-2, `MAX_PLANNING_HORIZON_WEEKS = 52`
- `src/supply_chain_optimizer.py` — removed `disruption_weeks` horizon coupling in both `optimize_allocation` and `optimal_allocate`
- `src/llm_analyst.py` — new `_feasibility_preamble`, `validate_recommendation`, hardened `SYSTEM_PROMPT_ANALYST`, `analyze_with_comparison` rewired
- `src/app.py` — `SUPPLIERS` / `SUPPLIER_SOURCE` module load, 4 call sites rewired, supplier-tab source label, LLM pipeline routed through `analyze_with_comparison`

New files (outside repo):
- `VT Supply Chain/VT Test Runs/2026-04-07_Meeting_Agenda.docx` (moved from Downloads)
- `VT Supply Chain/VT Test Runs/2026-04-13_scenarios.csv` (moved from Downloads, renamed with date prefix)

## Task List State (at handoff)

1. Diagnose suppliers.csv wiring — **completed**
2. Fix fastest_first empty allocation (B1) — **completed**
3. Fix planning horizon conflation (B2) — **completed**
4. Fix proportional feasibility flag (B5) — **completed**
5. Fix LLM recommends infeasible (B3) — **completed**
6. Fix optimal_* collapse (B4) — byproduct of #3; marked pending pending stress-test confirmation
7. Stress test all fixes — **in_progress** (blocks release)

## Open Questions for Next Session

1. **fastest_first semantics — pure greedy vs. round-robin?** My current fix is pure greedy (Titan-US gets the full 5000 in baseline). Students' existing test expected round-robin distribution across 3+ suppliers. Ask the team which they prefer before finalizing, OR pick greedy and document why.
2. **Disruption window as soft constraint.** Should delivery-exceeds-disruption be a warning note only, or should it be a second feasibility flag (`within_window: bool`)? Current fix leaves it as physical-capacity-only; students may want the window signal as a first-class output.
3. **Supplier keyword map in app.py** is hard-coded to the default 5 Titan-* names. If students add a new supplier via CSV (e.g., Titan-IN), the LLM classifier's keyword fallback won't find it. Out of today's scope but worth a follow-up ticket after stress test is green.

## Handoff Checklist for Tomorrow

- [ ] Re-run `pytest tests/test_model_fixes.py -v` to confirm same 16/8 split (no regression from overnight).
- [ ] Decide fastest_first semantics (greedy vs round-robin) with the student team OR pick one and document.
- [ ] Rewrite the 8 failing tests to lock in new correct behavior.
- [ ] Add disruption-window overrun warning to `run_disruption_scenario`.
- [ ] Write stress test harness (Task #7) with the 5 invariants above.
- [ ] Run end-to-end Streamlit smoke test against the 3 scenarios from `2026-04-13_scenarios.csv` and verify: (a) `fastest_first` produces non-empty allocations in all 3, (b) `proportional` now flags infeasible when over-subscribing, (c) LLM no longer recommends cheapest_first when infeasible.
- [ ] If all green: commit with message describing all six fixes and link to this archive.
- [ ] Draft reply to Boleslav / Jonathan / Camilo / Juan summarizing fixes and inviting them to test.
