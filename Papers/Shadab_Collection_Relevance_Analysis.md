# Shadab Collection — Cross-Reference to Research Projects

**Date:** 2026-02-23
**Source:** `C:\Users\pfwac\OneDrive - University of Arizona\Documents\04 Resource Library\Shadab\`

## Articles Reviewed (7 unique works)

| # | Short Title | Year | Core Contribution |
|---|------------|------|-------------------|
| S1 | Closed Systems Paradigm (76.pdf) | 2023 | Core/periphery framework; Law of Requisite Variety for intelligent systems |
| S2 | Systems-Theoretical Formalization | 2024 | Formal math for functional & informational closure |
| S3 | Product Herding | 2023 | Alternative to product-line engineering for AI systems |
| S4 | Core & Periphery in Bio/AI | 2025 | Empirical validation of core/periphery across biological & artificial systems |
| S5 | Shadab Dissertation (SE4AI) | 2024 | Overarching thesis unifying S1–S4 and S6–S7 |
| S6 | Interface Description Template | 2024 | Reuse framework for AI-enabled components |
| S7 | Scenario-to-Outcome-Based Engineering | 2024 | Transition from input-output to outcome-focused SE4AI |

**Note:** Alejandro Salado (U of A) is co-author/co-advisor across all works.

## Relevance Matrix

| Project | S1 | S2 | S3 | S4 | S5 | S6 | S7 | Overall |
|---------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|---------|
| **SE Math Foundations** | ++ | +++ | ++ | + | +++ | . | + | **Very High** |
| **Dissertation Journal (WySE)** | ++ | +++ | + | + | +++ | + | ++ | **Very High** |
| **Agentic AI Swarms SE** | ++ | + | ++ | ++ | ++ | ++ | ++ | **High** |
| **AI Circuit Breaker** | ++ | + | + | +++ | ++ | + | + | **High** |
| **AI4RE SLR** | + | . | . | . | + | ++ | +++ | **Moderate** |
| **Neuro-Symbolic Wargaming** | + | + | . | + | + | . | . | **Low–Moderate** |
| **AI Investing Platform** | . | . | . | . | . | . | . | **Low** |

`+++` = directly citable / foundational, `++` = strong conceptual alignment, `+` = supporting reference, `.` = minimal

## Project-by-Project Analysis

### 1. SE Math Foundations — Very High Relevance

The strongest match in the collection. Shadab's formalization paper (S2) uses the same morphism-based reasoning (homomorphism, isomorphism, topological equivalence) that anchors the isomorphism catalog. Product Herding (S3) explicitly introduces *pattern equivalence* and *topological equivalence* as alternatives to isomorphism for context-dependent systems. The dissertation (S5) builds on Mesarovic's System Theory with 7-tuple formalisms directly parallel to Wymore T3SD.

- **Cite S2** for formal closure definitions when discussing morphism preservation under discretization
- **Cite S3** for the argument that isomorphism breaks down for intelligent/adaptive systems (homomorphism becomes the operative relationship)
- **Cite S5** as the unifying theoretical reference

### 2. Dissertation Journal (WySE Metamodel) — Very High Relevance

Shared intellectual lineage — Salado is co-author on Shadab and connected to the WySE work. S2's functional/informational closure directly parallels Verification Model Morphic Conditions (VMMC). The closed-systems argument that intelligent systems cannot be fully specified through input-output pairs mirrors the finding that VM is *indirectly* defined through combined knowledge (SD + VR + VMMC).

- **Cite S2** for complementary formalization of closure constraints alongside morphic conditions
- **Cite S7** for the scenario-vs-outcome argument as analogous to the requirements-vs-verification model distinction
- **Cite S1** to position the verification framework within the broader SE4AI discourse

### 3. Agentic AI Swarms SE — High Relevance

Core/periphery (S1, S4) maps directly to swarm architecture: *core* = stable coordination protocols, *periphery* = adaptive specialist agents. Product Herding (S3) provides a framework for managing agent populations that diverge through learning while maintaining herd coherence — directly applicable to swarm governance. The interface template (S6) addresses how AI components are specified for reuse, relevant to agent interoperability.

- **Cite S1/S4** when discussing swarm architectures that balance stability with adaptability
- **Cite S3** in the section on agent lifecycle management and fleet-level coordination
- **Cite S6** for agent interface specification standards
- **Cite S7** for evaluating swarm performance by outcomes rather than scenario coverage

### 4. AI Circuit Breaker — High Relevance

The bio-inspired pillar has the strongest overlap. S4's treatment of homeostasis, immune response, and allostasis as core/periphery phenomena maps directly to Pillar 3 (bio-inspired adaptive regulation). Informational closure (S2) provides formal bounds on system-environment mutual information that could constrain SPC control limits. Product Herding (S3) is relevant for managing trust across a fleet of monitored AI systems.

- **Cite S4** as foundational for Pillar 3's biological regulation models
- **Cite S2** for mutual information constraints informing measurement theory (Pillar 1)
- **Cite S1** for the theoretical argument that AI systems require closed-system monitoring approaches

### 5. AI4RE SLR — Moderate Relevance

The scenario-to-outcome paper (S7) directly argues that requirements for AI systems must shift from input-output specification to outcome-based formulation — a key challenge the SLR identifies. The interface template (S6) is relevant to how AI component requirements are documented for reuse. S1 explicitly identifies requirements engineering as a research gap for intelligent systems.

- **Cite S7** in the discussion section on emerging RE paradigms for AI
- **Cite S6** when discussing requirements documentation for AI component reuse
- **Cite S1** for the broader framing of why traditional RE falls short for AI systems

### 6. Neuro-Symbolic Wargaming — Low–Moderate Relevance

Conceptual but not direct. Core/periphery could theoretically map to neuro-symbolic integration (symbolic reasoning = core stability, neural learning = peripheral adaptability), and S2's formalisms could complement game-theoretic formalization. However, Shadab's corpus does not address game theory, wargaming, or defense applications.

- **Possible cite of S1** if framing NeSy integration through a core/periphery lens
- Otherwise, these are background rather than primary references

### 7. AI Investing Platform — Low Relevance

No meaningful overlap. The platform is a software development project, not a theoretical research effort.

## Key Takeaway

The Shadab collection is a **core reference set for 4 of 7 projects**, with the strongest connections to SE Math Foundations and the Dissertation Journal through shared morphism-based systems theory. For Agentic AI Swarms and AI Circuit Breaker, the core/periphery and product herding frameworks offer novel theoretical framing that differentiates the work from purely empirical approaches.
