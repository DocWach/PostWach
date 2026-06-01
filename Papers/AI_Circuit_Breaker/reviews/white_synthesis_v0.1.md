# White Synthesis — RBW Adjudication of Abstract v0.2

**Inputs:** `red_team_v0.2.md`, `blue_team_v0.2.md`, `lit_review_scoping_v0.1.md`, `claim_ledger_v0.2.md`.
**Output:** revision directives for `Wach_Wallk_AICircuitBreaker_Abstract_v0.3.md`.

## Convergence between Red and Blue

Both teams, working independently from the same claim ledger, flagged the same five items for rework:

| ID | Issue | Red severity | Blue verdict | White directive |
|----|------|--------------|--------------|-----------------|
| C1 | "cannot currently measure" is hyperbolic | Major | Narrow to "lacks a shared continuous calibrated measurement" | Narrow + acknowledge NIST AI RMF, ISO/IEC 42001, AMLAS, runtime assurance as adjacent prior work; reposition CB as composition, not replacement |
| C15 | Composition theorem as stated is wrong in general | Major | No prior theorem located; treat as proposition to prove | Reword as "we propose and establish (proof in extended treatment)" and state the 1-Lipschitz assumption explicitly for the D_b bound |
| C22 | "100,858 beat annotations" does not match the canonical count | Minor | Narrow to "~110,000 reference annotations" | Accept Blue wording |
| C31, C32 | "First time" / "nobody applies GUM to AI" is falsified by Martin 2024 (*Measurement*) and Nanomanufacturing & Metrology 2025 | Fatal | Hedge with "to our knowledge"; position adjacent not identical | Hedge + cite the adjacent work + claim the tighter contribution: GUM-in-an-SE-venue-for-AI-trust, not GUM-for-ML-in-general |
| C34, C40 | Reference [10] conflates CISA ZTMM (5 pillars + 3 cross-cutting) with DoD ZT RA (7 pillars); "Visibility and Analytics" is a cross-cutting capability, not a pillar, in CISA's model | Major | Replace with NSA CSI *Advancing Zero Trust Maturity Throughout the Visibility and Analytics Pillar* (May 2024) | Accept; drop "Pillar 7" phrasing; use "the Visibility and Analytics capability within Zero Trust architectures" and cite the NSA CSI |

## Lit-review-driven additions

The scoping review identified the SPC dimension as empty across all eight target SE venues (Wiley SE journal, Wiley INSIGHT, Wiley INCOSE IS, IEEE OJSE, NPS Acquisition Research Symposium, NDIA Mission/SE conferences, CSER, SERC AI4SE workshop). This is the single strongest defensibility argument and should be surfaced explicitly as the primary contribution claim.

Nearest-neighbor papers to cite for positioning:

- **McDermott, Clifford, Beling, Blackburn, DeLaurentis (2020) INSIGHT, "Artificial Intelligence and Future of Systems Engineering"** — the community-authoritative problem framing. Citing it signals CB is responding to, not ignoring, the AI4SE research agenda.
- **Freeman (2020) INSIGHT, "Test and Evaluation for Artificial Intelligence"** — the canonical SE-venue statement that T&E for AI is a measurement problem. Directly supports the CB thesis framing.
- **Zeller (2023) INCOSE IS, "Safety Assurance of ML-Based Autonomous Systems"** — nearest industrial-MBSA neighbor; lets CB position as complement, not replacement.
- **Schierman et al. (2020) JGCD, "Runtime Assurance for Autonomous Aerospace Systems"** — engineering template for the breaker mechanism.
- **McDermott, Pepe, Clifford (2024) INCOSE IS, "Updated AI4SE Research Roadmap"** — most recent community gap synthesis.

## Reference accuracy fixes

- Ref [10] Zero Trust citation: replace "NSA/CISA Zero Trust Maturity Model, Pillar 7" with the correct document.
- Ref [5] CSER 2025 STcP MVP: Blue noted this needs a venue DOI once the proceedings are indexed; acceptable as published author-attested.
- Ref [4] CSER 2026: mark as "forthcoming" pending submission outcome.
- Ref [7] PTB-XL: keep record count 21,837; drop the patient count to avoid the 18,869 vs 18,885 discrepancy across sources.

## Internal-artifact hygiene (R016 tagging)

- Wallk TDD v2.0 is a research artifact (a). The 99.67% / 98.92% numbers remain plausible but internally attested. For a sponsor-ready abstract, supplement with an external ECG-ML benchmark (Hannun et al. 2019, *Nature Medicine*) so the baseline comparison rests on a peer-reviewed anchor.
- CBTO counts (25 classes, 20 object properties, etc.) are from the design spec; verify against the live CBTO file before final submission of the abstract.
- Runtime latency target (< 25 ms at 40 Hz) is aspirational; keep phrasing as "target" not "achieved."

## Claims that can stand as-is

- C2 (prior-work framing): exact titles and dates of NIST AI RMF 1.0, ISO/IEC 42001:2023, and EU Regulation 2024/1689 are verified — drop in.
- C7 (Wymore + GUM): both foundational cites verified.
- C10, C11, C12 (formal definitions of D_s, D_b, orthogonality): traceable to Wach 2022 dissertation and CSER 2025 STcP MVP.
- C13 (scope limitation already added to v0.2): retained.
- C14 (MSD/RLC canonical exemplar): traceable to CSER 2026 and supported by Olson 1943, Firestone 1933, Karnopp et al. 2012.
- C16, C17 (SPC 25-subgroup, Western Electric, CUSUM): Montgomery *Introduction to Statistical Quality Control* covers all three; Page 1954 is the CUSUM origin.
- C21, C24 (PTB-XL record count, AF clinical criteria): both verified.
- C35, C38, C39 (self-lineage + dataset references): verified.

## Claims to retire

None. All claims can be salvaged with narrowing, hedging, or citation.

## Contribution statement for v0.3

Moved from implicit to explicit in the opening of the Key Advancements section:

> The primary contribution of this work is the composition of three research traditions — Wymorian systems-theoretic morphisms, GUM-based measurement uncertainty, and statistical process control — into a single measurement instrument for AI trustworthiness, situated inside a target SE venue where, to our scoping review's knowledge, the SPC dimension has not previously been represented.

## Action items for v0.3

1. Rewrite opening paragraph per C1 directive.
2. Replace C15 composition-theorem prose with proposition + 1-Lipschitz qualifier.
3. Hedge C31/C32 novelty claims; cite Martin 2024 as adjacent.
4. Replace ZT Pillar 7 prose + fix Ref [10].
5. Change PTB-XL patient count to record count only.
6. Change MIT-BIH beat count to "~110,000 reference annotations."
7. Add Hannun 2019 external anchor for the ECG baseline.
8. Add McDermott 2020, Freeman 2020, Zeller 2023, Schierman 2020 citations in the right places.
9. Add an explicit contribution paragraph per above.
10. Tag CSER 2026 as forthcoming.
