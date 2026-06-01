# Module D --- Testbed and Validation Approach

**Shared module for all proposals. Source: CLARA proposal outline + ECG TDD v2.0 (Wallk, 2026).**

---

## D.1 Primary Domain: AI-Enabled Medical Devices (FDA-Regulated ECG)

The proof-of-concept testbed deploys the circuit breaker in a **diagnostic-grade ECG signal processing and arrhythmia classification** scenario. An AI classification engine processes 12-lead ECG signals and generates rhythm classifications and clinical alert recommendations; the circuit breaker monitors the morphism between the AI's cardiac model (Z_ai) and the patient's actual electrophysiological state (Z_real) as observed through calibrated electrode sensors.

**Why ECG:**

- AI-enabled medical devices are safety-critical systems-of-systems where a single misclassification can directly result in patient harm (missed STEMI, false-positive pacemaker capture, misclassified arrhythmia).
- ECG signals provide deterministic, physics-based ground truth: the electrochemical signal at the skin-electrode interface is governed by immutable laws of cardiac electrophysiology, making it an ideal anchor for the circuit breaker's deterministic veto.
- 950+ FDA-cleared AI/ML devices as of 2024; no existing framework composes assurance across device subsystems.
- Well-defined clinical standards (AHA/ACC, ANSI/AAMI EC11, IEC 60601-2-25) provide concrete, auditable engineering parameters for morphism quality thresholds.
- DARPA-mission relevant: DoD medical (combat casualty care, field hospitals, remote physiological monitoring).
- FDA's 510(k) "substantial equivalence" determination is itself a morphism question: does this device's model of the patient preserve the properties that the predicate device preserves?

## D.2 Datasets

- **Primary: PTB-XL** (Wagner et al., 2020, PhysioNet) --- 21,837 clinical 12-lead ECGs, expert-annotated with diagnostic labels, standard 10-fold stratified splits for reproducibility.
- **Secondary: MIT-BIH Arrhythmia Database** --- 48 half-hour ECG recordings, 100,858 beat-level annotations mapped to AAMI N/S/V/F/Q categories, used for fine-grained composition experiments.
- **SOA baseline:** FDA-cleared ECG arrhythmia detection algorithms (AliveCor/KardiaMobile AF detection, Apple Watch irregular rhythm notification). Published sensitivity/specificity from FDA De Novo/510(k) summaries.
- **Unconstrained ML baseline:** Ensemble decision tree classifier (Random Forest, 100 trees, bootstrap aggregating) with Wigner-Ville Distribution pseudo-energy + time-domain RR intervals + Higher Order Statistics features. Documented performance: 99.67% sensitivity, 98.92% positive predictivity across N/S/V classes on MIT-BIH (Wallk TDD v2.0, 2026). Serves as the unconstrained ML benchmark that the AR-constrained Transformer must match or exceed while providing formal composition guarantees.

## D.3 Testbed Components

| Component | Implementation |
|-----------|---------------|
| **Z_real specification** | OWL 2 DL cardiac domain ontology encoding ECG impossible states (HR > 300 bpm, PR < 60 ms, QRS < 60 ms in adults), AHA/ACC clinical guidelines, AAMI beat classification constraints |
| **Z_ai agent** | Transformer-based ECG encoder (Phase 1); Bayesian neural net (Phase 2); configurable hallucination injection |
| **Morphism instruments** | Structural (D_s): embedding distance in AR-defined space via FAISS ANN search. Behavioral (D_b): output comparison with expert-annotated ground truth labels |
| **SPC engine** | Control charts with Western Electric rules, CUSUM, data-derived thresholds (min 25 subgroups) |
| **Validation pipeline** | SHACL shape conformance + SPARQL CQ execution (two-tier gate: advisory + blocking) |
| **Provenance store** | PROV-O graph in triplestore (Apache Jena Fuseki) |
| **Bayesian LP inference** | ProbLog2: posterior P(morphism_holds | evidence) with uncertainty bounds |
| **Clinical context engine** | Patient metadata, electrode placement flags, filter state, environmental interference (from TDD Sections 4-8) |

## D.4 Composed Tasks

**Task 1 (ML+AR) --- Arrhythmia Classification (Phase 1 focus):**
ML (Transformer encoder) maps 12-lead ECG signals to diagnostic embeddings. AR (cardiac domain ontology + Bayesian LP) verifies that the classification is consistent with electrophysiological constraints (e.g., atrial fibrillation requires absence of P-waves AND irregular R-R intervals). Composed output: classification is both predicted (ML) and verified (AR) with a morphism quality certificate. Morphism h: Z_device -> Z_patient measures whether the device's internal cardiac model preserves the electrophysiological state distinctions that clinical practice requires.

