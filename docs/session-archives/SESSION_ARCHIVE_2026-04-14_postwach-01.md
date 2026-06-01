# Session Archive: 2026-04-14 PostWach-01

**Hive:** PostWach (faculty advisor role)
**Project:** VT Supply Chain Analysis (Virginia Tech ISE Senior Design Team 4)
**Date:** 2026-04-14
**Duration:** ~3 hours
**Focus:** Finish the 2026-04-13 fix set; red/blue/white review; clean up all review findings via parallel agents; produce student test strategy; commit + push v2.1.0 to GitHub with updated README

---

## Session Summary

Resumed from 2026-04-13_postwach-03. Started with handoff checklist: verified 16/8 split on existing pytest (no overnight drift), decided two open design questions (fastest_first = pure greedy; window-overrun = warning note not a second flag), added the overrun warning, rewrote the 8 failing tests to lock in correct post-fix semantics, and wrote a 12-test stress-test harness covering the 6 invariants. Full suite went from 16/8 to 36/36 green.

Ran a smoke test replay of the 3 original VT scenarios through the fixed code — all 6 strategies feasible in all 3 scenarios, fastest_first non-empty, optimal_* differentiated, window-overrun notes present for scenarios 1 and 3 (4wk and 1wk disruptions).

User requested red/blue/white testing before commit. Built `_rbw_review.py` and ran it: **0 BLUE failures** (every claimed fix verified against VT scenarios), **0 HIGH findings** in red or white; 10 informational findings surfaced.

User asked what it would take to fix all 10. I categorized by effort/risk and flagged that 3 items need live LLM+Streamlit validation (hand to students). User approved fixing all 10 locally via spawned agents.

**Spawned 4 parallel agents with strict file ownership** (no merge conflicts): sim cleanup (6 items), LLM validator (R10), app wiring (W1+W9), stress fixture (W10). All 4 completed successfully; full suite now 65/65 green.

User then asked for (a) session archive and (b) a student-facing test strategy for the parts PostWach cannot test. Produced `VT Supply Chain/Student_Test_Strategy_2026-04-14.md` covering L0-L3 test layers with a 12-scenario battery, scoring rubric, and 7-item red-team checklist.

## Key Decisions

- **D85:** `fastest_first` semantics = pure greedy (sort by lead time, fill fastest first to capacity × usable_weeks). Round-robin was an artifact of the buggy per-week loop. If students push back, this is a one-function revert.
- **D86:** Delivery-past-disruption-window = warning note, NOT a second feasibility flag. Keeps `feasible` as a pure physical-capacity concept. Students' concern about proportional not flagging overruns is addressed via the note.
- **D87:** 95% demand-met tolerance replaced with 1 kg rounding tolerance (R11b). The 5% slack was masking boundary infeasibility; the explicit 1 kg handles floating-point rounding and nothing else.
- **D88:** `infeasibility_reasons: list[str]` added to `ScenarioResult` as a kw-only field with `default_factory=list`. Backward-compatible (all positional ScenarioResult() calls still work). Reasons encoded as `"shortfall"`, `"over_capacity:<name>"`, `"no_suppliers_available"`.
- **D89:** `MAX_PLANNING_HORIZON_WEEKS` = 52 and `PLANNING_BUFFER_WEEKS` = 2 as module constants; both overridable via `max_horizon_weeks` kwarg on `run_disruption_scenario` and `compare_strategies`.
- **D90:** Supplier keyword fallback map now derived from `SUPPLIERS` at module load via `build_supplier_keywords(SUPPLIERS)`. Adding a supplier to `suppliers.csv` with a new region automatically gets keyword coverage; existing hardcoded aliases (Russia → "moscow", Japan → "tokyo"/"earthquake", US → "american"/"ohio"/"domestic", China → "beijing"/"chinese", Australia → "australian") preserved via a `REGION_ALIASES` dict inside `supplier_loader.py`.
- **D91:** Supplier data load path extracted from `app.py` into `src/supplier_loader.py` so it is unit-testable without booting Streamlit. The Streamlit module is a one-liner wrapper now.
- **D92:** Red/blue/white script `_rbw_review.py` stays in the repo as a one-shot audit tool; pytest ignores it via `tests/conftest.py` (collect_ignore). It is not a maintained test suite.
- **D93:** Parallel-agent work organization by strict non-overlapping file ownership (not git worktrees). Simpler, zero merge conflicts, each agent owns a specific set of files and is forbidden from touching others. Worked cleanly — 4 agents, no conflicts.
- **D94:** Student test strategy adopts Option C (structured manual session + scorecard + one LLM smoke test), rejecting Option A (pure unit tests) as insufficient coverage for the pipeline and Option B (pinning LLM output text) as brittle under non-deterministic generation.
- **D95:** 12-scenario manual battery varies all five axes the original 3-scenario CSV did not (duration, severity, qty, qualified_only, disrupted-supplier count) with explicit pass-fail gates tied to the 6 bug fixes.

