# Session Archive: 2026-04-09 PostWach-01

**Hive:** PostWach
**Date:** 2026-04-09
**Duration:** ~1.5 hours (wall clock; background agents ran in parallel)
**Focus:** Review of Taylan/VT Requirements-Assistant codebase for NNSA deliverable (PD Workbench)

---

## Objectives
1. Clone and review the authoritative VT codebase (`DocWach/Requirements-Assistant`) that is being proposed as the NNSA PD Workbench deliverable.
2. Produce a dual-audience review: (a) items we may want to edit ourselves, and (b) items NNSA is likely to raise concerns about.
3. Check gap vs. the March 31 integration plan (`PD_Workbench_Integration_Plan_2026-03-31.md`) that was given to Taylan.
4. Do not modify VT's code in this pass — review only.

## Context
- User flagged that Taylan and his students at Virginia Tech have code that "needs serious work," specifically calling out that "they have not successfully integrated the ontology."
- March 31 integration plan (authored by P. Wach) is in scope as the reference standard but does NOT need to be fully resolved. It is the paper trail for what was asked and what NNSA will expect.
- Review framing (per user): "for our use to make potential edits, plus notes of expected troubles NNSA will have." Not a hard grade of VT; a practical triage.

## Setup Work Completed

### Environment
- Ruflo (claude-flow) warmed up: **v3.5.7** confirmed working.
- Cloned `https://github.com/DocWach/Requirements-Assistant` to `03 Projects/01 NNSA/01 Deliverables/RE_Assistant_VT/` per user direction.

### Branch discovery (important finding)
Initial inspection of `main` alone showed only 2 commits and no integration attempt. After the user prompted to check branches, `git fetch --all` revealed **two additional remote branches** that main does not reflect:

```
* d5eda02 (origin/updated-agentic-code-version) Add agentic subagent analyzer, eval matrix tooling, and updated AI analyzer
* a0be5e7                                        Update backend AI analyzer, ontology loader, and service modules
* ad9f013 (origin/pd-workbench-phase1-3)         Add ontology-backed PD Workbench backend (Phases 1-3)
* a3c6f3d (HEAD -> main, origin/main, origin/HEAD) Add INCOSE Requirements Analyzer application
* 73080ec                                        Initial commit
```

- `main` — pre-integration baseline matching the "Current State" section of the March 31 plan.
- `pd-workbench-phase1-3` — VT's attempt at the integration plan (commit message literally says "Phases 1-3").
- `updated-agentic-code-version` — branched off `pd-workbench-phase1-3`, adds an agentic subagent analyzer and an eval matrix tooling layer.

This reframes the review: the "failed ontology integration" lives on the integration branches, not on main. Review must cover the integration branches.

### March 31 Integration Plan — authoritative reference
- File: `03 Projects/01 NNSA/01 Deliverables/PD_Workbench_Integration_Plan_2026-03-31.md`
- Documents current state of VT code (9 of 42 rules in flat JSON, zero RDF/SPARQL/OWL/SHACL, dead `characteristics_addressed` field, severity freely assigned by LLM, binding constraint: "operates on strings, not formal semantics," ~5–10% of Ch. 10 PD scope).
- Phase 1 (~8h): drop-in backend upgrade — replace flat JSON with SPARQL against `incose-req.ttl` (42 rules), add `ontology_loader.py`, refactor `ai_analyzer.py`, no frontend changes.
- Phase 2 (~16h): mint Claude JSON → RDF, SHACL-validate, coverage/quality-profile endpoints.
- Phase 3 (~24h): set-level analysis (C10–C15), cross-requirement conflicts.
- Division of labor puts Phase 1 almost entirely on Taylan.
- Phase 1 alone moves the deliverable from `(a) research artifact` to `(b) demonstrated capability` per R016.

## Review Plan

