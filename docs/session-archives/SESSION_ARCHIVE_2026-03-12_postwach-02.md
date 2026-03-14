# Session Archive: 2026-03-12 PostWach-02

**Date:** Thursday, 2026-03-12
**Hive:** PostWach (CTO)
**Duration:** ~2.5 hours (recovery + synthesis + planning)

## Context

Recovery session for a lost ~1.5 hour conversation from 2026-03-11 (~5:30 PM) that produced no persistent artifacts. That session scoped IGNITE '26 hackathon participation with multiple story arcs. Session expanded into full IGNITE planning and WRT-2516 deliverable strategy.

## Objectives
1. Recover lost session context via git history, session archives, and memory
2. Complete review of WRT-2406 Final Technical Report (pages 63-91)
3. Synthesize findings into story arc options for IGNITE '26
4. Debate structure and decide direction

## Accomplishments

### WRT-2406 Review Completed (Full 91 Pages)
- **Section 4.4 (V&V Planning):** BertScore, MAUVE, SynEngBench for LLM output validation; two-step V&V (internal + sponsor environment)
- **Section 4.5 (Sandbox Planning):** Safe experimentation environment reflecting sponsor's org and data architecture; technology maturation framework for readiness assessment
- **Section 4.6 (Governance, Security, Cyber Resilience):** Calls for governance as foundational (not peripheral), zero-trust, secure-by-design, data provenance policies across contractors/labs/operators
- **References:** 188 citations spanning DE strategy, sociotechnical barriers, AI/ML, SysML, workforce
- **Appendix C:** 29 DE capabilities across 4 categories (Admin LM x4, Engineering LM x14, DE Tech x5, Next Gen x6). Key capabilities for IGNITE: #11 (Org Knowledge Infusion), #23 (Parts Classification), #27 (Supply Chain Collaboration)
- **Appendix D:** Requirements capability challenges (limited HW-SE data, annotation needs, V&V balancing, adoption, hybrid model recommendation)
- **Appendix E:** Workforce gap analysis (DECF, DCWF, DAU mapping; 392-engineer quantitative study; RE competency gaps in AI context)
- **Publications:** Nerayo & Wach (CSER 2025, Fit-for-Transformation), Jurczyk et al. (CESUN 2025, Barriers), Jurczyk et al. (Hume 2025, Optimized DE)

### Sponsor Specific Recommendations (A01) Reviewed
- 5 key recommendations: (1) Agentic AI Pathfinder for RE, (2) Secure Interoperable Digital Ecosystem, (3) Governance/Security/Cyber Resilience from Outset, (4) Success Metrics, (5) Workforce Development
- 3-level requirements development pathway (Figure 1: System, Subsystem, Component)
- Near/Mid/Long-term development roadmap for agentic AI solutions

### IGNITE '26 Story Arc Synthesis

**Arc 1 (DTE&A) — BUILT.** Berserker MQ-99 dashboard (6 pages, ontology, morphisms, SPARQL). Demonstrates single-system success.