## Work Completed

### Simulation core (agent A)
- `run_disruption_scenario`: added `ValueError` guard for negative `order_quantity_kg`; added `max_horizon_weeks` kwarg.
- `compare_strategies`, `_allocate_order`: threaded `max_horizon_weeks`.
- `_delivery_planning_horizon`: `+2` replaced with named `PLANNING_BUFFER_WEEKS` constant.
- Feasibility tolerance tightened from 95% to 1 kg.
- `ScenarioResult` gained `infeasibility_reasons: list[str]` field; populated at every feasibility gate and in the no-suppliers-available early return.
- `format_result_summary`: renders a `Reasons:` line when reasons are non-empty.
- `tests/test_model_fixes.py`: appended `TestSeverityMapping` class (6 tests on clamping, monotonicity, total shutdown).

### LLM validator (agent B)
- `llm_analyst._normalize()` helper: lowercase, replace `_`/`-` with space, collapse whitespace.
- `validate_recommendation()`: rewritten to use `_normalize` + word-boundary regex so "cheapest first", "Cheapest First", "cheapest-first", and "cheapest_first" all match the canonical form. False positives on partial overlaps ("optimal" matching "optimal_time" when only "optimal balanced" was mentioned) eliminated via `\b` anchors.
- New `tests/test_llm_validator.py`: 7 fuzzy-match cases plus 1 word-boundary case.

### App wiring (agent C)
- New `src/supplier_loader.py` with `load_supplier_data(csv_path, defaults) -> (list, str)` and `build_supplier_keywords(suppliers) -> dict`. `REGION_ALIASES` dict inside the module preserves the old hardcoded aliases (moscow, tokyo, earthquake, american, ohio, domestic, beijing, chinese, australian).
- `app.py`: hardcoded `supplier_keywords` dict deleted; `SUPPLIER_KEYWORDS = build_supplier_keywords(SUPPLIERS)` computed once at module scope; pipeline's classification fallback iterates `SUPPLIER_KEYWORDS.items()`.
- New `tests/test_app_wiring.py`: 6 tests covering CSV load paths (present, missing, malformed) and keyword builder (default aliases preserved, new-region handled, lowercase invariant).
- New `tests/conftest.py`: adds `src/` to sys.path, sets `collect_ignore = ["_rbw_review.py"]`.

### CSV-replay regression (agent D)
- `tests/test_stress.py`: appended `TestVTScenariosReplay` class guarded by `skipif(not os.path.exists(VT_SCENARIOS_CSV))`. Loads `VT Test Runs/2026-04-13_scenarios.csv`, reconstructs the 3 scenarios, replays through `compare_strategies`, asserts B1 (non-empty fastest_first), B2 (no feasibility inversion), B4 (optimal_* differentiate), and window-overrun note presence for the two short-window rows. LLM recommendation bug (B3) explicitly deferred via docstring pointing to `test_llm_validator.py`.

