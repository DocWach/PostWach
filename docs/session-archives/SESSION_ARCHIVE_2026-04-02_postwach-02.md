# Session Archive: 2026-04-02 PostWach-02

**Date:** 2026-04-02
**Hive:** PostWach
**Focus:** PD Workbench planning, demo build, publication plan, M4 roadmap

---

## Session Summary

Strategic planning session for the PD Workbench followed by execution. Debated what should go in the workbench (capability tool vs diagnostic tool), established clear separation from assessment framework, scoped the PD workflow coverage (steps 3-9 of 9), identified differentiators from existing tools (ontology-grounded LLM analysis). Spawned 3 background agents: publication plan, Streamlit demo, M4/M4+ roadmap. Built and iteratively fixed the demo app with multiple rounds of CSS/color fixes.

## Key Decisions

1. PD Workbench is a capability tool, not a diagnostic tool. Assessment framework handles diagnostics. The 8 outcomes are shared anchor.
2. Differentiator: combination of LLM flexibility with ontological rigor. No existing tool combines BFO-aligned OWL with LLM-based analysis.
3. April 15: standalone Streamlit demo wrapping Phase 1-3 backend. Does not conflict with VT work.
4. Publication: two-paper strategy (ontology + tool). No existing tool has formal ontology + LLM + SHACL output.

## Deliverables

| # | Deliverable | Location | Status |
|---|-------------|----------|--------|
| 1 | Publication Plan | 01 NNSA/01 Deliverables/PD_Workbench_Publication_Plan_2026-04-02.md | Complete |
| 2 | Streamlit Demo (4 tabs) | 01 NNSA/01 Deliverables/pd_workbench_demo/ | Complete (:8504) |
| 3 | M4/M4+ Roadmap | 01 NNSA/01 Deliverables/PD_Workbench_M4_Roadmap_2026-04-02.md | Complete |

## Demo Layout (after restructuring)

- Tab 1 (Ontology Explorer): live SPARQL, 42 rules, 15 chars, cross-ref matrix, HTML dropdowns
- Tab 2 (Individual Analysis): quality profile grid at TOP, UAV test case, violation details
- Tab 3 (Set-Level Analysis): C10-C15 scores at TOP, glossary, terminology issues, conflicts
- Tab 4 (SHACL Validation): merged SHACL + stats at TOP, 9 CQ results in HTML tables

## CSS Fix Lesson Learned

Streamlit dark mode injects inline styles that override CSS class selectors. Only reliable fixes: (1) pure HTML with inline styles, (2) .streamlit/config.toml theme override. All st.expander replaced with HTML details elements. All st.dataframe/st.table/st.bar_chart replaced with HTML equivalents (pyarrow unavailable on ARM64).

## Agents: pub-planner, demo-builder, m4-packager (all complete)
