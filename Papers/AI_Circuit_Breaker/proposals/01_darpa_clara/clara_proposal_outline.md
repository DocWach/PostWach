# DARPA CLARA Full Proposal Outline
# "Morphism-Grounded Compositional Assurance for Autonomous AI Systems"

**Solicitation:** DARPA-PA-25-07-02
**Technical Area:** TA1
**PI:** Paul F. Wach, Ph.D. (University of Arizona)
**Deadline:** April 17, 2026, 4:00 PM ET (Amendment 01, Mar 11 2026)
**Submission:** .zip via baa.darpa.mil

---

## Volume 1: Task Description Document

### 1. Executive Summary (1 page)

- One-paragraph problem statement: no compositional assurance theory for AI systems-of-systems
- Core contribution: morphism theory provides a formal, composable, verifiable foundation for AR-based ML
- Key differentiator: trust bounds compose functorially (mathematical theorem, not assumption)
- AR kinds: Description Logic (OWL 2 DL) + Bayesian Logic Programs
- ML kinds: Neural Networks (Transformer-based) [Ph1] + Bayesian methods [Ph2]
- Application domain: AI-enabled medical devices (FDA-regulated ECG classification + clinical alerting), deepening across both phases
- Budget: $1.85M over 24 months

### 2. Technical Approach

#### 2.1 AR-ML Composition Approach (core theoretical contribution)

**2.1.1 The Morphism Composition Theory**
- Formal definition: every AI component as Wymore five-tuple Z = (S, I, O, N, R)
- Morphism h: Z_ai -> Z_real as the formal object connecting ML representations to reality
- Homomorphic distance D_h = (D_s, D_b): a vector characterizing distance from isomorphism along two orthogonal axes
  - D_s = 1 - sigma (structural distance): how far the mapping is from bijective [22]
  - D_b = max_t |y_ai(t) - y_real(t)| (behavioral distance): how far outputs deviate
  - D_h = (0, 0) is the isomorphic ideal
- Composition theorem: D_s_total >= max(D_s_i), D_b_total <= sum(D_b_i)
- The morphism chain: in observation-mediated systems (e.g., ECG), information flows through a chain of morphisms (sensor -> digitization -> processing -> feature extraction -> classification), each with its own D_h. The composition theorem identifies the bottleneck.
- Proof sketch for the composition theorem (functorial property)
- Why this is not just monitoring: morphism constraints define the valid space in which ML operates
- Scope: D_s assumes discrete enumerable state spaces with exact surjective homomorphisms. For continuous/approximate cases, D_s generalizes to the mutual information ratio (Phase 2 extension)

**2.1.2 AR Component: Description Logic + Bayesian Logic Programs**
- OWL 2 DL ontology (STOIC family) encodes system model structure, morphism types, composition constraints
- Constrained to EL++ / DL-Lite profile for polynomial tractability where full expressivity not needed
- Bayesian Logic Programs (via ProbLog2) encode probabilistic morphism quality inference
  - Given: ML-computed embedding distances, sensor comparisons
  - Compute: posterior P(morphism_holds | evidence) with uncertainty bounds
  - Compose: joint probability over component morphisms with conditional independence structure
- SHACL shapes as compositional pre-conditions: before composing two components, validate that their morphism specifications are compatible
- Logic program rules for graduated composition verdicts (Normal/Caution/Restrict/Halt/Lockdown)

**2.1.3 ML Component: Neural Networks**
- Transformer-based encoders map component states into embedding spaces
- Embedding spaces are AR-defined: the ontology specifies which state distinctions must be preserved (morphism conditions), and the embedding space is constructed to respect them
- Intent encoding: maps AI agent actions to reference ontology concepts via learned embeddings grounded in OWL class structure
- Structural distance instrument (D_s): approximate nearest-neighbor search in AR-defined embedding space
- Behavioral distance instrument (D_b): output comparison with sensor ground truth
- Cosine alignment monitor (d_cos): per-inference runtime sentinel for the circuit breaker trigger

