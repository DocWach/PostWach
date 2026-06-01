# AI Circuit Breaker Testbed Strategy

**Status:** Planning document, research program artifact (not part of any single abstract or paper).
**Created:** 2026-04-21.
**Source:** Session archive `docs/session-archives/SESSION_ARCHIVE_2026-04-14_postwach-02.md`, decisions D11-D14.

## Purpose

The AI Circuit Breaker is framed for a Systems Engineering Research Center (SERC) / Department of Defense (DoD) audience, so the primary testbeds are cyber-physical system (CPS) security datasets rather than the original electrocardiogram (ECG) testbed. The strategy is layered: four distinct testbeds are evaluated, and each is chosen because it enables a distinctive research outcome that the others do not. The layering is a long-term research program artifact; the SERC workshop abstract (INF-2026-09) uses dataset-free domain-level language and does not name these testbeds directly.

## Design principle

Each testbed is admitted only if it carries a unique experimental payload. Redundancy is avoided. The strategy places each testbed against one specific pillar of the framework, with a clear distinction between primary validation beds and calibration or extension beds.

## Testbed matrix

| Testbed | Full name | Role | Distinctive outcome | Access |
|---|---|---|---|---|
| SWaT | Secure Water Treatment | Primary | Six-link observation-mediated morphism chain enabling composition-theorem validation (the core theoretical contribution of the framework) | iTrust Google Form request, approximately 3 business days, no cost, no redistribution permitted |
| ORNL PSAD | Oak Ridge National Laboratory Power System Attack Dataset | Primary alternate | Statistical process control (SPC) common-cause / special-cause dichotomy expressed natively in the data (not retrofit onto it) | Public download, no gating |
| TEP | Tennessee Eastman Process (simulator-based) | Calibration bench | Type A (statistical) and Type B (prior-knowledge) uncertainty budget validation against simulator ground truth; only testbed where ground truth is exact by construction | Open simulator, no cost |
| EPIC | Electric Power and Intelligent Control (iTrust) | Phase II extension | Cyclic-load operational windows that exercise allostatic (anticipatory) regulation, the bio-inspired Pillar 3 contribution; not replicable on the other three beds | iTrust Google Form request, same process as SWaT |

## Phase mapping

- **Phase I.** SWaT is the primary bed (or ORNL PSAD if the iTrust form is a blocker). Phase I objective is to demonstrate the chain-composition proposition on a real 6-link CPS pipeline.
- **Phase II.** EPIC is added to stress the allostatic regulation layer under cyclic-load windows. TEP is added in parallel to close the uncertainty budget with a ground-truth reference.
- **Phase III.** Domain-transfer cost analysis. The matrix above is itself Phase III evidence: four distinct CPS domains (water, power grid, chemical process, smart grid with cyclic loads) share the same framework with measurable porting cost per domain.

## Access status (as of 2026-04-21)

| Dataset | Gating | Action status |
|---|---|---|
| SWaT | iTrust Google Form, 3-day SLA | Decision pending: file now versus defer (D13 open item) |
| EPIC | iTrust Google Form, same process | Tied to SWaT decision |
| ORNL PSAD | Public | Available, no action required |
| TEP | Public simulator (MATLAB and Python re-implementations exist) | Available, no action required |

## Why not ECG only (for this venue)

The ECG testbed remains useful for the Food and Drug Administration (FDA) regulatory framing and is retained as a companion artifact, but it does not resonate with the SERC / DoD audience and does not exhibit the six-link morphism chain that the framework's composition theorem needs for empirical validation. CPS beds give both.

## Risks and fallbacks

- **SWaT access denied or delayed.** Fallback: ORNL PSAD as primary. Loses the six-link chain depth (ORNL is shallower in its observation-to-classification pipeline) but retains the core SPC contribution.
- **iTrust redistribution restriction** limits ability to ship derived datasets with the paper. Results and trained models can be released; raw data cannot. This shapes the reproducibility statement.
- **TEP is simulator-based**, so some reviewers will discount its results as "not real." Positioning: TEP's role is calibration of uncertainty budgets, not field-realistic performance claims.

## Open questions

1. File the iTrust SWaT access form now (3-day SLA) or defer until proposal stage (D13 open item)?
2. Does the EPIC cyclic-load story require separate physical-plant modeling to ground the allostatic regulation, or is the testbed's own instrumentation sufficient?
3. Is there a second ECG-tier biomedical testbed worth listing as a second Phase III domain-transfer target, or does the four-CPS matrix stand on its own?

## References to related artifacts

- SERC workshop abstract (dataset-free framing): `02 My Outreach/2026_SERC_AI4SE_SE4AI/Wach_Wallk_AICircuitBreaker_Abstract_v0.4.md`
- AI Circuit Breaker design spec v4 (CBTO inline, Appendix E): `Papers/AI_Circuit_Breaker/AI_Circuit_Breaker_Design_Spec_v4.md`
- Session archive with decision rationale: `docs/session-archives/SESSION_ARCHIVE_2026-04-14_postwach-02.md`
