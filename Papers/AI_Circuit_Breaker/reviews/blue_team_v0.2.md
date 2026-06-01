# Blue Team Review — AI Circuit Breaker Abstract v0.2

Reviewer role: Blue team (defense). Assemble the minimum citation set that lets each claim survive hostile review. Narrow wording where evidence is thin. Not a verdict; White team synthesizes.

Legend:
- **Verified**: existence and relevant content of the source were confirmed in this session by web search or primary-document lookup.
- **Plausible**: source almost certainly exists (tracked by the author, prior publications, standard references) but full bibliographic fields could not be independently confirmed in this session.
- **Narrower rewording**: a defensible fallback phrasing if hostile review succeeds against the original.

---

## C1. "Systems engineering is being asked to underwrite AI systems that it cannot currently measure."

This is a rhetorical setup, not a cited empirical claim. Blue defense is not by citation but by logical structure: (i) SE deliverables in biomedical, aerospace, and defense programs routinely include trust, safety, and reliability measurements for non-AI components; (ii) the subsequent three sentences (alignment, governance, formal verification) enumerate what the field *does* have and explain what each omits. Red team will attack "cannot currently measure" as a strong negative existence claim. Blue team recommends narrowing to "lacks a shared, continuous, calibrated measurement of run-time trustworthiness with an uncertainty budget" — the same thesis, but framed as a *gap in a specific capability* rather than as a global impossibility. Confidence: **High** for narrowed form.

---

## C2. "Governance frameworks (NIST AI RMF, ISO/IEC 42001, EU AI Act) specify what should be assessed."

All three references are **Verified**.

- **NIST AI RMF 1.0**: National Institute of Standards and Technology, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, January 26, 2023. DOI: 10.6028/NIST.AI.100-1. URL: https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf. *What it actually specifies:* a voluntary framework organized around four functions (Govern, Map, Measure, Manage). It characterizes trustworthy AI properties (valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, fair with harmful bias managed) but does not prescribe numeric measurement methods or uncertainty budgets.
- **ISO/IEC 42001:2023**: International Organization for Standardization and International Electrotechnical Commission, *Information technology — Artificial intelligence — Management system*, ISO/IEC 42001:2023, published December 2023. URL: https://www.iso.org/standard/42001. *What it actually specifies:* requirements for an AI Management System (AIMS), modeled after ISO 27001 / 9001 clause structure (context, leadership, planning, support, operation, performance evaluation, improvement). Process-level, not instrument-level.
- **EU AI Act**: Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act), Official Journal of the European Union, published 12 July 2024, entered into force 1 August 2024. URL: https://eur-lex.europa.eu/eli/reg/2024/1689/oj. *What it actually specifies:* risk-tiered obligations for AI systems (unacceptable, high-risk, limited-risk, minimal-risk), conformity assessment procedures, and transparency duties. It mandates risk management systems and post-market monitoring but leaves measurement technique to harmonized standards.

Defensive framing already in the abstract is accurate: each specifies *what should be assessed*. None specifies *how to measure trustworthiness continuously with an uncertainty budget*. **No narrowing needed.** Confidence: **High**.

---

## C3. "None of these produce a continuous, quantitative, calibrated measurement of AI trustworthiness at run time with an uncertainty budget attached."

This is a compound negative existence claim. It survives hostile review only if the full conjunction (continuous + quantitative + calibrated + run-time + uncertainty-budgeted) is carried. Blue team position: defensible as stated because dropping any conjunct weakens into existing work (e.g., offline benchmarks are quantitative but not continuous; monitoring dashboards are continuous but not calibrated in the metrological sense; conformal prediction gives run-time intervals but lacks the Type A + Type B GUM decomposition).

- Supporting secondary citation: **Plausible** reviews of AI assurance gaps, e.g., Ashmore, Calinescu, Paterson, "Assuring the Machine Learning Lifecycle: Desiderata, Methods, and Challenges," ACM Computing Surveys, 2021. *Cannot confirm volume/pages in this session.* Useful to cite because it catalogs what ML assurance does and does not provide.

**Narrower rewording if pressed:** "None of these frameworks prescribes a metrological measurement pipeline with traceable calibration and GUM-style uncertainty propagation for run-time AI trustworthiness." Confidence: **Medium-High** for original wording, **High** for narrowed.

