# DEVS Collection — Cross-Reference to Research Projects

**Date:** 2026-02-23
**Source:** `C:\Users\pfwac\OneDrive - University of Arizona\Documents\04 Resource Library\DEVS\`

## Articles Reviewed

| # | Short Title | Authors | Year | Type |
|---|------------|---------|------|------|
| D1 | MBSE with/without Simulation: State of the Art and Way Forward | Zeigler, Mittal, Traoré | 2018 | Journal (MDPI *Systems*) |
| D2 | Theory of Modeling and Simulation (3rd Ed.) | Zeigler, Muzy, Kofman | 2019 | Textbook (Elsevier, 694 pp.) |

**Note:** Zeigler is at University of Arizona and is the originator of the DEVS formalism — direct institutional connection.

## Relevance Matrix

| Project | D1 | D2 | Overall |
|---------|:--:|:--:|---------|
| **SE Math Foundations** | +++ | +++ | **Very High** |
| **Dissertation Journal (WySE)** | +++ | +++ | **Very High** |
| **Agentic AI Swarms SE** | ++ | + | **Moderate–High** |
| **AI Circuit Breaker** | + | ++ | **Moderate** |
| **Neuro-Symbolic Wargaming** | ++ | + | **Moderate** |
| **AI4RE SLR** | + | . | **Low** |
| **AI Investing Platform** | . | . | **Low** |

`+++` = directly citable / foundational, `++` = strong conceptual alignment, `+` = supporting reference, `.` = minimal

## Project-by-Project Analysis

### 1. SE Math Foundations — Very High Relevance

These are **primary references**. D2 Part 3 (Chapters 14–17) covers the hierarchy of system morphisms, abstraction, model families, and approximate morphisms — the exact theoretical backbone of the isomorphism catalog. D1 introduces base-lumped model pairs with morphic projections that preserve behavioral equivalence, directly paralleling the discretization-and-morphism-preservation analysis.

- **Cite D2 Ch. 14–17** as the definitive reference for system morphisms, abstraction hierarchies, and approximate morphisms
- **Cite D1** for the multiresolution methodology (base vs. lumped models) and consistency verification through experimental frames
- D2's treatment of DEVS+DESS+DTSS multi-formalism integration is directly relevant to cross-domain analogies

### 2. Dissertation Journal (WySE Metamodel) — Very High Relevance

The WySE metamodel is grounded in T3SD and DEVS. D2 is the canonical source for the DEVS formalism the verification model framework builds upon. D1's experimental frame concept maps directly to verification model specification — both define observation conditions under which model equivalence is evaluated. The base-lumped morphism methodology in D1 parallels VMMC's approach to bounding infinite equivalence classes.

- **Cite D2** as the foundational DEVS reference (the 3rd edition adds morphism hierarchy and approximate morphisms)
- **Cite D1** for the MBSE-M&S integration workflow and experimental frame formalization
- D1's SES (System Entity Structure) is relevant to how verification model configurations are pruned from the design space

### 3. Agentic AI Swarms SE — Moderate–High Relevance

D1 directly addresses Complex Adaptive Systems of Systems (CASOS) — systems with emergent behavior, agent learning, and incomplete information. The paper's framework for controlling epistemological emergence through DEVS closure under coupling is relevant to ensuring predictable swarm behavior. The UAV fleet case study demonstrates multi-agent coordination with adaptive sustainment.

- **Cite D1** when discussing formal foundations for controlling emergent behavior in agent swarms
- **Cite D1** for the multifaceted modeling ontology (Production/Consumption/Coordination faces) as a lens for swarm role taxonomy
- D2's DEVS Markov extensions (Ch. 21–22) relevant to stochastic agent behavior modeling

### 4. AI Circuit Breaker — Moderate Relevance

D2's treatment of DEVS Markov modeling (Ch. 21–22) and model lumping provides formal methods for the stochastic monitoring components of the circuit breaker. D1's experimental frame concept supports the measurement theory pillar — defining observation conditions under which trust metrics are valid. The multiresolution approach could inform graduated response levels (coarse monitoring → fine-grained intervention).

- **Cite D2 Ch. 21–22** for stochastic model foundations in Pillar 1 measurement theory
- **Cite D1** for experimental frame methodology applied to trust metric validation

### 5. Neuro-Symbolic Wargaming — Moderate Relevance

D1's CASOS framework addresses exactly the kind of multi-agent adversarial systems that wargaming models. The multiobjective, multiperspective modeling methodology supports the multi-domain nature of wargaming scenarios. D2's spiking neuron modeling chapter (Ch. 23) provides a bridge between DEVS formalism and neural computation relevant to the neuro-symbolic framing.

- **Cite D1** for formal simulation infrastructure supporting wargaming scenario modeling
- **Cite D2 Ch. 23** if arguing for DEVS as a unifying formalism for neuro-symbolic integration

### 6. AI4RE SLR — Low Relevance

Tangential only. D1 mentions how MBSE requirements can be derived from simulation results, but this is not the focus of the LLM-for-RE survey.

### 7. AI Investing Platform — Low Relevance

No meaningful overlap.

## Key Takeaway

The DEVS collection provides **canonical foundational references** for SE Math Foundations and the Dissertation Journal — these are not just relevant but arguably essential citations given the work's grounding in Wymore/DEVS theory and Zeigler's institutional connection at U of A. For Agentic AI Swarms and Neuro-Symbolic Wargaming, D1's CASOS framework offers formal simulation infrastructure for complex multi-agent systems.