### Audit + review artifacts
- `tests/_rbw_review.py`: one-shot red/blue/white audit script — 14 red probes, 6 blue verifications, 10 white methodology checks. Ignored by pytest.
- `VT Supply Chain/Student_Test_Strategy_2026-04-14.md`: 4-layer test strategy (L0 automated → L3 exploratory), 12-scenario battery with scoring rubric, 7-item red-team checklist, pass/fail gates tied to the 6 bug fixes, tracking recommendations.

### Test state
- **Before today:** 16/8 (8 failing tests were pinning the old buggy behavior).
- **Mid-session:** 24/0 after rewrite + 12/0 stress harness = 36/0.
- **After agent cleanup:** **65/0 across 5 test files** (test_model_fixes 30, test_stress 21, test_llm_validator 8, test_app_wiring 6; plus conftest ignore for the audit script).

## Files Created or Modified (uncommitted)

**Modified:**
- `VT Supply Chain/src-repo/src/supply_chain_sim.py`
- `VT Supply Chain/src-repo/src/supply_chain_optimizer.py`
- `VT Supply Chain/src-repo/src/llm_analyst.py`
- `VT Supply Chain/src-repo/src/app.py`
- `VT Supply Chain/src-repo/tests/test_model_fixes.py`

**New:**
- `VT Supply Chain/src-repo/src/supplier_loader.py`
- `VT Supply Chain/src-repo/tests/test_stress.py`
- `VT Supply Chain/src-repo/tests/test_llm_validator.py`
- `VT Supply Chain/src-repo/tests/test_app_wiring.py`
- `VT Supply Chain/src-repo/tests/conftest.py`
- `VT Supply Chain/src-repo/tests/_rbw_review.py`
- `VT Supply Chain/Student_Test_Strategy_2026-04-14.md`

## Task List State (at handoff)

All 7 session tasks completed. Also during this session:

- README.md updated with v2.1.0 release notes section documenting all 12 fixes (6 team-reported + 6 internal cleanup), updated project structure, and new test-file inventory.
- Committed 12 files (1711 insertions, 102 deletions) as single commit `d9a6c13` on `main` with message "v2.1.0: Fix 6 team-flagged bugs + 6 internal cleanup items; expand tests 24 -> 65". Co-authored-by claude-flow.
- Pushed `main` to `origin` (`306a873 -> d9a6c13`) at `DocWach/Supplychain-Analysis-VT-ISE-Senior-Design`.

**Repository visibility note:** User indicated at end of session that the VT repo is no longer public. Confirm access model (org-internal vs. private) before advising any external reviewer or including repo URLs in shareable materials. The Student Test Strategy doc lives outside the repo in the PostWach workspace, so that distribution path is unaffected.

## Follow-ups for Next Session

1. Reply to VT team (Boleslav / Jonathan / Camilo / Juan) summarizing the 6 fixes + 10 cleanup items and attaching the Student Test Strategy. Point them at commit `d9a6c13` and the README v2.1.0 section.
2. (Optional) Open GitHub issue for the fastest_first semantics decision (greedy vs round-robin) if the team wants to debate.
3. (Optional) Add `suppliers.csv` schema for an optional `keywords` column in a future iteration — current approach uses region-derived keywords only.
4. Clarify repo visibility change: when did it go private, who has access, and does this affect any planned sponsor demo pathway?

## Open Questions for Next Session

1. **Repo access model** — Now that the repo is no longer public, who has access? Does The Aerospace Corp (sponsor) need to be added? Does the Student Test Strategy distribution plan change?
2. **What does the Streamlit session look like for the team?** Should I prepare a one-hour walkthrough or just send the test strategy doc?

## Handoff Checklist

- [x] Commit v2.1.0 (single commit: `d9a6c13`)
- [x] Push to origin/main
- [x] Update README with release notes
- [ ] Send student test strategy + fix summary to the team
- [ ] Schedule a test session with them if they want to walk the battery together
- [ ] Resolve fastest_first semantics if team pushes back
- [ ] Confirm repo-access model (private now; sponsor access?)