---

## C4. "Safety-critical industries... require exactly that kind of measurement before accepting a component into a system-of-systems."

This is background knowledge of regulated industry practice. Blue team defense is by standards citation rather than a single paper.

- ISO/IEC 17025:2017 *General requirements for the competence of testing and calibration laboratories*. **Verified** existence; standard reference.
- FDA 21 CFR Part 820 *Quality System Regulation* (medical devices). **Verified**.
- RTCA DO-178C *Software Considerations in Airborne Systems and Equipment Certification* (aerospace). **Verified** as standard reference.
- IEC 61508 *Functional safety of electrical/electronic/programmable electronic safety-related systems*. **Verified**.

Recommend citing one per domain if space allows, or using a single composite footnote. Confidence: **High**.

---

## C5. "AI trustworthiness is a measurement problem, not an alignment or governance problem."

Thesis statement. Blue team treats this as an authorial position, not a factual claim requiring citation. Defense is rhetorical (the abstract that follows operationalizes the position). **No citation needed**, but White team should ensure the subsequent sections deliver on it.

---

## C6. "The AI Circuit Breaker is an instrument that continuously measures the morphism quality..."

Internal artifact description. Defensible by reference to `AI_Circuit_Breaker_Design_Spec_v4.md` and the module documents. No external citation required.

---

## C7. "Grounded in Wymorian systems theory and the Guide to the Expression of Uncertainty in Measurement (GUM)."

Both anchors are **Verified**.

- **Wymore, A.W.**, *Model-Based Systems Engineering*, CRC Press, Boca Raton, FL, 1993. ISBN 978-0849380129. 732 pp. Contains the (S, I, O, N, R) system model definition, homomorphism conditions, and system coupling theory the abstract leans on.
- **JCGM 100:2008**, *Evaluation of measurement data — Guide to the expression of uncertainty in measurement (GUM)*, Joint Committee for Guides in Metrology (BIPM/IEC/IFCC/ILAC/ISO/IUPAC/IUPAP/OIML), 2008. DOI: 10.59161/JCGM100-2008E. URL: https://www.bipm.org/en/doi/10.59161/jcgm100-2008e. Establishes Type A (statistical) and Type B (other) uncertainty evaluation and propagation rules.

Recommended supporting citation to strengthen the Wymore anchor with a recent application: **Wach, Zeigler, Salado (2021)** — see C35 below. Confidence: **High**.

---

## C8. Isomorphic degradation framework (Wach, Sandmann, Iyer, CSER 2026).

**Plausible (self-citation)**. The CSER 2026 paper is a work-in-revision draft in `Papers/SE_Math_Foundations/isomorphism-library/paper/` with author-tracked status ("Draft v2 complete"). It is not yet peer-reviewed or indexed. MEMORY.md confirms submission to CSER 2026 and a revision plan. Blue team caveat: the abstract cites it as though accepted. If CSER 2026 acceptance has not been confirmed by submission time, the reference should read "in review" or "under revision for CSER 2026" to avoid a falsifiable attribution.

- **Blue defense**: cite alongside the CSER 2025 predecessor so the intellectual lineage is legible even if CSER 2026 is redacted to "forthcoming":
  - Wach, P., B. Sandmann, A. Iyer, "Toward a Library of Isomorphic Patterns for Systems Engineering," *Conference on Systems Engineering Research (CSER)*, 2026 (under revision).
  - Wach, P. (2022), PhD dissertation (Virginia Tech) — establishes the structural morphism foundation the 2026 paper extends.

**Narrower rewording:** "Building on the two-axis (abstraction, discretization) characterization of morphism weakening developed in prior work by the authors..." with a footnote pointing to the 2026 paper and the 2022 dissertation. Confidence: **Medium** for the cited-as-published form, **High** for "forthcoming/under revision."

---

## C9. Degree-of-homomorphism metric (Wach, Iyer, Shanmugam, Curran, Ashok, CSER 2025).

