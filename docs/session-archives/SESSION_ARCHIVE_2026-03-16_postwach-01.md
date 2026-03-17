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

## Open Items
1. **Cameo XMI export question** -- Does cross-project traceability exist? Ask Brad or parse proxies.
2. **Arc 0 scoping** -- DE ecosystem page (tools, workflows, V1toV2, Agentic Plugin)
3. **Grounded synthetic data** -- Calibrate Arc 2/3 values based on cross-model findings
4. **IDSK decomposition in Arc 1** -- Populate with real measure/requirement data
5. **Measures catalog** -- Classify 243 measures, identify orphans
6. **Branch management** -- `idsk-enterprise-sim` not yet pushed or merged to main
7. **Presentation deck** -- Still needed
8. **Brad/RTSync integration** -- V1toV2 and Agentic Plugin for Arc 0
