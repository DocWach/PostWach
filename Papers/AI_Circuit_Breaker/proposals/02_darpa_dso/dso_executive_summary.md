# DARPA DSO Office-Wide BAA --- Executive Summary

## Bio-Inspired Metrological Self-Regulation for Autonomous AI Trust

---

**BAA:** HR001125S0013 (DARPA DSO Office-Wide)
**Thrust:** Complex, Dynamic, and Intelligent Systems
**PI:** Paul F. Wach, Ph.D., Researcher, University of Arizona
**Period of Performance:** 24 months
**Estimated Cost:** Up to $2M

---

## 1. Problem: AI Lacks Metrological Self-Regulation

Autonomous AI systems deployed in safety-critical environments cannot answer a fundamental engineering question: *"How trustworthy am I right now, and with what confidence?"* Current AI safety approaches --- training-time alignment (RLHF), static runtime filters (NeMo Guardrails), and governance frameworks (NIST AI RMF) --- share a critical limitation: **none provide continuous, self-regulating measurement of AI trustworthiness with quantified uncertainty.**

Biological organisms solved this problem billions of years ago. The human body maintains homeostatic equilibrium across dozens of physiological parameters, detects threats through innate and adaptive immune responses, anticipates environmental changes via allostatic regulation, and executes controlled self-termination (apoptosis) of compromised subsystems. These mechanisms are not metaphors --- they are formal control dynamics with well-characterized transfer functions, stability bounds, and failure modes.

We propose to build the first **bio-inspired, metrologically grounded self-regulation system for autonomous AI trust**. The system continuously measures its own trustworthiness against formal specifications, maintains trust within a viable operating envelope, and adaptively regulates its sensitivity based on operational context --- just as biological systems do.

## 2. Technical Approach: Three Pillars

### Pillar 1 --- Measurement Foundation (the "sensory system")

AI trustworthiness is formalized as a **morphism quality problem** [5], [22]. An AI's internal model (Z_ai) must be homomorphic to reality (Z_real). We measure this morphism along two orthogonal axes using established metrological standards (GUM [24]):

- **Structural quality (sigma):** Degree of homomorphism --- does the AI distinguish every state that reality distinguishes? [22]
- **Behavioral quality (D):** Output distance --- do the AI's predictions match sensor ground truth?

Each metric carries a formal uncertainty budget (Type A statistical + Type B prior knowledge). The traceability chain from sensor ground truth through derived metrics to trust verdicts follows GUM propagation --- giving every verdict a confidence interval, not just a binary pass/fail.

### Pillar 2 --- Enforcement Architecture (the "nervous system")

A five-layer circuit breaker architecture translates morphism measurements into graduated responses:

1. **Reference Standards** --- Formal specification of valid system behavior (OWL 2 DL ontology, SHACL constraints, federated SPARQL topology)
2. **Morphism Instruments** --- Real-time measurement of structural and behavioral morphism quality (< 25 ms, ~40 Hz)
3. **Statistical Process Control** --- Data-derived control limits (SPC, Western Electric rules, CUSUM) replace arbitrary thresholds
4. **Closed-Loop Maintenance** --- Feedback system maintaining morphism quality over time, with bounded control dynamics
5. **Underwriting Interface** --- Human operator as ultimate underwriter, with PROV-O queryable audit trail

### Pillar 3 --- Bio-Inspired Adaptive Regulation (the "homeostatic system")

This is the DSO-specific contribution. We formalize biological self-regulation mechanisms as **control dynamics for AI trust**, not metaphors:

