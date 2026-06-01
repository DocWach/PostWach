---
title: "DARPA CLARA: Concept Diagrams"
subtitle: "Morphism-Grounded Compositional Assurance for Autonomous AI Systems"
date: "2026-03-24"
geometry: margin=0.5in
fontsize: 10pt
header-includes: |
  \usepackage{float}
  \floatplacement{figure}{H}
---

## Diagram 1: The Big Picture -- What Is the Circuit Breaker?

A high-level overview accessible to any audience. The AI Circuit Breaker continuously measures how well an AI's internal model matches reality, then triggers a graduated response when quality degrades.

![The Big Picture](diagrams_tmp/diagram1.png){ width=100% }

\newpage

## Diagram 2: The Morphism Chain (ECG Domain)

Information flows from the patient's heart to a clinical classification through five transformation stages (h1-h5). Each link has its own morphism quality D_h = (D_s, D_b). The composition theorem says the weakest structural link bounds the whole chain.

![Morphism Chain](diagrams_tmp/diagram2.png){ width=100% }

\newpage

## Diagram 3: Two-Axis Morphism Quality

D_s (structural distance) and D_b (behavioral distance) are two independent axes. Four quadrants characterize different failure modes. The ideal is D_h = (0, 0).

![Two-Axis Quality](diagrams_tmp/diagram3.png){ width=100% }

\newpage

## Diagram 4: Five-Layer Architecture

The circuit breaker's five layers, from foundational (Layer 1, Reference Standards) to human-facing (Layer 5, Underwriting Interface). Shows where AR and ML components sit and data flow between layers.

![Five-Layer Architecture](diagrams_tmp/diagram4.png){ width=95% }

\newpage

## Diagram 5: AR-ML Tight Coupling

The bidirectional relationship between Automated Reasoning and Machine Learning. AR shapes ML training through the loss function; ML provides runtime evidence that AR reasons over. This is NOT AR bolted on as a post-hoc filter.

![AR-ML Tight Coupling](diagrams_tmp/diagram5.png){ width=95% }

\newpage

## Diagram 6: Terminology Hierarchy

How all morphism quality terms relate. D_h is the master vector. D_s and D_b are its two axes. d_cos is a fast runtime proxy that does NOT decompose into structural vs. behavioral. MTBH is longitudinal.

![Terminology Hierarchy](diagrams_tmp/diagram6.png){ width=100% }

\newpage

## Diagram 7: Phase 1 / Phase 2 Workflow

24-month program timeline. Phase 1 (15 months, $1.1M) proves the composition theorem on ECG. Phase 2 (9 months, $0.75M) deepens with a second ML kind, full pipeline, and domain-transfer analysis.

![Timeline](diagrams_tmp/diagram7.png){ width=100% }

\newpage

## Diagram 8: Composition Theorem Visual

Two component tasks (Classification and Guideline Compliance) each with their own D_h compose into end-to-end monitoring. Structural bound: D_s_total >= max(D_s_i). Behavioral bound: D_b_total <= sum(D_b_i). Includes a concrete numerical example.

![Composition Theorem](diagrams_tmp/diagram8.png){ width=100% }
