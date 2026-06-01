# Session Archive — 2026-05-28 postwach-03

> PROVENANCE: claude-opus-4-7[1m] (Anthropic, Claude Code CLI). All session artifacts (HTML demo, archive, scorecard, memory updates) produced by this model in this access mode.

**Hive:** PostWach
**Scope:** NNSA project review and creation of a new "TRAK Framework Overview" demo aimed at NNSA decision-makers. Inventoried existing TRAK assets, built a new framework explainer from the WRT-2516_v2 `framework_demo_v2.html` source, iteratively reshaped it across 5 review rounds until aligned with the TRAK practitioner model (3D × 3Q) and stripped of all WRT-2516 4D vestiges.
**Platform:** Ruflo v3.7.0-alpha.14 (warmed at session start); claude-opus-4-7 (1M context); Windows 11. No subagents — entire session was orchestrator-only with iterative discuss-before-execute checkpoints.
**Outcome:** Self-contained framework demo at `01 NNSA/01 Deliverables/TRAK/docs/framework-demo/index.html` (~1900 lines including inline CSS + SVG + JS), TRAK-palette + NNSA-logo branded, 12 sections, fully aligned to the TRAK 3D × 3Q model. (b) demonstrated capability per [R016].

---

## 1. Entry state

User invoked with: "NNSA project review. warm up ruflo. Pull up: 1. TRAK Excel 2. TRAK Streamlit app 3. MACQ demo. Also, did we fix the TRAK 1-pager?" Three assets were known from memory (`memory/project_trak.md`); the 1-pager status question was the only open thread.

---

## 2. Approach

Two-phase session:

**Phase A — Inventory and launch (~early session).** Located and opened TRAK Excel (`docs/samples/TRAK_Tool_v1_blank.xlsx`), started TRAK Streamlit workbench on `:8501`, opened MACQ demo v11 HTML. Initial `cmd /c start` from the Bash tool silently failed; switched to PowerShell `Start-Process` to reliably launch on Windows. Answered 1-pager question: HTML edited 2026-05-19 (vN strings stripped) but PDF not re-rendered. Inventoried six TRAK-adjacent demo assets including the pre-review snapshot freeze and the pd_workbench_demo predecessor; user corrected that pd_workbench_demo is NOT a TRAK product (saved to memory).

**Phase B — Framework demo build (bulk of session).** Five review rounds, each discuss-before-execute:

1. **Initial scaffold.** Copied `framework_demo_v2.html` → `framework-demo/index.html`. Re-skinned to TRAK palette (navy `#14233b`, NNSA gold `#c9a227`, supporting blue, Y/P/N colors). Source Sans Pro typography. NNSA logo in sidebar header. Title and badge "WRT-2516 v2" strings stripped per the internal-vN rule.
2. **Logo + Section 5 reframe + new Sections 6, 7.** Enlarged logo to 132px, dropped "NNSA Sponsor" label. Section 5 rewritten from 4D (Evidence Quality / Readiness / Governance / Quality) to TRAK 3D (Readiness / Governance / Quality) with C(3,2)=3 pairwise quadrants. Added Section 6 "The Three Questions" (Q1 Can use? / Q2 Do use? / Q3 Trust?) with TRAK-verbatim language. Added Section 7 "The 9-Cell Matrix (D × Q)" — 3×3 interactive grid with hover/focus-driven meaning panel using TRAK-verbatim per-cell wording. **Removed Worked Example section entirely** — 177 lines of heatmap JS + DOM + the cell-detail overlay HTML deleted via PowerShell line-range splice.
3. **Tagline + Quantifying Uncertainty + Domain Tailoring rework.** Sidebar subtitle changed to "SE Transformation Assessment Kit (TRAK)". New Section 10 "Quantifying Uncertainty" (Posteriors / ETV / Shadow prices cards + expert detail) inserted after Gap Analysis; redundant Bayesian expert panel removed from Gap Analysis. Section 11 reworked to "Domain Tailoring: NNSA Shall-Statement Requirements" — opening narrative on TRAK's generic core + tailoring layer; Generic→NNSA-Instance layered Q diagram using shall-statements as the worked method (per the TRAK Practitioner Guide source confirmed by grep of `Practitioner_Assessment_Guide_Draft_2026-04-10.md`); existing regulatory stack reframed as "where D2 plugs in"; Evidence Thresholds table reframed off the obsolete 4D "Evidence Quality" axis and onto the TRAK ontology's Established/Inferred/Synthetic source classifications. Bottom citation box rewritten to TRAK Practitioner Guide (Wach & Salado, SERC WRT-2516).
4. **Section 2/3 swap + Section 10 visual.** Sections 2 and 3 reordered: Four-Layer Framework now Section 2 (architectural primer leads); "The Measurement Problem" (renamed from "Why Single-Instrument Assessment Fails") now Section 3 (motivation flows into GRL in Section 4). Section 10 got Option E visual aid: inline-SVG before/after posterior comparison (point estimate `GRL=5` vs 9-bar posterior with right tail shaded gold, labeled "72% of mass") + illustrative ETV ranking table (4 candidate interventions ranked by `ETV = P × V − C`, top row highlighted as binding-constraint relaxation) + shadow-prices annotation line. Table explicitly marked "Illustrative example — values are notional" per data-provenance feedback rule.
5. **4D vestige scrub.** Section 9 Dimensional Gaps subsection rewritten under 3D: Readiness-Quality (D1-D3), Readiness-Governance (D1-D2), Governance-Quality (D2-D3). Section 12 "Instrument D4" card renamed to "Instrument D3 Quality". Orphan `.axis-d4 .axis-tag` CSS rule deleted.