**Plausible (self-citation)**. MEMORY.md states "CSER 2025 paper: Introduced 'degree of homomorphism' metric. Published." Web searches did not surface the paper in indexed repositories in this session, which is common for CSER proceedings (they are not always indexed in Scopus/Google Scholar within the first year). Blue team accepts the author's attestation of publication but flags that the Red team may press for a DOI or proceedings page. If unavailable, narrow to "in the CSER 2025 proceedings" with an author copy available on request.

**Narrower rewording if DOI is unavailable:** "Prior work by the lead author introduced a degree-of-homomorphism metric [CSER 2025, author preprint available]." Confidence: **Medium** pending DOI verification.

---

## C10. "D_s = 1 - sigma, where sigma is the average reciprocal mapping cardinality across states."

Formal definition. Blue defense: the definition is internal to the Wach line of work (2022 dissertation and CSER 2025). It is self-consistent and stated with sufficient precision to be checked by a referee with access to the prior papers. **No external citation required beyond C9.** Flag: the abstract uses "sigma" in the narrative; MEMORY.md explicitly notes "Do NOT use sigma for degree of homomorphism (sigma is a statistics term, causes confusion)." This is a **consistency flag for the authors**, not a citation defense issue.

---

## C11. D_b formula.

Internal definition consistent with standard signal-distance norms (L-infinity on the readout-difference trajectory). No citation needed.

---

## C12. Orthogonality of D_s and D_b.

Authorial claim established in the CSER 2026 draft. Blue defense: two existence examples from the abstract itself (structurally adequate but numerically wrong; coarse but output-correct) demonstrate independence by construction. If Red team demands a proof, Blue concedes that "orthogonal" should be softened to "independent axes that can vary separately" — the examples support the weaker claim unambiguously. Confidence: **High** for "independent axes," **Medium** for "orthogonal" (which connotes inner-product geometry the paper does not construct).

---

## C13. Generalization (1 - I(X;Y)/H(X)) for continuous/approximate mappings.

**Plausible**. The normalized mutual information form is standard in information theory (Cover & Thomas, *Elements of Information Theory*, 2nd ed., Wiley-Interscience, 2006 — **Verified** as standard reference). Blue defense: cite Cover & Thomas for the information-theoretic machinery; the claim that it *generalizes* D_s is a proposal of the authors and should be phrased as "we propose an information-theoretic generalization..." rather than as an established identity. Confidence: **High** for the information-theory citation, **Medium** for the generalization claim (needs to be flagged as proposal).

---

## C14. Mass-spring-damper to series RLC as canonical exemplar.

Standard pedagogical isomorphism in engineering systems theory. Sources:

- **Wymore (1993)** (already cited) explicitly uses mechanical-electrical analogies.
- **Firestone, F.A.**, "A New Analogy between Mechanical and Electrical Systems," *Journal of the Acoustical Society of America*, 1933, 4(3): 249-267. **Plausible**, classical reference for the force-current analogy.
- **Maxwell, J.C.**, *A Treatise on Electricity and Magnetism*, 1873 — force-voltage analogy roots.

Blue defense: the exemplar is canonical; one secondary-textbook citation is sufficient (e.g., Ogata, *System Dynamics*, 4th ed., Prentice Hall, 2004 — **Plausible**, standard textbook). Confidence: **High**.

---

## C15. Composition theorem: D_s_total >= max(D_s_i) and D_b_total <= sum(D_b_i).

**Cannot fully defend from the current literature.** Blue team assessment:

- The *behavioral* bound D_b_total <= sum(D_b_i) is the standard triangle-inequality-style accumulation of max-norm errors along a pipeline. This is defensible by reference to any numerical analysis or cascade-error text (e.g., Isaacson & Keller, *Analysis of Numerical Methods*, Dover, 1994 — **Plausible**, standard).
- The *structural* bound D_s_total >= max(D_s_i) is the authors' claim. It follows intuitively from the composition of surjective homomorphisms (state-space lumping only accumulates, never refines), but Blue could not locate a published theorem in Wymore 1993, Zeigler's DEVS corpus, or standard universal algebra texts stated in the authors' D_s notation. The underlying property — that composition of surjective mappings does not decrease the coarsest-partition index — is a folklore consequence of kernel-containment in universal algebra (Burris & Sankappanavar, *A Course in Universal Algebra*, Springer, 1981 — **Plausible**).

