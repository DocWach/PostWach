# Claim Ledger — AI Circuit Breaker Abstract v0.2

Source: `02 My Outreach/2026_SERC_AI4SE_SE4AI/Wach_Wallk_AICircuitBreaker_Abstract_v0.2.md`

Each claim is tagged with an ID, verbatim or near-verbatim quote, and the paragraph it appears in. The RBW teams work this ledger.

## Framing claims (Abstract opening)

- **C1.** "Systems engineering (SE) is being asked to underwrite AI systems that it cannot currently measure." [Strong negative-existence claim. Primary target of user critique 2026-04-14.]
- **C2.** "Alignment research tunes model behavior... governance frameworks (NIST AI RMF, ISO/IEC 42001, EU AI Act) specify what should be assessed... formal verification proves pre-deployment properties."
- **C3.** "None of these produce a continuous, quantitative, calibrated measurement of AI trustworthiness at run time with an uncertainty budget attached."
- **C4.** "Safety-critical industries that SE already serves, biomedical devices, aerospace, telecom, and manufacturing, require exactly that kind of measurement before they accept a component into a system-of-systems."

## Central thesis

- **C5.** "AI trustworthiness is a measurement problem, not an alignment or governance problem."
- **C6.** "The AI Circuit Breaker is an instrument... that continuously measures the morphism quality between an AI agent's internal model of the world and the world itself, then renders a verdict with known confidence bounds."
- **C7.** "Grounded in Wymorian systems theory and the Guide to the Expression of Uncertainty in Measurement (GUM)."

## Methodology claims

- **C8.** "The *isomorphic degradation* framework (Wach, Sandmann, Iyer, CSER 2026) establishes that an exact isomorphism between two system models can weaken along two orthogonal axes [abstraction and discretization]."
- **C9.** "Degree-of-homomorphism metric (Wach, Iyer, Shanmugam, Curran, Ashok, CSER 2025)."
- **C10.** "D_s = 1 - sigma, where sigma is the average reciprocal mapping cardinality across states (the degree of homomorphism)." [Formal definition — attributable to Wach 2022 dissertation and CSER 2025 STcP MVP.]
- **C11.** "D_b = max_t |R_ai(s_ai(t)) - R_real(s_real(t))|, the worst-case output discrepancy."
- **C12.** "The axes are independent." [Orthogonality of D_s and D_b.]
- **C13.** "D_s in [0,1] as defined assumes an exact surjective homomorphism on discrete, enumerable state spaces; for continuous or approximate mappings the structural distance generalizes to an information-theoretic form (1 - I(X;Y)/H(X))."
- **C14.** "The canonical mass-spring-damper to series RLC pair serves as the reference exemplar... exhibiting both axes of degradation on a system pair that is exactly isomorphic at the physics level."
- **C15.** "Composition theorem applies: D_s_total >= max(D_s_i) and D_b_total <= sum(D_b_i)." [Needs formal proof citation. Currently stated without one.]

## Architecture claims

- **C16.** "Minimum 25 baseline subgroups" for SPC control limits. [Standard SPC convention, needs citation: Montgomery, ASTM, ISO 7870.]
- **C17.** "Western Electric rules, and CUSUM" — standard SPC tools, should cite Western Electric Handbook or Montgomery.
- **C18.** "CBTO... 25 classes, 20 object properties, 12 data properties, 6 SHACL validation shapes..., 10 SPARQL competency queries." [Internal artifact. Verify these numbers against actual CBTO file before submission.]
- **C19.** "Runtime assessment (under 25 ms at roughly 40 Hz)." [Performance claim. Currently aspirational; no measurement yet. Should be framed as target, not achieved.]
- **C20.** "Basic Formal Ontology (BFO 2020) alignment." [Verifiable vs CBTO file.]

## Phased application claims

- **C21.** "PTB-XL (21,837 clinical ECGs)." [Verifiable against Wagner et al. 2020. Actual count is 21,837 records across 18,869 patients — confirm.]
- **C22.** "MIT-BIH (48 recordings, 100,858 beat annotations)." [Verifiable against Moody & Mark 2001 and PhysioNet.]
- **C23.** "Random Forest classifier (Wallk TDD v2.0, 2026, reported 99.67% sensitivity and 98.92% positive predictivity on MIT-BIH)." [Claim sourced from internal Wallk TDD; original source of those numerics should be traced.]
- **C24.** "Atrial fibrillation requires absence of P-waves AND irregular R-R intervals." [Clinical claim. Cite AHA/ACC guideline.]
- **C25.** "FDA 510(k) 'substantial equivalence' determination is itself a morphism question." [Novel interpretive claim. Defensible as analogy; should not be stated as established.]

## Expected outcomes (targets, not achieved)

- **C26.** "Hallucination true-positive rate above 95% at 5% false-positive rate."
- **C27.** "Arrhythmia classification AUROC at or above FDA-cleared state-of-the-art."
- **C28.** "Morphism quality certificate coverage above 95%."
- **C29.** "Cold-start graduation within 25 subgroups."
- **C30.** "End-to-end decision latency under 25 ms."

  [C26-C30 are PHASE TARGETS, not achieved results. Wording must make that unambiguous.]

## Uniqueness / gap claims

- **C31.** "GUM-based uncertainty propagation (Type A + Type B) applied end-to-end to AI trust measurement for the first time." [Strong novelty claim. Red team must test whether true.]
- **C32.** "Nobody applies GUM to AI trustworthiness." [From Module B — must be rigorously tested against lit review.]
- **C33.** "Biomedical, aerospace, and manufacturing engineers already think in SPC and metrology." [Defensible generalization, but needs qualification.]
- **C34.** "NSA Zero Trust Pillar 7 (Visibility and Analytics)... continuous verification of system behavior is the core tenet." [Verify against NSA/CISA ZT publications. Pillar 7 title and framing should be exact.]

## Attribution / reference accuracy

- **C35.** Reference [1] Wach, Zeigler, Salado 2021 Applied Sciences — verify DOI, volume, page.
- **C36.** Reference [4] CSER 2026 authors Wach, Sandmann, Iyer. Confirm against actual paper.
- **C37.** Reference [5] CSER 2025 STcP MVP authors. Confirm.
- **C38.** Reference [7] PTB-XL: Wagner et al. Scientific Data 2020, 7(1): 154. Verify.
- **C39.** Reference [8] Moody & Mark 2001 IEEE EMBS — verify volume/issue/page.
- **C40.** Reference [10] "NSA/CISA Zero Trust Maturity Model, Pillar 7." Actual publisher is CISA (the Zero Trust Maturity Model is CISA's). NSA ZT is separate (NSA Zero Trust Implementation Guidelines). Needs disambiguation.
