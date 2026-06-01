# Side Note: WySE Metamodel Ontology Development

**Date.** 2026-05-20.
**Status.** Candidate ticket to GI-JOE. Not yet filed.
**Source.** Conversation thread on D_r systems-theoretic construct, 2026-05-20. Specifically the user's framing of point 1 in the discussion following synthesis_v2.md.

## What

The WySE Metamodel is, in current form, an informal top-level ontology of the systems engineering design process. It names problem spaces (system requirement, verification requirement) and the morphisms among them. The math (degree of homomorphism, behavioral preservation, chain bounds) is the formalization layered on top of this ontology; the ontology itself sits underneath the math and has not been formalized as such.

Proposed extension during the conversation: the WySE ontology should also include stakeholder needs problem spaces and validation problem spaces, which are problem spaces of outcomes (distinct from the system requirement and verification requirement problem spaces, which are problem spaces of input/output functions).

The pair of axes that fall out of this framing:
- WySE chain axis (role in design process): stakeholder need, system requirement, design, verification requirement, validation. Each role names a problem space.
- DEVS hierarchy axis (structural commitment level): Level 0 Observation Frame, Level 1 I/O Behavior, Level 2 I/O Function, Level 3 State Transition, Level 4 Coupled Component.
- A specific problem space is a (level, role) cell.

## Why it may be a GI-JOE ticket

GI-JOE owns the portfolio ontology infrastructure (TBox, ABox, SHACL, SPARQL CQs, ontology-gate enforcement) and has the working pattern for formalizing informal top-level ontologies into OWL 2 DL with validation. Formalizing the WySE Metamodel as a portfolio-level ontology would fit that workflow.

Candidate scope:
- TBox for the WySE Metamodel: classes for ProblemSpace, IOFunctionProblemSpace, OutcomeProblemSpace, StakeholderNeedProblemSpace, SystemRequirementProblemSpace, VerificationRequirementProblemSpace, ValidationProblemSpace; object properties for the chain of morphisms; data properties for problem-space attributes.
- Cross-axis with DEVS hierarchy: each ProblemSpace instance carries a specification level (Level 0 through 4 of the SSH).
- SHACL shapes for ontology consistency: a verification requirement problem space must be morphism-linked to a system requirement problem space, etc.
- SPARQL CQs: identify the problem-space chain for any system, identify gaps in the chain, identify morphisms whose quality is below threshold.

## Cross-references

- `Papers/AI_Circuit_Breaker/research/Dr_systems_theoretic/v2/synthesis_v2.md` Section 1.1 (corrected reading that WySE TTSD carries the context morphism at the design-time problem-space layer).
- `Papers/AI_Circuit_Breaker/research/Dr_systems_theoretic/v2/01_wyse_metamodel.md` (deep read of AIOS-WySE Part IV; missed the cross-problem-space machinery).
- `Papers/AIOS_WySE/paper/sections/part4_formal_foundations.md` (the AI-OS-specific instantiation that does not surface the cross-problem-space construct).
- Wymore 1993 *Model-Based Systems Engineering* (the foundational T3SD text; not directly read in either swarm).
- Salado 2018a and Salado 2021 (validation theory; flagged by user as not fully formalized; relevant to the validation problem space definition).
- GI-JOE Portfolio Ontology TBox, ABox, SHACL, SPARQL CQs (the working pattern this ticket would extend).

## Open items before filing

- Confirm with user whether this is the right time to file or whether the conversation on D_r should converge further first.
- Decide whether the WySE Metamodel ontology belongs in the existing portfolio-governance ontology (`GI-JOE/ontologies/domain/portfolio-governance.ttl`) or as a separate domain ontology.
- Confirm the namespace prefix (candidate: `wyse:`).
- Identify the primary source documents that would inform the TBox (Wymore 1993, Wach 2021 conjoining paper, the Bayesian SE draft).

## Future-exploration item logged 2026-05-20

**Alternative declarations of a problem space.** SES is one apparatus for declaring a problem space; other apparatuses exist (set-theoretic enumeration, logical predicates, grammars, generative models, type-theoretic specifications, feature models). For the WySE ontology and for due literature review and method comparison, this needs investigation:
- What other declaration apparatuses are in use in the SE / DEVS / formal methods literatures?
- When do two declarations (in the same or different apparatuses) declare the same problem space?
- Is there a meta-formalism for "declaration of a problem space" that the various apparatuses are instances of?
- Could WySE be expanded to use multiple declaration apparatuses depending on the problem-space role and level?

**Citation lead.** Rao Kannan at the University of Alabama in Huntsville (UAH) is reported by user to have relevant work in this area. Specific paper or research thread to be identified. Pull citation before formal literature review.

This item is for future session work, not for the current D_r conversation.

## Future-exploration item logged 2026-05-20 (continued)

**SES equivalence as an algorithmic-efficiency move.** Two SESes can declare the same problem space (the set of admissible elements they enumerate is identical, even though the tree structures differ). This is structurally analogous to multiple equivalent regular expressions or finite automata describing the same regular language. Three ways this happens: different decomposition orders; decomposition vs explicit Cartesian product; different model-base couplings that produce equivalent executable models after synthesis.

If SES equivalence is formalized, several algorithmic-efficiency moves become available:
- **Canonicalization.** Transform an SES into a canonical form for the problem space it declares. Canonical-form lookups, comparisons, and validations become tractable.
- **Pruning-efficiency selection.** Among equivalent SESes, choose the one whose pruning operations are cheapest for the deployment workload.
- **Synthesis-efficiency selection.** Choose the SES whose MB synthesis is cheapest.
- **Validation-efficiency selection.** Choose the SES whose SHACL / SPARQL validation is fastest.
- **Equivalence-checking.** Decide whether two SESes from different teams declare the same problem space, supporting cross-team integration.

For the WySE ontology, SES equivalence should be a formal relation in the TBox, with SPARQL CQs to identify equivalent SESes and SHACL shapes to validate equivalence claims.

This item is also for future session work.