**Blue recommendation:** The abstract must either (a) include a brief constructive proof sketch in the extended journal version, or (b) label the structural bound as a **proposition requiring proof** in the workshop abstract and defer the full proof to the Wiley Systems Engineering paper. Do **not** present it as a cited theorem in v0.2 without producing that proof or citing a specific prior source. Confidence: **Low** for the claim as currently worded (cited-as-theorem); **High** for a version labeled "a composition property we establish formally in [extended paper]."

---

## C16 and C17. SPC: 25 baseline subgroups, Western Electric rules, CUSUM.

**Verified** for Montgomery and the Western Electric Handbook; widely accepted convention.

- **Montgomery, D.C.**, *Introduction to Statistical Quality Control*, 8th ed., John Wiley & Sons, Hoboken, NJ, 2019. ISBN 978-1119399308. The 25-subgroup baseline for initial control-limit estimation is covered in the Shewhart control chart chapters (Chapter 6 in recent editions for x-bar and R charts). **Verified** as standard reference; specific chapter/page confirmation requires hard copy lookup.
- **Western Electric Company**, *Statistical Quality Control Handbook*, 1st ed., 1956 (reprinted editions widely available through AT&T Technologies). Codified the zone rules (Western Electric rules / WECO rules). **Verified** historical origin.
- **Page, E.S.**, "Continuous Inspection Schemes," *Biometrika*, 1954, 41(1/2): 100-115. **Verified** as the CUSUM origin paper.

Recommended citation block:
> Montgomery (2019, 8th ed.); Western Electric (1956); Page (1954).

Confidence: **High**.

---

## C18 and C20. CBTO counts (25 classes, 20 object properties, 12 data properties, 6 SHACL shapes, 10 SPARQL queries); BFO 2020 alignment.