**2.1.4 The Tight Coupling**
- AR constrains ML training: loss function includes morphism quality penalty terms
  - Structural penalty: embedding distances that violate ontology-defined state distinctions
  - Behavioral penalty: output predictions outside AR-defined tolerance bounds
  - Composition penalty: component embeddings that violate SHACL compatibility shapes
- AR constrains ML inference: every ML output is accompanied by a morphism quality certificate
  - The certificate is a logic program proof that the output satisfies morphism conditions
  - If proof fails, the system can explain which conditions failed and why
- ML informs AR: embedding distances and sensor comparisons provide evidence for Bayesian LP inference
- This is not "AR bolted on": the ML's learned representations are structurally shaped by AR constraints during training. The AR is in the loss function, not just the output filter.

#### 2.2 Logical Explainability Properties (Sec. I.E compliance)

- Every composition verdict has a proof tree rooted in morphism conditions
- Proof structure: hierarchical (component -> composition -> system), fine-grained (per-axis, per-component)
- Natural deduction style: morphism conditions as premises, composition theorem as inference rule, assurance level as conclusion
- Unfolding depth: bounded by composition depth (typically 2-4 for realistic AI systems-of-systems), well within <= 10 requirement
- Human-readable explanation: "Component X's structural distance (D_s = 0.18) exceeds the composition threshold (D_s_max = 0.10) because its embedding space fails to distinguish states [s3, s7] that the reference ontology separates. The composite system's structural distance is therefore at least 0.18."
- Line-level debugging: SHACL violation reports identify the specific shape, property, and value that failed

#### 2.3 Computational Tractability

- OWL 2 EL++ profile: polynomial-time classification and consistency checking
- Bayesian LP inference via ProbLog2: polynomial in the size of the ground program for acyclic programs; bounded grounding via magic sets
- Embedding computation: O(d) per vector operation, O(n log n) via ANN search
- SPC monitoring: O(1) per observation (running statistics)
- End-to-end inference latency budget: < 25 ms at ~40 Hz
- Training: AR constraints add O(k) per batch (k = number of SHACL shapes checked), polynomial in model size
- Scalability argument: polynomial time complexity as function of knowledge input size for both inferencing (Ph1) and training (Ph2)

### 3. Application Domain and SOA Benchmarks

#### 3.1 Domain: AI-Enabled Medical Devices (FDA-Regulated)

- AI-enabled medical devices are safety-critical systems-of-systems: physiological signal processing (ML) + clinical decision logic (AR) + alarm/alert generation (ML+AR)
- FDA's Total Product Life Cycle (TPLC) framework is fundamentally a systems engineering process; the 510(k) "substantial equivalence" determination is a morphism question (does this device's model of the patient preserve the properties that the predicate device preserves?)
- 950+ FDA-cleared AI/ML devices as of 2024; no existing framework composes assurance across device subsystems
- DARPA-mission relevant: DoD medical (combat casualty care, field hospitals, remote physiological monitoring), critical safety-critical AI
- FDA's 2023 guidance on predetermined change control plans for ML-based devices explicitly identifies the compositional assurance gap this work addresses
- Well-defined ground truth: annotated physiological signals with expert clinical consensus labels

#### 3.2 SOA Baseline

- **SOA system to compare against:** FDA-cleared ECG arrhythmia detection algorithms (e.g., AliveCor/KardiaMobile AF detection, Apple Watch irregular rhythm notification). Published sensitivity/specificity from FDA De Novo/510(k) summaries provide concrete, citable performance baselines.
- **Benchmark dataset:** PTB-XL (21,837 clinical 12-lead ECGs, expert-annotated with diagnostic labels, Wagner et al. 2020, PhysioNet) as primary. MIT-BIH Arrhythmia Database (48 half-hour ECG recordings, beat-level annotations) as secondary for fine-grained composition experiments.
- **Performance metrics:**
  - AUROC for composed task reliability (arrhythmia classification + guideline compliance)
  - Sensitivity/specificity at clinically relevant operating points (matching FDA-cleared device thresholds)
  - Morphism quality certificate coverage: fraction of outputs with valid proofs