| Biological Mechanism | AI Trust Function | What It Replaces | Formal Model |
|---------------------|-------------------|-----------------|--------------|
| **Homeostasis** | Actively maintain sigma and D within viable envelope; steer back toward center, don't just react at boundaries | Reactive-only SPC | Set-point tracking with proportional-integral control; stability analysis via Lyapunov functions |
| **Immune response** (innate + adaptive) | Two-tier threat detection: fast pattern-matching for known morphism failures (innate); slower learning of novel failure signatures (adaptive) | Single-layer semantic filter | Innate: hash-based lookup (O(1)); Adaptive: embedding-based novelty detection with incremental learning |
| **Allostasis** | Anticipatory threshold adjustment: tighten sigma/D limits *before* entering high-risk operational windows (maintenance, config changes) | Flat SPC limits | Predictive gain scheduling; context-dependent control limit modulation |
| **Inflammatory response** | Graduated system response (Normal --> Caution --> Restrict --> Halt --> Lockdown) with formal escalation/de-escalation dynamics | Static graduated response | State machine with rate-limited transitions; hysteresis prevents oscillation |
| **Circadian regulation** | Temporal awareness: different trust profiles for different operational cycles (peak hours vs. maintenance windows) | Flat 24/7 thresholds | Time-varying control limits; scheduled gain adjustment |
| **Apoptosis** | Controlled self-termination of compromised subsystems to protect composite system integrity | No existing equivalent | Formal subsystem isolation protocol; morphism quality propagation analysis |

Each mechanism is modeled with explicit transfer functions, stability bounds, and gain scheduling. The testbed validates that bio-inspired regulation outperforms static SPC in dynamic environments.

## 3. DSO Thrust Alignment

The DSO BAA's "Complex, Dynamic, and Intelligent Systems" thrust explicitly calls for:

- **Homeostatic mechanisms** --- Our Pillar 3 is a direct response to this call. The bio-inspired regulation mechanisms formalize homeostasis, allostasis, and immune response as control dynamics for AI systems.
- **Foundations of intelligence** --- Our Pillar 1 contributes a measurement-theoretic foundation: intelligence (trustworthiness) as a morphism quality measurand with metrological traceability.
- **Human-AI ecosystems** --- Our Pillar 2 places the human as an underwriter of morphism quality, with K_trust quantifying the joint health of the morphism and the human's oversight capacity.
- **Systems that evolve and adapt** --- The closed-loop architecture (Layer 4) and bio-inspired regulation (Pillar 3) create a system that adapts its own trust regulation based on operational experience.

## 4. Why DARPA: Unique Lane, No Prior Art

No published work combines:
1. GUM metrological uncertainty applied to AI trustworthiness
2. Wymore morphism theory for formal trust characterization
3. SPC for data-derived trust thresholds
4. Bio-inspired adaptive regulation formalized as control dynamics
5. OWL 2 DL ontological grounding with PROV-O queryable provenance

This project occupies a unique intersection. The PI's prior publications [4], [22], [23], [25] establish the mathematical foundations. The design specification (v4.0, 2,076 lines) provides the architectural blueprint. DARPA funding enables the transition from theory to validated prototype.

## 5. PI and Team

**Paul F. Wach, Ph.D.** --- Researcher (Systems Engineering & AI), University of Arizona. Published contributions in morphism-based system model comparison (CSER 2025), isomorphism libraries for SE (CSER 2026), WySE Metamodel, and OWL 2 DL governance ontologies. Clinical ECG monitoring provides the primary testbed domain.

**Cost/Schedule:** 24 months, up to $2M. Phase 1 (months 1--12): Measurement foundation + enforcement architecture + testbed. Phase 2 (months 13--24): Bio-inspired regulation + second-domain feasibility + integration.

---

## References

[4] P. F. Wach, T. Sandman, and N. Iyer, "Toward a Library of Isomorphic Patterns for Systems Engineering," *CSER 2026* (in revision).
[5] A. W. Wymore, *Model-Based Systems Engineering*, CRC Press, 1993.
[22] P. F. Wach et al., "Degree of homomorphism for characterizing morphic relationships between system models," *Proc. ASME IDETC*, 2024.
[23] P. F. Wach, "The WySE Metamodel," 2025.
[24] JCGM 100:2008 (GUM).
[25] P. F. Wach, "JOE-G Portfolio Governance Ontology," OWL 2 DL, v1.1.0, 2026.