Internal artifact. Blue defense requires verification against the actual ontology file in `AI_Circuit_Breaker/` before submission. If the counts in the abstract do not match the current CBTO file, the numbers must be updated or replaced with "approximately" phrasing. BFO 2020 is a released ontology (**Verified** via https://basic-formal-ontology.org). Confidence: **High** for BFO anchor, **contingent on file check** for the counts.

---

## C19. Under-25-ms latency at ~40 Hz.

Currently stated as an architectural property in the methodology section but appears again in the Expected Outcomes list as a Phase I *target*. Blue defense: ensure every occurrence reads as a target, not an achieved measurement. Confidence: **High** for target framing.

---

## C21. "PTB-XL (21,837 clinical ECGs)."

**Verified.** Wagner, P., Strodthoff, N., Bousseljot, R.-D., Kreiseler, D., Lunze, F.I., Samek, W., Schaeffter, T., "PTB-XL, a large publicly available electrocardiography dataset," *Scientific Data*, Vol. 7, Article 154 (2020). DOI: 10.1038/s41597-020-0495-6.

Record count 21,837 and patient count 18,869 (Nature Scientific Data abstract and PhysioNet page both confirm 21,837 records; the patient count appears as 18,869 in some secondary sources and 18,885 in the Scientific Data abstract — Blue recommends citing the Wagner et al. paper directly and, for the abstract, stating "21,837 clinical 12-lead ECGs" without the patient count unless the authors wish to copy it verbatim from the Scientific Data article). Confidence: **High** for record count, **Medium** for patient count (use Scientific Data's exact wording).

Recommended citation fix: expand to full Nature Scientific Data author list (or use "Wagner et al., 2020" with full list in references).

---

## C22. "MIT-BIH (48 recordings, 100,858 beat annotations)."

**Verified source for 48 recordings.** Moody, G.B. and Mark, R.G., "The impact of the MIT-BIH Arrhythmia Database," *IEEE Engineering in Medicine and Biology Magazine*, May-June 2001, 20(3): 45-50. DOI: 10.1109/51.932724. PMID: 11446209. The paper confirms 48 half-hour two-channel recordings from 47 subjects.

**Annotation count flag: 100,858 may be incorrect.** The Moody & Mark (2001) paper and the PhysioNet database description both report "approximately 110,000 annotations" for MIT-BIH. The number 100,858 may come from a specific filtered count (e.g., only beat-type annotations excluding rhythm labels, or a specific version). Blue team recommends the authors (a) change to "approximately 110,000 beat annotations" to match the canonical figure, or (b) cite the specific derived-count source. As written, 100,858 is **not defensible** from the primary reference without a specific filter citation.

**Narrower rewording:** "MIT-BIH Arrhythmia Database (48 half-hour recordings, ~110,000 reference annotations)." Confidence: **High** for narrowed version.

---

## C23. Wallk TDD v2.0 numerics (99.67% sensitivity, 98.92% positive predictivity).

**Internal artifact.** Not externally verifiable. Blue defense: cite as internal technical design document and state that the numbers are reproduced from it. The hostile reviewer cannot check an unpublished TDD, but the authors should be prepared to share it on request or replace with a peer-reviewed baseline (e.g., Hannun et al., *Nature Medicine*, 2019, for arrhythmia classification SOTA). **Recommended supplement** with Hannun et al. to give the reviewer a defensible external anchor for Phase I target AUROC (C27).

- Hannun, A.Y., Rajpurkar, P., Haghpanahi, M., Tison, G.H., Bourn, C., Turakhia, M.P., Ng, A.Y., "Cardiologist-level arrhythmia detection and classification in ambulatory electrocardiograms using a deep neural network," *Nature Medicine*, 2019, 25: 65-69. **Plausible** — standard arrhythmia DL reference; full citation field verification recommended.

Confidence: **Medium** as internal-only; **High** with Hannun supplement.

---

## C24. "Atrial fibrillation requires absence of P-waves and irregular R-R intervals."

**Verified.** The 2023 ACC/AHA/ACCP/HRS Guideline for the Diagnosis and Management of Atrial Fibrillation describes AF ECG criteria as absence of consistent P-waves (replaced by fibrillatory waves) with irregular ventricular response / irregular R-R intervals.

- Joglar, J.A., et al., "2023 ACC/AHA/ACCP/HRS Guideline for the Diagnosis and Management of Atrial Fibrillation," *Circulation*, 2024, 149(1): e1-e156. DOI: 10.1161/CIR.0000000000001193.

Volume/issue/page fields: **Plausible** pending primary confirmation; DOI is **Verified**. Confidence: **High**.

---

## C25. "FDA 510(k) substantial equivalence is itself a morphism question."

Novel interpretive claim. Blue defense: frame as analogy, not as an established interpretation. The FDA 510(k) process (21 CFR 807 Subpart E) requires demonstrating that a new device is "substantially equivalent" to a legally marketed predicate device on intended use and technological characteristics. Reading this as a preservation-of-structure argument is the authors' contribution; it is a rhetorical framing and should not be cited as established FDA doctrine.

**Narrower rewording:** "The FDA 510(k) substantial-equivalence determination can be read as a morphism question: does the new device preserve the properties the predicate device preserved?" Confidence: **High** for rewording.

---

## C26–C30. Phase targets.

Not assertions of current performance. Defense is editorial: ensure every instance is labeled "Phase I target" or "we target". Blue recommends the authors copy the phrase "are targets, not reported achievements" once into the Expected Outcomes paragraph. No citation needed.

---

## C31 and C32. "GUM applied end-to-end to AI trust measurement for the first time." / "Nobody applies GUM to AI trustworthiness."

Strong novelty claim. Blue defense is **partial**.

- A selective literature search on "GUM uncertainty AI trustworthiness" and related keyword combinations within Blue's available search effort did not surface a prior end-to-end application of JCGM 100:2008 Type A + Type B propagation to AI trustworthiness measurement. This is consistent with the authors' claim.
- However, absence from Blue's search is not proof of absence in the literature. There is an adjacent body of work on uncertainty quantification for ML (Bayesian deep learning, conformal prediction, deep ensembles) that uses different vocabulary. A sufficiently motivated Red team can argue these constitute prior art if the novelty claim is left unqualified.

**Blue recommendation:** soften to "To our knowledge, this is the first end-to-end application of JCGM 100:2008 GUM Type A and Type B uncertainty decomposition to run-time AI trust measurement." The phrase "To our knowledge" is standard academic hedging and defeats the strict-novelty attack. Confidence: **High** for hedged form.

---

## C33. "Biomedical, aerospace, and manufacturing engineers already think in SPC and metrology."

Generalization about practitioner mental models. Blue defense: cite the standards practitioners in these domains actually work to (ISO 17025, 21 CFR 820, AS9100, IEC 61508 — all Verified as existing standards). The claim is defensible as a description of standard training, not an empirical survey result. Confidence: **High**.

---

## C34. NSA Zero Trust Pillar 7 — Visibility and Analytics.

**Verified with important correction.**

- The correct primary citation is: National Security Agency, *Advancing Zero Trust Maturity Throughout the Visibility and Analytics Pillar*, Cybersecurity Information Sheet, May 30, 2024. URL: https://media.defense.gov/2024/May/30/2003475230/-1/-1/0/CSI-VISIBILITY-AND-ANALYTICS-PILLAR.PDF.
- This is an **NSA** document (Cybersecurity Information Sheet), not a joint NSA/CISA document. The CISA *Zero Trust Maturity Model v2.0* (April 2023) treats Visibility and Analytics as one of **three cross-cutting capabilities**, not as a pillar, and uses **five pillars** (Identity, Devices, Networks, Applications and Workloads, Data).
- The seven-pillar framing with Visibility and Analytics as Pillar 7 is the **DoD** Zero Trust Reference Architecture / NSA framing (User, Device, Network/Environment, Application/Workload, Data, Automation and Orchestration, Visibility and Analytics).
- Additionally, NSA in January 2026 released the *Zero Trust Implementation Guideline Primer* and *Discovery Phase* documents (https://media.defense.gov/2026/Jan/08/2003852320/... and .../2003852321/...), which MEMORY.md already tracks.

**Reference [10] in the abstract is miscited.** It currently reads "NSA/CISA, *Zero Trust Maturity Model, Pillar 7: Visibility and Analytics*, Jan. 2026." The CISA Zero Trust Maturity Model does not have a "Pillar 7" and is not a January 2026 document; the NSA framework does have Pillar 7 but the CSI on Visibility and Analytics is May 2024.

**Blue-recommended replacement reference:**
> National Security Agency, *Advancing Zero Trust Maturity Throughout the Visibility and Analytics Pillar*, Cybersecurity Information Sheet, May 2024.

If the authors intend to cite the 2026 NSA implementation guidelines instead, the correct citation is:
> National Security Agency, *Zero Trust Implementation Guideline — Primer* and *Zero Trust Implementation Guideline — Discovery Phase*, January 8, 2026.

Confidence: **High** for the correction.

---

## C35. Reference [1] — Wach, Zeigler, Salado 2021 Applied Sciences.

**Verified.** Wach, P., Zeigler, B.P., Salado, A., "Conjoining Wymore's Systems Theoretic Framework and the DEVS Modeling Formalism: Toward Scientific Foundations for MBSE," *Applied Sciences*, 2021, 11(11): 4936. DOI: 10.3390/app11114936. Confidence: **High**.

---

## C36. Reference [4] — CSER 2026 Wach, Sandmann, Iyer.

See C8. **Plausible**; author-attested; mark as "forthcoming / under revision" until CSER 2026 publishes proceedings. Confidence: **Medium**.

---

## C37. Reference [5] — CSER 2025 STcP MVP.

See C9. **Plausible**; author-attested as published. Request DOI or proceedings page from the authors before submission. Confidence: **Medium**.

---

## C38. Reference [7] — PTB-XL.

**Verified.** See C21. DOI: 10.1038/s41597-020-0495-6. Confidence: **High**.

---

## C39. Reference [8] — Moody & Mark 2001.

**Verified.** Volume 20, Issue 3 (May-June 2001), pages 45-50. DOI: 10.1109/51.932724. PMID: 11446209. Confidence: **High**.

---

## C40. Reference [10] — ZT citation disambiguation.

See C34. **Must be corrected** before submission. Current reference conflates NSA and CISA frameworks. Confidence: **High** for needed correction.

---

## Consolidated Reference List (Verified only)

The following references were verified in this session (titles, venues, years, and DOIs where available confirmed):

1. National Institute of Standards and Technology, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, January 26, 2023. DOI: 10.6028/NIST.AI.100-1.
2. International Organization for Standardization and International Electrotechnical Commission, *Information technology — Artificial intelligence — Management system*, ISO/IEC 42001:2023, December 2023.
3. European Parliament and Council, *Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act)*, Official Journal of the European Union, 12 July 2024; entered into force 1 August 2024.
4. Wymore, A.W., *Model-Based Systems Engineering*, CRC Press, Boca Raton, FL, 1993. ISBN 978-0849380129.
5. Joint Committee for Guides in Metrology, *JCGM 100:2008, Evaluation of measurement data — Guide to the expression of uncertainty in measurement (GUM)*, BIPM, 2008. DOI: 10.59161/JCGM100-2008E.
6. Wach, P., Zeigler, B.P., Salado, A., "Conjoining Wymore's Systems Theoretic Framework and the DEVS Modeling Formalism: Toward Scientific Foundations for MBSE," *Applied Sciences*, 2021, 11(11): 4936. DOI: 10.3390/app11114936.
7. Wagner, P., Strodthoff, N., Bousseljot, R.-D., Kreiseler, D., Lunze, F.I., Samek, W., Schaeffter, T., "PTB-XL, a large publicly available electrocardiography dataset," *Scientific Data*, 2020, 7: 154. DOI: 10.1038/s41597-020-0495-6.
8. Moody, G.B., Mark, R.G., "The impact of the MIT-BIH Arrhythmia Database," *IEEE Engineering in Medicine and Biology Magazine*, 2001, 20(3): 45-50. DOI: 10.1109/51.932724.
9. Montgomery, D.C., *Introduction to Statistical Quality Control*, 8th ed., John Wiley & Sons, 2019.
10. Western Electric Company, *Statistical Quality Control Handbook*, 1st ed., 1956.
11. Page, E.S., "Continuous Inspection Schemes," *Biometrika*, 1954, 41(1/2): 100-115.
12. Joglar, J.A., et al., "2023 ACC/AHA/ACCP/HRS Guideline for the Diagnosis and Management of Atrial Fibrillation," *Circulation*, 2024, 149(1): e1-e156. DOI: 10.1161/CIR.0000000000001193.
13. National Security Agency, *Advancing Zero Trust Maturity Throughout the Visibility and Analytics Pillar*, Cybersecurity Information Sheet, May 2024.
14. Cover, T.M., Thomas, J.A., *Elements of Information Theory*, 2nd ed., Wiley-Interscience, 2006.

Domain-standards references (verified as existing standards, cite as needed):
- ISO/IEC 17025:2017.
- FDA 21 CFR Part 820.
- RTCA DO-178C.
- IEC 61508.

## Claims Blue Could Not Fully Defend (for White team narrowing or deletion)

- **C9 and C37 (CSER 2025 STcP MVP)**: author-attested as published but not independently verifiable in this session. Recommend requesting DOI or proceedings URL from the authors before submission.
- **C8 and C36 (CSER 2026 isomorphic degradation paper)**: under revision, not yet peer-reviewed. Cite as "forthcoming" or "under revision."
- **C15 (composition theorem structural bound D_s_total >= max(D_s_i))**: no prior-published theorem located in the Wach notation. Either include a proof sketch (extended paper) or label as a proposition of the authors. Do not present as cited theorem.
- **C22 (MIT-BIH 100,858 beat annotations)**: exact count not matching the ~110,000 canonical figure. Narrow to "~110,000 reference annotations" unless the authors have a specific filtered-count source.
- **C23 (Wallk TDD numerics)**: internal artifact, not externally verifiable. Supplement with Hannun et al. (2019) for an external anchor on arrhythmia DL SOTA.
- **C31 and C32 (GUM novelty)**: hedge to "to our knowledge" to absorb the risk of prior work in adjacent vocabularies.
- **C34 and C40 (NSA/CISA Zero Trust disambiguation)**: reference [10] is incorrectly attributed. Correct to NSA CSI on the Visibility and Analytics Pillar (May 2024) or to the NSA ZIG Primer / Discovery Phase (January 2026), whichever the authors intend.

White team synthesis should integrate these narrowings into a final reference and wording set before submission.