- **Train/test split:** PTB-XL provides standard 10-fold stratified splits (Wagner et al. 2020). Will use published splits for reproducibility.
- **Sample complexity (Phase 2):** Compare learning curves (AUROC vs. training set size) for AR-constrained vs. unconstrained ML to quantify sample efficiency gain from ontological priors.

#### 3.3 Composed Task Examples

- **Task 1 (ML+AR):** ECG arrhythmia classification. ML (transformer encoder) maps 12-lead ECG signals to diagnostic embeddings. AR (STOIC-grounded ontology + Bayesian LP) verifies that the classification is consistent with electrophysiological constraints (e.g., atrial fibrillation requires absence of P-waves AND irregular R-R intervals). Composed: classification is both predicted (ML) and verified (AR) with a morphism quality certificate. Morphism h: Z_device -> Z_patient measures whether the device's internal cardiac model preserves the electrophysiological state distinctions that clinical practice requires.
- **Task 2 (ML+AR):** Clinical guideline compliance. ML predicts alert priority from classified rhythm + patient context. AR (ontology-encoded AHA/ACC guidelines) verifies that the alert recommendation is consistent with published clinical protocols and does not violate contraindication rules. Composed: alert is both ML-predicted and AR-validated.
- **Task 3 (composition):** End-to-end patient monitoring. Arrhythmia classification (Task 1) feeds guideline-based alerting (Task 2). Composed morphism quality: D_s_total >= max(D_s_classification, D_s_alerting), D_b_total <= D_b_classification + D_b_alerting. The composition theorem guarantees that if either subsystem's patient model degrades, the composite system's assurance level degrades within formal bounds.

#### 3.4 Phase 2: Deepened ECG Pipeline + Generalization Analysis

- Phase 2 extends the ECG domain with a second ML kind (Bayesian neural networks) and AR-constrained training
- Full three-task composed pipeline: arrhythmia classification (Task 1) -> guideline compliance (Task 2) -> end-to-end patient monitoring (Task 3)
- AR-constrained training: ontology-defined structural priors in the loss function reduce sample complexity vs. unconstrained ML
- Unconstrained ML baseline comparison: ensemble decision tree classifier (Random Forest with WVD + HOS + RR interval features, documented 99.67% sensitivity on MIT-BIH) serves as the unconstrained SOA baseline; AR-constrained Transformer must match or exceed while providing formal composition guarantees
- Domain-transfer cost analysis: formal assessment of what would be required to apply the morphism composition framework to a second safety-critical domain (e.g., autonomous vehicles, telecom network management), demonstrating domain-agnosticity through the formal framework without requiring a full second-domain implementation

### 4. Approach Comparison to AI DevOps SOA

- Current AI DevOps: test-time evaluation, binary pass/fail, no compositional guarantees, no explainability of composition failures
- Our approach: continuous compositional assurance with formal bounds, hierarchical explainability, data-derived thresholds (SPC vs. static), graduated response
- Specific improvements:
  - Explainability: from "confidence = 0.87" (opaque) to "D_s = 0.18 because states [s3,s7] conflated" (structural)
  - Composition: from "hope the pipeline works" to "D_s_total formally bounded by max(D_s_i)"
  - Debugging: from "which layer failed?" to "which morphism condition, on which axis, for which component?"

