# D_r Literature Scoping v0.1

**Purpose.** Independent scoping of adjacent literatures that formalize the question *"is the AI model being used in the right operational context?"* — to inform whether Wallk's proposed D_r (context relevancy distance) should sit as a third axis alongside D_s and D_b, or be formalized differently. Not a final recommendation; landscape map only.

**Author.** Literature Reviewer agent, on commission from PostWach (CTO).
**Date.** 2026-05-20.
**Version.** v0.1 (cross-disciplinary scoping; not a venue-bound SE literature review — that exists separately in `lit_review_scoping_v0.1.md`).

**Scope boundary.** Ten adjacent fields requested. ML/CS venues included (unlike the SE-bound v0.1 review). Coverage focuses on the formalization of "right context / scope of validity," not on the broader topic of each field. Citation confidence: each citation below was verified against publisher page, arXiv abstract, or DOI in this session; items I could not confidently attribute are marked `(verify)` and are kept only when the construct itself is well-attested in the field.

**Construct under study.** D_r ("context relevancy distance"): captures the failure mode where an AI is near-isomorphic to its training context (low D_s, low D_b) but misaligned with the operational context at hand. Paul's framing: model-to-reality morphism quality (D_s, D_b) is conceptually distinct from "is this the right slice of reality?" (scope-of-validity / applicability).

---

## How to read each section

For each field:
- **Construct summary.** One paragraph on what the field calls "right context."
- **Formalization.** Distance / predicate / set / envelope / coverage. Structural vs statistical.
- **Key citations.** 3-5 verified.
- **Strengths / weaknesses for D_r.** What transfers, what does not.

---

## 1. Operational Design Domain (ODD)

### 1.1 Construct summary

ODD is the explicit declaration of the conditions under which a driving automation feature is designed to operate. SAE J3016 defines it as "operating conditions under which a given driving automation system or feature thereof is specifically designed to function, including, but not limited to, environmental, geographical, and time-of-day restrictions, and/or the requisite presence or absence of certain traffic or roadway characteristics." ISO 21448 (SOTIF) uses the ODD as the boundary of where functional safety and SOTIF arguments hold; outside the ODD, the system must transition to a minimal risk condition. BSI PAS 1883:2020 provides a structured taxonomy (scenery, environmental conditions, dynamic elements) for expressing an ODD in a machine-readable, comparable form.

### 1.2 Formalization

- **Type:** Predicate over a structured taxonomy. "In-ODD" / "out-of-ODD" is binary at the spec level; can be relaxed into a fuzzy / probabilistic coverage measure at runtime via ODD monitors.
- **Structural vs statistical:** Primarily **declarative-structural** (a taxonomy of conditions), with statistical instantiation at runtime (sensor-driven inference of current conditions).
- **Set/envelope flavor:** ODD = a set in a typed condition space. Operational Domain (OD) = the actual conditions encountered. Safe operation requires OD ⊆ ODD; the gap OD \ ODD is the SOTIF concern.

### 1.3 Key citations

1. SAE International. *J3016: Taxonomy and Definitions for Terms Related to Driving Automation Systems for On-Road Motor Vehicles.* Recommended Practice, multiple revisions through 2021. (Origin of ODD term in autonomy.)
2. ISO. *ISO 21448:2022 Road vehicles — Safety of the intended functionality (SOTIF).* (ODD as the locus of SOTIF argument.)
3. British Standards Institution. *PAS 1883:2020 Operational Design Domain (ODD) taxonomy for an Automated Driving System (ADS) — Specification.* BSI, August 2020.
4. Koopman, P., and Wagner, M. "Challenges in autonomous vehicle testing and validation." *SAE International Journal of Transportation Safety*, 4(1), 2016. (Cited foundation for ODD-based scenario coverage arguments.)
5. Krajewski, R., et al. "Formalization of operational domain and operational design domain for automated vehicles." arXiv:2408.14481, 2024. *(verify final venue; preprint confirmed.)*

### 1.4 Strengths and weaknesses for D_r

**Strengths.**
- ODD is the closest existing standardized concept to D_r intent: it asks exactly "is this the right context?" before the model is allowed to act.
- Mature structured taxonomy (PAS 1883) means D_r could inherit a vocabulary rather than invent one.
- Tied to safety-case arguments (ISO 21448), which is the same regulatory framing as AI Circuit Breaker's target use (FDA, DoD).

**Weaknesses.**
- ODD is binary at the spec level — fundamentally a predicate, not a distance. Mapping to a continuous metric requires extension.
- ODD is **declared a priori** by designers, not measured from the model. D_r needs to be measurable at inference time, possibly from the model itself.
- Strongly domain-bound to driving (taxonomy is roads, weather, traffic). Generalizing to medical AI or LLM agents requires re-construction of the taxonomy each time.
- Does not address the *structural-vs-statistical* split that D_s and D_b already encode; ODD lives entirely in the input-condition space.

---

## 2. Out-of-Distribution (OOD) Detection

### 2.1 Construct summary

OOD detection in ML asks whether a given input at inference time is drawn from the same distribution as the training data. The field grew out of Hendrycks and Gimpel's 2016 / 2017 baseline using maximum softmax probability (MSP), and now spans confidence-based, distance-based, energy-based, and density-based methods. The unifying intuition: a model is trustworthy in the **support** of its training distribution; everywhere else, predictions are unreliable. Yang et al.'s 2022 survey unifies anomaly detection, novelty detection, open-set recognition, OOD detection, and outlier detection under "generalized OOD detection."

