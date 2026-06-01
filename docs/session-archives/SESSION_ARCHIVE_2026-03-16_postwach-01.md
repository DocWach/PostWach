# Session Archive: 2026-03-16 PostWach-01

**Date:** Monday, 2026-03-16 (IGNITE Day 1)
**Hive:** PostWach (CTO)
**Duration:** ~3 hours
**Branch:** `idsk-enterprise-sim` in IGNITE_Disruption_2026 repo

## Context

IGNITE '26 hackathon Day 1. User is in a mini-tutorial. Session focused on inventory, data extraction, and research scoping for the week.

## Accomplishments

### Comprehensive Provenance Inventory
- Traced every IGNITE artifact to its upstream source project (isomorphism-library, GI-JOE, Transformation-Roadmapping, MACQ, WRT-2406, DOD SAFE)
- Classified each as: imported, adapted, original, live integration, or research data
- Identified key lineage chain: DOD SAFE mdzip -> extract -> JSON -> ontology -> morphisms -> assessment

### Generic mdzip Extractor Built and Run
- `src/extract_all_mdzip.py`: Generic extractor for any Cameo MagicDraw .mdzip
- Extracts: blocks, SysML stereotypes, requirements, activities, use cases, packages, associations, dependencies, interfaces, enumerations, signals, state machines, constraints, measures (MOE/MOP/MOS), UAF elements
- **All 10 DOD SAFE models extracted** to `src/data/extracted/` (10 JSON + catalog)
- Key findings:
  - 1,590 blocks (504 SysML), 264 requirements, 993 activities, 243 measures
  - SEAD (Suppression of Enemy Air Defenses) is embedded in MissionArchStyleGuide (5 blocks, 4 activities, 4 measures) and Berserker SFR (mission config block), not a separate model
  - MissionArchStyleGuide is richest in measures (105); CapyBARA second (60)
  - BaseQueriesDistA is empty (query definitions only)

### Research Questions Documented
- `docs/MDZIP_RESEARCH_QUESTIONS.md`: 5 research questions with hypotheses, methods, and IGNITE arc connections
- RQ-1: Digital thread traceability across models
- RQ-2: Conway's Law model-to-org boundary mapping
- RQ-3: Measure coverage and orphan analysis
- RQ-4: Delta between three Berserker models (SFR, Impl Library, Product Baseline)
- RQ-5: Reference model role in assessment

### Synthetic vs. Real Data Audit
User discovered (via provenance questioning) that much of the app uses synthetic data:
- **Real:** System hierarchy, blocks, requirements, activities from DOD SAFE extraction
- **Synthetic:** Morphism sigma/D values (random perturbations), Arc 3 capability ratings (hardcoded), assessment recommendations, test schedules, Arc 2 degradation constants
- Feedback saved: always proactively flag synthetic vs. real data (`memory/feedback_data_provenance.md`)

### Key Context Notes from User
- MissionArchStyleGuide and Mission Meta Model UAF 1.3 are **reference/exemplar models** (Cameo EA tool-specific approach, not required but may be desired by government)
- The extracted measures are typical reusable measures for engineered systems; WRT-2516 also needs enterprise-level measures
- User wants Arc 0 focused on DE ecosystem (tools, workflows, pipelines, APIs)
- User wants to demo V1toV2 converter and Agentic Plugin at IGNITE
- User's questioning about provenance was implicitly asking "is this real or synthetic?" -- important feedback for future interactions

### User Reframe on Research Questions
- User redirected from academic RQs toward practical: "What key info/data do we have to complete our self-assigned work for the week and the NNSA deadline?"
- The models give us a taxonomy of measures, example flow-down to a specific system
- Need to map extracted data to deliverable needs (IGNITE demo this week, WRT-2516 v0.1 April 15)
- Documentation of research questions still valuable for revisit during/after IGNITE

### Cross-Model Analysis (Option C)
- Built and ran cross-model traceability analysis: `src/data/extracted/_cross_model_analysis.json`
- **Key finding: ZERO block name overlap** between SFR (397 blocks) and Implementation Library (72 blocks) or Product Baseline (153 blocks). Three models of the same system with completely divergent naming.
- 251 SysML blocks in SFR have zero named counterparts in the Implementation Library
- Impl Library and Baseline share 11 block names (closer in origin to each other)
- Measure overlap: only generic terms ("MOS") shared across models. No substantive mission-to-system measure linkage.
- CapyBARA: User believes it is a Cameo tool profile, not a separate system model. 60 measures likely reference/exemplar.

### IDSK Decomposition with Real Data
Populated Q1-Q5 with concrete findings:
- Q1: 233 requirements, 25 system measures, 105 mission measures, 473 activities
- Q2: Zero design-to-implementation traceability, zero mission-to-system measure links, 7/10 models have zero requirements
- Q3: Need cross-model name resolution, ontology alignment, or tool-based link recovery
- Q5: Digital thread, V1toV2, Agentic Plugin are the mechanisms

