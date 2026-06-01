# D_r Recommendation Memo — Reformulation for v0.6

**Date:** 2026-05-20.
**Inputs:** `Dr_construct_analysis_v0.1.md`, `Dr_literature_scoping_v0.1.md`.
**Purpose:** Resolve how Jeffrey's "context relevancy distance" intent gets into v0.6 without the construct confusion of the 2026-05-07 PDF. Drop-in language for the Layer 1 and Layer 3 sections plus the symbol choice, reference additions, and what gets deferred to journal-length follow-on.

## Adjudication

Both the construct analysis (algebraic-logician) and the literature scout (literature-reviewer) converged on the same verdict, from different starting points:

1. **D_r as a third axis on the same morphism distance metric is not coherent.** It fails at least one metric axiom (symmetry, probably; identity of indiscernibles, underspecified), conflates morphism quality with operational applicability, and the claimed extension of the CSER 2026 chain-bound theorem to three axes has no derivation and cannot be constructed in the existing algebra. Construct analyst Sections 1.2 to 1.4.

2. **The intent is sound and well-attested.** "Near-isomorphic to the wrong context" is a real and documented failure mode (silent domain shift). Three independent literatures formalize Paul's exact distinction between morphism quality and scope of validity: ASME V&V 40 (calibration domain vs prediction domain), assume-guarantee contracts (assume clause as precondition of the guarantee), and Wymore-native morphism scope (the morphism is asserted on a specific tuple, not on all tuples). Literature scout Sections 4, 6, 7, 10.

3. **The right formalization is at Layer 1 plus Layer 3, not Layer 2.** It is a property of the deployment triple (Z_ai, h, Z_real), not of the morphism h. The construct analyst's F1 (applicability predicate at Layer 1) + F2 (continuous coverage measure entering Layer 3 SPC) gives the smallest defensible formulation that preserves Jeffrey's intent. The literature scout's Candidate A (QSAR Applicability Domain / Williams plot) supplies the regulatory anchor and a direct 2D visual precedent.

## Recommended formulation for v0.6

**Symbol.** Retire the name "D_r" to avoid (a) the false-distance implication and (b) the collision with Paul's existing `C_r` in Design Spec v4 (where `C_r` denotes the behavioral axis equivalent to D_b). Use **C_env(q)**: envelope coverage of operational query q. Single symbol, two modes:

- **Continuous coverage signal** C_env(q) in [0, 1], where 1 means q is well inside the certified envelope and 0 means q has no support in the certified envelope. Feeds Layer 3 SPC as an additional control chart.
- **Derived precondition predicate** A(q) := (C_env(q) >= tau_env). When A(q) = false, the breaker emits a "context-unverified" verdict for that invocation; D_s and D_b are not reported as trust evidence for that query.

This is the F1 + F2 hybrid the construct analyst recommended, expressed with a single symbol so it can be referenced in one Figure 2 update or one Layer 1 paragraph without inflating vocabulary.

**Type signature.**

    C_env : Profile_op x Envelope_cert --> [0, 1]
    A     : Profile_op x Envelope_cert --> {true, false}
    A(q)  := C_env(q) >= tau_env

Profile_op is the live operational profile. Jeffrey's WHO/WHAT/WHEN/WHERE/WHY five-tuple is one valid encoding; ODD-style taxonomies (BSI PAS 1883) are another; the choice is a Layer 1 specification decision, not a Layer 2 measurement decision.

**Layer placement.**

- **Layer 1.** Envelope_cert is part of the Layer 1 reference standard, alongside the domain ontology. It is the set of operational profiles for which the morphism h has been certified. Specified at certification time using the chosen profile taxonomy. SHACL-expressible.
- **Layer 2.** No change. D_s and D_b remain the two morphism distances. Layer 2 fires when A(q) = true; otherwise Layer 2 measurement is suppressed and the breaker reports "context-unverified."
- **Layer 3.** SPC machinery acquires a third control chart on the C_env(q) time series. Escalation rules become: trip if D_s out of SPC limit, or D_b out of SPC limit, or C_env out of SPC limit, or A(q) = false. Coverage degradation and morphism degradation are independent escalation pathways.

**Composition behavior.** C_env does not compose with D_s and D_b in the same morphism-chain algebra. It does not need to. The composition is at the **verdict-gating** level: the joint trust signal at time t is (D_s(t), D_b(t); C_env(t)), with the precondition A gating whether the (D_s, D_b) pair is reportable at all. This preserves the CSER 2026 two-axis chain bound exactly, with no modification.

**GUM uncertainty.** C_env carries a Type A budget (sampling variance over the certified-profile distribution) and a Type B budget (prior-knowledge uncertainty on the certified-distribution model, e.g., KDE bandwidth or conformal calibration set size). Both are characterizable on a held-out certified-profile dataset. The predicate A also carries a false-positive and false-negative rate characterization. Both fit the existing GUM Type A + Type B treatment that D_s and D_b already use.

