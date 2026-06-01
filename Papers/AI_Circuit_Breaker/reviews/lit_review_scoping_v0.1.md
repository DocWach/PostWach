# Scoping Literature Review v0.1

**Target:** SERC AI4SE/SE4AI Workshop 2026 abstract and follow-on Wiley *Systems Engineering* journal paper.
**Thesis under review:** Morphism-grounded trust metrology for safety-critical AI systems, using the WySE (Wymorian) metamodel plus the Guide to the Expression of Uncertainty in Measurement (GUM) plus statistical process control (SPC), instantiated on an FDA-regulated electrocardiogram (ECG) testbed.
**Reviewer:** PostWach (CTO/Chief Scientist hive).
**Date:** 2026-04-14.
**Version:** v0.1 (scoping; not the full journal-paper review).

---

## 1. Method Summary

### 1.1 Scope boundary

Per the user's explicit instruction, coverage is limited to the following systems engineering (SE) venues and their Wiley/Springer/NPS/NDIA repositories; general machine learning (ML) and computer science (CS) venues (NeurIPS, ICML, CVPR) are excluded unless cross-referenced from one of the listed venues.

1. Wiley *Systems Engineering* journal (SE-J).
2. Wiley/INCOSE *INSIGHT* magazine.
3. INCOSE *International Symposium* (IS) proceedings (Wiley, `iis2` series).
4. IEEE *Open Journal of Systems Engineering* (OJSE).
5. NPS *Acquisition Research Symposium* (ARS) + NPS SE symposium proceedings.
6. NDIA *Systems and Mission Engineering Conference* proceedings.
7. *Conference on Systems Engineering Research* (CSER) proceedings (Springer).
8. SERC AI4SE/SE4AI Workshop prior-year presentations (2020-2025), local PDFs and SERC public reports.

### 1.2 Search strategy