### 2.2 Formalization

- **Type:** Continuous **score** (MSP, energy, Mahalanobis distance) thresholded to a binary in/out predicate. Sometimes calibrated to a probability of OOD.
- **Structural vs statistical:** Purely **statistical** — operates on input distributions or learned feature distributions; does not consider whether the model's internal structure matches reality.
- **Set/envelope flavor:** Implicit support set of the training distribution; "in-distribution" = high likelihood under that support.

### 2.3 Key citations

1. Hendrycks, D., and Gimpel, K. "A baseline for detecting misclassified and out-of-distribution examples in neural networks." ICLR 2017 (arXiv:1610.02136). *Maximum softmax probability baseline.*
2. Liang, S., Li, Y., and Srikant, R. "Enhancing the reliability of out-of-distribution image detection in neural networks." ICLR 2018 (arXiv:1706.02690). *ODIN: temperature scaling + input perturbation.*
3. Lee, K., Lee, K., Lee, H., and Shin, J. "A simple unified framework for detecting out-of-distribution samples and adversarial attacks." NeurIPS 2018. *Mahalanobis-distance OOD score in feature space.*
4. Liu, W., Wang, X., Owens, J., and Li, Y. "Energy-based out-of-distribution detection." NeurIPS 2020.
5. Yang, J., Zhou, K., Li, Y., and Liu, Z. "Generalized out-of-distribution detection: A survey." arXiv:2110.11334, 2021-2022. *Unifying taxonomy.*
6. Hendrycks, D., Mazeika, M., and Dietterich, T. "Deep anomaly detection with outlier exposure." ICLR 2019 (arXiv:1812.04606).

### 2.4 Strengths and weaknesses for D_r

**Strengths.**
- Mature, well-cited, with standard benchmarks. Any D_r formulation will be compared against MSP / Mahalanobis / energy.
- Genuinely *measurable at inference time* from the model itself — unlike ODD, which requires external sensors.
- Mahalanobis-based scores are natural distances; they map cleanly to the metric framing of D_s and D_b.