---

## 3. Final section structure (12 sections)

1 Introduction · 2 Four-Layer Framework · 3 The Measurement Problem · 4 The GRL · 5 The Three Dimensions · 6 The Three Questions · 7 The 9-Cell Matrix · 8 Conceptual Quicksand · 9 Gap Analysis · 10 Quantifying Uncertainty · 11 Domain Tailoring · 12 What's Next.

---

## 4. Files touched

- **Created:** `01 NNSA/01 Deliverables/TRAK/docs/framework-demo/index.html` (~1900 lines, inline CSS + SVG + JS)
- **Created:** `01 NNSA/01 Deliverables/TRAK/docs/framework-demo/assets/img/NNSA_logo.jpg` (copied from `TRAK/docs/demo/assets/img/`)
- **Untouched (source artifact preserved):** `01 NNSA/01 Deliverables/Vision_and_Roadmap/WRT-2516_v2/demo/framework_demo_v2.html`
- **Untouched (peer demo):** `01 NNSA/01 Deliverables/TRAK/docs/demo/` (the practitioner demo)
- **PostWach repo:** `docs/session-archives/SESSION_ARCHIVE_2026-05-28_postwach-03.md` (this file); `Papers/AI_Swarm_Productivity/data/scorecards/2026-05-28-postwach-03.yaml`; `.claude/projects/.../memory/project_trak.md` updated.

The TRAK repo (where the new demo lives) is `DocWach/TRAK`. This session did not commit or push to it; that is a separate handoff.

---

## 5. Decisions / judgment calls

- **D1: New demo, not edit of existing.** Demo built as a separate folder (`docs/framework-demo/`) sibling to the practitioner demo (`docs/demo/`), source artifact (`Vision_and_Roadmap/WRT-2516_v2/demo/`) left untouched.
- **D2: Single-page sidebar, not multi-page top-nav.** Audience purpose is "explain the framework"; sidebar single-page UX is better for sequential explanatory content than TRAK practitioner demo's 3-page scroll. Two design idioms persist in the portfolio but each serves its audience.
- **D3: Drop framework's D1 Evidence Quality dimension entirely.** TRAK is 3D (Readiness / Governance / Quality); the framework's 4th axis (Evidence Quality) doesn't exist in the practitioner kit. Evidence quality is captured in TRAK via the cell-stamp ontology (Established / Inferred / Synthetic), so the concept survives — just not as a numbered dimension.
- **D4: Generic-vs-domain is a Q-layer story, not a D-layer story.** User redirect confirmed by TRAK Guide source: "Q1, Q2, and Q3 assess method potential: the domain-agnostic question of whether a method is sound, practiced, and trusted in principle." Section 11 layered diagram puts generic Qs on top, NNSA shall-statement instance Qs on the bottom.
- **D5: ETV table flagged "Illustrative — values are notional"** per the data-provenance feedback rule, so the $3.45M shadow price on governance isn't mistaken for a real NNSA estimate.
- **D6: Worked Example removed, not migrated.** The 4D heatmap (Element × Evidence/Readiness/Governance/Quality scores) doesn't translate to TRAK's outcome × Q × D structure without rewriting the underlying data model. Removed cleanly; section count net +1 (one removed, two added — 3Qs and 9-Cell Matrix).
- **D7: Bottom box cites TRAK Practitioner Guide.** Per user direction. Wach & Salado as principal authors per memory; WRT-2516 retained as SERC report number umbrella citation.

---

## 6. Out-of-scope items still flagged

- **TRAK 1-pager (Flyer v3)**: HTML edited 2026-05-19 but PDF not re-rendered. Open from prior session, not touched this session.
- **DocWach/TRAK push of `docs/framework-demo/`**: not committed/pushed in this session. The framework demo lives only in the local `01 NNSA/01 Deliverables/TRAK/` mirror.
- **Cross-link strategy**: framework demo is fully standalone per user direction — no link back to the practitioner demo. If a "see also" link is later wanted, it's a small footer addition.

---

## 7. Open backlog

None new from this session. Existing TRAK backlog (10 demo review comments from 2026-05-18 postwach-03 archive) is unchanged.

---

## 8. Memory updates

- `memory/project_trak.md` — appended the framework-demo location and the "SE Transformation Assessment Kit (TRAK)" tagline observation. The framework demo is a separate artifact from the practitioner demo and has a different audience (NNSA decision-makers seeing the framework for the first time vs. practitioners using the kit).
- `MEMORY.md` index — no new pointer needed (project_trak.md is already indexed).

---

## 9. Termination

- Background TRAK Streamlit on `:8501` (task `bkwu1b28h`) terminated at end of session.
- Background pd_workbench_demo Streamlit on `:8502` (task `bwecirza9`) was already terminated mid-session after user corrected that it is not a TRAK product.
- No other background tasks or agents running.
