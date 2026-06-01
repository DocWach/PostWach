# Session Archive: 2026-03-31 PostWach-01

**Date:** 2026-03-31
**Hive:** PostWach
**Focus:** Meeting prep for Taylan/VT on WRT-2516 Requirements Engineering capability

---

## Session Summary

Prepared briefing for morning meeting with Taylan (VT professor, NNSA WRT-2516 collaborator) on the Requirements Engineering capability deliverable. Cross-referenced GI-JOE ontology work and NNSA deliverables to build a comprehensive status picture.

## Context Gathered

### NNSA Deliverables Reviewed (01 NNSA/01 Deliverables/)

| Document | Date | Purpose |
|---|---|---|
| PD_Layer0_Outcomes | Mar 26 | 8 mission-level outcomes (O1-O8) |
| PD_Outcome_Level_Matrix | Mar 26 | 8 outcomes x 5 executional levels |
| PD_Overall_Assessment | Mar 26 | Three-step transformation story (As-Is, +Team Demo, +Integration) |
| PD_Bayesian_GRL_Profile | Mar 26 | 6-thread readiness (T/M/W/G/F/K) across 3 steps |
| PD_Assessment_Framework_Baseline | Mar 27 | 4-stage pipeline, Q1/Q2/Q3 structure |
| PD_Shall_Statement_Assessment v1+v2 | Mar 27 | 72-cell matrix assessing NL requirements against O1-O8 |
| INCOSE_Requirements_Ontology_Plan | Mar 26 | Plan to formalize INCOSE Guide V4 in OWL/BFO (~8 hrs) |

### GI-JOE Session Archives Reviewed

| Archive | Key RE Content |
|---|---|
| 2026-03-26 (Session 02) | MOACRA Cyber Rosetta review (not RE-specific) |
| 2026-03-27 / 2026-03-30 | OML vs OWL/TTL investigation; Joe Gregory feedback on incose-req; Requirements-Assistant repo analysis; OML conversion completed (22 files); 5-layer validation architecture; test ABox (UAV); Gradle pipeline blocked on OML syntax |

### GI-JOE Ontology Artifacts (incose-req)

| Artifact | Status | Key Metrics |
|---|---|---|
| incose-req.ttl (TBox) | Complete | 12 classes, 168 triples, 100% BFO-aligned |
| incose-req-rules.ttl (ABox) | Complete | 42 rules, 15 characteristics, 78 individuals, 570 triples |
| incose-req.shapes.ttl (SHACL) | Complete | 7 shapes, CONFORMS |
| 9 SPARQL CQs | Complete | 6/9 substantive, 3 need assessment data |
| OML conversion (22 files) | Complete | Full project with SWRL, disjointness, test ABox |
| Gradle 5-layer pipeline | Blocked | OML syntax errors; needs Joe review in OML Rosetta |
| incose-req-report.md | Complete | 311 lines, full analysis report |

### Requirements-Assistant Analysis (from GI-JOE Mar 30)

- Only 9 of 42 INCOSE rules implemented in incose_rules.json
- characteristics_addressed field is dead code
- Zero programmatic rule checking; all intelligence prompt-inlined
- RAG via ChromaDB; no semantic technology
- All Q3 (Trust) cells are "No" in shall statement assessment

### Division of Labor (Decided Mar 30)

- Our team: OML project, axioms, SWRL, 5-layer validation pipeline (formal knowledge artifact)
- Taylan's team: Expanding rules 9 to 42, making characteristics live, SPARQL-to-JSON bridge, prompt engineering, NNSA domain rules

### Key Findings for Meeting

1. **Capability inversion pattern:** Tools (T=6) outpace Foundations (F=3). Technology operates on strings, not formal semantics.
2. **Binding constraint is Foundations, not Technology.** Step 2 to 3 requires integrating existing research artifacts, not building new tools.
3. **Requirements-Assistant covers ~5-10% of Ch. 10's Problem Definition scope.**
4. **Three-step transformation story:** As-Is (L1), +Team Demo (L1-2), +Integration (L3, paradigm shift to model-driven).
5. **INCOSE ontology is built** but not yet connected to Requirements-Assistant. Integration path defined.
6. **OML pipeline blocked** on syntax; needs Joe's tooling.

## Deliverables Produced

### 1. Integration Document

**File:** `01 NNSA/01 Deliverables/PD_Workbench_Integration_Plan_2026-03-31.md` + `.pdf`

