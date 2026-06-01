# Session Archive: 2026-03-23 PostWach-01

## Session Metadata
- **Date:** 2026-03-23
- **Hive:** PostWach
- **Researcher:** Paul Wach
- **Model:** claude-opus-4-6 (1M context)
- **Duration:** ~4 hours
- **Focus:** AI Circuit Breaker inventory, Jeffrey's contributions review, DARPA CLARA proposal restructuring, sigma vs. Sa metric analysis, Z_real/isomorphism debate, terminology framework, approximate morphism extension path

## Objectives
1. Warm up ruflo; inventory the AI Circuit Breaker topic ahead of meeting with Jeffrey (Mar 24)
2. Ingest and review Jeffrey's two new documents (ECG TDD v2.0, ECG Signal Architecture presentation)
3. Ingest Paul's notes from `98 Proposal Phase/AI Circuit Breaker Notes.docx`
4. Restructure proposal phasing: drop telecom, ECG-only across both phases
5. Research and resolve the sigma vs. Sa terminology/metric conflict
6. Debate what Z_real means in ECG domain; whether isomorphism is the right starting point
7. Resolve terminology: "degradation" vs. "divergence" vs. "fidelity" vs. "quality"
8. Determine path for extending sigma to approximate/partial/continuous morphisms
9. Correct citation: degree of homomorphism originated at CSER 2025, not ASME IDETC 2024

## Key Decisions
1. **Telecom dropped.** Jeffrey and Paul agreed not to target telecom industry. ECG is the sole domain for both Phase 1 and Phase 2.
2. **Phase structure:** Phase 1 (15 months) = prove composition theorem on narrow ECG scope (1 task, 1 ML kind). Phase 2 (9 months) = deepen ECG (second ML kind, full pipeline, domain-transfer analysis).
3. **Sigma vs. Sa verdict:** Keep both metrics with clearly differentiated roles. Rename Jeffrey's Sa to D_align. They are fundamentally different mathematical objects (set-theoretic vs. geometric) measuring different failure modes (structural conflation vs. operational divergence).
4. **Three-axis framework proposed:** Structural (sigma, design-time), Behavioral (D, runtime), Alignment (D_align, runtime). More novel than two-axis for DARPA.
5. **v3 design spec claim "Sa approximates 1 - sigma" must be retracted or heavily qualified** before DARPA submission. Not mathematically defensible.

## Artifacts Created/Modified

### Files Copied to Project
- `Papers/AI_Circuit_Breaker/ECG_Technical_Design_with_AI_Circuit_Breaker_TDD_v2.0.pdf` (from Downloads)
- `Papers/AI_Circuit_Breaker/ECG_Signal_Architecture_Presentation.pdf` (from Downloads)
- `Papers/AI_Circuit_Breaker/AI_Circuit_Breaker_Notes_Paul.docx` (from 98 Proposal Phase)

### Files Modified
- `Papers/AI_Circuit_Breaker/proposals/01_darpa_clara/clara_proposal_outline.md` -- removed telecom, restructured Phase 1/Phase 2, updated Jeffrey's role, updated TODO items
- `Papers/AI_Circuit_Breaker/proposals/shared/module_d_testbed.md` -- complete rewrite for ECG-only (was telecom-primary)
- `memory/circuit-breaker-details.md` -- added Jeffrey's contributions inventory, terminology reconciliation table, Paul's architecture notes

### Files Not Yet Updated (deferred)
- `Papers/AI_Circuit_Breaker/proposals/shared/module_e_timeline.md` -- still has old telecom phasing
- `Papers/AI_Circuit_Breaker/proposals/shared/module_a_technical_core.md` -- telecom ABox reference needs removal
- `Papers/AI_Circuit_Breaker/proposals/shared/module_b_positioning.md` -- minor telecom audience reference

## Research: Sigma vs. Sa Analysis (3 agents)

### Agent 1: Cosine Distance in AI (cosine-research)
- Cosine distance is the standard embedding similarity metric, widely used for anomaly detection and guardrails
- The Sa formula is a standard pattern in the literature (validated)
- Found that the v3 claim "Sa approximates 1 - sigma" is not defensible without five restrictive conditions
- Suggested Sa may measure a third axis (proximity to valid state space) rather than approximating sigma
- Found Similarity Algebra paper (arXiv 2602.14075, Feb 2026) as potential formalization bridge
- Key external sources: arXiv 2403.05440 (gauge freedom), arXiv 2602.14259 (hallucination cluster geometry), arXiv 2602.14075 (similarity algebra)