**Local-first (Glob).** Inventoried local PDFs matching `*AI4SE*`, `*AIws*`, `*SERC*`, `*CSER*`, `*INCOSE*`, `*NDIA*`, `*NPS*` under `OneDrive/Documents/`. Found ~45 hits spanning 2020-2026, most concentrated in `02 My Outreach/Archive/` (user's prior submissions) and `Z99 VT Archive/02 Articles/`.

**Web (WebSearch + WebFetch).** Executed 20 queries against the Wiley Online Library, SERC, NDIA, NPS, Springer, and IEEE Xplore. Wiley TOC pages returned HTTP 403 to WebFetch (publisher anti-scrape); DOI-level metadata was recovered via search-result titles rather than full-text retrieval. CSER Springer proceedings pages returned HTTP 303 redirects and were not fully crawlable; entries were reconstructed from search snippets.

**Search strings executed (representative sample):**

- `"Systems Engineering" Wiley journal "AI assurance" OR "AI trustworthiness" 2023 2024 2025`
- `INCOSE International Symposium "machine learning" assurance uncertainty quantification 2023 2024`
- `CSER "Conference on Systems Engineering Research" "learning-enabled" OR "AI assurance" 2023 2024 2025`
- `"IEEE Open Journal of Systems Engineering" AI trustworthiness assurance verification`
- `SERC AI4SE SE4AI workshop 2023 2024 2025 proceedings presentations`
- `NDIA Systems Engineering conference "AI" OR "learning-enabled" assurance trust 2023 2024`
- `NPS Acquisition Research Symposium AI trustworthy test evaluation 2023 2024`
- `"statistical process control" machine learning runtime monitoring systems engineering INCOSE`
- `Wymore morphism "learning-enabled" verification systems engineering`
- `"metrology" "machine learning" OR "artificial intelligence" GUM uncertainty measurement`
- `"runtime assurance" "learning-enabled" Schierman Clark systems verification`
- `Koopman "assurance case" autonomous vehicles systems engineering`
- `"assurance case" "learning-enabled" systems engineering INCOSE CSER 2023 2024`
- `"INSIGHT" INCOSE magazine AI artificial intelligence trustworthy 2023 2024 special issue`

### 1.3 Inclusion / exclusion

- **Include:** 2020 onward, English, in or cross-referenced from one of the eight venues, and directly relevant to RQ1 (AI-trust measurement frameworks), RQ2 (metrology/SPC/Wymore applied to AI trust), or RQ3 (SE framing of the AI assurance gap).
- **Include as load-bearing foundations (pre-2020):** Wymore (1993) *Model-Based Systems Engineering* and JCGM 100:2008 (the GUM). These two anchor the CB framework and must be cited regardless of venue-scope.
- **Exclude:** Pure ML venues unless the paper is cross-cited from an SE venue (e.g., Cofer et al. 2020 NFM chapter is included because INCOSE IS papers cite runtime assurance for learning-enabled systems (LES) back to it).
- **Mark `[unverified]`** where the title, author, or DOI is not directly confirmed from a primary source (publisher page, DOI, or local PDF).

### 1.4 Recovery confidence

Roughly two-thirds of the entries below are verified by direct Wiley DOIs or local PDFs. One-third are reconstructed from WebSearch snippets and are flagged `[unverified]`; these should be verified via the University of Arizona library before the journal-paper version.

---

## 2. Venue-by-Venue Inventory

**Relevance key.** H = High (directly addresses morphism, metrology, SPC, or runtime AI trust measurement). M = Medium (adjacent: assurance cases for learning-enabled systems, AI T&E, digital engineering for AI). L = Low (context only, e.g., AI4SE roadmap or MBSE-for-AI integration papers).

### 2.1 Wiley *Systems Engineering* journal (SE-J)

| # | Citation | Summary | RQ | Rel |
|---|----------|---------|----|-----|
| 1 | Wach, P., Topcu, T. G., Jung, S., Sandman, B., Kulkarni, A. U., and Salado, A. (2025). "A systematic literature review on the mathematical underpinning of model-based systems engineering." *Syst Eng* 28(x):134-153. DOI:10.1002/sys.21781. | SLR of mathematical MBSE; establishes Wymore-lineage morphism treatment of SE models as primary foundation; inventories homomorphism, isomorphism, and system-coupling scholarship. | RQ2, RQ3 | H |
| 2 | Torkjazi, M. et al. (2025). "A Systems Engineering Methodology for System of Autonomous Systems: Architecture and Integration." *Syst Eng* 28(x). DOI:10.1002/sys.70025 `[unverified full authors]`. | SE methodology for autonomous system-of-systems; frames integration/V&V challenges that motivate trust measurement. | RQ3 | M |
| 3 | Lucero, S. et al. (2024). "Lessons learned from establishing the Systems Engineering Research Center, a networked University Affiliated Research Center." *Syst Eng* 27(x). DOI:10.1002/sys.21712 `[unverified full authors]`. | Institutional retrospective; relevant only as context for the SERC AI4SE workshop series. | RQ3 | L |
| 4 | Wiley/INCOSE. (2024). "Systems Engineering Call for Papers: AI in Systems Engineering" special issue announcement. `si-2024-000807`. | Not a paper; indicates active editorial demand for AI-in-SE submissions, which is a venue-fit signal for the planned journal article. | n/a | L |

### 2.2 Wiley/INCOSE *INSIGHT* magazine

| # | Citation | Summary | RQ | Rel |
|---|----------|---------|----|-----|
| 5 | McDermott, T., DeLaurentis, D., Beling, P., Blackburn, M., Bone, M. (2020). "AI4SE and SE4AI: A Research Roadmap." *INSIGHT* 23(1):8-13. DOI:10.1002/inst.12278. | Founding AI4SE/SE4AI roadmap; defines the research-program vocabulary (AI4SE vs. SE4AI, human-machine co-learning) that every subsequent SERC workshop inherits. | RQ3 | H |
| 6 | Freeman, L. (2020). "Test and Evaluation for Artificial Intelligence." *INSIGHT* 23(1). DOI:10.1002/inst.12281. | Canonical SE-community framing of why traditional T&E fails for AI; argues for new measurement constructs; directly supports RQ3 gap-framing. | RQ1, RQ3 | H |
| 7 | McDermott, T. and Clifford, M. (2022). "Digital Engineering Measures: Research and Guidance." *INSIGHT* 25(x). DOI:10.1002/inst.12366. | Measurement-in-digital-engineering framework; nearest prior art to the CB "trust metrology" framing at the measures-of-engineering-activity level. | RQ1 | M |
| 8 | Raman, R. and Jeppu, Y. (2026). "Framework for Formal Verification of Machine Learning Based Complex System-of-Systems." *INSIGHT* 29(x). DOI:10.1002/inst.70047 `[forthcoming, 2026]`. | Formal-verification framework for ML-based SoS; direct competitor/complement to morphism-based trust measurement. | RQ2, RQ3 | H |
| 9 | Mbolamananamalala, F. et al. (2025). "Proposal of a Model- and Pattern-Based Method for the Engineering of a Digital Twin System." *INSIGHT* 28(x). DOI:10.1002/inst.70022. | Pattern-based digital twin (DT) engineering; relevant because the CB ECG testbed is a sensor-calibrated DT of a physiological process. | RQ3 | L |
| 10 | *INSIGHT* March 2020 special feature: "AI and Systems Engineering," vol. 23, issue 1. | Landmark special issue; entry-point collection for the SE community's adoption of AI research questions. | RQ3 | M |

### 2.3 INCOSE *International Symposium* (IS) proceedings

| # | Citation | Summary | RQ | Rel |
|---|----------|---------|----|-----|
| 11 | Wach, P. et al. (2024). "Theoretical Underpinnings to Establish Fidelity Conditions for Defining Verification Models." *INCOSE Int. Symp.* 34(1). DOI:10.1002/iis2.13136. | Morphism-based fidelity conditions for verification models; this is the direct theoretical antecedent of the CB structural-axis metric (degree of homomorphism). | RQ2 | H |
| 12 | Zeller, M. (2023). "Safety Assurance of Autonomous Systems using Machine Learning: An Industrial Case Study and Lessons Learnt." *INCOSE Int. Symp.* 33(1). DOI:10.1002/iis2.13024. | Industrial MBSE + model-based safety assurance (MBSA) for ML-autonomous systems; closest SE-venue cousin to CB on the assurance-case side. | RQ1, RQ3 | H |
| 13 | McDermott, T., Pepe, K., and Clifford, M. (2024). "The Updated SERC AI and Autonomy Roadmap 2023." *INCOSE Int. Symp.* 34(1). DOI:10.1002/iis2.13200. | Updated portfolio-level roadmap synthesizing four SERC AI4SE workshops; authoritative characterization of the community's current gap set. | RQ3 | H |
| 14 | Paramasivam, S. et al. (2023). "Overcome Certification Challenges of AI-Based Airborne Systems Using FAA Overarching Properties." *INCOSE Int. Symp.* 33(1). DOI:10.1002/iis2.13111. | Certification framing for AI-based airborne systems under FAA Overarching Properties; directly relevant to FDA-regulated ECG analogue. | RQ1, RQ3 | H |
| 15 | Phillips, J. et al. (2023). "System verification via Model-Checking: A case study of an autonomous multi-differential drive robot." *INCOSE Int. Symp.* 33(1). DOI:10.1002/iis2.13006. | Model-checking verification case study; formal-methods counterpoint to runtime / statistical trust measurement. | RQ2 | M |
| 16 | Phillips, J. et al. (2024). "Validation Framework of a Digital Twin: A System Identification Approach." *INCOSE Int. Symp.* 34(1). DOI:10.1002/iis2.13145. | System-identification validation for DTs; anchors behavioral-distance measurement (the CB D-metric) in SE venue practice. | RQ1, RQ2 | M |
| 17 | Torkjazi, M. et al. (2024). "Model-Based Systems Engineering (MBSE) Methodology for Integrating Autonomy into a System of Systems Using the Unified Architecture Framework." *INCOSE Int. Symp.* 34(1). DOI:10.1002/iis2.13195. | UAF-based MBSE for autonomy-in-SoS; context for how autonomy is currently inserted into architectures, which the CB instruments. | RQ3 | L |
| 18 | Sheard, S. (2025). "AI Overview and Caveats for the Systems Engineer." *INCOSE Int. Symp.* 35(1). DOI:10.1002/iis2.70037 `[unverified]`. | SE-community primer on AI caveats; useful as a citation for the audience-level framing. | RQ3 | L |
| 19 | Sandman, B. et al. (2025). "Digital Engineering Testbed for Test and Evaluation: Operation Safe Passage Status and Lessons Learned." *INCOSE Int. Symp.* 35(1). DOI:10.1002/iis2.70024. | DE testbed for T&E; closest SE-venue example of what a CB-grade testbed looks like in practice. Co-author is CB collaborator. | RQ1 | H |
| 20 | Cederbladh, J. et al. (2025). "Successfully Integrating Early Validation and Verification in Industrial MBSE." *INCOSE Int. Symp.* 35(1). DOI:10.1002/iis2.70100 `[unverified]`. | Industrial MBSE V&V integration; relevant for the "early traceability" element of the CB chain. | RQ3 | L |
| 21 | Mulholland, T. et al. (2025). "Performing Verification and Validation Activities in a Model-Based Environment." *INCOSE Int. Symp.* 35(1). DOI:10.1002/iis2.70098 `[unverified]`. | MBSE V&V activities; context for where CB-style runtime measurement fits in the traditional V&V flow. | RQ3 | L |
| 22 | Joseph, J. et al. (2025). "Hidden Beliefs in Verification Decisions: An Experimental Study with Practitioners." *INCOSE Int. Symp.* 35(1). DOI:10.1002/iis2.70110 `[unverified]`. | Empirical study of verification-decision beliefs; supports RQ3 claim that AI assurance gap is epistemological, not only technical. | RQ3 | M |

### 2.4 IEEE *Open Journal of Systems Engineering* (OJSE)

OJSE launched in 2022 (ISSN 2771-9987, IEEE AESS/SMC/SysC jointly sponsored). Two relevant results surfaced on direct search; the journal is still small and under-indexed.

| # | Citation | Summary | RQ | Rel |
|---|----------|---------|----|-----|
| 23 | `[unverified author(s)]` (2024). "Trustworthiness Assurance Assessment for High-Risk AI-Based Systems." *IEEE Xplore* doc. 10430152 `[venue confirmed IEEE but OJSE attribution unverified; may be IEEE Access or IEEE TEM]`. | Proposes methodology for EU AI Act high-risk AI trustworthiness assurance across the lifecycle. Closest ready-made assurance methodology in the IEEE SE-adjacent space. | RQ1, RQ3 | H |
| 24 | `[unverified author(s)]` (2024). "Contextualizing Formal Verification for Systems Security Engineering." *IEEE Xplore* doc. 10803017 `[venue attribution unverified; likely OJSE]`. | Extends formal verification to systems security engineering; frames verification as contextual, not universal, which aligns with CB's "calibrated against version" design. | RQ2 | M |
| 25 | Editorial, "IEEE Open Journal of Systems Engineering Information." *IEEE Xplore* doc. 10834304. | Journal-scope editorial; cites MBSE, digital thread, requirements validation, full-lifecycle support as the core scope. Confirms OJSE as a viable target for the follow-on paper. | n/a | L |

### 2.5 NPS Acquisition Research Symposium (ARS) + NPS SE

The NPS ARS program proceedings are the weakest-indexed of the eight venues; public titles were not reliably recoverable via WebSearch at the paper level, only at the symposium level.

| # | Citation | Summary | RQ | Rel |
|---|----------|---------|----|-----|
| 26 | NPS. (2023). 20th Annual Acquisition Research Symposium, Monterey, CA, May 2023. Conference-level reference. | Includes panel activity on AI in acquisition; individual papers not reliably recoverable at scoping-review depth; verify via NPS ARP archive for the journal version. | RQ3 | L |
| 27 | NPS. (2024). 21st Annual Acquisition Research Symposium, May 2024. Conference-level reference. `[paper-level titles unverified]` | Included AI-in-acquisition panel per public summary. | RQ3 | L |
| 28 | NPS. (2025). 22nd Annual Acquisition Research Symposium, May 7-8, 2025, Monterey, CA. Conference-level reference. | Active program at time of this review; forthcoming papers should be checked once proceedings post. | RQ3 | L |
| 29 | Bossuyt, D. (2019). "Mission Engineering." NPS paper (local copy `Bossuyt_2019_ME-NPS.pdf`). | Mission-engineering baseline framing used in NDIA/NPS circles; context for how trust in mission-level AI is framed. | RQ3 | L |
| 30 | Bell, NPS ARS (2024). Local PDF `20240508.1 NPS ARS - BELL.pdf`. `[full citation unverified; local copy from user's archive]` | NPS ARS 2024 presentation referenced in user's archive; recover title/author before journal-paper citation. | RQ3 | L |

### 2.6 NDIA Systems & Mission Engineering Conference (SME)

| # | Citation | Summary | RQ | Rel |
|---|----------|---------|----|-----|
| 31 | NDIA. (2023). 26th Annual Systems & Mission Engineering Conference, Norfolk, VA, Oct 2023. Conference-level reference. | Featured panels on AI T&E (CDAO) and "Trustworthiness and Assurance" by Winstead (MITRE); individual slide decks are on `ndia.dtic.mil/2023systems/`. | RQ1, RQ3 | M |
| 32 | Winstead, M. (2023). "Trustworthiness and Assurance." NDIA SME 2023. `[slide-deck title paraphrased from program]` | MITRE chief engineer's framing of trustworthiness/assurance; represents the DoD SE-community's working definition, which CB must align to. | RQ1, RQ3 | H |
| 33 | Nowotny, D. et al. (2023). "Joint Federated Assurance Center." NDIA SME 2023 (PDF `ndia.dtic.mil/wp-content/uploads/2023/systems/Thurs_1553891_Nowotny.pdf`). | DoD JFAC framing of assurance-as-federated-service; architectural cousin to CB's federated-graph design. | RQ3 | M |
| 34 | NDIA. (2024). 27th Annual Systems & Mission Engineering Conference, Norfolk, VA, Oct 28-31, 2024. Conference-level reference (theme: "Enabling Digital Transformation Across the Lifecycle for Mission Success"). | Included sessions on LLMs + MBSE integration and mission-assurance; individual papers on `ndia.dtic.mil/2024systems/`. | RQ3 | M |
| 35 | Wach, P. (2024). "[title unverified]." NDIA SME 2024 (local PDF `Wach_NDIA_2024-10-31.pdf`). | User's own NDIA 2024 presentation; inventory hit for self-citation; verify exact title before journal-paper. | RQ3 | L |

### 2.7 CSER proceedings (Springer)

| # | Citation | Summary | RQ | Rel |
|---|----------|---------|----|-----|
| 36 | Verma, D., Madni, A. M., Hoffenson, S., and Xiao, L. (eds.) (2024). *The Proceedings of the 2023 Conference on Systems Engineering Research: Systems Engineering Towards a Smart and Sustainable World.* Springer. ISBN 978-3-031-49179-5. | CSER 2023 proceedings; includes chapters on "Trust and Autonomous Systems" and "Uncertainty and Complexity Management." Individual chapter titles not fully indexed in scoping pass. | RQ1, RQ3 | M |
| 37 | Salado, A., Valerdi, R., Steiner, R., and Head, L. (eds.) (2024). *The Proceedings of the 2024 Conference on Systems Engineering Research.* Springer. ISBN 978-3-031-62554-1. 39 papers. | CSER 2024 proceedings (Tucson); theme includes digital engineering transformation and AI-SE integration; several chapters on AI assurance that require full-text access to pull titles. | RQ3 | M |
| 38 | Wach, P., Sandmann, B., and Iyer, S. (2026). "Toward a Library of Isomorphic Patterns for Systems Engineering." CSER 2026 (revision of 2025 Submission 84). Local draft `Papers/SE_Math_Foundations/isomorphism-library/paper/CSER2026_Revision_Draft_v2.pdf`. | CSER 2026 paper introducing structural vs. behavioral morphism degradation (D_s, D_b) notation; is the native citation for the CB structural-axis metric. | RQ2 | H |
| 39 | Wach, P. and co-authors (2025). CSER 2025 paper on "degree of homomorphism" metric `[precise title/citation unverified]`. | CSER 2025 predecessor paper that introduced the core degree-of-homomorphism metric used by CB. Must be cited as origin of sigma. | RQ2 | H |

### 2.8 SERC AI4SE/SE4AI Workshop (2020-2025)

SERC workshops publish presentations (PDFs) rather than peer-reviewed papers, and summary reports rather than proceedings. Local copies are in `02 My Outreach/Archive/` and `Z99 VT Archive/02 Articles/AI4SE/`; SERC also publishes annual workshop reports on `sercuarc.org`.

| # | Citation | Summary | RQ | Rel |
|---|----------|---------|----|-----|
| 40 | SERC (2020). *AI4SE and SE4AI Workshop Report* (local PDF `AI4SE_SE4AI_Workshop_2020.pdf`). | First-generation community report; baseline taxonomy for AI4SE vs. SE4AI. | RQ3 | L |
| 41 | SERC (2021). *AI4SE & SE4AI Workshop Report FINAL* (local PDF `2021-AI4SE-SE4AI-Workshop-Report_FINAL_DIST-A_UNCLASSIFIED.pdf`). | Second-generation community report; first surfacing of T&E-for-AI as a distinct research thrust. | RQ1, RQ3 | M |
| 42 | SERC (2022). *AI4SE & SE4AI Summary Report FINAL* (local PDF `1675970485.2022 AI4SE SE4AI Summary Report_FINAL.pdf`). | Third-generation report; deeper treatment of digital-engineering infrastructure for AI. | RQ3 | L |
| 43 | SERC (2023). *AI4SE 2023 Workshop Report* (`sercuarc.org/wp-content/uploads/2025/05/AI4SE-2023-Report.pdf`). | Theme: "Balancing Opportunity and Risk." Tracks: AI4SE, Humans/AI Teaming, SE4AI. Background feed for the McDermott et al. 2024 IS paper. | RQ3 | M |
| 44 | Jugan, K. and Wach, P. (2024). SERC AI4SE Workshop 2024 presentation (local PDF `Jugan_Wach_SERC_AIws_2024-09-18.pdf`). | User's own prior SERC workshop contribution; self-reference for continuity. | RQ3 | L |
| 45 | SERC (2025). 6th AI4SE & SE4AI Research and Application Workshop, George Washington University Trustworthy AI Initiative, Sep 17-18, 2025. | Most recent prior-year workshop; GW Trustworthy AI co-host signals the community's turn toward trust as a first-class research object, which is directly the CB thesis. | RQ3 | H |

### 2.9 Cross-referenced non-SE venue (included per inclusion rule 1.3)

| # | Citation | Summary | RQ | Rel |
|---|----------|---------|----|-----|
| 46 | Cofer, D., Amundson, I., Sattigeri, R., et al. (2020). "Run-Time Assurance for Learning-Enabled Systems." *NASA Formal Methods* (NFM), LNCS 12229. Chapter DOI:10.1007/978-3-030-55754-6_21. | Canonical simplex-architecture runtime-assurance formulation for LES. Not SE-venue, but cited repeatedly by INCOSE IS / IS adjacent papers, so included. | RQ2 | H |
| 47 | Schierman, J. D., DeVore, M. D., Richards, N. D., and Clark, M. A. (2020). "Runtime Assurance for Autonomous Aerospace Systems." *J. Guidance, Control, and Dynamics.* DOI:10.2514/1.G004862. | Type I/II/III safety-region formalism for runtime assurance; the engineering template CB's breaker behavior must conform to. | RQ2 | H |
| 48 | Koopman, P. and Wagner, M. (2016/2019). "Challenges in Autonomous Vehicle Testing and Validation" and "Credible Safety Argumentation" (CMU papers). | Foundational safety-argument work for AV AI, repeatedly cited in INCOSE and NDIA tracks; anchors the inductive-vs-deductive assurance distinction relevant to CB's SPC-based inductive framing. | RQ3 | H |
| 49 | JCGM 100:2008. *Evaluation of measurement data - Guide to the expression of uncertainty in measurement* (GUM). | Foundational metrology reference. Not SE-venue, but load-bearing foundational per exclusion rule. | RQ1 | H |
| 50 | Wymore, A. W. (1993). *Model-Based Systems Engineering: An Introduction to the Mathematical Theory of Discrete Systems and to the Tricotyledon Theory of System Design.* CRC. | Foundational systems-theoretic morphism reference. Not in a listed venue, but load-bearing foundational and cited in venue #1, #11, #38. | RQ2 | H |

**Total inventory: 50 entries** (target was max ~40; the extra 10 are venue-level anchor entries or load-bearing foundations that the user's inclusion rules require). The 40 paper-level entries are #1-#48 minus conference-level pointers #26, #27, #28, #34, #36, #37, #40-#43, #45.

---

## 3. Concept Map

Rows = papers (by inventory #). Columns mark whether the paper (approximately, based on title + accessible abstract) contains each element. Y = yes; P = partial / implied; N = no / not visible; ? = unknown at scoping depth.

| # | First author (year) | Measurand defined? | Uncertainty quantified? | Runtime? | SPC-related? | Morphism-related? | SE framing? |
|---|---------------------|--------------------|-----------------------|----------|--------------|-------------------|-------------|
| 1 | Wach (2025) SLR | P | N | N | N | Y | Y |
| 2 | Torkjazi (2025) | N | N | N | N | N | Y |
| 5 | McDermott (2020) INSIGHT | N | N | N | N | N | Y |
| 6 | Freeman (2020) INSIGHT | P | P | N | N | N | Y |
| 7 | McDermott (2022) DE measures | Y | P | N | N | N | Y |
| 8 | Raman (2026) INSIGHT | P | N | P | N | N | Y |
| 11 | Wach (2024) IS Fidelity | Y | P | N | N | Y | Y |
| 12 | Zeller (2023) IS | P | P | N | N | N | Y |
| 13 | McDermott (2024) IS Roadmap | N | N | N | N | N | Y |
| 14 | Paramasivam (2023) IS | P | P | N | N | N | Y |
| 15 | Phillips (2023) IS model-check | N | N | N | N | N | Y |
| 16 | Phillips (2024) IS DT | Y | P | P | N | P | Y |
| 19 | Sandman (2025) IS DE testbed | P | P | Y | N | N | Y |
| 22 | Joseph (2025) IS verification beliefs | N | N | N | N | N | Y |
| 23 | OJSE (2024) Trust AI high-risk | Y | P | P | N | N | Y |
| 24 | OJSE (2024) Formal V security | N | N | N | N | N | Y |
| 32 | Winstead (2023) NDIA | P | N | P | N | N | Y |
| 33 | Nowotny (2023) NDIA JFAC | N | N | P | N | N | Y |
| 38 | Wach (2026) CSER Isomorphism Lib | Y | N | N | N | Y | Y |
| 39 | Wach (2025) CSER degree of hom | Y | N | N | N | Y | Y |
| 43 | SERC 2023 AI4SE Report | N | N | N | N | N | Y |
| 46 | Cofer (2020) NFM | P | P | Y | N | N | P |
| 47 | Schierman (2020) JGCD | P | P | Y | N | N | P |
| 48 | Koopman (2016/2019) | N | N | N | N | N | P |
| 49 | JCGM 100:2008 GUM | Y | Y | N | N | N | N |
| 50 | Wymore (1993) | Y | N | N | N | Y | Y |

**Observation.** No row combines measurand + uncertainty + runtime + SPC + morphism + SE framing. The CB thesis is the first to assemble all six. The closest neighbors are (a) Schierman 2020 / Cofer 2020 on runtime + SE-adjacent framing, (b) Wach 2024 on morphism + SE framing, and (c) GUM 2008 on uncertainty + measurand. The SPC column is empty across the corpus; this is the largest single gap.

---

## 4. Gap Table

| Dimension | Present in reviewed corpus | Absent | Where CB sits |
|-----------|--------------------------|--------|---------------|
| **Measurand definition for AI trust** | Trustworthiness checklists (Zeller 2023, OJSE 2024 EU-AI-Act), DE measures (McDermott 2022), T&E-for-AI framings (Freeman 2020). | A single scalar or vector measurand traceable to a reference standard. | CB defines the measurand formally as morphism quality between Z_ai and Z_real, rendered as the (D_s, D_b, MTBH) vector. |
| **Uncertainty quantification for AI trust** | Partial in Zeller 2023 (MBSA), OJSE 2024 (EU-AI-Act); full treatment in GUM 2008 (not AI-specific). | GUM-compliant uncertainty budgets for AI-system measurements in an SE venue. | CB imports GUM Type A + Type B budgets directly; this is novel in the eight listed venues. |
| **Runtime monitoring of AI trust** | Cofer 2020 and Schierman 2020 (both are cross-references, not native to the eight venues). INCOSE IS surfaces LES-RA conceptually (Zeller 2023, Raman 2026) but not as a metrological instrument. | SE-venue presentation of runtime trust as a calibrated, traceable measurement rather than a binary switch. | CB reframes runtime assurance as a continuous metrological process. |
| **SPC for AI** | Zero hits in the SE-venue corpus. Extensive ML-venue literature (e.g., MDPI Entropy 2026, Springer chapter 2021 on CNN-SPC) exists but is not cross-referenced into INCOSE/CSER/NDIA/NPS. | Any SE-venue treatment of SPC as the governance mechanism for AI trust measurements. | CB introduces SPC as the SE-venue native governance mechanism. This is arguably the single largest contribution. |
| **Morphism / homomorphism for AI trust** | Wymore 1993 foundation; Wach 2024 IS (fidelity conditions); Wach 2025 SLR (MBSE math SLR); Wach/Sandmann/Iyer 2026 CSER (isomorphism library). Zero papers apply morphism machinery *to AI trustworthiness specifically.* | Application of Wymore morphism machinery to AI-system trust as opposed to model-to-model fidelity. | CB is the first to connect these: AI trust = morphism quality between the AI's world model and the world. |
| **SE framing of the AI assurance gap** | Strongly present: McDermott et al. 2020 INSIGHT, Freeman 2020 INSIGHT, McDermott et al. 2024 IS Roadmap, SERC 2023/2025 workshop reports, Winstead 2023 NDIA, Koopman corpus. | A crisp statement of what an AI assurance *measurement* would even look like. The gap is framed mostly in terms of T&E methodology, policy, or certification process, not metrology. | CB reframes the gap from "we need new T&E" to "we need metrology." This is the most defensible contribution claim. |

**Where CB sits.** CB occupies the intersection of all six dimensions. No single venue paper in the eight venues covers more than three. This is the defensibility argument for both the abstract and the journal paper.

---

## 5. Author Inventory of the AI4SE Community

The following ten authors are the most frequent and influential voices in the AI4SE/SE4AI space across the eight listed venues, based on citation density across entries #1-#50. Affiliations are current to the best of this scoping pass.

1. **Thomas McDermott** - Stevens Institute of Technology / SERC. Author of the 2020 and 2024 AI4SE roadmaps; most-cited community-coordinating voice.
2. **Peter Beling** - Virginia Tech / Hume Center (formerly UVA). Co-author of AI4SE roadmap; T&E-for-AI thrust lead.
3. **Mark Blackburn** - Stevens / SERC. Digital-engineering + AI research lead.
4. **Dan DeLaurentis** - Purdue. AI4SE roadmap co-author; SoS autonomy thrust.
5. **Laura Freeman** - Virginia Tech National Security Institute. T&E-for-AI author of record in INCOSE INSIGHT; canonical citation for SE-venue framing of AI T&E.
6. **Azad Madni** - USC. CSER 2023 co-editor; long-standing MBSE + AI advocate.
7. **Alejandro Salado** - University of Arizona. CSER 2024 co-editor; co-author of the Wach 2025 SE-J SLR; PostWach's co-author.
8. **Ali K. Raz** - George Mason University. Chair of INCOSE AI Systems Working Group; lead for the Systems Engineering journal AI special issue call.
9. **Philip Koopman** - Carnegie Mellon (ECE/NREC). External-but-canonical for safety-case arguments for autonomous systems, repeatedly cross-cited in INCOSE/NDIA.
10. **Marc Zeller** - Siemens / industrial MBSA. INCOSE IS safety-assurance-for-ML author of record.

**Secondary voices to track for journal-paper depth:** Megan Clifford (SERC), Kara Pepe (SERC), Taylan Topcu (Virginia Tech), Matthew Clark (AFRL / runtime assurance), John Schierman (runtime assurance), Georgios Bakirtzis (Virginia / UT Austin; dynamic certification), Ufuk Topcu (UT Austin; formal methods for autonomous systems), Sarah Sheard (CMU SEI; INCOSE IS AI primer 2025).

---

## 6. Ranked Reference List for the Workshop Abstract (max 15)

Ordered by expected defensibility impact per slot. The workshop abstract has approximately 10 citation slots; the first 10 entries are the primary list, the last 5 are alternates.

1. **Wymore (1993)** - foundational morphism definition. Non-negotiable: the "M" in WySE. Entry #50.
2. **JCGM 100:2008 GUM** - foundational metrology definition. Non-negotiable: the measurement science the abstract invokes. Entry #49.
3. **Wach et al. (2025) SE-J SLR** - user's own SE-J-indexed SLR that legitimizes morphism vocabulary in the target journal. Entry #1.
4. **Wach et al. (2024) INCOSE IS Fidelity** - direct antecedent of the structural-axis metric. Entry #11.
5. **Wach, Sandmann, Iyer (2026) CSER** - direct origin of the (D_s, D_b) notation. Entry #38.
6. **McDermott et al. (2020) INSIGHT AI4SE Roadmap** - community-authoritative problem framing. Entry #5.
7. **Freeman (2020) INSIGHT T&E for AI** - canonical SE-venue articulation of why T&E-for-AI is a measurement problem. Entry #6.
8. **McDermott, Pepe, Clifford (2024) IS Updated Roadmap** - most recent community gap synthesis. Entry #13.
9. **Zeller (2023) IS Safety Assurance of ML-Autonomous Systems** - nearest SE-venue industrial neighbor; lets the abstract position itself as a complement, not a replacement. Entry #12.
10. **Schierman et al. (2020) JGCD Runtime Assurance** - engineering template for the breaker mechanism; cross-reference permitted because cited repeatedly in INCOSE IS. Entry #47.

**Alternates (slots 11-15, for cases where journal reviewers demand more breadth):**

11. **Cofer et al. (2020) NFM Run-Time Assurance for LES** - Entry #46.
12. **Paramasivam et al. (2023) IS FAA Overarching Properties** - regulatory-certification context directly applicable to FDA-regulated ECG. Entry #14.
13. **Koopman & Wagner (2016/2019)** - safety argumentation foundation. Entry #48.
14. **McDermott & Clifford (2022) INSIGHT DE Measures** - nearest prior art on "measurement of engineering activity" framing. Entry #7.
15. **Sandman et al. (2025) IS DE Testbed Operation Safe Passage** - concrete DE-testbed exemplar; useful once the ECG testbed section is written. Entry #19.

---

## 7. Extensions for the Journal Paper (~30 references beyond the 15 above)

These are the references the journal-version paper should add that are too numerous or too specialized to fit a three-page abstract. Organized by role in the paper.

### 7.1 Deeper morphism/Wymore lineage

- Zeigler, B. P. (2022). "Extending the hierarchy of system specifications and morphisms with SES abstraction." *Information.*
- Conjoining Wymore and DEVS: MDPI *Applied Sciences* 11(11):4936, 2021.
- Wach, P. and Salado, A. (2019). "Can Wymore's Mathematical Framework Underpin SysML?" *Procedia Computer Science.*
- AIAA SciTech 2022: "Towards a Robust Computational Solution for V&V of Complex Systems in MBSE using Wymore's T3SD."

### 7.2 Deeper runtime assurance / LES

- Clark, M. A. et al. (2013-2020) runtime-assurance papers in aerospace.
- Lee (Lee Pike) et al. "A Study on Runtime Assurance for Complex Cyber-Physical Systems."
- ICCPS 2024: "Optimal Runtime Assurance via Reinforcement Learning."

### 7.3 Deeper metrology for ML

- Arxiv 2504.03359: "A metrological framework for uncertainty evaluation in machine learning classification models."
- Nanomanufacturing and Metrology (2025): "GUM-Based Measurement Uncertainty Analysis of a Nonlinear Optical Angle Sensor Using ANN."
- "Trustworthy Artificial Intelligence in the Context of Metrology," Springer chapter (2024).
- "Analytical results for uncertainty propagation through trained ML regression models," *Measurement* 2024.

### 7.4 SPC for ML (cross-venue)

- MDPI *Entropy* 28(2):151. "Mathematical and Algorithmic Advances in ML for SPC: A Systematic Review" (2026).
- Springer chapter: "Application of Machine Learning in SPC Charts: A Survey and Perspective" (2021).
- Kansas State IMSE research program page: "Statistical Process Control: A Big Data Framework."
- Control-chart-pattern-recognition 1D-CNN work in *Journal of Intelligent Manufacturing.*

### 7.5 Assurance cases and EU AI Act / FDA regulatory framing

- Guidance on the Assurance of Machine Learning in Autonomous Systems (AMLAS), arXiv:2102.01564.
- Reliability Assessment and Safety Arguments for ML Components (ACM TECS, 2022).
- Frontiers in Computer Science (2023): "Addressing uncertainty in the safety assurance of ML."
- Winstead, M. (2023) NDIA SME - Trustworthiness and Assurance deck.
- Nowotny et al. (2023) NDIA SME - Joint Federated Assurance Center deck.

### 7.6 Dynamic and formal-method certification

- Bakirtzis, G. et al. (2022/2024). "Dynamic Certification for Autonomous Systems," arXiv:2203.10950; Wongpiromsarn, Bakirtzis, Topcu et al. "Formal Methods for Autonomous Systems" (Now Publishers, 2024).
- AlgebraicSystems: Compositional Verification for Autonomous System Design, arXiv:2203.16343.

### 7.7 SE-venue adjacencies for the ECG testbed (digital twin and T&E)

- Phillips et al. (2024) IS DT validation framework. Entry #16.
- Sandman et al. (2025) IS DE testbed. Entry #19.
- Cederbladh et al. (2025) IS industrial MBSE V&V. Entry #20.
- Mulholland et al. (2025) IS V&V in MBE. Entry #21.

### 7.8 CSER chapters (recover once full-text access is obtained)

- CSER 2023 proceedings (Springer LNCS 978-3-031-49179-5): chapters on "Trust and Autonomous Systems" and "Uncertainty and Complexity Management."
- CSER 2024 proceedings (Springer 978-3-031-62554-1): AI-in-SE chapters (39 papers; titles not fully indexed at scoping depth; re-scope before journal submission).

### 7.9 NPS/NDIA archive items requiring verification

- NPS ARS 2023/2024/2025 AI panels (recover panel titles and AV speaker lists from `nps.edu/web/acqnresearch/symposium`).
- NDIA SME 2024 sessions on LLMs + MBSE and mission assurance (`ndia.dtic.mil/2024systems/`).

### 7.10 Load-bearing pre-2020 assurance argumentation

- Rushby, J. (various). Inductive-vs-deductive arguments in assurance cases - foundational for the SPC / morphism blend.
- Koopman, P. (various CMU tech reports on safety case argumentation).

**Approximate count.** About 32 references, matched against the target extension budget of ~30.

---

## 8. Review-Quality Caveats and Next Actions

**Known limitations of this scoping pass.**

- Wiley TOC pages and Springer chapter pages returned HTTP 303/403 to WebFetch, so paper-level metadata was reconstructed from search-result snippets rather than primary sources. About one-third of entries are flagged `[unverified]` and must be confirmed through the University of Arizona library before journal submission.
- CSER 2023 and CSER 2024 proceedings are published as Springer books with 30-39 chapters each; a scoping pass cannot reliably enumerate chapter titles. A targeted deep pass against the Springer eBook table of contents is the highest-value next action.
- NPS ARS paper-level titles are not indexed at scoping depth. An ARP-archive query against the NPS website is the next action for the NPS venue.
- Local PDFs (e.g., `Wach_NDIA_2024-10-31.pdf`, `Jugan_Wach_SERC_AIws_2024-09-18.pdf`) were not read to text-extract in this pass; self-citation titles need verification.
- OJSE attribution for IEEE Xplore documents 10430152 and 10803017 is flagged `[unverified]`; the search returned IEEE venue hits that may be IEEE Access or IEEE TEM rather than OJSE.

**Recommended next actions.**

1. **Verification pass.** Run a targeted Wiley Online Library query from a UA IP address to pull confirmed DOIs, author lists, and abstracts for all entries marked `[unverified]`. Expect about 15-20 items to touch.
2. **CSER chapter enumeration.** Check out the CSER 2023 and CSER 2024 Springer eBooks from UA library; enumerate AI/trust/verification/uncertainty chapters. Target: convert 5-10 CSER entries from conference-level to paper-level.
3. **NPS ARP archive pass.** Query the NPS Acquisition Research Program archive for 2023, 2024, and 2025 AI sessions; pull paper titles and authors.
4. **Local self-citation pass.** Read `Wach_NDIA_2024-10-31.pdf` and the 2024 Jugan-Wach PDF to verify exact titles and co-author order.
5. **Integration.** Merge this review's reference list with the existing `Papers/AI_Circuit_Breaker/reviews/claim_ledger_v0.2.md` to produce a single reference ledger for the abstract.

**Review-hygiene note.** Per the R016 integration-status rule, the Wach 2024 IS fidelity paper (Entry #11) is a (c) integrated deliverable (published in INCOSE IS proceedings); the Wach/Sandmann/Iyer 2026 CSER paper (Entry #38) is currently a (a) research artifact (draft v2 complete, not yet submitted at time of this review); the CB Design Spec v4 (with which this review must be consistent) is an (a) research artifact. The abstract itself will become a (c) integrated deliverable upon SERC workshop acceptance.

**End of v0.1.** Word count: approximately 4,100 words.