**Arc 2 (Conway's Law / Organizational Barriers):** Diagnosed from WRT-2406 empirical evidence:
- 49 sociotechnical barriers, 6 dimensions, Culture/People dominant
- M&O contractor model: 8 independent contractors, fee-at-risk competition, data silos
- Data sharing barriers: proprietary claims, CUI over-marking, mosaic effect
- Conway's Law: org structure mirrors (and constrains) system architecture
- Solution direction: federated ontology (shared TBox, local ABox, federated SPARQL)

**Arc 3 (Transformation Achievement — EMERGING):** User identified that Arc 1 + Arc 2 are stepping stones to Arc 3, which addresses how to actually achieve the transformation. Connects to:
- WRT-2516 v2 roadmap assessment framework (4-dimensional: D1 Evidence Quality, D2 System Readiness/GRL, D3 Governance Compliance, D4 Product/Process Quality). NOTE: These are Ch 8's operational dimensions. The companion paper taxonomy (Ch 5) uses C1-C4 for a different categorization scheme.
- GRL (Generic Readiness Level) as the readiness measurement backbone
- Technology assessment tooling as part of the demonstration
- The prescription (Conway's Inverse): use system architecture to reshape organizational behavior

Three options debated for Arc 2: (A) Diagnose the Disease, (B) Federated Interoperability, (C) Prescription via Conway's Inverse. User leaned toward C but expanded to Arc 3 as the ultimate goal.

## Team Logistics (Recovered from Lost Session)
- **Violet Labs:** Minimal to no live participation at IGNITE week (Mar 16-19). Asked for deliverables ASAP for upfront work on their end.
- **Brad Philipbar / RTSync:** Time TBD. Likely upfront work contributor. Brad's repos were inventoried in the lost session.
- **Joe Gregory:** Ontology technical lead (UAOS)
- **Paul Wach:** Captain / Chief Engineer

## Decisions
- **3-arc structure confirmed:** Arc 1 (DTE&A demo) + Arc 2 (Conway's Law diagnosis) + Arc 3 (Transformation achievement with assessment tooling)
- **Connect to WRT-2516:** IGNITE work feeds back into WRT-2516 v2 deliverables and project work
- **Priority:** Get deliverables to Violet Labs ASAP; scope Brad's contribution from repo inventory

## Corrections Applied

- **Date correction:** Today is THURSDAY March 12, not Wednesday. IGNITE starts Monday Mar 16 (4 calendar days).
- **4D model correction:** WRT-2516 assessment framework is 4-dimensional, not 3D. The 4D PDF exists at `WRT-2516_v2/Transformation_Roadmap_Framework_4D_v2.pdf`. Dimensions: D1 Evidence Quality, D2 System Readiness (GRL), D3 Governance Compliance, D4 Product/Process Quality (ISO 25000 SQuaRE). Six gap types: 3 structural (vertical, horizontal, feasibility) + 3 dimensional. "Conceptual quicksand" finding: binding constraint is absence of scientific/mathematical foundations. NOTE: Ch 5 taxonomy constructs (C1-C4) are a different scheme, resolved in session 03.

## Brad/RTSync Repo Inventory (bmpwach-lab GitHub org)

33 repos found under `bmpwach-lab` GitHub organization. Key repos for IGNITE:

1. **E2E_DEVS_SWARM_DEM-S** -- End-to-End DEVS-Swarm Distributed Engineering Modeling & Simulation. C++ DEVS engine, Cameo EA integration, Kill Web visualization. 3,063 files, ~68MB. Architecture: DEVS core (C++20) + Cesium/Unreal visualization + Hive-Mind AI Swarms + JLVC interop.
2. **MBSE_Agentic_Plugin** -- Java plugin for Cameo EA: 97 Java source files, activity/sequence diagram generation, Claude API integration, DEVS bridge (RTSyncDEVSBridge.java, HomomorphismVerifier.java, SysMLToDEVSTransformer.java). 330MB with models.
3. **MBSE_Agentic_Plugin_CEA26xSysMLV2** -- Cameo EA 2026x plugin for native SysML V2 model generation via KerML/EMF. Multi-provider AI (Claude, Gemini, GPT-4o). Real-time bi-directional coupling.
4. **V1toV2** -- Python automated converter: NAVSEM SysML v1.5 MagicDraw to SysML v2 textual notation. 458 elements, 30 activity diagrams, 309 control flows. 100% V&V pass rate. Author: Brad Philipbar, model by Paul Wach.
5. **Agentic-DEVS-SWARM** -- C++20 DEVS simulation platform for military wargaming. 954 passing tests, 97% architecture aligned. HAF WarMatrix RFI response. 1,473,867x speedup claimed.
6. **DEVS_Swarm_CESIUM_DEMO** -- INCOSE 2026 paper: DEVS-based agentic AI swarm orchestration with SES of Queens formalism.
7. **CFD_FEM_HIVE** -- Hierarchical queen multi-agent for CFD/FEM simulation with Byzantine consensus.
8. **AgentCyberWargame** -- CULEX 2026 educational cyber defense wargame.
9. **VIRTUAL_MDO_DEVS_SWARM** -- UE5 + Cesium visualization for DEVS-Swarm sUAS/cUAS simulation.
10. **AdvancedMathematicsForAgenticSwarms** -- The 163pp paper Paul previously reviewed.

Other notable repos: RTSyncCorpMarketing, JCO_BlueStaq (ParaDEVS sales capture), MORS_94th submission, DOD_AI_GAPS_WP (3-article series), AI_API_TokenUsageResearch, agent-infra (220+ skills, 98 agents).

## DEF Materials Found

Located at `C:\Users\pfwac\OneDrive - University of Arizona\Documents\04 Resource Library\DEF Materials\`. Contains conference materials across 2023-2025 (CESUN, CSER, GPDIS, AIAA SciTech, ASEE, IAC, IEEE Aerospace, INCOSE IS, Integrate, LEAD, OntoNexus, SECESA, Stratdec, Zuken IW), plus Demos/ (3 .mkv/.mp4 files) and Journal Articles/.

## Strategic Reframing

User clarified that IGNITE is a forcing function, not the product:
- **Primary:** WRT-2516 assessment framework software tool. First iteration due Apr 15, second Sep 15.
- **INCOSE interest:** INCOSE has asked to use the assessment framework for their own organization. Tool must be domain-agnostic.
- **IGNITE:** Forcing function to build v0.1 prototype of the April 15 deliverable.

## Remaining Work (Revised)
- Extract 4D framework data model from WRT-2516 LaTeX into YAML schema
- Build assessment framework as reusable software (not throwaway demo code)
- Contact Brad re: which bmpwach-lab repos to integrate for IGNITE
- Contact Violet Labs with deliverable specs for upfront work
- Presentation deck and demo script for 3-arc narrative
- Repository decision: standalone repo for assessment framework (recommended, since INCOSE is also a customer)

## Build Initiated and Completed (Thu Mar 12)

### Transformation-Roadmapping-Hive Created and Pushed
- **Repo:** https://github.com/DocWach/Transformation-Roadmapping-Hive
- **Local clone:** `03 Projects/08 Transformation-Roadmapping/`
- **Purpose:** WRT-2516 assessment framework software tool (v0.1 due Apr 15, v0.2 due Sep 15)
- **Also serves:** INCOSE (domain-agnostic, pluggable tailoring sets)
- **IGNITE role:** Arc 3 demonstration is the v0.1 prototype of this tool
- **Commits:** `305a806` (engine + configs + tests), `cd10e67` (.gitignore cleanup)

### Build Completed — All Tasks Done
1. **4D framework extraction (DONE):** 5 YAML configs extracted from WRT-2516 LaTeX, Python assessment engine built, 50 tests passing
2. **IGNITE execution plan (DONE):** `docs/IGNITE_EXECUTION_PLAN.md` committed and pushed (commit `0c4c662`)
3. **Session archive (DONE):** This file

### Artifacts Created

**Config (YAML framework definitions):**
- `config/dimensions.yaml` — 4D dimension definitions (D1 Evidence Quality 9-category scale, D2 GRL Readiness, D3 Governance Compliance plug-in, D4 Product/Process Quality ISO 25000 SQuaRE profile)
- `config/grl.yaml` — GRL 9-level scale, 6 core threads (T,P,I,H,O,K), 3 extended threads, 3 phases, composite measures
- `config/gap_types.yaml` — 6 gap types (3 structural + 3 dimensional) with formulas, thresholds, diagnostic patterns
- `config/tailoring/generic.yaml` — Generic tailoring set (4 governance domains)
- `config/tailoring/nnsa.yaml` — NNSA tailoring set (5 governance domains inc. 7-pillar Zero Trust, evidence thresholds by criticality, decision gate mapping, D2 adaptations)

**Python (assessment engine):**
- `src/assessment/models.py` — 15 data classes: EvidenceCategory (IntEnum 0-8), Phase, GRLLevel, Thread, Dimension, DimensionRating, Capability, AssessmentScore (4D vector), Gap, BindingConstraint, GovernanceDomain, TailoringSet, Assessment, GapType
- `src/assessment/engine.py` — AssessmentEngine class: bottleneck readiness, phase characterization, vertical/horizontal/feasibility gap detection, 3 dimensional gap types, evidence threshold checks, binding constraint identification, full pipeline (`run_assessment()`)
- `src/assessment/config_loader.py` — YAML config loading into dataclasses
- `tests/test_engine.py` — 50 unit tests (config loading, GRL, all gap types, binding constraints, evidence thresholds, ordinal validity)
- `CLAUDE.md` — Hive governance [T001-T010]

**IGNITE:**
- `05 IGNITE/IGNITE_Disruption_2026/docs/IGNITE_EXECUTION_PLAN.md` — 3-arc demo structure, build schedule, team assignments, demo narrative

### Key Design Decisions
- **Dimension numbering follows Ch 8/11 formal model** (D1=Evidence Quality, D2=Readiness, D3=Compliance, D4=Quality), not Ch 5 construct presentation order (D1=Product Readiness, D2=Org Process Capability, D3=Practice Adoption, D4=Evidence Quality). This is a document inconsistency in WRT-2516 v2 that needs resolution.
- **Ordinal-valid only:** min, max, median used for aggregation. No arithmetic means on ordinal data (Kujawski/Stevens critique).
- **Domain-agnostic core:** NNSA is a tailoring set YAML file, not built into the engine. INCOSE or any organization adds a new YAML.
- **SEAD hive evaluated for reuse:** SEAD is TypeScript/Node.js with no Python/Streamlit. Architectural patterns (orchestrator, task routing) are conceptually useful but no code to reuse directly. Real reusable Streamlit asset is the IGNITE Berserker dashboard (Arc 1).

### Remaining Work
- Build Arc 2 Streamlit page (Conway's Law visualization)
- Build Arc 3 Streamlit UI (assessment framework frontend)
- Contact Brad re: which bmpwach-lab repos to integrate
- Contact Violet Labs with deliverable specs
- Presentation deck and demo script
- ~~Resolve WRT-2516 dimension numbering inconsistency (Ch 5 vs Ch 8/11)~~ RESOLVED 2026-03-12 session 03

---

## Session 03 Continuation (2026-03-12)

### WRT-2516 Dimension Numbering -- RESOLVED

Root cause: Ch 5 uses the companion paper's taxonomy labels (originally D1-D4, now relabeled C1-C4 for Constructs). Ch 8 defines the report's operational assessment dimensions (D1-D4). The two schemes are related but not identical.

**Fix applied across 4 files:**
- `ch05_taxonomy.tex` -- All D1-D4 relabeled to C1-C4 throughout Sections 5.2, 5.3, 5.4, 5.5. Added header comment and Remark box explaining the convention. Reconciliation table (Section 5.4) rewritten with explicit "neither one-to-one nor onto" mapping.
- `ch08_three_dimensional.tex` -- Added protective header comment defining D1-D4 and distinguishing from C1-C4.
- `app_c_literature.tex` -- Fixed two stale "three-dimensional" references to "four-dimensional."
- `ch11_full_assessment.tex` -- Verified, no changes needed (all D1/D2/D4 references already correct).

**PDF recompiled:** `Transformation_Roadmap_Framework_4D_v2.pdf` (179 pages). Naming convention established: never use generic names like `main.pdf`.

**Memory files corrected:**
- `memory/ignite-2026-scoping.md` line 27 -- fixed from wrong Ch 5 labels to correct Ch 8 labels
- `memory/nnsa-details.md` lines 21-24 -- fixed, added NOTE about C1-C4 vs D1-D4 distinction

### IGNITE Execution Plan -- Stale Labels Fixed

`IGNITE_EXECUTION_PLAN.md` line 22 had stale Ch 5 taxonomy labels. Corrected to Ch 8 operational dimensions: D1 Evidence Quality x D2 System Readiness (GRL) x D3 Governance Compliance x D4 Product/Process Quality.

### Arc 2 -- Federal Program Office Note Added

For DoD audiences, Arc 2's organizational topology needs to translate NNSA M&O contractor structure to DoD equivalents: System Program Offices (SPOs), PEO hierarchy, Prime/subcontractor relationships. Noted as iterative update in execution plan.

### Repository Updates
- **IGNITE README** updated: 3-arc structure, corrected dimension labels, expanded architecture diagram, added Arc 2/3 components
- **Transformation-Roadmapping README** created: 4D framework, gap analysis, domain tailoring, quick start, design decisions, related links

### Remaining Work (Updated)
- ~~Build Arc 2 Streamlit page (Conway's Law visualization)~~ DONE session 03
  - Include Federal program office / SPO / PEO hierarchy translation for DoD context (iterative, future)
- ~~Build Arc 3 Streamlit UI (assessment framework frontend)~~ DONE session 03
- ~~Wire Berserker as Arc 3 worked example~~ DONE session 03 (7 capabilities, 14 gaps, binding constraints)
- Contact Brad re: which bmpwach-lab repos to integrate
- Contact Violet Labs with deliverable specs
- Presentation deck and demo script

---

## Session 03 Build Phase (2026-03-12, evening)

### Arc 2 + Arc 3 Built and Pushed

**Arc 2: Conway's Law** (`src/pages/arc2_conway.py`)
- M&O contractor network topology (8 nodes, sparse edges, color-coded by type)
- WRT-2406 barrier classification (49 barriers, 6 dimensions, horizontal bar + sunburst)
- Conway's Law Sankey diagram (org factors to architectural consequences)
- Data sharing barrier cards (proprietary claims, CUI over-marking, mosaic effect, classification culture)
- Conway's Inverse solution callout pointing to Arc 3
- DoD SPO/PEO translation note included

**Arc 3: 4D Assessment** (`src/pages/arc3_assessment.py`)
- Tab 1 (Berserker Demo): 7 subsystem capabilities with realistic 4D ratings, grouped bar chart, GRL radar charts, gap analysis table (14 gaps: 2 horizontal, 7 quality-compliance, 1 quality-readiness, 4 evidence threshold), top 5 binding constraints
- Tab 2 (Interactive): Capability builder with sliders, session state persistence, tailoring set selector, live assessment
- Tab 3 (Framework Reference): 4D model cards, evidence categories, GRL levels, threads, gap type formulas (all loaded from YAML configs)

**App integration** (`src/app.py`): Arc selector in sidebar, `st.stop()` dispatch pattern. Arc 1 unchanged.

**Verification:** Python import check passed, syntax check passed, engine integration test passed (7 caps, 14 gaps, binding constraints correct).

**Commits pushed:**
- Transformation-Roadmapping-Hive: `1420811` (README with 4D docs and usage examples)
- IGNITE_Disruption_2026: `f99bb87` (Arc 2 + Arc 3 pages, app routing, README rewrite, execution plan fixes)

### READMEs Finalized
- **IGNITE README** rewritten: leads with 3-arc narrative, correct file structure with `src/pages/`, dependencies, strategic context
- **Transformation-Roadmapping README** expanded: fixed Quick Start (correct API: `load_tailoring_set` not `load_all_configs`), added working code example with Capability/DimensionRating construction

### Feedback Captured
- **PDF naming convention:** Never use generic names like `main.pdf`. Use descriptive names (e.g., `Transformation_Roadmap_Framework_4D_v2.pdf`). Saved to `memory/feedback_pdf_naming.md`.

### Next Session Priorities (noted by user)
1. ~~**App walkthrough / user manual**~~ DONE session 04
2. **MBSE traceability** -- IN PROGRESS, scoping debate underway (session 04)
3. ~~**Student roles**~~ DONE session 04
4. Contact Brad re: bmpwach-lab repo integration
5. Contact Violet Labs with deliverable specs
6. Presentation deck and demo script
7. Test-drive the app (user testing during session 04)

---

## Session 04 (2026-03-13, morning)

### App Walkthrough Created
- `docs/APP_WALKTHROUGH.md` -- Full user manual: setup, sidebar nav, all 3 arcs page-by-page, 10-12 min demo script with timestamps, "what to avoid" list
- PDF: `docs/IGNITE_2026_App_Walkthrough.pdf` (170 KB, pandoc via pdflatex)

### Student Roles Defined
- `docs/STUDENT_ROLES.md` -- Two complementary roles:
  1. **Assessment Analyst** -- operates Arc 3 on new use cases, creates capability profiles, drives tool live during demos
  2. **Evaluation Researcher and Stakeholder Liaison** -- designs feedback instrument, collects structured attendee data, maps collaboration opportunities
- PDF: `docs/IGNITE_2026_Student_Roles.pdf` (139 KB)
- Three-role structure: captain (depth) + analyst (breadth) + evaluator (evidence)

### MBSE Traceability Scoping -- In Progress
- **Decision:** PostWach scopes, SysMLv2 Hive builds
- **Architecture:** Two-layer model proposed
  - Layer 1: Framework architecture (persistent, grows to April 15+). 4D model as system, requirements from WRT-2516, stakeholder concerns.
  - Layer 2: IGNITE instantiation (current scope, subset of Layer 1). 3-arc demo, Berserker use case, page/tab realizations, data flows.
- **Traceability type debate (unresolved):**
  - A. Requirements to implementation -- classic but we'd be reverse-engineering requirements
  - B. Data flow -- practical, shows what connects to what, critical for deployment
  - C. Artifact dependencies -- overlaps B, build/deployment view
  - D. Feature to test coverage -- gap is real (50 engine tests, 0 UI tests) but won't close before Monday
  - E. Stakeholder concerns to framework dimensions -- intellectual backbone, "why does D1-D4 exist"
  - Current lean: B + E (data flow + stakeholder-to-dimension traceability)
  - **User asked "what's pulling you toward traceability?" -- question unanswered, session paused**

### Remaining Work
- **Resume MBSE traceability scoping** -- answer the "why traceability" question, finalize scope, hand to SysMLv2 Hive
- Test-drive app (user was testing during session, no feedback reported yet)
- Contact Brad + Violet Labs
- Presentation deck and demo script

---

## Session 05 (2026-03-13, continued)

### Context Continuation -- Immediate Archive

Session resumed after context compression. No substantive work performed; user requested immediate archive. Status summary provided and confirmed.

### Open Items (3 Days to IGNITE)
1. **App test-drive feedback** -- user has not yet reported results
2. **IGNITE streams list** -- user to provide full 6-7 streams (DTE&A, DOT&E, TMRC, Cyber Resilience + others)
3. **MBSE traceability scoping** -- paused at "why traceability" and streams/hive mapping
4. **Hive-of-hives cross-stream mapping** -- MACQ, PLM, Fort Wachs, GI-JOE capabilities to IGNITE streams
5. **Presentation deck and demo script**
6. **Contact Brad (RTSync) and Violet Labs**

---

## Session 06 (2026-03-13, afternoon)

### Arc Redesign Debate -- Major Conceptual Shift

User test-drove the app. Arc 1 confirmed as strong. Arcs 2 and 3 flagged as "very unclear how they will be used."

**User's revised vision for Arc 2:** Not a static infographic but an **enterprise decision simulation**. Core idea: take Arc 1's data, then degrade it by organizational constraints (contractor silos, document-only formats, classification barriers, CUI/mosaic, decision-maker ignorance of data existence). Show how decision quality collapses even when the data technically exists. Connects to the Mirroring Hypothesis (Conway's Law formalized): organizational structure constrains data flow constrains decision quality.

**Key insight from user:** 4D assessment scores change depending on who can see what. A capability might score D1=6 from the contractor's view but D1=2 from the government decision-maker's view. The data hasn't changed, only the accessibility.

**Arc 2 ↔ Arc 3 iteration proposed by user:** Arc 3 (4D assessment) could feed back into Arc 2, showing alternative outcomes after assessment. User questioned whether Arc 3 should come first, or whether there should be an iterative loop.

**Four approaches debated:**
- **A (Linear, current):** Arc 1→2→3. Arc 2 gets sliders for data sharing. Con: no feedback loop.
- **B (Reorder):** Arc 1→3→2. Assess under perfect info, then degrade. Con: ends on the problem, not the solution.
- **C (Iterative Loop):** Arc 1→Arc 2↔Arc 3. Set constraints in Arc 2, see assessment in Arc 3, change constraints, re-assess. Demonstrates Conway's Inverse live. Recommended by Claude.
- **D (Unified):** Merge Arc 2+3 into single simulation page. Con: loses pedagogical separation.

**Recommendation pending user review:** Approach C with scenario selector. Requires a degradation model (data sharing configuration → 4D score modifications) and shared session state between Arc 2 and Arc 3.

### IDSK Integration Flagged

User noted Arc 1 needs to reflect the Integrated Decision Support Key (IDSK) from DoDI 5000.89. Not yet researched. Need to locate document in background docs or online.

### Integration Architecture Discussed

Reviewed how ontology connects to app (rdflib in-memory graph, live SPARQL, works directly). Simulation integration with Brad/RTSync is fully stubbed (no API contract, no message format). Three options discussed: file exchange, REST API, shared ontology as RDF triples.

### Remaining Work (Updated)
- ~~User reviewing Approach A-D recommendations~~ DECIDED: Approach C (session 07)
- ~~IDSK research~~ DONE (session 07)
- ~~Degradation model design~~ DONE (session 07)
- **Brad/RTSync integration contract** -- define parameter/result exchange format
- IGNITE streams list (user to provide)
- MBSE traceability scoping (paused)
- Presentation deck and demo script
- Contact Brad + Violet Labs

---

## Session 07 (2026-03-13, evening)

### Approach C Implemented -- IDSK Enterprise Decision Simulation

User selected Approach C (iterative loop). Full implementation completed across 3 files.

**Arc 1 -- IDSK reframe** (`src/app.py`):
- System Overview page now opens with the 5-question IDSK framework from DoDI 5000.89 Section 3.1.d
- Each question mapped to live metrics (triples, subsystems, morphisms, gaps, events)
- Sidebar caption: "Framework: IDSK (DoDI 5000.89)"

**Arc 2 -- Enterprise Decision Simulation** (`src/pages/arc2_conway.py`, complete rewrite ~848 lines):
- 4 preset scenarios: Full Digital Thread (ideal), Federated Ontology (realistic best), Document-Based Sharing (current state), Siloed Operations (worst case)
- Each scenario configures 5 parameters: c2c sharing, c2g sharing, g2g sharing, classification level, AI assist level
- Degradation model: weighted sharing formula (0.4 c2c + 0.35 c2g + 0.25 g2g) with classification penalties and AI boost
- Per-GRL-thread degradation with thread-specific floor/sensitivity: T(0.60/0.7), P(0.50/0.8), I(0.15/1.0), H(0.35/0.5), O(0.10/0.9), K(0.05/0.6)
- 6 visualization sections: scenario config, IDSK impact analysis, org topology, barrier analysis, Sankey, decision quality scorecard
- Stores results in `st.session_state['degradation_factors']` for Arc 3

**Arc 3 -- Degradation Integration** (`src/pages/arc3_assessment.py`):
- `_apply_degradation()`: deep copies capabilities, applies per-dimension factors
- Scenario banner showing name, IDSK coverage, confidence, latency
- Side-by-side comparison bar chart (baseline vs degraded)
- Comparison table with baseline reference columns and delta
- Gap analysis runs on degraded data; additional gap count highlighted
- Binding constraints reframed for enterprise context

**Commits:**
- `acd6244` -- Add IDSK framework + enterprise decision simulation (Approach C)
- `205f742` -- Fix pyarrow dependency + add IDSK enterprise simulation manual

### pyarrow ARM64 Fix

`st.dataframe()` requires pyarrow, which fails to build on ARM64 Windows. Replaced all 16 `st.dataframe()` calls (7 in app.py, 9 in arc3_assessment.py) with `_show_table()` helper using `df.to_html()` + CSS via `st.markdown(unsafe_allow_html=True)`.

### Technical Manual Written

`docs/IDSK_ENTERPRISE_SIM_MANUAL.md` -- Comprehensive 12-section manual documenting every formula, constant, scenario preset, degradation model, and design decision. Includes worked example (Siloed Operations hand calculation), updated demo script, appendices with parameter tables and FAQ.

PDF: `docs/IDSK_Enterprise_Sim_Manual_2026-03-13.pdf` (346 KB)

### User Feedback
- Arc 1 IDSK reframe needs "continued framing" -- tie between System Overview metrics and IDSK questions not yet obvious enough
- Arc 2 scenarios and analysis thread need to be "categorically understood" before demo -- manual addresses this
- Arc 3 with degradation working correctly after pyarrow fix

### Remaining Work (3 Days to IGNITE)
1. **IDSK framing refinement** -- strengthen Arc 1 System Overview to IDSK question mapping
2. **Presentation deck and demo script** -- use manual's demo script as basis
3. **Brad/RTSync integration contract** -- define parameter/result exchange
4. **MBSE traceability scoping** -- paused
5. Contact Brad + Violet Labs
6. IGNITE streams list (user to provide)