### 5. Risk Identification and Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| OWL 2 DL tractability for large ontologies | Medium | High | Constrain to EL++ profile; precompute at design-time; cache for runtime |
| Bayesian LP grounding explosion | Medium | Medium | Bounded grounding via magic sets; acyclic program restriction; benchmark early |
| Medical device domain expertise gap | Medium | Medium | PI's systems engineering methodology is domain-agnostic; collaborate with UA BME/clinical faculty for domain validation; FDA-cleared device performance data is public |
| PhysioNet data credentialing timeline | Low | Low | CITI training can be completed in ~2 weeks; PTB-XL is open-access without full credentialing |
| AR-constrained training instability | Medium | Medium | Gradual constraint introduction (curriculum-style); ablation studies; fallback to inference-only AR in worst case |
| Morphism composition theorem assumes independence | Low | Medium | Empirically validate on medical device testbed; extend theory to handle correlated degradation in Phase 2 |
| Clinical ontology completeness | Medium | Medium | Scope to arrhythmia classification (well-bounded); leverage existing AHA/ACC ontologies and SNOMED-CT for clinical concepts |
| Small team capacity for 15-month Phase 1 | Medium | High | Focused scope (2 kinds, 1 domain); leverage existing STOIC ontology and CBTO; open-source tool reuse (ProbLog2, OWL API, Jena) |

### 6. Software Substantiation

| Component | Software | Role |
|-----------|----------|------|
| AR: Ontology | OWL API + Apache Jena Fuseki | STOIC/CBTO ontology management, SPARQL queries, SHACL validation |
| AR: Logic Programs | ProbLog2 (KU Leuven) | Bayesian Logic Program inference for probabilistic morphism quality |
| ML: Signal Processing | PyTorch + tsai (time-series AI) | Transformer-based ECG encoding and embedding space construction |
| ML: ANN Search | FAISS (Meta) | Approximate nearest-neighbor for real-time D_s measurement |
| SPC Engine | Custom (Python, scipy) | Statistical process control with Western Electric rules, CUSUM |
| Provenance | PROV-O via rdflib | Queryable audit trail for composition verdicts |
| Integration | Python + REST APIs | Glue layer connecting AR and ML components |

- AR software (ProbLog2, OWL API, Jena): open-source, mature, well-documented
- ML software (PyTorch, FAISS): industry-standard, Apache 2.0 compatible
- All project code released under Apache 2.0 per CLARA requirements

### 7. Metrics Mapping

| CLARA Metric | Our Approach | Phase 1 Target | Phase 2 Target |
|-------------|-------------|----------------|----------------|
| Verifiability without loss of performance | Morphism quality certificates with OWL + LP proofs; AUROC-based performance comparison | Fully verifiable; error rate <= SOA | Fully verifiable; error rate <= SOA |
| Multiplicity of Kinds in Composition | Intra: Neural Nets (ML) + Description Logic (AR) + Bayesian LP (AR) | >= 2 kinds (1 ML + 1 AR, tight) | >= 3 kinds (2 ML + 1 AR) |
| Computational Time Complexity | EL++ polynomial classification; bounded LP grounding; O(n log n) ANN | Polynomial for inferencing | Polynomial for inferencing + training |
| Composed Task Reliability | Morphism-bounded composition on medical device testbed vs. FDA-cleared SOA | Reliability > SOA | Reliability > SOA |
| Sample Complexity in Training | AR constraints reduce training data needs (ontology provides structural priors) | N/A | Sample complexity < SOA |
| Inter-performer Composition | Hackathon participation; morphism framework as common composition interface | Hackathon participation | Hackathon participation |

### 8. Schedule and Milestones

#### Phase 1 (15 months, $1.1M) — Prove the Composition

Narrow scope: one ECG task (arrhythmia classification), one ML kind (Transformer), one AR kind (OWL 2 DL + Bayesian LP). Goal is to prove the morphism composition theorem works on real clinical data.