**Task 2 (ML+AR) --- Clinical Guideline Compliance (Phase 1, months 8-12):**
ML predicts alert priority from classified rhythm + patient context. AR (ontology-encoded AHA/ACC guidelines) verifies that the alert recommendation is consistent with published clinical protocols and does not violate contraindication rules. Composed output: alert is both ML-predicted and AR-validated.

**Task 3 (composition) --- End-to-End Patient Monitoring (Phase 2):**
Arrhythmia classification (Task 1) feeds guideline-based alerting (Task 2) feeds graduated safe-state activation (Level 1 Soft Alert / Level 2 AI Hold / Level 3 Emergency Halt). Composed morphism quality: D_s_total >= max(D_s_classification, D_s_alerting), D_b_total <= D_b_classification + D_b_alerting. The composition theorem guarantees that if either subsystem's patient model degrades, the composite system's assurance level degrades within formal bounds.

## D.5 Validation Protocol

The testbed validates all three research pillars:

**Pillar 1 --- Measurement Theory:**
- Characterize uncertainty budgets (Type A + Type B) for D_s and D_b empirically on PTB-XL
- Demonstrate GUM uncertainty propagation through the traceability chain
- Validate that ontology completeness ratio correctly predicts Type B uncertainty magnitude
- Measure cold-start period: how many operational cycles before SPC control limits stabilize (target: < 25 subgroups)
- Compare AR-constrained Transformer vs. unconstrained Random Forest baseline: AUROC, sensitivity/specificity at clinically relevant operating points

**Pillar 2 --- Enforcement Architecture:**
- Inject known hallucinations at varying rates (1%, 5%, 10%, 25%) and measure detection accuracy (true positive rate, false positive rate)
- Inject adversarial inputs designed to evade the cosine-distance check while producing harmful outputs (two-axis robustness test)
- Test graduated response transitions: verify Normal/Caution/Restrict/Halt/Lockdown activate at correct SPC violations
- Compare detection performance: static thresholds (v1 approach) vs. SPC limits (v3) vs. allostatic adjustment (Pillar 3)
- Validate ECG-specific circuit breaker logic: impossible state detection, filter state monitoring, compression integrity checks (from TDD Sections 10-11)

**Pillar 3 --- Bio-Inspired Adaptive Regulation (Phase 2):**
- Demonstrate homeostatic maintenance of D_s and D_b within the viable operating envelope
- Validate allostatic anticipatory adjustment: tighten control limits before high-risk operational windows
- Test recursive sanitization (SOP-03): CB-flagged epochs excluded from training data, preventing model collapse
- Measure Human-AI Calibration Coefficient dynamics: threshold adjustment based on estimated operator cognitive load

## D.6 Success Criteria

| Metric | Phase 1 Target | Phase 2 Target |
|--------|----------------|----------------|
| Hallucination detection (TPR) | > 95% at 5% FPR | > 97% at 5% FPR |
| Arrhythmia classification AUROC | >= FDA-cleared SOA | >= SOA with formal guarantees |
| Morphism quality certificate coverage | > 95% | > 98% |
| Composition theorem validation | D_s_total >= max(D_s_i) empirically confirmed | Confirmed for 3-task pipeline |
| Cold-start graduation | < 25 subgroups | < 25 subgroups |
| Decision latency | < 25 ms end-to-end | < 25 ms end-to-end |
| Sample complexity (AR-constrained vs. unconstrained) | N/A | AR-constrained requires less data |
| Two-axis adversarial robustness | > 90% detection | > 95% detection |

## D.7 Domain-Transfer Analysis (Phase 2)

Phase 2 includes a formal domain-transfer cost analysis assessing what would be required to apply the morphism composition framework to a second safety-critical domain. Candidate domains include autonomous vehicle perception, telecom network management, and industrial process control. The analysis quantifies: (a) ABox population effort, (b) domain ontology construction effort, (c) sensor-to-morphism-instrument mapping effort, and (d) SPC re-baselining timeline. This demonstrates domain-agnosticity through the formal framework without requiring a full second-domain implementation within the program timeline.

---

*This module is designed for inclusion in all proposals. Adjust success criteria and emphasis per solicitation requirements.*