### Synthetic Data Strategy Debated
- Agreed: Option C (analysis) first, then decide on UI changes
- User clarified: synthetic data still valid for shaping Arc 2 and 3, but should be grounded
- Need to determine how much changes with Cameo XMI export (resolves proxy references, cross-project links, SysML trace/satisfy/verify relationships)
- **Critical question:** Does cross-project traceability exist in Cameo that our zip-level extraction misses? Zero overlap could be artifact of name-based matching when real traceability is ID-based.
- Two paths: (1) Ask Brad to check in Cameo (fastest), (2) Parse proxy snapshots ourselves

## Commits (all on `idsk-enterprise-sim` branch)
- `7f10272` -- Add generic mdzip extractor and extract all 10 DOD SAFE models
- `cac06a8` -- Add research questions for DOD SAFE mdzip collection analysis
- (uncommitted) `_cross_model_analysis.json`

---

## Session 02 (2026-03-17, IGNITE Day 2 at venue)

### Plan Review and Status Assessment

Reviewed execution plan against reality. Key findings:

**Plan vs. actual:**
- Inc 0-2 (build): Done. Engine, Arc 2 rebuild, Arc 3, IDSK reframe all complete.
- Inc 3 (integration, deck, rehearsal): Partially done. Technical manual written. No deck, no rehearsal, no team integration.
- Inc 4 (execution): In progress at venue.

**Joe's Arc 0 vision discovered** (commits `5b5cbae`, `7c9ebbb`, `b826e8e` on remote):
- New workflow: Practitioner tools (Jama, Cameo v1, SysON v2, GENESYS) -> Violet integration -> OML generation -> UofA Semantic Dashboard -> SPARQL queries -> dashboard views
- OML becomes the ASOT (Authoritative Source of Truth) for Arcs 1-3
- Joe needs all data Paul has used in examples
- Hunter and Carter (students) to create SysML models
- Violet Labs may need to update OML generation capability
- Joe said he can start Arc 0 on Tuesday

**Remote repo diverged from local branch:**
- `main` has Joe's execution plan updates + 10 mdzip files pushed to remote (`3cb6731`)
- `idsk-enterprise-sim` has IDSK/enterprise sim work + extraction + analysis
- Merge needed

**Team status (largely unknown):**
- Brad/RTSync: Not contacted. V1toV2 and Agentic Plugin wanted for Arc 0.
- Violet Labs (Katie/Mike): Unknown. OML generation may need update.
- Alejandro: No deck to review yet.
- Students (Hunter/Carter): Role assignments written but unclear if aligned with Joe's SysML model creation task.

**Missing deliverables:**
1. Presentation deck (was due Mar 15)
2. Arc 0 (Joe owns, not started)
3. Brad/Violet Labs integration (stubbed)
4. Branch merge
5. OML data handoff to Joe

### Team Status Update (confirmed at venue, Day 2)

**Joe Gregory:**
- Creating Arc 0
- Building OML representations of the data
- Updating ontologies as needed
- Has requested access to Paul's ontologies and SPARQL queries

**Carter and Hunter (UofA students):**
- Converting mdzip files to XMI
- Adding mdzip files to UofA Digital Engineering Factory (DEF)
- Extracting requirements from mdzip files to add to JAMA on the DEF
- Will help with other tasks afterwards, including defining potential SPARQL queries
- Goal: data/models in the DEF whether used this week or not
- Ideally also working in the Violet instance through the DEF

**Brad Philipbar (RTSync):**
- Converting mdzip files to SysML v2 (.sysml format)
- Will run DEVS-based analysis for kill chain, tests, test resource planning

**Violet Labs:**
- Minimal to no appearance at IGNITE
- Hunter/Carter working through Violet instance via DEF instead

**Paul (self):**
- Orchestrating the group
- Continuing work on Arc 2 and Arc 3
- Needs to share ontologies and SPARQL queries with Joe
- Supporting Hunter/Carter and others with SPARQL query definition

**Architecture decision:** OML is the authoritative source of truth. IGNITE git repo for data storage. This is parallel to the future plan of everything on the DEF using Violet.

### XMI Export Comparison (all 10 models complete)

**Initial comparison (9 models, SFR missing):**
- Block counts identical to mdzip extraction
- NEW traceability relationships found: CapyBARA 97 links, UML Test Profile 66, Product Baseline 29 allocate, MissionArch 9
- More measures in XMI: MissionArch 105->127, Meta Model 20->23, Cyber Schema 9->12
- Cross-project references (allocate in Product Baseline) have empty client/supplier; can't resolve without multi-model loading
- **CapyBARA acronym note:** "Capability Based Acquisition Resource Assessment" per user.

**Full comparison (all 10 models including SFR):**

Students completed all XMI exports. SFR was split into 3 parts due to GitHub 100MB limit (27.8 MB total). Reassembled and analyzed.

SFR deep dive:
- 524 blocks (291 SysML), 233 requirements, 507 activities, 15 use cases, 25 measures
- **936 traceability links** (608 Allocate, 240 Trace, 73 Refine, 15 Satisfy)
- Richest model by far; CapyBARA second with 227 links