| Month | Milestone | Deliverable |
|-------|-----------|-------------|
| 1 | Kickoff | Personnel assigned; PTB-XL data access confirmed; names to Government |
| 1-4 | Theory + ECG ontology | Composition theorem formalized and proved; cardiac domain ontology (ECG impossible states, AHA/AAMI constraints) encoded in OWL; ProbLog2 pipeline prototyped; STOIC alignment verified in EL++ |
| 3 | Progress report | SOA baselines from FDA 510(k) summaries; PTB-XL benchmark methodology; ACAs in place |
| 4-8 | Single-task AR+ML prototype | Transformer encoder on PTB-XL; AR constraints in loss function (ontology-defined state distinctions); morphism quality instruments (D_s via embedding distance, D_b via sensor comparison, d_cos as runtime sentinel) |
| 6 | Demo: initial AR-ML capability | Working prototype: OWL + Bayesian LP constraining Transformer inference on PTB-XL arrhythmia classification; morphism quality certificates generated |
| 8-12 | Composition experiments | Compose Task 1 (classification) + Task 2 (guideline compliance); validate composition bounds (D_s_total, D_b_total); hallucination injection at 1/5/10/25%; SPC baseline collected |
| 9 | Demo: composed AR-ML capability | Two-task composed system with formal bounds; SOA comparison vs. FDA-cleared baselines; software + docs for IV&V; Hackathon #1 prep |
| 9-12 | Hackathon preparation + inter-performer work | Integration with TA2 library patterns; Workshop #3 participation |
| 12 | Hackathon #1 | Demonstrate composed AR-ML on ECG classification + guideline compliance |
| 12 | Progress report | Inter-performer compositions; composition theorem validation results |
| 12-15 | Phase 1 closeout | Full experimental results; Phase 1 paper draft; all software + documentation |
| 15 | Phase 1 final deliverable | Theory, software, data, training materials |

Phase 1 success criteria: composition theorem demonstrated empirically; AUROC >= FDA-cleared SOA on PTB-XL; morphism quality certificate coverage > 95%; hallucination detection TPR > 95% at 5% FPR; polynomial time verified for inference.

#### Phase 2 (9 months, $0.75M) — Deepen and Scale

Wider scope: second ML kind (Bayesian methods), third composed task (end-to-end patient monitoring), AR-constrained training, domain-transfer analysis.

| Month | Milestone | Deliverable |
|-------|-----------|-------------|
| 16-18 | Second ML kind + AR-constrained training | Bayesian neural net on ECG data; AR constraints in training loop (not just inference); sample complexity comparison vs. unconstrained ML baseline |
| 18 | Demo: extended AR-ML | Three ML+AR kinds composed (Transformer + Bayesian + OWL/LP); AR-constrained training demonstrated |
| 19-21 | Full ECG pipeline + generalization | Task 3 (end-to-end patient monitoring): classification -> guideline compliance -> alert generation; SPC vs. static vs. allostatic comparison; domain-transfer cost analysis |
| 21 | Demo: composed capability | Three-task composed system; Phase 2 metric targets; Hackathon #2 prep |
| 22 | Hackathon #2 | Full ECG pipeline with three composed tasks |
| 22-24 | Closeout | Domain-transfer analysis report; open-source release; final report; integration paper |
| 24 | Phase 2 final | Complete software, data, publications, open-source release |

Phase 2 success criteria: >= 2 ML + 1 AR kinds tightly composed; sample complexity < unconstrained SOA; three-task composition with formal bounds; polynomial time for inference and training.

### 9. Team and Qualifications

#### 9.1 PI: Paul F. Wach, Ph.D.

- Postdoctoral Research Associate, University of Arizona, Dept. of Systems & Industrial Engineering
- Ph.D. Virginia Tech (2022): "Study of equivalence in systems engineering within the frame of verification"
- Published work establishing the mathematical foundations:
  - Degree of homomorphism metric: CSER 2025
  - Isomorphism library (extends degree of homomorphism with sigma notation and two-axis framework): CSER 2026 (in revision)
  - Wymore-DEVS conjoining: Applied Sciences 2021
  - Bayesian + systems theory for T&E: INSIGHT 2022
  - WySE Metamodel / STOIC ontology family: INCOSE 2022, ongoing
  - Portfolio governance ontology: 119 individuals, 778 triples, 20 SPARQL CQs (2026)