### Agent 2: Sigma Homomorphism Metric (sigma-research)
- Sigma = 1 / HarmonicMean(fiber sizes) -- clean characterization
- Bounded: sigma in (0, 1]; sigma = 1.0 iff bijective
- Composition: sigma(h2 o h1) <= sigma(h1) whenever h2 is proper surjection
- Not multiplicatively composable, but always degrades or maintains under composition
- More sensitive to non-uniform lumping (counterintuitive: non-uniform yields higher sigma)
- Related to but distinct from: bisimulation distances, enriched category morphism strengths, mutual information ratios, partition refinement measures
- Fundamental incompatibility with cosine similarity confirmed: different mathematical categories (set-theoretic vs. geometric)

### Agent 3: Debate Agent (debate-agent)
- Recommendation: **(c) Keep both with clearly differentiated roles**
- Sigma: design-time/verification-time, provides composition theorem (DARPA's key requirement)
- Sa (renamed): runtime monitoring, per-inference circuit breaker trigger
- Failure modes are orthogonal: sigma catches structural conflation, Sa catches operational divergence
- Sa does NOT compose (cosine distance not subadditive under function composition) -- critical gap if used as sole metric
- Naming: rename Jeffrey's Sa to D_align or delta_a to eliminate collision with published sigma

## Consolidated Terminology Recommendation

| Layer | Metric | Role | Source |
|-------|--------|------|--------|
| Design-time | **sigma** | Structural fidelity; composition theorem | Paul (IDETC 2024) |
| Design-time | **D** | Behavioral output distance | Paul (CSER 2026) |
| Runtime | **D_align** (was Sa) | Per-inference cosine divergence; CB trigger | Jeffrey (TDD v2.0), renamed |
| Runtime | **CRI** | Context/sensor quality | Jeffrey (TDD v2.0) |
| Longitudinal | **MTBH** | Morphism failure rate | Shared |
| Longitudinal | **VDC** | Drift detection | Jeffrey (TDD v2.0) |
| Operational | **ASAR** | Physician adoption rate | Jeffrey (TDD v2.0), dashboard only |

## Research: Z_real, Isomorphism, and Terminology (3 agents, round 2)

### Agent 4: Z_real in ECG Domain (z-real-debate)
- **No isomorphic starting point exists in ECG.** The chain (heart -> electrode -> ADC -> filter -> features -> classification) is a cascade of lossy homomorphisms. h1 (cardiac state to surface ECG) is physically ill-posed (Helmholtz/Geselowitz); sigma(h1) < 1.0 by the laws of electrophysics.
- Z_real candidates all have problems: patient's cardiac state (unobservable), electrode signal (already degraded), expert annotations (noisy, 10-15% inter-reader disagreement), AHA/ACC guidelines (normative, not observed).
- **The framework applies as chain composition, not point degradation.** The composition theorem (sigma_total <= min(sigma_i)) tells you the weakest link bounds the system. Engineering-useful.
- Sigma at classification level is trivial/circular: 5 AAMI states in, 5 out = sigma 1.0 regardless of accuracy. Framework applies better at the representation level or across the full chain.
- Recommended reframe: "The Circuit Breaker monitors morphism quality of the ECG measurement-to-classification chain."

### Agent 5: Morphism Chain Analysis (morphism-chain-debate)
- Detailed per-link assessment: h1 (sigma < 1.0 by physics), h2 (~0.95-0.99, Nyquist), h3 (~0.85-0.95, filter design), h4 (very low raw, high task-conditional), h5 (very low by design, D is the useful metric)
- D composition (D_total <= sum(D_i)) matches engineering practice: main errors from h4 and h5
- Circuit breaker placement: should support hierarchical breakers (chain-level + stage-level)
- Reference isomorphism must be staged: each h_i has its own reference, not one global Z_real
- Four extensions needed: (1) continuous state space sigma, (2) task-conditional weighting, (3) uncertainty composition via GUM, (4) staged reference concept
- GUM + Wymore composition is the bridge: sigma provides the structural axis GUM lacks; GUM provides the uncertainty machinery sigma lacks

### Agent 6: Terminology Analysis (terminology-debate)
- **"Degradation"** presupposes a prior better state; fine for isomorphism library (mass-spring/RLC), wrong for ECG/CLARA
- **"Divergence"** collides with KL divergence, is symmetric (morphisms are directional), connotes unboundedness. Avoid.
- **"Isomorphic degradation"** has grammatical ambiguity: "degradation that is isomorphic" vs. "degradation of isomorphism"
- **Recommendation: Option C -- "Morphism Quality"** with **"Structural Fidelity"** (sigma) and **"Behavioral Distance"** (D)
- "Fidelity" is native to signal processing and metrology; no collisions across SE, DARPA, biomedical, or publications
- For CLARA/Circuit Breaker line: use "morphism quality." For isomorphism library papers: keep "isomorphic degradation" (it's accurate there).

## Key Decisions (continued from round 2)

6. **Citation corrected.** Degree of homomorphism originated at CSER 2025, NOT ASME IDETC 2024. Fixed in proposal outline, shared modules, and memory.
7. **D_h = (D_s, D_b) is a vector, not a scalar.** D_h = homomorphic distance (umbrella). D_s = 1 - sigma (structural distance). D_b = max_t |y1(t) - y2(t)| (behavioral distance). d_cos = 1 - cos(I, N_o) (cosine distance, runtime instrument, standard literature notation).
8. **Sigma is NOT design-time only.** Computable at runtime for discrete classifiable state spaces (AAMI categories, ontology-defined states). "Design-time only" was an oversimplification driven by continuous state space difficulty.
9. **D_s in [0,1] assumes exact surjective homomorphism.** Non-surjective, partial, or approximate morphisms break this bound. Three-layer extension path identified:
   - Layer 1 (exact): Original sigma. For CSER 2025/2026.
   - Layer 2 (coverage): (coverage, sigma_covered) pair. Approach C. Handles blind spots.
   - Layer 3 (continuous): I(X;Y)/H(X) mutual information ratio. For DARPA CLARA, AI/ML systems.
   - T3SD/DEVS analogy: exact sigma is T3SD (clean, tractable), MI ratio is DEVS (more expressive). Exact embeds ordinally into MI framework.
10. **For CSER 2026 (this week/next week):** Keep exact sigma. Add Approach C (coverage + sigma_covered) as brief remark. Future work paragraph on MI ratio generalization. Do NOT introduce MI ratio in this paper.
11. **For DARPA CLARA:** One paragraph acknowledging the gap and naming MI ratio as Phase 2 extension. Phase 1 uses exact formulation on discrete clinical categories.
12. **ECG ontology does not exist yet.** No published OWL cardiac electrophysiology ontology with SHACL shapes. Must be built as part of the project (months 1-4).
13. **"Isomorphic degradation" stays for isomorphism library papers** (mass-spring/RLC have genuine isomorphic starting points). "Morphism quality" for CLARA/Circuit Breaker line only.

## Files Modified (round 2)
- `proposals/01_darpa_clara/clara_proposal_outline.md` -- corrected IDETC 2024 -> CSER 2025 citation
- `proposals/shared/module_a_technical_core.md` -- corrected IDETC 2024 -> CSER 2025
- `proposals/shared/module_c_pi_and_related_work.md` -- corrected IDETC 2024 -> CSER 2025
- `memory/MEMORY.md` -- updated SE Math Foundations section with CSER 2025 origin, notation lineage, CSER 2026 revision items

## Open Items for Jeffrey Meeting (Mar 24)
1. Present terminology reconciliation; get buy-in on d_cos naming for his Sa formula
2. Present D_h = (D_s, D_b) vector framework
3. Settle ML architecture (Transformer vs. RF, or both with different roles)
4. Settle technology stack (Jena/ProbLog2 vs. GraphDB/Metaphactory)
5. Divide proposal writing responsibilities
6. Send Jeffrey DARPA/NSF/NIH framing expectations (per Paul's notes)
7. UA Sponsored Projects -- has OT review been initiated?
8. BAA portal registration status

## Paul's Architecture Notes (from docx)
- DEVS-based MCP, WySE MCP -- consistent context scaffolding via ontology
- Knowledge engineering must account for lifecycles
- "Let the data talk to the data, translation to humans occurs along the way"
- Research question: "How do we create coordinated immune systems?"

## Agent Summary (9 agents total this session)
1. cosine-research -- cosine distance in AI literature
2. sigma-research -- degree of homomorphism deep analysis
3. debate-agent -- Sa vs. sigma keep/drop/rename
4. z-real-debate -- what is Z_real in ECG, is isomorphism the right starting point
5. morphism-chain-debate -- ECG chain as morphism composition h1-h5
6. terminology-debate -- degradation vs. divergence vs. fidelity vs. quality
7. dh-debate -- D_h naming convention evaluation
8. approx-morphism-debate -- three approaches to extending sigma for approximate morphisms
