# Action Plan for PostWach: AI Circuit Breaker Design Spec Revision

## Phase 1 - Fix Internal Consistency (Foundation Work)

### 1.1 Resolve the Immutability Paradox
- Rewrite Subsystem 1 language: replace "Immutable Truth" with a **versioned truth** model (e.g., "Deterministic Knowledge at Version V_n")
- Define an explicit ontology versioning protocol in Subsystem 4 that governs how "Ontology Enhancement" promotes candidate changes through review gates before they enter the knowledge layer
- Add a version hash to every ontological node so the audit trail (Subsystem 5) can trace *which version* of truth was used for any given decision

### 1.2 Tighten the "Deterministic" Claim
- Distinguish between two tiers: **sensor-deterministic** (LiDAR, optical power meters - truly deterministic) and **consensus-deterministic** (ontologies, taxonomies - human-curated, revisable)
- Make this distinction explicit in the framework language so reviewers don't conflate the two

---

## Phase 2 - Mathematical Tightening

### 2.1 Bound K_trust
- Replace K_trust = H_ai / L_h with a bounded formulation, e.g.:
  - K_trust = sigmoid(H_ai - L_h) mapping to (0, 1), or
  - K_trust = H_ai / (L_h + epsilon) with a clamped output range
- Define the lockdown threshold relative to the new bounded range
- Document edge cases: what happens when both H_ai and L_h are near zero?

### 2.2 Justify or Parameterize Thresholds
- For each threshold (S_a < 0.15, C_r > 0.85, K_trust < 0.5, MTBH domain minimums):
  - Either cite an empirical basis, or
  - Explicitly label them as **tunable hyperparameters** with a recommended calibration procedure
- Add a "Threshold Calibration Protocol" appendix describing how an adopting organization would set these values for their domain

### 2.3 Revisit the MTBH Distribution Assumption
- Acknowledge that hallucinations may cluster (non-exponential)
- Propose a windowed MTBH variant (e.g., rolling 72-hour window) alongside the cumulative MTBH to catch degradation trends
- Consider adding a **hallucination clustering coefficient** as a secondary metric

### 2.4 Address C_r Independence Assumption
- Add a note on variable interaction effects
- Suggest a covariance-weighted variant for domains where environmental variables are correlated, or at minimum flag this as a known simplification

---

## Phase 3 - Add Missing Design-Spec Elements

### 3.1 Threat Model
- Identify attack surfaces: adversarial manipulation of intent vectors to stay within S_a threshold, poisoning of the vector DB, spoofing sensor ground truth
- For each surface, describe the mitigation within the existing architecture or note it as a gap
- Specifically analyze: can an adversarial agent craft inputs that always pass the cosine-distance check while still being harmful?

### 3.2 Failure Mode Analysis for the Breaker Itself
- Define what happens when:
  - The knowledge graph is unavailable (network partition, DB failure)
  - Sensor ground truth is stale or missing
  - The breaker logic itself throws an exception
- Propose a **default-deny** posture: if the breaker cannot render a verdict, the action is blocked
- Consider redundancy: dual-breaker or watchdog pattern

### 3.3 Latency Budget
- Define a target end-to-end latency for the validation flow (intent to verdict)
- Break it down by component: vector DB lookup, graph traversal, S_a computation, C_r computation, threshold comparison
- Reassess the 100Hz claim against this budget - either justify it or downscope to a realistic frequency with rationale

### 3.4 Cold-Start Protocol
- Define how the system behaves before sufficient MTBH history exists
- Propose a bootstrap mode: conservative thresholds + mandatory human approval for the first N decisions or first T hours of operation
- Define the graduation criteria from bootstrap to autonomous mode

---

## Phase 4 - Positioning & Validation

### 4.1 Related Work Section
- Position against:
  - **NIST AI RMF** (governance framework - how does the circuit breaker operationalize NIST's "Measure" and "Manage" functions?)
  - **IEEE P7000 series** (ethical AI standards)
  - **Runtime monitoring literature** (Desai et al., runtime verification for autonomous systems)
  - **AI guardrails** (NeMo Guardrails, Llama Guard) - how is this different from prompt-level guardrails?
  - **RLHF / Constitutional AI** - these shape the model; the circuit breaker constrains the deployment. Complementary, not competing.
- Articulate the **unique contribution**: metrology-grade quantitative trust underwriting, which none of the above provide

### 4.2 Domain Transfer Argument
- Generalize at least one example beyond telecom (healthcare or autonomous vehicles are natural fits given the sensor-grounding emphasis)
- Create an abstract "domain onboarding checklist" showing what an adopter must provide (ontology, sensor sources, threshold calibration data)

---

## Phase 5 - Proof of Concept

### 5.1 Prototype the Semantic Veto (S_a + Subsystem 3)
- Implement a minimal prototype:
  - A small domain ontology (even synthetic)
  - An intent vector generator (simulated AI actions)
  - The S_a computation + threshold check
  - A log of trips vs. passes
- Use the prototype to empirically calibrate the 0.15 threshold and validate the cosine-distance approach
- This becomes the paper's **evaluation section**

---

## Suggested Sequencing

| Priority | Phase | Rationale |
|----------|-------|-----------|
| 1st | Phase 1 | Internal consistency is a blocker for everything else |
| 2nd | Phase 2 | Reviewers will target the math first |
| 3rd | Phase 3.1-3.2 | Threat model + failure modes are the most conspicuous gaps |
| 4th | Phase 4.1 | Related work is required for any venue |
| 5th | Phase 3.3-3.4 | Important but secondary to the above |
| 6th | Phase 4.2 + 5 | Strengthens the paper significantly but can be a fast-follow |