### Lenses (parallel background agents)
1. **"What we should fix before NNSA touches it"** — fragile/broken things we'd want to patch before the deliverable leaves our hands. Prioritized (P0/P1/P2).
2. **"What NNSA will probably notice and ask about"** — stale deps, secrets handling, prompt injection surface, missing tests, overclaimed README, ontology gap. Things to have an answer ready for.
3. **"Gap vs. March 31 plan"** — Phase 1 reality check: which parts of the plan are present in `pd-workbench-phase1-3` / `updated-agentic-code-version`, and what's broken or missing.

### Branches to review
- **Primary:** `updated-agentic-code-version` (newest, builds on Phase 1–3 work, includes agentic additions)
- **Secondary:** `pd-workbench-phase1-3` (to understand the integration attempt before the agentic layer was added)
- **Baseline diff:** `main` → integration branches (what did VT actually change?)

### Output location
Review deliverable will be saved under `03 Projects/01 NNSA/01 Deliverables/` with a dated filename. **No modifications to VT code, no pushes, no PRs to VT repo.**

---

## Work Completed

### Deliverable produced
`03 Projects/01 NNSA/01 Deliverables/PD_Workbench_VT_Code_Review_2026-04-09.md` — 8-section consolidated code review report, ~30 KB markdown. Sections: executive summary, branch map, punch list (P0/P1/P2 across three lenses), integration plan gap tables (Phases 1/2/3), "things to have an answer for," recommendations (Options A/B/C with push-back-to-VT list), file inventory, provenance.

### Headline findings