**Wymore mapping.** C_env is a property of the operational triple (Z_ai, h, Z_real) relative to the certified envelope, not of h itself. It asks: is the certified Z_real the right Z_real for this invocation? It is structurally compatible with Wymore's morphism domain (the (Z_in, Z_state, Z_out) triple on which a homomorphism is asserted), and extends Wymore-native binary set membership to a continuous coverage measure.

**Runtime procedure (one of several valid).** Three implementable variants, ranked by deployability:

1. **Kernel density on certified profiles.** Fit a KDE over the historical certified-context profile distribution; C_env(q) = normalized density estimate at q. Lightweight. Requires a meaningful profile encoding.
2. **Conformal nonconformity over certified manifold.** Use a learned representation; C_env = 1 - conformal nonconformity rank. Gives finite-sample coverage guarantees (Tibshirani et al. 2019).
3. **Per-dimension coverage decomposition.** Per WHO/WHAT/WHEN/WHERE/WHY dimension, compute a coverage component and aggregate to C_env. Preserves Jeffrey's five-dimensional intuition without claiming a five-dimensional metric.

The abstract can name C_env without committing to a specific runtime variant; pick one for the Phase I testbed.

## Drop-in language for v0.6

**Layer 1 addition (one paragraph, replaces or extends current Layer 1 paragraph).**