Technical integration plan for Taylan covering:
- Current state assessment (Requirements-Assistant + incose-req ontology)
- O1-O8 outcome coverage table (current vs. Phase 1/2/3 targets)
- Three phased upgrade path (Phase 1: ~8h, Phase 2: ~16h, Phase 3: ~24h)
- Division of labor (Wach team: ontology/SHACL/SPARQL; Taylan team: backend integration/frontend)
- Files to share, success criteria, mapping to WRT-2516 report chapters

Sent to Taylan after meeting.

### 2. PD Workbench Backend (Phases 1-3)

**Repo:** `DocWach/Requirements-Assistant`
**Branch:** `pd-workbench-phase1-3`
**Commit:** `ad9f013` (20 files, 2,658 lines)

#### Phase 1: Ontology-Backed Rules (drop-in backend upgrade)

| File | Lines | Purpose |
|---|---|---|
| `backend/ontology_loader.py` | 121 | rdflib SPARQL loader for 42 rules, 15 characteristics |
| `backend/ontology/incose-req.ttl` | (copied) | TBox from GI-JOE |
| `backend/ontology/incose-req-rules.ttl` | (copied) | ABox from GI-JOE |
| `backend/ontology/incose-req.shapes.ttl` | (copied) | SHACL shapes from GI-JOE |
| `backend/ontology/queries/CQ-IR01..09.rq` | (copied) | SPARQL competency queries |
| `backend/ai_analyzer.py` | (modified) | OntologyLoader singleton; 174-line prompt with 42 rules by category |
| `backend/requirements.txt` | (modified) | Added rdflib>=7.0.0 |

Smoke test: 42 rules, 15 characteristics (9 individual, 6 set), 14 categories, 9 dictionary-dependent rules. Prompt: 174 lines, 9,823 chars.

#### Phase 2: Ontology-Grounded Assessment

| File | Lines | Purpose |
|---|---|---|
| `backend/ontology_service.py` | ~220 | Mint RDF from Claude JSON, SHACL validation, SPARQL coverage/quality/severity |
| `backend/main.py` | (modified) | +3 endpoints: /coverage, /quality-profile, /validation |
| `backend/requirements.txt` | (modified) | Added pyshacl>=0.25.0 |

Smoke test: 755 triples, SHACL conforms, 3/15 characteristics covered (correct for single R7 violation), 1/42 rules triggered.

#### Phase 3: Set-Level Analysis

| File | Lines | Purpose |
|---|---|---|
| `backend/set_analyzer.py` | ~270 | Glossary extraction, terminology checking, conflict detection, C10-C15 assessment |
| `backend/set_analysis_prompt.py` | ~80 | Claude prompt for semantic set-level analysis |
| `backend/main.py` | (modified) | +4 endpoints: POST/GET /set-analysis, /glossary, /conflicts |
| `backend/feedback_storage.py` | (modified) | +2 functions: save/load set analysis |

Smoke test (6 requirements with known issues): 6 glossary terms, 6 terminology issues, 2 conflicts (contradictory 5s vs 10s timing, 84% near-duplicate), C10=0.33, C11=0.00, C12=0.70, C13=0.71, C14=0.67, C15=N/A.

### Integration Status (R016)

All backend code is **(a) research artifact** (exists in branch, smoke-tested in isolation, not connected to frontend or tested end-to-end). Taylan's team owns frontend integration and E2E testing to move toward (b) demonstrated capability.

### What Taylan's Team Needs To Do

- Pull branch `pd-workbench-phase1-3`
- Frontend: coverage dashboard component (Phase 2)
- Frontend: set analysis tab (Phase 3)
- End-to-end testing with real Claude API calls
- NNSA domain-specific rule extensions (NQA-1, MIL-STD-882)

### What Remains On Our Side

- OML pipeline fix (needs Joe Gregory's review in OML Rosetta)
- SHACL shape refinement if Claude output patterns reveal edge cases
- Phase 4 (future): STOIC/readiness integration, traceability, change impact

## Memory Updates

- Saved: Taylan is a VT professor on NNSA WRT-2516 (not related to VT ISE Senior Design supply chain project)

## Corrections

- Initial prep mistakenly oriented toward VT ISE Senior Design titanium supply chain project. Corrected after user clarification that Taylan/VT context is NNSA WRT-2516.

---

## Session Status: COMPLETE