**The "not successfully integrated" observation is correct but has a specific shape:**
1. **Single-requirement analysis (ai_analyzer.py) IS ~80% ontology-grounded.** The SPARQL-to-prompt flow works; 42 rules with characteristic annotations land in Claude's prompt (`ai_analyzer.py:40-82`, `_build_rules_text`).
2. **Set analysis is fake-grounded.** `SetAnalyzer.__init__` takes `ontology_service`, stores it as `self._svc`, and never references it again in the entire 388-line file (`set_analyzer.py:42-44`). All C10-C15 analysis is regex + `difflib.SequenceMatcher`.
3. **SHACL is decorative.** `ai_analyzer.py:289-339` normalizes bad rule IDs via a hardcoded `VALID_RULE_IDS = {f"R{i}" for i in range(1,43)}` Python set *before* any RDF is minted. `pyshacl.validate` runs only from an opt-in endpoint (`main.py:457`) that the frontend never calls.
4. **The "agentic" layer of `updated-agentic-code-version` branch is orphaned.** `subagent_analyzer.py` (359 LOC) is reachable only from `eval_10runs.py` and `smoke_test_gps.py`; `main.py` imports only `ai_analyzer`. The headline feature of this branch is not in production.
5. **`GET /api/rules` (the plan's Phase 1 acceptance gate) does not exist.** Phase 1 cannot be accepted against its stated criterion.
6. **Frontend has zero references to Phase 2/3 endpoints** (`coverage`, `quality-profile`, `validation`, `set-analysis`). Backend work is invisible to users.
7. **Security posture: RED.** No auth, wildcard CORS + credentials, `host="0.0.0.0"` + `http://` everywhere, misleading frontend hint omitting that requirement text leaves the environment, `/api/knowledge/reset` unauthenticated, `anthropic==0.34.0` ~50 versions behind.
8. **Good news #1:** No sponsor data leak. The 7 committed eval JSONs are a toy 13-requirement point-mass/GPS example, not sponsor content. BUT they leak Windows developer paths (`C:\Users\Owner\Downloads\...`) and 6 of 7 contain embedded `cp1252` Unicode crash errors.
9. **Good news #2:** The ontology layer itself is the strongest piece of the codebase. Fix-in-place is viable; rewrite is unnecessary.

### Fix-in-place viability
Confirmed viable. Three tight options in the review document:
- **Option A (4-6h):** Minimum viable — add `/api/rules`, fix smoke test, drop unused `SetAnalyzer` parameter, fix the 26-rule fallback map, tighten CORS, add auth to `/reset`, rewrite frontend hint, purge committed artifacts, pin anthropic SDK.
- **Option B (+4-6h, recommended):** Make SHACL load-bearing. Move `_validate_and_fix_violations` to call `mint_assessment_rdf` + `validate_assessment` synchronously in `/api/upload`. Add UAV Navigation Requirements fixture. Closes the one plan item explicitly assigned to Wach.
- **Option C (+8-12h, optional):** Close Phase 3 honestly with at least one SPARQL-backed set check (C11 "contradictory-constraint-on-shared-subject" is the obvious first target) plus minimal frontend panels.

### R016 classification
Current state: **`(a) research artifact`**. Any cover memo describing this as "integrated" or "production-ready" crosses the R016 line. Option B would move it to `(b) demonstrated capability`. Only Option C closure approaches `(c) integrated deliverable`.

## Agents Spawned

3 parallel background agents under ruflo v3.5.7:

| Lens | Agent type | Focus | Runtime |
|---|---|---|---|
| **Lens 1** | `reviewer` | Internal-fix punch list (P0/P1/P2) — what PostWach should patch in place | ~12 min |
| **Lens 2** | `security-auditor` | NNSA-external review — data handling, secrets, CVEs, prompt injection, ZT alignment | ~12 min |
| **Lens 3** | `code-analyzer` | Gap vs. March 31 integration plan — "looks integrated but isn't" analysis | ~15 min |

Each agent read source directly from `origin/updated-agentic-code-version` with secondary verification against `origin/pd-workbench-phase1-3`. All findings cite `file:line`. Convergent findings across multiple lenses (SetAnalyzer fake grounding, orphaned subagent_analyzer, broken smoke_test, decorative SHACL, CORS wildcard) are more confidently load-bearing.

## Key Decisions

- **D27: Branch to review = `updated-agentic-code-version`.** Primary target is the newest branch (builds on Phase 1–3 work, adds agentic/eval layer). Secondary verification against `pd-workbench-phase1-3` to identify which problems trace to the initial integration vs. the agentic overlay.
- **D28: Fix in place, do not rewrite.** The ontology wiring is ~80% correct in the critical `ai_analyzer.py` path. Rewriting would discard 2,658 LOC of legitimate Phase 1–3 scaffolding for no gain.
- **D29: Review framing is dual-audience.** Per user direction: "for our use to make potential edits, plus notes of expected troubles NNSA will have." Reflected in Lens 1 (internal) and Lens 2 (external) split and the §5 "Things to Have an Answer For" section.
- **D30: R016 status of deliverable is `(a) research artifact`.** No cover memo or sponsor-facing language should claim more until at least Option B is implemented.
- **D31: Committed eval JSONs are not sponsor data.** Verified by Lens 2 grep — content is a 13-requirement toy point-mass/GPS example. Still must be purged (developer path leakage, embedded crash errors) but not a P0 data incident.

## Outstanding

- **User decision needed:** which Option (A / A+B / A+B+C) to execute, and whether to execute in PostWach repo or push back to Taylan as a review note.
- **User decision needed:** history rewrite on a delivery fork vs. scrub-and-forward-commit for the 7 eval JSONs + 2 developer-path leaks.
- **User decision needed:** how to communicate findings to Taylan. Options: (i) share the full review document, (ii) send a subset (e.g., push-back items only), (iii) handle quietly via PostWach patches.
- **If Option B is chosen**, the UAV Navigation Requirements fixture must be copied from `02 Hives/05 GI-JOE/ontologies/domain/incose-req-rules.ttl` into the delivery fork.
- **Long-standing open thread unaffected by this session:** WySE ontology stack still needs work (still high priority per MEMORY.md); this review does not touch it.

## Related Files

- **Review deliverable:** `03 Projects/01 NNSA/01 Deliverables/PD_Workbench_VT_Code_Review_2026-04-09.md`
- **Reference standard:** `03 Projects/01 NNSA/01 Deliverables/PD_Workbench_Integration_Plan_2026-03-31.md`
- **VT codebase:** `03 Projects/01 NNSA/01 Deliverables/RE_Assistant_VT/` (clean clone, 3 branches fetched, no modifications)
- **Ontology source of truth:** `02 Hives/05 GI-JOE/ontologies/domain/incose-req*.ttl` + `queries/incose-req/CQ-IR01..09.rq`

---

## Phase 2: Execution (A + B + C)

### Decision (2026-04-09, post-review)

User confirmed **Options A + B + C** after a recommendation-and-debate exchange. Key calibrations during the debate:

1. **Reviewer's characterization corrected:** User described VT code as "entirely insufficient and sloppy." Assistant pushed back: the accurate characterization is "partially functional in the one place it matters (single-requirement analysis is ~80% ontology-grounded), architecturally sloppy everywhere else, operationally careless throughout." The distinction matters because "entirely insufficient" leads to "rewrite" while the accurate framing supports "surgical patches on good bones."
2. **Memory staleness failure acknowledged:** Assistant's initial recommendation against Option C was anchored on DARPA CLARA being an 8-day deadline. User corrected: CLARA was decided against. Memory updated at `memory/MEMORY.md` to reflect decision. Also updated: WySE ontology priority is flexible (internal deliverable, no external deadline).
3. **Revised recommendation:** With CLARA off the table and WySE flexible, the calendar argument against Option C collapsed. Assistant reversed to support A+B+C, with Option C refined to be backend-first and frontend-minimal (skip the React "Set Analysis tab," extend the existing results page instead).

### Execution plan

**Option A (4-6h) — security + hygiene + correctness:**
- Add `GET /api/rules` endpoint in `main.py` (the plan's Phase 1 acceptance gate)
- Tighten CORS: read allowlist from env var, drop wildcard+credentials combo
- Add bearer-token gate to `/api/knowledge/reset`
- Fix `smoke_test.py:11,14` (URL + version assertion)
- Replace `subagent_analyzer.py:88-96` hardcoded 26-rule `RULE_TO_CHAR` with dynamic lookup from OntologyLoader
- Pin `anthropic>=0.87` in requirements.txt; add missing runtime deps (pandas, matplotlib, openpyxl)
- Rewrite misleading data-flow hint in `frontend/src/pages/UploadPage.jsx:91`
- Repo hygiene: `git rm --cached` the 7 eval JSONs + 14 chart PNGs + 4 xlsx files; add `.gitignore` entries; `git mv run_analysis.py backend/`
- Fix `run.bat:16` hardcoded developer path

**Option B (4-6h) — SHACL load-bearing + UAV acceptance test:**
- Move `_validate_and_fix_violations` (`ai_analyzer.py:289-339`) to call `mint_assessment_rdf` + `validate_assessment` synchronously in the upload flow
- Route SHACL failures back into the violation list as structured errors
- Create UAV Navigation Requirements pytest fixture from GI-JOE ABox
- Create `test_uav_navigation_acceptance.py` pytest case asserting the expected minimum violations

**Option C refined (6-10h, backend-first) — set-level SPARQL:**
- Add CQ-IR10 and CQ-IR11 to `02 Hives/05 GI-JOE/ontologies/queries/incose-req/` (governance: new queries live in GI-JOE first, then copy into the fork)
- Copy the .rq files into `RE_Assistant_VT/backend/ontology/queries/`
- Wire `SetAnalyzer` to actually consume `self._svc` for C11 (consistency) and one other set characteristic using the new queries
- Label remaining regex-based set checks as `# HEURISTIC: pending ontology extension`
- Frontend (minimal): extend existing results page with a "Set Analysis" section + "Coverage Summary" section. No new routes, reuse existing components

### Branch strategy

Created local branch `postwach-delivery-fixes` in `RE_Assistant_VT/` clone, based on `origin/updated-agentic-code-version`. This branch does NOT push to VT's GitHub repo — it is a PostWach-internal working branch. All three execution agents are instructed: **no commits, no pushes, no PRs**. User will review diffs and commit manually.

### Execution agents (3 parallel, background)

| Agent | Scope | Files |
|---|---|---|
| **Agent 1 — Backend code** | `sparc-coder`. Python backend: A1 (`/api/rules`), A2 (CORS), A3 (reset auth), A4 (smoke_test fix), A5 (RULE_TO_CHAR dynamic lookup), A6 (deps), B1 (SHACL in upload flow), C1 (SetAnalyzer wiring to SPARQL queries) | `backend/main.py`, `ai_analyzer.py`, `ontology_loader.py` (read), `ontology_service.py` (read), `set_analyzer.py`, `subagent_analyzer.py`, `smoke_test.py`, `requirements.txt` |
| **Agent 2 — Frontend + repo hygiene** | `sparc-coder`. F1 (misleading hint rewrite), F2 (minimal Set Analysis + Coverage sections on existing results page), H1 (git rm --cached eval JSONs, charts, xlsx), H2 (`git mv run_analysis.py`), H3 (.gitignore), H4 (`run.bat:16` developer path fix) | `frontend/src/pages/*.jsx`, `.gitignore`, `run.bat`, repo root files |
| **Agent 3 — Ontology queries + test fixtures** | `sparc-coder`. G1 (inspect existing ontology), G2 (CQ-IR10), G3 (CQ-IR11), G4 (copy to backend), G5 (UAV fixture), G6 (pytest test file), G7 (match existing query style) | `02 Hives/05 GI-JOE/ontologies/queries/incose-req/CQ-IR10.rq`, `CQ-IR11.rq`, `backend/ontology/queries/` (copies), `backend/tests/fixtures/`, `backend/tests/test_uav_navigation_acceptance.py`, `backend/tests/__init__.py`, `backend/tests/conftest.py` |

**File scope non-overlap:** Agent 1 owns `backend/*.py` except tests/ontology subdirs. Agent 2 owns frontend + root + `.gitignore` + `run.bat`. Agent 3 owns GI-JOE ontology dir + `backend/ontology/queries/CQ-IR10.rq`, `CQ-IR11.rq` (new files) + `backend/tests/**` (new directory). **No two agents write the same file.**

**Dependency note:** Agent 1's SetAnalyzer wiring references query files at `backend/ontology/queries/CQ-IR10.rq` and `CQ-IR11.rq`. Agent 3 creates those files. Agent 1's code loads them lazily with `try/except FileNotFoundError` fallback to the existing regex behavior, so Agent 1 and Agent 3 can run in parallel even though there is a logical dependency.

### Documentation work still running

The detailed findings document agent (launched earlier) is also still running in the background. It is producing `PD_Workbench_VT_Findings_Detail_2026-04-09.md` — the comprehensive companion to the consolidated review, structured for later extraction into a Taylan-facing communication. This agent is independent of the three execution agents and does not touch the same files.

**Total agents in flight at this point: 4** (1 documentation + 3 execution).

### Constraints shared by all execution agents

- No commits in any repo. No pushes. No PRs to VT.
- Do not touch `main` branch in `RE_Assistant_VT`. All work on `postwach-delivery-fixes`.
- Do not modify `02 Hives/05 GI-JOE` outside of the new query files (G2, G3).
- Prioritize A > B > C if time is short; leave TODO comments rather than half-implementing.
- User is on a ~30 minute internet window. Work will continue server-side even if user disconnects.

---

*Session continued on 2026-04-10. See `SESSION_ARCHIVE_2026-04-10_postwach-02.md` for: Adi's refactor delta analysis, hybrid integration, Streamlit pivot (D34), SEAD handoff (SEAD-PD-001), and the cross-hive ticket routing question (D36).*