Layer 1 anchors the certified envelope: the set of operational profiles for which the morphism is calibrated, declared at certification time and version-controlled alongside the domain ontology. An operational profile spans the WHO, WHAT, WHEN, WHERE, and WHY of an invocation (per Wallk's Master Composition Document; treated here as a profile schema, not as a third metric axis). At each invocation, a coverage indicator C_env(q) reports how well the operational query q sits inside the certified envelope; a derived predicate A(q) gates whether the morphism-quality numbers from Layer 2 are reportable as trust evidence for q. This separation between morphism quality (D_s, D_b) and envelope coverage (C_env, A) is the same separation drawn in ASME V&V 40 between fidelity-of-calibration and applicability-to-prediction-domain, applied to AI components.

**Layer 3 update (one added clause).**

Escalation triggers expand to four channels: D_s out of SPC limit, D_b out of SPC limit, C_env out of SPC limit, or A(q) = false. Coverage degradation is an independent pathway to graduated response, distinct from morphism degradation; an AI well-calibrated to a reality that is not the deployment reality can produce green D_s and D_b on in-envelope strata while C_env trends down or A fires on out-of-envelope strata.

**Figure 2 update.**

Replace Jeffrey's "D_r scale (low / medium / high)" sidebar with a C_env color or a marginal-axis indicator. The (D_s, D_b) plane stays as in v0.5; "context mismatch" becomes the low-D_s, low-D_b region with C_env shading marking the precondition failure. The Williams plot (leverage by residual) from QSAR applicability-domain literature is the direct visual precedent.

**Key Advancements bullet replacement.**

Drop the v0.5+J bullet "Composition result for observation-mediated morphism chains, extending the two-axis bounds from [Wach et al., CSER 2026] to three axes with five-dimensional relevancy bounds." Replace with: "Envelope coverage indicator C_env paired with the two-axis morphism distance, separating fidelity-of-calibration (D_s, D_b) from applicability-to-deployment (C_env, A) along the V&V 40 distinction."

## References to add

Minimum set for the abstract; full coverage lives in the journal-length follow-on.

1. **Sahigara, F., Mansouri, K., Ballabio, D., Mauri, A., Consonni, V., Todeschini, R.** "Comparison of Different Approaches to Define the Applicability Domain of QSAR Models." *Molecules* 17(5), 2012, 4791-4810. Williams plot, leverage-based AD, OECD principle 3 regulatory anchor.
2. **ASME V&V 40-2018.** *Assessing Credibility of Computational Modeling through Verification and Validation: Application to Medical Devices.* American Society of Mechanical Engineers. Calibration-domain vs prediction-domain distinction; FDA-aligned for the ECG testbed.
3. **Tibshirani, R., Foygel Barber, R., Candes, E., Ramdas, A.** "Conformal Prediction under Covariate Shift." *NeurIPS* 2019. Finite-sample coverage guarantees for shift-aware certification; the closest comparator if C_env is implemented via conformal nonconformity.
4. **Benveniste, A., et al.** "Contracts for System Design." *Foundations and Trends in Electronic Design Automation* 12(2-3), 2018, 124-400. Assume-guarantee contracts; A(q) reads cleanly as the assume clause.
5. **Wymore, A. W.** *Model-Based Systems Engineering.* CRC Press, 1993. Required grounding for Wymore-native readers (Salado / Bahill lineage); morphism scope as set membership on the morphism domain.
6. **Wallk, J.** "Morphism Assurance (Master Composition Document)," 2026 (internal). R016 status (a) research artifact. Cite for the five-dimensional WHO/WHAT/WHEN/WHERE/WHY profile schema.
7. **Wallk, J.** "5 Dimensions of Relevancy," 2026 (internal). R016 status (a). Cite alongside the Master Composition Document for the per-dimension envelope structure.

Existing v0.5 reference list keeps INSIGHT 2022, CSER 2026, JCGM 100:2008, Montgomery, NSA 2024, McDermott et al. 2020.

## What gets deferred to the journal-length follow-on

The construct analyst's F3 (operational-domain morphism composition: Z_ai --h_model--> Z_real(cert) --h_use--> Z_real_op) is the most theoretically satisfying option and the only one that preserves Jeffrey's "it composes with D_s and D_b" intuition in a way that survives review. It requires a two-stage extension of the CSER 2026 chain-bound theorem. The required mathematical work is real but tractable and is appropriate for a journal-length follow-on (Systems Engineering journal special issue, INCOSE IS, or the CSER 2027 line).

Flag for the journal extension: a *degree of scope match* in Wymore-compatible vocabulary, paralleling the degree-of-homomorphism construct from CSER 2025. The literature scout identified this as genuine open ground (Section 13, item 2).

## What this preserves and what it changes

**Preserves.**
- Paul's two-axis morphism construct (D_s, D_b) unchanged.
- CSER 2026 chain-bound theorem unchanged.
- Existing Layer 2 morphism instruments unchanged.
- Jeffrey's WHO/WHAT/WHEN/WHERE/WHY taxonomy intact, repurposed as the envelope profile schema.
- Layer 3 SPC machinery extended in the obvious way (one more control chart).
- Existing GUM Type A + Type B uncertainty treatment extended in the obvious way to C_env.

**Changes.**
- Retires the name "D_r" and the "three-axis morphism distance" framing.
- Retires the claim that the CSER 2026 chain-bound theorem extends to a third axis.
- Demotes the third construct from a morphism property (Layer 2) to a deployment-triple property (Layer 1 + Layer 3 gating).
- Adds C_env and A as Layer 1 and Layer 3 constructs with their own GUM budgets.
- Adds four external citations to anchor the construct (Sahigara, V&V 40, Tibshirani, Benveniste).
- Resolves the Figure 2 visual contradiction by treating C_env as a coverage shading or sidebar indicator on the existing (D_s, D_b) plane, not as a third axis.

## Open items

1. **Profile-schema selection.** Adopt Jeffrey's five-dimensional WHO/WHAT/WHEN/WHERE/WHY directly, or compose it with an existing standardized taxonomy (PAS 1883 ODD style, ASME V&V 40 prediction-domain descriptors). Recommend keeping Jeffrey's schema for v0.6 to preserve co-author contribution; revisit for the journal version.
2. **Runtime variant for Phase I.** KDE, conformal, or per-dimension decomposition. Recommend conformal under covariate shift (Tibshirani et al. 2019) for the strongest external positioning and finite-sample guarantees.
3. **tau_env threshold.** Set via SPC calibration on the certified-profile distribution in Phase I, parallel to the existing cold-start protocol for D_s and D_b.
4. **L1-L5 assurance levels.** Jeffrey's draft references L1-L5 anchors but does not cite an external standard. For v0.6, either cite an external assurance-level taxonomy (ARP4754 DAL, DO-178C, AMLAS) or define inline. Decision deferred to co-author conversation.
5. **Verify the four added citations.** Sahigara 2012 (verified by scout), V&V 40-2018 (verified by scout), Tibshirani 2019 (verified by scout), Benveniste 2018 (verified by scout). Confirm each is accessible through UA library before submission.
6. **Cross-check against Wallk's TDD v2.0.** The construct analyst flagged that if Jeffrey has a separate D_r specification in his TDD lineage that was not visible in the 2026-05-07 PDF, the metricity analysis should be re-checked against it. Ask Jeffrey directly.

## Closing note

The recommended reformulation preserves every operational behavior Jeffrey's draft asked for. It also preserves every formal property Paul's existing two-axis framework already has. The only thing it does not preserve is the claim that "D_r is the third axis of morphism distance and composes with the CSER 2026 bounds," which does not hold and which the abstract is stronger without. Conversion cost is one Layer 1 paragraph, one Layer 3 clause, one Figure 2 indicator, one Key Advancements bullet replacement, four references, and a symbol rename. Net effect is to keep Jeffrey's contribution visible while protecting the CSER 2025 / CSER 2026 lineage and the design-spec v4 vocabulary from a regression neither paper can support.