Traceability summary across all models:
- SFR: 936 (Allocate=608, Trace=240, Refine=73, Satisfy=15)
- CapyBARA: 227 (Trace=167, DeriveReqt=20, Satisfy=14, Refine=12, Verify=8, Allocate=6)
- UMLTestProf: 66 (Satisfy=32, Verify=32, Refine=2)
- ProdBase: 29 (Allocate=29)
- MissionArch: 9 (Trace=8, Allocate=1)
- MetaModel: 5 (Trace=4, Refine=1)
- CyberSchema: 1 (Refine=1)
- ImplLib, BaseQueries, CryptoProf: 0

**CONFIRMED: Zero block name overlap between SFR and other Berserker models (XMI validates mdzip finding)**
- SFR x ImplLib: 0 overlap (522 vs 108 blocks)
- SFR x ProdBase: 0 overlap (522 vs 153 blocks)
- ImplLib x ProdBase: 11 shared (hardware-level: 28VDC, MIL-STD-1553, sensors)
- Only 20 block names shared across all 10 models total; all generic ("Sensor", "Engine", "GPS")

Measure overlap: 5 names shared across any pair; all generic placeholders ("measurement1", "MOS")

**Key conclusion:** The zero overlap is NOT an extraction artifact. Three models of the same Berserker system genuinely use completely different naming. The 936 SFR trace links are internal (requirements to subsystems within SFR), not cross-model. This is strong Conway's Law evidence for Arc 2.

Analysis saved to `src/data/extracted/_xmi_full_analysis.json` (uncommitted, per user instruction to wait for student completion; students are now done).

### Ontology Assets Cataloged for Joe

Located GI-JOE readiness level ontologies Joe needs for Arc 0 / OML work:
- 7 RL domain ontologies: `02 Hives/05 GI-JOE/ontologies/domain/rl-{trl,mrl,irl,hrl,krl,orl,bridge}.ttl`
- 7 SHACL shapes: `02 Hives/05 GI-JOE/ontologies/shapes/rl-*.shapes.ttl`
- STOIC family also in GI-JOE (stoic-devs, stoic-t3sd, stoic-bridge)
- Berserker assessment ontology + SPARQL queries already in IGNITE repo (`src/ontology/`)
- **Decision:** Joe adds his own ontologies and SPARQL queries to the IGNITE repo directly

### IGNITE Keynote Notes (Day 2)

Four observations from keynote speaker and event context:
1. **Antiquated policies** -- Need to account for outdated policies and propose corrections. Maps to Arc 2 (organizational barriers), D3 (Governance Compliance), WRT-2406 barrier taxonomy.
2. **Tool-agnostic technical stack** -- Should not rely on Cameo or specific tools. Aligns with Arc 0 (OML as ASOT), extraction pipeline, 4D ontology design.
3. **TEMP (Test and Evaluation Master Plan)** -- Include alongside IDSK. berserker-assessment.ttl has TestEvent/TEMetric/AssessmentMilestone but needs explicit TEMP structure.
4. **Data owner / data originator** -- Identify who owns and originated each data element. Partially covered by PROV-O. Cross-model zero-overlap finding is evidence of ownership silos. Maps to Arc 2 + D1.

### 4D Assessment Ontology Scoped for GI-JOE

- **Decision:** GI-JOE builds, Roadmapping Hive stores (canonical deployment location)
- Formalizes WRT-2516 Ch 8: D1 Evidence Quality, D2 System Readiness (GRL), D3 Governance Compliance, D4 Product/Process Quality
- ~35-40 OWL classes, BFO-aligned, following GI-JOE patterns
- Incorporates all 4 keynote observations (antiquated policies, tool-agnostic, TEMP, data provenance)
- TEMP as separate reusable ontology (`temp.ttl`)
- Companion: SHACL shapes, ABox (framework individuals + NNSA tailoring), 12 SPARQL CQs
- Source data: 5 YAML configs already in Roadmapping Hive (`config/`)
- Plan written to GI-JOE: `docs/PLAN_4D_Assessment_Ontology.md`
- Estimated effort: 5-7 hours

## Open Items (Updated)
1. **Joe adds ontologies/SPARQL to IGNITE repo** -- His task; RL ontologies in GI-JOE available for reference
2. **Branch merge** -- `idsk-enterprise-sim` needs merge with updated `main`
3. **Arc 2 and Arc 3 continued work** -- Paul's primary task
4. **Grounded synthetic data** -- Calibrate Arc 2/3 values based on cross-model findings
5. **IDSK decomposition** -- Populate with real measure/requirement data
6. **Cameo XMI export question** -- RESOLVED. All 10 XMI exports complete. Zero cross-model overlap confirmed. Ready to commit analysis.
7. **Presentation deck** -- Still needed
8. **SPARQL query support** -- Help Hunter/Carter/Joe define queries
9. **4D Assessment Ontology** -- GI-JOE builds, deploys to Roadmapping Hive. Plan at `GI-JOE/docs/PLAN_4D_Assessment_Ontology.md`
10. **Berserker SFR XMI** -- RESOLVED. 936 trace links found, all internal. Zero cross-model block overlap confirmed.
11. **Commit XMI analysis** -- Students done; `_xmi_full_analysis.json` ready to commit to IGNITE repo
