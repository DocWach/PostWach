# NSF EDSE Proposal — Working Document

*Target Program:* NSF Engineering Design and Systems Engineering (EDSE), CMMI Division
*Accepts proposals:* Anytime (no fixed deadline)
*Contact:* Harrison Kim, EDSE@nsf.gov, (703) 292-7328
*Session:* February 16, 2026

---

## Overall Objective

Establish the formal mathematical methods for characterizing cross-domain morphisms and apply them to quantitatively determine verification model fidelity, including empirical investigation of the implicit morphism assumptions engineers make when defining verification models.

## Overall Outcome

A validated theory and toolset for morphism-based verification model fidelity assessment: (1) a formally characterized catalog of cross-domain morphisms with a quantitative quality metric, (2) formal correspondence between morphism quality and VMMC fidelity conditions with Bayesian confidence quantification, and (3) empirical evidence characterizing how accurately engineers reason about morphism assumptions in verification model definition.

---

## Year 1: Fundamental Methods and Characterizations

**Sub-Objective:** Develop and validate the fundamental mathematical methods for characterizing cross-domain morphisms, including a comprehensive formally-proven catalog and a multi-layered morphism quality metric satisfying metric space axioms.

**Sub-Outcome:** A validated catalog of 19+ cross-domain morphisms each formally characterized across four mathematical representations with classification proofs; a 5-layer morphism quality metric with proven mathematical properties; degradation bounds for each morphism; and an open-source computational library.

**Tasks:**
1. Complete formal state-space characterization for all Tier 1 entries (I-1 through I-7) with proofs of isomorphism type
2. Extend Tier 1 characterizations to bond graph, port-Hamiltonian, and categorical representations
3. Characterize Tier 2 entries (I-8 through I-13) across all four representations
4. Investigate and classify Tier 3 entries (I-14 through I-19); prove or disprove conjectured morphism types
5. Define the 5-layer morphism quality metric (structural, behavioral, energy, information, categorical); prove or disprove metric space axioms for each layer and the composite
6. Quantify degradation bounds: for each Tier 1 morphism, measure error from Euler, RK4, and exact discretization; identify nonlinearity thresholds where isomorphism degrades to homomorphism
7. Identify cases where commonly assumed morphisms are weaker than believed or do not hold
8. Implement all characterizations and metrics in the open-source Python library with automated testing
9. Submit catalog paper (Idea 5) and metric paper (Idea 6) for peer review

---

## Year 2: Application to Verification Model Fidelity

**Sub-Objective:** Apply the morphism characterization methods and quality metric to verification model fidelity assessment, formally connecting morphism quality to the 6 VMMC types and developing a Bayesian framework for quantifying confidence in verification outcomes.

**Sub-Outcome:** Formal proofs of correspondence between the morphism quality metric and the 6 VMMC fidelity types; a Bayesian framework connecting morphism quality to verification confidence; and 3 cross-domain case studies demonstrating the full chain from morphism characterization to verification confidence.

**Tasks:**
1. Map each of the 6 VMMC types to specific regions in the morphism quality metric space; prove correspondence
2. Derive fidelity conditions: given a morphism quality score, determine which VMMC types are achievable
3. Develop Bayesian framework: define prior distributions over morphism quality, likelihood functions from verification evidence, posterior confidence in verification outcomes
4. Case study 1 (exact morphism): MSD ↔ Series RLC — full chain from characterization → metric score → VMMC type → verification confidence
5. Case study 2 (partial morphism): Electrical ↔ Thermal — demonstrate how partial morphism limits verification; identify which requirements can/cannot be addressed
6. Case study 3 (selected based on Year 1 findings): a Tier 2 or 3 morphism that challenges the framework
7. Extend computational library with verification fidelity assessment tools
8. Submit VMMC correspondence paper and Bayesian confidence paper (Idea 3) for peer review

---

## Year 3: Cognitive Foundations of Verification Morphism Reasoning

**Sub-Objective:** Investigate how engineers implicitly reason about morphism assumptions when defining verification models, measuring the accuracy and calibration of those assumptions against the formal framework from Years 1–2.

**Sub-Outcome:** Validated morphism elicitation protocol; empirical characterization of engineers' implicit morphism assumptions in verification model definition (hidden beliefs, calibration accuracy, heuristic reliability); and evidence-based recommendations for verification practice and SE education.

**Tasks:**
1. Obtain IRB approval for human subjects research at UA
2. Design morphism elicitation protocol: structured verification model definition tasks for cross-domain systems with think-aloud capture of morphism reasoning
3. Pilot with 5–8 engineers across experience levels; refine protocol based on results
4. Hidden beliefs study (n ≈ 20–30): present engineers with cross-domain verification scenarios, elicit assumed morphism conditions, compare against Year 1 formal ground truth; identify believed-but-false and true-but-unrecognized conditions
5. Calibration study: for each scenario collect engineer's confidence rating; correlate with Year 1 morphism quality score
6. Heuristic accuracy study: identify most common heuristic assumptions about verification model fidelity; measure each against the formal metric; assess variation by domain pair and experience level
7. Analyze for systematic patterns: overconfidence, layer-selective attention, domain-dependent accuracy
8. Synthesize evidence-based recommendations for verification practice and SE curriculum
9. Submit cognitive basis papers (Ideas 20, 21, 23) for peer review

---

## Three Overarching Impacts

| Impact | Description |
|---|---|
| **Education** | Explores the extent to which SE is a fundamental discipline that should be studied as part of all engineering programs |
| **Practice** | Establishes reuse of engineering knowledge across domains through a scientific approach |
| **Fundamental science** | Challenges and/or confirms assumptions engineers make about cross-domain relationships |

---

## Decisions Made

- Digital twin is out of scope (ancillary; low-hanging fruit after fundamental work)
- Morphism quality metric belongs in Year 1 (foundational method, not application)
- Year 2 is specifically application to verification model fidelity (VMMC, Bayesian confidence)
- Proposal is narrowed from "all of SE" to verification model fidelity
- Broader portfolio vision (SE as domain-agnostic discipline) stored in future_research_ideas.md

## Next Steps (for next session)

1. **Project Summary (1 page)** — Overview, Intellectual Merit, Broader Impacts
2. Introduction / motivation narrative (gap → thesis → contribution)
3. Prior results section (catalog, code, dissertation)
4. Broader impacts detail
5. Budget and personnel
6. Timeline / management plan

## Key References

- Wach (2022) — dissertation, T3SD/DEVS, VMMC framework
- National Academies (2024) — VVUQ gaps for digital twins (fidelity argument)
- Olson (1943) — classical analogies
- Karnopp et al. (2012) — system dynamics
- Girard & Pappas (2007) — approximate bisimulation
- van der Schaft (2006) — port-Hamiltonian systems