- Systems engineering methodology is domain-agnostic; morphism theory applies to any system with formal state spaces
- Experience with DARPA program participation context (defense-relevant application domains)

#### 9.2 Co-PI: Jeffrey Wallk

- The Value Enablement Group, LLC
- 20+ years in data architecture and autonomous systems
- Systems architecture and AI safety engineering
- ECG domain expertise: authored Technical Design Document (TDD v2.0) for diagnostic-grade ECG signal processing with AI Circuit Breaker integration (32 pages, 17 sections, AHA/ANSI/AAMI standards compliance)
- On-prem/cloud integration expertise

#### 9.3 Institutional Support

- University of Arizona: Carnegie R1, HSI, computational infrastructure
- Access to interdisciplinary collaborators (SIE, CS, ECE, BME for clinical domain validation)

### 10. Travel and Meetings

- 8 two-day program-wide meetings over 24 months
  - 4 in Washington, D.C. area (including Phase 1 kickoff)
  - 4 in San Francisco area
  - 1 week-long back-to-back pair at phase transition (D.C.)
- 2 essential personnel per meeting
- Budget: [CALCULATE based on UA travel rates]

---

## Volume 2: Price Volume

- Use Streamlined Cost Buildup Workbook (CLARA_TA1.xlsx)
- Categories:
  - Direct labor (PI, Co-PI, graduate students, postdoc if applicable)
  - Fringe benefits (UA rates)
  - Travel (8 meetings x 2 people x est. $2,500/trip = ~$40,000)
  - Equipment/compute (GPU cluster time, cloud compute for training)
  - Materials and supplies
  - Subcontract (Value Enablement Group)
  - Indirect costs (UA F&A rate)
  - Fee (if applicable for OT)
- Schedule of Milestones and Payments tab

## Volume 3: IP and Data Rights

- All software Apache 2.0 (per CLARA preference)
- STOIC/CBTO ontologies: open-source
- PI's prior published work: available per journal terms
- No proprietary data or restricted IP anticipated
- UA IP policy compliance

---

## Open Items / TODO

1. ~~**SOA Benchmark (CRITICAL):**~~ **RESOLVED.** Domain: AI-enabled medical devices. SOA: FDA-cleared ECG algorithms. Dataset: PTB-XL (primary), MIT-BIH (secondary). Metrics: AUROC, sensitivity/specificity at clinical thresholds.
2. **ProbLog2 Integration Feasibility:** Prototype the OWL-to-ProbLog2 pipeline to validate that Bayesian LP can reason over morphism quality in polynomial time for realistic ontology sizes.
3. **EL++ Profile Verification:** Confirm that STOIC/CBTO can be constrained to EL++ without losing essential expressivity for morphism conditions.
4. **Budget Detail:** Build out cost workbook with UA rates, subcontract structure, compute needs.
5. **Parent PA Format:** Obtain DARPA-PA-25-07 Section 5 for exact formatting requirements (page limits, fonts, margins).
6. **BAA Portal Registration:** Register UA organization on baa.darpa.mil; verify SAM UEI.
7. **ACA Clause:** Review sample Associate Contractor Agreement clause; prepare for TA2 collaboration.
8. **DARPA-SN-26-28:** Check for any updated special notices.
9. **UA Sponsored Projects:** Engage UA Office of Research, Discovery & Innovation for institutional sign-off, F&A rate certification, and OT agreement review.
10. **Second ML Kind (Phase 2):** Decide between Bayesian methods (Bayesian neural nets, Bayesian optimization) or Reinforcement Learning. Bayesian aligns better with the uncertainty quantification theme.
11. ~~**Second Domain (Phase 2):**~~ **RESOLVED (updated 2026-03-23).** Telecom dropped. Phase 2 deepens ECG (second ML kind, full pipeline, AR-constrained training) + domain-transfer cost analysis.