**Weaknesses.**
- OOD is a **statistical** notion (distributional shift), not a **contextual** one. An input can be in-distribution but in the wrong *operational context* (e.g., a chest X-ray that looks like training but is being used for a downstream task the model wasn't trained for).
- OOD assumes a fixed training distribution; D_r needs to handle the case where the deployment context is *known* and different.
- Most methods produce a score, not a calibrated probability; comparability to D_s, D_b on the [0,1] interval requires explicit calibration.
- OOD does not distinguish "novel input" from "wrong-task input." Wallk's failure mode is closer to the latter.

---

## 3. Concept Drift / Dataset Shift

### 3.1 Construct summary

Dataset shift is the umbrella term for any disagreement between training and deployment joint distributions P_train(X, Y) ≠ P_deploy(X, Y). The literature distinguishes covariate shift (P(X) shifts, P(Y|X) stable), prior probability / label shift (P(Y) shifts, P(X|Y) stable), and concept shift / concept drift (P(Y|X) shifts). Concept drift is the temporal variant — the underlying generative process evolves while the model stays fixed. Gama et al.'s 2014 survey and Lu et al.'s 2019 IEEE TKDE review are the canonical entry points. Quinonero-Candela et al.'s 2009 MIT Press volume is the field's foundational compendium; Moreno-Torres et al.'s 2012 paper provides the unifying terminology.

### 3.2 Formalization

- **Type:** Most foundational definitions are **predicates** on probability distributions (equality vs inequality). Detection methods produce a **score** (e.g., KL divergence, Wasserstein distance, MMD, two-sample test statistic) plus a threshold.
- **Structural vs statistical:** Statistical, with a particular structure (covariate / label / concept). The taxonomy itself is structural: it tells you *which* part of the joint distribution shifted.
- **Set/envelope flavor:** Not a set, but a comparison between two distributions. Adaptation methods may reconstruct a target-domain "valid region" via importance weighting (Sugiyama et al.).

### 3.3 Key citations

1. Quinonero-Candela, J., Sugiyama, M., Schwaighofer, A., and Lawrence, N. D., eds. *Dataset Shift in Machine Learning.* MIT Press, 2009. (Foundational volume; includes Storkey's taxonomy chapter.)
2. Moreno-Torres, J. G., Raeder, T., Alaiz-Rodriguez, R., Chawla, N. V., and Herrera, F. "A unifying view on dataset shift in classification." *Pattern Recognition* 45(1):521-530, 2012.
3. Gama, J., Zliobaite, I., Bifet, A., Pechenizkiy, M., and Bouchachia, A. "A survey on concept drift adaptation." *ACM Computing Surveys* 46(4):44, 2014.
4. Sugiyama, M., Krauledat, M., and Muller, K.-R. "Covariate shift adaptation by importance weighted cross validation." *JMLR* 8:985-1005, 2007.
5. Lu, J., Liu, A., Dong, F., Gu, F., Gama, J., and Zhang, G. "Learning under concept drift: A review." *IEEE Transactions on Knowledge and Data Engineering* 31(12):2346-2363, 2019.
6. Storkey, A. "When training and test sets are different: characterising learning transfer." Chapter in Quinonero-Candela et al. 2009.

### 3.4 Strengths and weaknesses for D_r

**Strengths.**
- Provides the cleanest *taxonomy* the AI Circuit Breaker could borrow: covariate / label / concept shift are orthogonal failure modes, paralleling the D_s / D_b / D_r question.
- Each shift type has known distance measures (KL, MMD, Wasserstein) — gives D_r candidate functional forms.
- The literature explicitly separates "the input distribution changed" from "the input-output relation changed" — this is exactly the distinction Paul is drawing between D_s/D_b (model-to-reality morphism) and Wallk's D_r (wrong-context).

**Weaknesses.**
- Drift is fundamentally **temporal/comparative** (train vs deploy distributions). It does not directly model "context as a known operational scope" the way ODD does.
- Detection methods need samples from both distributions; for D_r used at inference on a single input, drift formalism is awkward.
- Concept shift (P(Y|X)) is the closest analog to Wallk's intent, but it is the *hardest* shift to detect because labels are typically unavailable at deployment.

---

## 4. Applicability Domain (AD) in QSAR / Cheminformatics

### 4.1 Construct summary

In QSAR (Quantitative Structure-Activity Relationship) modeling, the Applicability Domain is the response and chemical-structure space within which the model makes predictions with a given reliability. OECD principle 3 (2007) requires every regulatory QSAR model to declare its AD. Sahigara et al.'s 2012 *Molecules* review catalogs four families: range-based (bounding box on descriptors), distance-based (e.g., k-NN in descriptor space), leverage-based (hat-matrix leverage threshold h* = 3p/n, visualized in the Williams plot), and probability-density-based (kernel density on training set).

### 4.2 Formalization

- **Type:** Set or envelope in descriptor space. Range-based = hyperrectangle; leverage-based = an ellipsoid via leverage h_i; distance-based = union of balls; density-based = high-density region of a fitted distribution.
- **Structural vs statistical:** Both. Range and distance are statistical (over training descriptors); leverage is structural (geometric in feature space); density is statistical with a structural model.
- **Set/envelope flavor:** This is the field that most explicitly uses the word "envelope." Predictions for queries *outside* the AD are reported as unreliable.

### 4.3 Key citations

1. OECD. *Guidance Document on the Validation of (Quantitative) Structure-Activity Relationship [(Q)SAR] Models.* OECD Environment Health and Safety Publications, Series on Testing and Assessment No. 69, 2007. (The five OECD principles, including Principle 3 on AD.)
2. Sahigara, F., Mansouri, K., Ballabio, D., Mauri, A., Consonni, V., and Todeschini, R. "Comparison of different approaches to define the applicability domain of QSAR models." *Molecules* 17(5):4791-4810, 2012.
3. Jaworska, J., Nikolova-Jeliazkova, N., and Aldenberg, T. "QSAR applicability domain estimation by projection of the training set in descriptor space: a review." *ATLA — Alternatives to Laboratory Animals* 33(5):445-459, 2005. *(verify exact pagination; review well-attested.)*
4. Netzeva, T. I., et al. "Current status of methods for defining the applicability domain of (quantitative) structure-activity relationships." *ATLA* 33(2):155-173, 2005. *(verify exact pagination.)*
5. Gramatica, P. "Principles of QSAR models validation: internal and external." *QSAR & Combinatorial Science* 26(5):694-701, 2007. *(Williams plot and leverage approach.)*

### 4.4 Strengths and weaknesses for D_r

**Strengths.**
- Most disciplined regulatory analog: OECD requires AD declaration *as a precondition for model acceptance*. Same regulatory pattern AI Circuit Breaker is targeting.
- Multiple compatible formalizations (range, distance, leverage, density) provide a menu rather than a single forced choice.
- Leverage-based AD is *geometrically interpretable* in the same way Wymore morphisms are — could plausibly compose with D_s.
- Williams plot is a precedent for a 2D visualization (leverage × standardized residual) that mirrors a (D_r, D_b) plot exactly.

**Weaknesses.**
- AD is defined on input *descriptors*, not on model behavior. Translating to deep models with learned representations is non-trivial (though feature-space Mahalanobis OOD is essentially the same idea).
- AD in QSAR is usually static (computed once on training set). D_r may need to be context-dependent: "the right context for this query *now*."
- The field's safety stakes are lower than autonomy/medicine; reviewers may not weight this analog heavily unless paired with a higher-stakes domain.

---

## 5. Envelope of Validity in Control / Aerospace V&V

### 5.1 Construct summary

In aerospace and control, the **flight envelope** is the region of state space (altitude, airspeed, load factor, angle of attack, …) within which an aircraft can safely operate. Adjacent to this is the **model validation envelope** in computational V&V: the subset of conditions where the model has been validated against experimental data. Roy and Oberkampf (2011) provide the most cited modern framework: predictions inside the validation envelope inherit measured model-form uncertainty; predictions outside require *extrapolation* of uncertainty, with explicitly increased uncertainty bounds. NASA-STD-7009 institutionalizes this in a credibility-assessment scale (0-4) tracking how far a simulation result is from validated experimental conditions.

### 5.2 Formalization

- **Type:** Set in operational state space (flight envelope) + **uncertainty bound** that grows as the query moves away from validated points (Roy-Oberkampf).
- **Structural vs statistical:** Structural for the envelope itself; statistical for the uncertainty bound.
- **Set/envelope flavor:** Explicit — this is where the word "envelope" comes from. With an extrapolation function attached.

### 5.3 Key citations

1. Roy, C. J., and Oberkampf, W. L. "A comprehensive framework for verification, validation, and uncertainty quantification in scientific computing." *Computer Methods in Applied Mechanics and Engineering* 200(25-28):2131-2144, 2011.
2. Oberkampf, W. L., and Roy, C. J. *Verification and Validation in Scientific Computing.* Cambridge University Press, 2010 (expanded 2nd ed. 2023).
3. NASA. *NASA-STD-7009A: Standard for Models and Simulations.* NASA Office of the Chief Engineer, 2016 (rev. B 2024). *Credibility Assessment Scale.*
4. AIAA. *AIAA G-077-1998: Guide for the Verification and Validation of Computational Fluid Dynamics Simulations.* (Foundational community standard predating ASME V&V 10.) *(verify, well-attested.)*
5. Trujillo, M. F., and Pantano, C. "Quantification of model uncertainty in aerodynamic simulations." (Representative of flight-envelope V&V practice.) *(verify; field is well-established but I cannot confidently attribute a single canonical paper.)*

### 5.4 Strengths and weaknesses for D_r

**Strengths.**
- Provides the *strongest precedent* for an explicit envelope with attached uncertainty growth — Roy-Oberkampf's extrapolation framework is a direct template for D_r as "distance from validated context."
- Distance-from-envelope can be a true metric, compatible with the metrological framing AI Circuit Breaker uses (GUM).
- NASA-STD-7009's credibility-scale lineage is structurally similar to AI Circuit Breaker's intent: a measurement-grade scale of model trustworthiness, decomposed into specific dimensions.

**Weaknesses.**
- Aerospace/control envelopes are defined on *low-dimensional physical state spaces*. AI deployment contexts are high-dimensional, semantic, and often non-metric.
- The framework assumes you can identify validated conditions experimentally. For AI, the "validated conditions" are the training set, which is implicit and high-dimensional.
- Extrapolation uncertainty growth is well-defined only when you have a parametric model form to extrapolate; deep nets do not provide this cleanly.

---

## 6. Assume-Guarantee Contracts in Formal Verification

### 6.1 Construct summary

In formal methods, a contract is a pair (A, G) of an **assume clause** (precondition on the environment / inputs) and a **guarantee clause** (postcondition the component delivers when the assumption holds). Assume-guarantee reasoning composes contracts so that system-level guarantees follow from component-level ones, provided each component's assumptions are discharged by neighboring components' guarantees. Benveniste et al.'s 2018 monograph (*Foundations and Trends in EDA*) is the canonical modern treatment, unifying assume-guarantee, interface theories, and rely-guarantee under a single meta-theory.

### 6.2 Formalization

- **Type:** **Predicate** (the assume clause). Logical, not statistical: either the environment satisfies A or it doesn't. Refined into temporal-logic formulas (LTL, MTL) for reactive systems.
- **Structural vs statistical:** Structural-logical. Contracts are first-class artifacts in the system architecture.
- **Set/envelope flavor:** The set of environments satisfying A. Contracts compose set-theoretically; refinement is set inclusion.

### 6.3 Key citations

1. Benveniste, A., Caillaud, B., Nickovic, D., Passerone, R., Raclet, J.-B., Reinkemeier, P., Sangiovanni-Vincentelli, A., Damm, W., Henzinger, T. A., and Larsen, K. G. "Contracts for system design." *Foundations and Trends in Electronic Design Automation* 12(2-3):124-400, 2018.
2. Meyer, B. "Applying 'design by contract.'" *IEEE Computer* 25(10):40-51, 1992. *(Eiffel-era origin of the contract programming pattern.)*
3. Jones, C. B. "Tentative steps toward a development method for interfering programs." *ACM TOPLAS* 5(4):596-619, 1983. *(Rely-guarantee.)*
4. Sangiovanni-Vincentelli, A., Damm, W., and Passerone, R. "Taming Dr. Frankenstein: contract-based design for cyber-physical systems." *European Journal of Control* 18(3):217-238, 2012.
5. Platzer, A. *Logical Foundations of Cyber-Physical Systems.* Springer, 2018. (KeYmaera-X, differential dynamic logic with assumed initial regions.)

### 6.4 Strengths and weaknesses for D_r

**Strengths.**
- *Conceptually exactly* the right framing: the assume clause is the precondition for model validity. If the assumption fails, the guarantee is voided. This matches Paul's intuition that D_r is conceptually different from D_s/D_b: it is the *precondition*, not the *quality of the morphism itself*.
- Composable: contracts at component level compose to system level. AI Circuit Breaker's eventual claim could be that AI components carry assume clauses (D_r predicates) and the SE-level safety case discharges them.
- Logical clarity: avoids the metric-conflation problem that putting D_r on the same axis as D_s/D_b would create.

**Weaknesses.**
- Predicates, not distances. AI Circuit Breaker has so far been a measurement framework (continuous scale, GUM uncertainty); pure predicates do not compose cleanly with this.
- Real AI environments are statistical and ill-specified; writing a temporal-logic assume clause for "image taken with the right camera in the right lighting for the right diagnosis" is not feasible in practice.
- Probabilistic contracts (Saoud, Sangiovanni-Vincentelli) exist but are less standardized; the field is open here, which is also an opportunity.

---

## 7. Domain of Validity in Scientific Model V&V (ASME / NASA)

### 7.1 Construct summary

The V&V community distinguishes the **calibration domain** (the region of inputs where the model has been tuned to experimental data) from the **prediction domain** (the region where the model is being used to make predictions). ASME V&V 10 (computational solid mechanics, 2006/2019), ASME V&V 40 (medical devices, 2018), and NASA-STD-7009 codify this distinction and require credibility/risk assessments commensurate with the distance between the two. V&V 40 in particular is explicit: credibility of a computational model must be commensurate with (a) the model's influence on the decision and (b) the consequence of an incorrect decision — both modulated by the prediction domain's distance from the validation domain.

### 7.2 Formalization

- **Type:** Two sets (calibration domain, prediction domain) plus a relationship between them. Encoded operationally as a multi-dimensional **credibility-assessment matrix** (NASA-STD-7009: 0-4 scale across 8 factors; V&V 40: similar matrix across categories like verification, validation, applicability).
- **Structural vs statistical:** Structural (domain definitions) + statistical (uncertainty quantification within the validated domain).
- **Set/envelope flavor:** Set, but with explicit "distance" treated through the credibility scale and uncertainty extrapolation.

### 7.3 Key citations

1. ASME. *V&V 10-2019: Standard for Verification and Validation in Computational Solid Mechanics.* ASME, 2019 (orig. 2006).
2. ASME. *V&V 40-2018: Assessing Credibility of Computational Modeling through Verification and Validation: Application to Medical Devices.* ASME, 2018.
3. NASA. *NASA-STD-7009A: Standard for Models and Simulations.* (See section 5.)
4. Pathmanathan, P., et al. "Credibility assessment of computational models according to ASME V&V 40." Several application papers, 2017-2023.
5. Mongiardini, M., et al. "Credibility assessment of models and simulations based on NASA's Models and Simulation Standard using the Delphi method." *Systems Engineering* 17(4):450-466, 2014. *(Cross-references NASA-STD-7009 into SE; useful for the SE-journal target venue.)*

### 7.4 Strengths and weaknesses for D_r

**Strengths.**
- ASME V&V 40 is, structurally, the *closest standard* to what AI Circuit Breaker is trying to be. Its calibration / prediction domain split *is* the D_s/D_b vs D_r split, almost word for word.
- Already accepted by FDA for medical-device computational models — strong regulatory precedent and a venue (FDA testbed) that aligns with the ECG case study.
- Risk-informed: credibility *must* be commensurate with risk, which mirrors the AI Circuit Breaker philosophy that trust is decision-contingent.

**Weaknesses.**
- The framework is *process-oriented* (a credibility matrix to be filled out by humans) more than a runtime computable metric. AI Circuit Breaker needs runtime computation.
- The domains are typically declared, not inferred. Same limitation as ODD.
- ASME V&V 40's matrix categories are not orthogonal in the way (D_s, D_b) are; adopting wholesale would weaken the parsimony of the AI Circuit Breaker measurand.

---

## 8. Distributional Robustness / Shift-Aware Certification

### 8.1 Construct summary

Distributionally robust optimization (DRO) trains a model to minimize worst-case loss over a ball of distributions (typically Wasserstein or KL) around the empirical training distribution. Sinha, Namkoong, and Duchi's 2018 ICLR paper certifies robustness within a Wasserstein ball. Conformal prediction under covariate shift (Tibshirani, Foygel Barber, Candes, Ramdas, NeurIPS 2019) provides distribution-free prediction intervals that remain valid when the deployment distribution differs from training, *provided the likelihood ratio is known or estimable*. These give the field its sharpest formal statement of "how far can the deployment context shift before guarantees break?"

### 8.2 Formalization

- **Type:** **Distance** in distribution space (Wasserstein, KL, or chi-squared ball radius). Predictions carry a *certificate* valid for any deployment distribution within that ball.
- **Structural vs statistical:** Statistical, but with rigorous worst-case structural guarantees.
- **Set/envelope flavor:** Envelope in the space of distributions (not the space of inputs).

### 8.3 Key citations

1. Sinha, A., Namkoong, H., and Duchi, J. "Certifying some distributional robustness with principled adversarial training." ICLR 2018 (arXiv:1710.10571).
2. Tibshirani, R. J., Foygel Barber, R., Candes, E. J., and Ramdas, A. "Conformal prediction under covariate shift." NeurIPS 2019 (arXiv:1904.06019).
3. Duchi, J. C., and Namkoong, H. "Learning models with uniform performance via distributionally robust optimization." *Annals of Statistics* 49(3):1378-1406, 2021.
4. Esfahani, P. M., and Kuhn, D. "Data-driven distributionally robust optimization using the Wasserstein metric." *Mathematical Programming* 171(1):115-166, 2018.
5. Cauchois, M., Gupta, S., Ali, A., and Duchi, J. "Robust validation: confident predictions even when distributions shift." arXiv:2008.04267, 2020-2024 (JASA, 2024). *(verify final venue.)*

### 8.4 Strengths and weaknesses for D_r

**Strengths.**
- Provides the **most rigorous quantitative bridge** between training distribution and deployment context. The Wasserstein radius is, in effect, a D_r.
- Already aligns with metrological framing (uncertainty bounds, certificates).
- Conformal-under-shift gives a calibrated coverage probability — a number directly comparable to the D_s, D_b interval.

**Weaknesses.**
- Wasserstein balls are agnostic to the *semantics* of the shift. A small Wasserstein distance in pixel space may correspond to a catastrophic semantic context change.
- Likelihood ratios are rarely known in practice; the certificates degrade gracefully but are not free.
- The framework is most natural for marginal-distribution shift (covariate), less so for shift in P(Y|X) or in operational task.

---

## 9. Coverage Measures in Safety Cases

### 9.1 Construct summary

In safety-case practice (Goal Structuring Notation GSN, Claims-Arguments-Evidence CAE), the safety case argues that a system is acceptably safe. The argument explicitly bounds itself to a scope (Context elements in GSN), and reviewers ask "how much of the operational space does the evidence cover?" Scenario-coverage metrics in autonomous-vehicle safety cases (Koopman and Wagner 2016; Koopman 2020-2022 series) try to quantify what fraction of the ODD is exercised by test scenarios.

### 9.2 Formalization

- **Type:** **Coverage** = fraction (or fraction-with-uncertainty) of an operational space that is supported by evidence. Practically: a ratio scenarios_tested / scenarios_required.
- **Structural vs statistical:** Both. Structural in GSN (Context nodes scope the argument); statistical in coverage measurement.
- **Set/envelope flavor:** A set (the scoped operational space) with a measure on it; coverage = measure of evidenced subset.

### 9.3 Key citations

1. Kelly, T. P. "Arguing safety — A systematic approach to managing safety cases." PhD thesis, University of York, 1998. (GSN origin.)
2. Weaver, R. A., and Kelly, T. P. "The goal structuring notation — A safety argument notation." *Proceedings of the Dependable Systems and Networks 2004 Workshop on Assurance Cases*, 2004.
3. Bishop, P., and Bloomfield, R. "A methodology for safety case development." *Safety-Critical Systems Symposium*, 1998. (CAE origin.) Followed by Bloomfield, R., and Netkachova, K. "Building blocks for assurance cases." 2014.
4. Koopman, P., and Wagner, M. "Challenges in autonomous vehicle testing and validation." SAE 2016.
5. SCSC Assurance Case Working Group. *Goal Structuring Notation Community Standard, Version 3.* Safety-Critical Systems Club, 2021. *(verify exact version year; standard is well-attested.)*
6. Salay, R., and Czarnecki, K. "Using machine learning safely in automotive software: An assessment and adaption of software process requirements in ISO 26262." arXiv:1808.01614, 2018 *(verify exact arXiv ID)*; and Salay, R., Queiroz, R., and Czarnecki, K. "An analysis of ISO 26262: Using machine learning safely in automotive software." SAE Technical Paper 2018-01-1075, 2018.

### 9.4 Strengths and weaknesses for D_r

**Strengths.**
- Coverage is a natural complement to a distance: distance tells you "how far from training," coverage tells you "how much of where we will actually operate is supported." These are dual, not redundant.
- GSN's Context-node concept matches Paul's intuition that "scope of validity" is a separate ontological category from "morphism quality."
- Coverage measures are already required artifacts in regulated AI domains (FDA SaMD guidance, EASA AI Roadmap), strong reviewer alignment.

**Weaknesses.**
- Coverage is a **set-level / population-level** metric, while D_r as Wallk proposed it is per-inference. Different granularity.
- GSN coverage is qualitative as often as quantitative; turning it into a [0,1] scalar that composes with D_s, D_b requires care.
- The link from coverage to per-instance trustworthiness is not direct; coverage answers "should we trust this *deployment*," not "should we trust this *inference.*"

---

## 10. Wymore-Specific: Morphism-Theoretic Scope of Validity

### 10.1 Construct summary

Wymore's 1993 *Model-Based Systems Engineering* and the surrounding T3SD (Tricotyledon Theory of System Design) literature gives morphisms — primarily homomorphisms between systems — as the central mathematical object linking design specifications to realizations. The T3SD framework explicitly distinguishes the **Functionality space**, **Buildability space**, and **Implementability space** (the implementable designs being those buildable designs that map functionally to functional requirements). DEVS extensions (Zeigler, Praehofer, Kim 2000; Zeigler-Muzy-Kofman 2018) refine this with a system specification hierarchy where homomorphisms across levels carry validity conditions. The closest Wymore-native treatment of "scope" is the requirement that the homomorphism's *commutativity diagram* be satisfied — and this is conditional on the input set, state set, and output set being correctly specified for the operational context.

### 10.2 Formalization

- **Type:** Set-theoretic. A morphism h: S → R holds over specified input/state/output sets. Scope of validity = the input/state subsets on which the commutativity is asserted.
- **Structural vs statistical:** **Purely structural.** Wymore's framework is pre-statistical; uncertainty/probability are not first-class.
- **Set/envelope flavor:** Set. The triple (Z_in, Z_state, Z_out) defines the scope; the morphism's domain is exactly this triple.

### 10.3 Key citations

1. Wymore, A. W. *Model-Based Systems Engineering: An Introduction to the Mathematical Theory of Discrete Systems and to the Tricotyledon Theory of System Design.* CRC Press, 1993.
2. Wach, P., et al. (CSER 2026). *Toward a Library of Isomorphic Patterns for Systems Engineering.* (Author's own line; degree-of-homomorphism metric.)
3. Zeigler, B. P., Muzy, A., and Kofman, E. *Theory of Modeling and Simulation: Discrete Event & Iterative System Computational Foundations.* Academic Press, 3rd ed., 2018.
4. Zeigler, B. P., Koertje, C., and Zanni, C. "The utility of homomorphism concepts in simulation: building families of models from base-lumped model pairs." *Simulation* 100(11), 2024.
5. Saadawi, H. (or Wainer's group). "Conjoining Wymore's systems theoretic framework and the DEVS modeling formalism: toward scientific foundations for MBSE." *Applied Sciences* 11(11):4936, 2021. *(verify lead author.)*

### 10.4 Strengths and weaknesses for D_r

**Strengths.**
- The native vocabulary of the AI Circuit Breaker. D_r in Wymore-native form would be a *scope predicate on the morphism's domain* — a clean construct that does not pollute the morphism-quality measurand.
- The T3SD distinction (Functionality/Buildability/Implementability spaces) provides a precedent for layering: D_s and D_b live in the Functionality/Implementability comparison; D_r would live as a scope tag on the comparison itself.
- DEVS hierarchies make explicit that homomorphisms at one level carry preconditions inherited from upper levels — exactly the assume-guarantee pattern, in Wymore-compatible form.

**Weaknesses.**
- Wymore does *not* provide a continuous metric for scope. He gives set membership, not distance.
- The CSER 2025 / CSER 2026 lineage already uses "degree of homomorphism" for the structural axis (D_s); reusing morphism vocabulary for D_r risks confusion.
- Statistical operational context (medical imaging across hospitals, LLM deployment across user populations) is not naturally captured in Wymore's set-theoretic frame. Augmentation is needed.

---

## 11. Summary Table

| # | Field | Construct type | Formalization | Structural vs Statistical | Per-inference? | Fit for D_r intent |
|---|---|---|---|---|---|---|
| 1 | ODD (J3016, ISO 21448, PAS 1883) | Predicate over taxonomy | In/out of declared set | Structural (declarative) | Yes, with runtime sensors | **High** for declared scope; weak as a runnable distance |
| 2 | OOD detection | Score → predicate | Distance in feature space; energy; MSP | Statistical | Yes | Medium; statistical, not contextual |
| 3 | Dataset shift / concept drift | Predicate on distributions; distances (KL, MMD, Wasserstein) | P_train vs P_deploy | Statistical (with structural taxonomy) | Mostly population-level | **High** as taxonomy; medium as per-inference |
| 4 | Applicability Domain (QSAR) | Set/envelope in descriptor space | Range, leverage, distance, density | Both | Yes (per-query leverage) | **High**; regulatory analog, multiple formalizations |
| 5 | Validation envelope (V&V, flight) | Set + extrapolation of uncertainty | Roy-Oberkampf extrapolation; flight envelope | Both | Yes (compute distance from validated points) | **High**; precedent for distance + uncertainty |
| 6 | Assume-guarantee contracts | Logical predicate | (A, G) clauses | Structural-logical | Yes | **Conceptually best fit;** but pure predicate, not metric |
| 7 | ASME V&V 10/40, NASA-STD-7009 | Set pair + credibility matrix | Calibration vs prediction domain | Both, process-oriented | No (process artifact) | **High** as regulatory template; weak as runtime metric |
| 8 | Distributional robustness | Distance in distribution space | Wasserstein/KL ball radius | Statistical | Yes (for the certificate) | **High** for shift-certification; semantic-agnostic |
| 9 | Coverage in safety cases (GSN/CAE) | Coverage measure on operational space | scenarios_tested / scenarios_required | Both | No (population-level) | Medium; right ontological role, wrong granularity |
| 10 | Wymore / DEVS morphism scope | Set membership on morphism domain | (Z_in, Z_state, Z_out) triple | Structural | Yes (in principle) | Native vocabulary; lacks a continuous metric |

---

## 12. Closest Existing Formalizations

Three candidates the AI Circuit Breaker could stand on, with brief argument for each. (No recommendation among them — that is the construct analyst's call.)

### Candidate A. **Applicability Domain (leverage-based, QSAR) extended to learned feature space**

The leverage-based AD computes h_i = x_i^T (X^T X)^{-1} x_i and flags h_i > h* = 3p/n as out-of-domain. In a deep model, "x_i" is the learned feature vector. This is mathematically identical to the Mahalanobis-distance OOD score (Lee et al. 2018), and *also* identical to a Wymore-compatible scope predicate when h* is interpreted as the boundary of the morphism's declared domain. The Williams plot (leverage × residual) is a direct 2D precedent for a (D_r, D_b) plot. Regulatory backing exists (OECD principle 3). Weakness: it is fundamentally a property of inputs, not of operational task.

### Candidate B. **ASME V&V 40 calibration-domain / prediction-domain distinction, lifted to AI**

V&V 40's risk-informed credibility framework already operationalizes the very split Paul is drawing: model-fidelity dimensions (calibration, validation) are conceptually orthogonal to applicability dimensions (prediction-domain distance, decision consequence). D_s and D_b would map to credibility-of-fidelity; D_r would map to applicability. FDA has already accepted this framework for medical-device computational models — direct regulatory transfer for the ECG testbed. Weakness: V&V 40 is a process matrix, not a runtime number.

### Candidate C. **Assume-Guarantee contracts with Wasserstein-ball relaxation**

Treat D_r as the assume clause of the AI component's contract, but quantified: instead of "the environment satisfies A," the assume clause states "the deployment distribution P lies within Wasserstein distance epsilon of the training distribution." This combines Benveniste et al.'s contract framework with Sinha-Namkoong-Duchi's certifiable robustness. The output is a number (epsilon) that is composable both with safety-case arguments (predicate flavor when epsilon exceeds a threshold) and with the metrological framing (epsilon is a distance). Weakness: Wasserstein in raw input space is semantically opaque; would need a learned representation to be meaningful.

---

## 13. Open Ground (Novelty Opportunities)

Places where the AI Circuit Breaker's intended D_r does not map cleanly to any existing construct.

1. **Per-inference, semantic, task-aware scope.** All ten fields give either (a) per-inference distance/score in input or feature space (OOD, AD, DRO) without task-awareness, or (b) population-level, task-aware scope (ODD, GSN coverage, V&V 40) without per-inference numbers. The *combination* — a per-inference D_r that is sensitive to whether the *task* the AI is being asked to perform is the task it was trained for — appears to be open ground. This is precisely Wallk's failure mode: well-calibrated to training task, wrong task at deployment.

2. **Morphism-theoretic scope with a continuous degradation metric.** Wymore gives binary set membership. The CSER 2025/2026 line gives a *degree* of homomorphism for the morphism's quality (D_s). A corresponding *degree of scope match* — a continuous measure of how far the deployment scope deviates from the morphism's declared domain, in Wymore-compatible vocabulary — is not, to my reading, formalized in the existing Wymore/DEVS literature. There is a parallel paper opportunity here.

3. **Three-way separation: morphism quality vs scope vs decision consequence.** ASME V&V 40 separates fidelity and applicability but folds in decision consequence as a third dimension. AI Circuit Breaker currently has D_s, D_b (fidelity); D_r (scope) would be the second. A *fourth* axis for decision consequence — already implicit in the V&V 40 risk matrix — is plausibly part of the same construct family but is *not* what Wallk is proposing. Flagging because reviewers may push for it.

4. **Composition rule across multiple AI components.** Assume-guarantee gives composition of predicates; metric DRO does not give clean composition of robustness radii across components. AI Circuit Breaker is being framed as a portfolio-scale capability (multiple AI components in regulated stacks); a *composition rule for D_r across components* is not standardized anywhere I surveyed. This is genuine open ground and matches the SE-level positioning AI Circuit Breaker is targeting.

5. **D_r as a coverage measure on (D_s, D_b) quality, not on inputs.** Re-frame: instead of "how far from training context," ask "what fraction of operationally relevant contexts have been measured at acceptable D_s, D_b?" This re-routes D_r through coverage (Section 9) rather than distance, and may sidestep the conflation problem entirely. Not in the surveyed literature in this form.

---

## 14. Critical Citations (likely reviewer-cited for or against D_r)

The 5-10 papers most likely to come up when reviewers respond to any D_r formalization. Listed with the reason each is critical.

1. **Hendrycks and Gimpel, ICLR 2017 (arXiv:1610.02136).** The MSP baseline. Any new score will be benchmarked against this. *Defensive citation.*
2. **Lee et al., NeurIPS 2018.** Mahalanobis-distance OOD in feature space. Mathematically equivalent to leverage AD. *Direct comparator if D_r is distance-based.*
3. **Tibshirani, Foygel Barber, Candes, Ramdas, NeurIPS 2019.** Conformal prediction under covariate shift. The state-of-the-art for shift-aware certification with finite-sample coverage. *Reviewer will ask how D_r relates to this.*
4. **Sinha, Namkoong, Duchi, ICLR 2018.** Certifiable distributional robustness via Wasserstein. *Reviewer will ask: why not just use a Wasserstein radius?*
5. **Sahigara et al., *Molecules* 2012.** AD review. Regulatory precedent (OECD); leverage / Williams plot. *Reviewer in any regulatory-AI venue will know this.*
6. **Moreno-Torres et al., *Pattern Recognition* 2012.** Unifying view on dataset shift. *Reviewer will use this to test whether D_r conflates covariate / label / concept shift.*
7. **Roy and Oberkampf, *CMAME* 2011.** Comprehensive V&V/UQ framework with explicit prediction-domain extrapolation. *Reviewer in a metrology or SE venue will use this as the comparator.*
8. **ASME V&V 40-2018.** Medical-device computational model credibility. *FDA-aligned reviewers will cite this; if D_r ignores it, expect a reviewer comment.*
9. **Benveniste et al., *Foundations and Trends in EDA* 2018.** Contracts for system design. *Formal-methods reviewer will ask why D_r isn't an assume clause.*
10. **Wymore, *Model-Based Systems Engineering* 1993.** Author's own framework. Any D_r proposed *must* be defensible against Wymore-native readers (Salado, Bahill lineage). *Mandatory grounding citation.*

---

## 15. Notes on confidence

- **High-confidence verified citations** (verified DOI / publisher / arXiv page in this session): items in Sections 1-3, 5-8 are largely verified.
- **`(verify)` flags** on a small number of items where the work is well-attested in the field but I could not confidently attribute a specific paper-author-venue tuple in this session. Authors at UA library should verify before drafting.
- **Notable absence I did not pursue.** Anomaly detection in time-series industrial monitoring (e.g., Chandola, Banerjee, Kumar 2009 ACM CSUR survey) overlaps with OOD and could be a tenth field; I omitted it because it does not add a distinct formalization beyond what OOD and concept drift already provide.
- **Notable absence I flag for v0.2.** Causal-inference treatments of out-of-domain generalization (Peters, Buhlmann, Meinshausen "Causal inference using invariant prediction" JRSS-B 2016; Arjovsky et al. "Invariant Risk Minimization" 2019). These offer a structurally different formalization of "right context" through invariance under environment, which I would add in v0.2 if requested.
