# Scoping Review Protocol: Neuro-Symbolic AI and Game Theory for Wargaming and Systems Engineering

**Version:** 1.0
**Date:** February 16, 2026
**Author:** Paul F. Wach, PhD
**Affiliation:** University of Arizona, Systems & Industrial Engineering
**Framework:** PRISMA-ScR (Tricco et al., 2018) and JBI Scoping Review Methodology (Peters et al., 2020)

---

## 1. Review Title

Neuro-Symbolic AI Meets Game Theory: A Scoping Review with Applications to Wargaming and Systems Engineering

## 2. Objective

To systematically map the existing literature at the intersection of neuro-symbolic artificial intelligence and game theory, identify how these fields have (or have not) been integrated, and assess opportunities for their combined application to wargaming and defense systems engineering.

## 3. Research Questions

**RQ1 (Landscape):** What is the current state of research integrating neuro-symbolic AI methods with game-theoretic reasoning?

**RQ2 (Taxonomy):** How can existing work be classified along two dimensions — neuro-symbolic integration type and game-theoretic solution concept — and where are the populated vs. empty cells?

**RQ3 (Application):** To what extent have neuro-symbolic and/or game-theoretic AI methods been applied to wargaming, military decision-making, and defense systems engineering?

**RQ4 (Gaps):** What are the key research gaps at the intersection of these fields, and what research agenda would address them?

**RQ5 (Architecture):** What architectural patterns have been proposed or implemented for systems that combine neural learning, symbolic reasoning, and game-theoretic optimization?

## 4. Population, Concept, Context (PCC) Framework

| Element | Description |
|---|---|
| **Population** | AI systems, algorithms, frameworks, and architectures |
| **Concept** | Integration of neuro-symbolic AI methods with game-theoretic reasoning — including but not limited to: neural game solvers with symbolic components, symbolic game representations with neural learning, hybrid architectures for strategic decision-making, formal verification of learned game strategies |
| **Context** | All application domains, with particular attention to wargaming, military decision-making, defense acquisition, mission engineering, and systems engineering |

## 5. Eligibility Criteria

### 5.1 Inclusion Criteria

A paper is included if it meets **at least one** of the following:

| ID | Criterion |
|---|---|
| I1 | Combines neural and symbolic methods for game-theoretic reasoning (equilibrium computation, mechanism design, strategic interaction, multi-agent decision-making) |
| I2 | Applies neuro-symbolic AI to wargaming, military simulation, or defense decision-making |
| I3 | Applies game-theoretic methods to wargaming with AI augmentation (neural, symbolic, or hybrid) |
| I4 | Proposes architectural frameworks integrating neural learning, symbolic reasoning, and game-theoretic optimization |
| I5 | Surveys or reviews literature at any two-way intersection of: neuro-symbolic AI, game theory, wargaming/defense, or systems engineering |
| I6 | Applies formal/symbolic verification methods to neural game-playing or game-solving agents |
| I7 | Applies game-theoretic frameworks to systems engineering problems using AI methods |

### 5.2 Exclusion Criteria

| ID | Criterion |
|---|---|
| E1 | Purely neural approaches to games without any symbolic component or formal game-theoretic analysis (e.g., standard deep RL for Atari games) |
| E2 | Purely symbolic game theory without any neural/learning component (e.g., classical economics papers) |
| E3 | Neuro-symbolic AI papers with no connection to strategic interaction, multi-agent reasoning, or game-theoretic concepts |
| E4 | Non-English publications |
| E5 | Abstracts, editorials, or opinion pieces without technical contribution |
| E6 | Duplicate publications (retain the most complete version) |

### 5.3 Borderline Cases

Papers in the following categories will be included in a **secondary corpus** (charted but analyzed separately):

- Neural game-solving papers (Deep CFR, ReBeL, etc.) that lack symbolic components but are foundational to the field
- Symbolic game formalisms (GDL, ATL) that lack neural components but provide key infrastructure
- Proto-neuro-symbolic defense AI (e.g., Soar + RL, knowledge graphs + RAG) that does not use the NeSy label but exhibits hybrid characteristics
- Existing surveys in adjacent domains (NeSy surveys, GT+AI surveys, AI-for-wargaming reports) that inform scope but do not themselves sit at the intersection

## 6. Information Sources

### 6.1 Electronic Databases

| Database | Coverage | Rationale |
|---|---|---|
| IEEE Xplore | Engineering, CS, systems | SE venues, IEEE Systems Journal |
| ACM Digital Library | Computer science | AAMAS, ACM EC, JACM |
| Scopus | Multidisciplinary | Broad coverage, citation analysis |
| Web of Science | Multidisciplinary | Impact metrics, citation networks |
| arXiv (cs.AI, cs.GT, cs.MA, cs.LO) | Preprints | Rapid dissemination venue for AI/GT |
| DTIC (Defense Technical Information Center) | DoD research | NPS theses, military technical reports |
| NATO STO Publications | NATO research | SAS, MSG panel proceedings |

### 6.2 Targeted Venue Searches

| Venue | Type | Rationale |
|---|---|---|
| NeurIPS, ICML, ICLR | AI/ML conferences | Neural game solvers, NeSy methods |
| AAAI, IJCAI | Broad AI conferences | NeSy, game representations, strategic reasoning |
| AAMAS | Multi-agent systems | Game-theoretic multi-agent AI |
| ACM EC, WINE, SAGT | Economics + computation | Mechanism design, algorithmic game theory |
| GameSec | Security games | Defense game theory |
| INCOSE IS, CSER | Systems engineering | SE applications |
| NDIA SME Conference | Defense SE | AI4SE, mission engineering |
| SERC/AIRC publications | DoD UARCs | Defense SE research |
| NPS Calhoun repository | Naval research | Wargaming, defense game theory |
| RAND publications | Policy research | AI for wargaming assessments |

### 6.3 Grey Literature

- DARPA program descriptions (ANSR, Gamebreaker, SABER, XAI)
- NATO STO Technical Activity Proposals and meeting proceedings
- DoD SBIR/STTR topics related to neuro-symbolic AI
- Institutional technical reports (RAND, MITRE, JHU APL)

### 6.4 Supplementary Search Methods

- Backward citation tracking (reference lists of included papers)
- Forward citation tracking (papers citing included papers, via Google Scholar)
- Author tracking (publication lists of key researchers identified in preliminary scan)
- Expert consultation (researchers identified in Section 7 of the white paper)

## 7. Search Strategy

### 7.1 Search String Construction

The search strategy uses three concept blocks combined with Boolean operators:

**Block A — Neuro-Symbolic AI:**
```
("neuro-symbolic" OR "neurosymbolic" OR "neural-symbolic" OR "hybrid AI"
OR "neural" AND "symbolic" AND "reasoning"
OR "knowledge graph" AND ("neural" OR "deep learning" OR "LLM")
OR "differentiable logic" OR "neural theorem prov*"
OR "logic tensor network" OR "DeepProbLog")
```

**Block B — Game Theory:**
```
("game theory" OR "game-theoretic" OR "Nash equilibrium" OR "Stackelberg"
OR "mechanism design" OR "strategic interaction" OR "multi-agent"
OR "adversarial reasoning" OR "equilibrium computation"
OR "cooperative game" OR "non-cooperative game" OR "extensive-form game"
OR "Bayesian game" OR "mean-field game" OR "security game")
```

**Block C — Wargaming / Defense / Systems Engineering:**
```
("wargam*" OR "war game" OR "military decision" OR "defense planning"
OR "command and control" OR "mission engineering" OR "mission planning"
OR "systems engineering" OR "acquisition" OR "defense system*"
OR "combat simulation" OR "course of action" OR "COA"
OR "rules of engagement" OR "doctrine")
```

### 7.2 Search Combinations

| Search | Combination | Purpose |
|---|---|---|
| S1 | A AND B | Core intersection: NeSy + game theory |
| S2 | A AND C | NeSy applied to defense/SE |
| S3 | B AND C AND ("artificial intelligence" OR "machine learning" OR "neural" OR "deep learning") | GT + AI in defense/SE |
| S4 | A AND B AND C | Triple intersection |
| S5 | ("neuro-symbolic" OR "neurosymbolic") AND ("game" OR "strategic" OR "adversarial" OR "multi-agent") | Targeted NeSy + games |
| S6 | ("formal verification" OR "model checking") AND ("game" OR "equilibrium") AND ("neural" OR "learned" OR "reinforcement learning") | Verification of learned game strategies |

### 7.3 Date Range

**Primary:** January 2015 – February 2026 (covers the modern NeSy and deep RL for games era)

**Extended (for foundational works):** No date restriction for papers meeting I5 (surveys) or establishing foundational formalisms (GDL, ATL, etc.)

### 7.4 Language

English only (E4).

## 8. Selection of Sources of Evidence

### 8.1 Screening Process

**Stage 1 — Title and abstract screening.**
Two reviewers independently screen titles and abstracts against inclusion/exclusion criteria. Disagreements resolved by discussion or a third reviewer.

**Stage 2 — Full-text review.**
Full texts of papers passing Stage 1 are retrieved and assessed against all inclusion/exclusion criteria. Reasons for exclusion recorded.

**Stage 3 — Borderline classification.**
Papers not meeting primary inclusion criteria but matching borderline case descriptions (Section 5.3) are classified into the secondary corpus.

### 8.2 PRISMA-ScR Flow Diagram

A PRISMA flow diagram will document: records identified, duplicates removed, records screened, records excluded (with reasons), full-text articles assessed, articles included in primary corpus, articles included in secondary corpus.

### 8.3 Pilot Testing

The screening criteria will be pilot-tested on 30 randomly selected records from S1 (NeSy + GT search). Inter-rater reliability will be assessed using Cohen's kappa (target: >= 0.80).

## 9. Data Charting (Extraction)

### 9.1 Data Extraction Form

For each included paper, the following fields will be extracted:

**Bibliographic:**
- Authors, title, year, venue, DOI/URL
- Publication type (journal, conference, thesis, report, preprint)

**Classification:**
- NeSy integration type (Kautz taxonomy: Types 1–6; see Section 10)
- Game-theoretic concept (Nash, Stackelberg, evolutionary, mechanism design, mean-field, cooperative, Bayesian, other)
- Game information structure (perfect/imperfect, complete/incomplete)
- Number of players/agents (2-player, n-player, population/mean-field)
- Application domain (wargaming, defense, cybersecurity, SE, general games, other)

**Technical:**
- Neural component(s) used (RL, deep learning, LLM, GNN, other)
- Symbolic component(s) used (logic programming, ontology, knowledge graph, formal verification, planning, other)
- Integration mechanism (how neural and symbolic components interact)
- Game-theoretic property addressed (equilibrium computation, strategy synthesis, mechanism design, verification, other)
- Evaluation method (formal proof, empirical benchmark, simulation, case study, conceptual)

**Assessment:**
- Maturity level (conceptual, prototype, deployed)
- Explainability addressed? (yes/no/partial)
- Defense/military relevance (direct, indirect, none)
- Key contribution (1–2 sentences)

### 9.2 Charting Process

Data will be extracted by one reviewer and verified by a second. A calibration exercise on 10 papers will be conducted first to ensure consistent interpretation of extraction fields.

## 10. Proposed Taxonomy

The core intellectual contribution of this review is a two-dimensional classification framework:

### 10.1 Dimension 1: Neuro-Symbolic Integration Type (adapted from Kautz, 2020)

| Type | Label | Description | Example |
|---|---|---|---|
| 1 | Symbolic[Neural] | Symbolic system with neural subroutines | Knowledge graph with neural link prediction for game state evaluation |
| 2 | Neural|Symbolic | Neural system informed by symbolic knowledge | RL agent pre-trained with doctrinal rules |
| 3 | Neural:Symbolic→Neural | Neural system with symbolic output compiled to neural form | Game rules compiled into neural network architecture |
| 4 | Neural_{Symbolic} | Neural system with symbolic internal representations | Neural network with differentiable logic layer for game reasoning |
| 5 | Neural[Symbolic] | Neural system calling symbolic solvers | LLM calling a Nash equilibrium solver |
| 6 | Symbolic∩Neural | Tightly integrated system where neural and symbolic are indistinguishable | Differentiable game-theoretic reasoning engine |

### 10.2 Dimension 2: Game-Theoretic Solution Concept

| Concept | Description | Defense Relevance |
|---|---|---|
| Nash Equilibrium | Mutual best response in non-cooperative games | Adversarial wargaming, force-on-force |
| Stackelberg Equilibrium | Leader-follower commitment model | Security resource allocation, deterrence |
| Correlated Equilibrium | Coordination via shared signal | Coalition operations, joint planning |
| Evolutionary Stable Strategy | Population dynamics stability | Doctrinal evolution, force structure |
| Mechanism Design | Designing rules to achieve desired outcomes | Acquisition contracts, incentive structures |
| Cooperative Game Theory | Coalition formation and value distribution | Alliance burden-sharing, SoS architecture |
| Bayesian Game / POSG | Games with incomplete information and beliefs | Intelligence, fog of war |
| Mean-Field Game | Large-population strategic interaction | Large-scale simulation, swarm behavior |

### 10.3 Classification Matrix

The primary output will be a matrix with NeSy types as rows and GT concepts as columns. Each cell will contain:
- Count of papers
- Key papers (by citation key)
- Assessment of maturity (empty / conceptual / prototype / deployed)

Empty cells represent specific research opportunities.

## 11. Synthesis of Results

### 11.1 Quantitative Summary

- Frequency distribution by NeSy type, GT concept, application domain, year, and venue
- Co-occurrence analysis (which NeSy types appear with which GT concepts)
- Temporal trends (growth/decline of specific intersections)
- Geographic and institutional distribution

### 11.2 Thematic Analysis

Results will be synthesized around:
- **Theme 1: Learning to play** — Neural methods for game-theoretic reasoning, and where symbolic components add value
- **Theme 2: Reasoning about play** — Symbolic methods for game analysis, and where neural components add capability
- **Theme 3: Verifying play** — Formal verification of learned game strategies
- **Theme 4: Designing the game** — Mechanism design and game construction with hybrid methods
- **Theme 5: Applying to defense** — Wargaming, mission engineering, and acquisition applications

### 11.3 Gap Map

A visual gap map will present the classification matrix with color coding:
- **Green:** Well-populated cell (>= 5 papers, mature work)
- **Yellow:** Emerging cell (1–4 papers, early-stage work)
- **Red:** Empty cell (0 papers, identified research opportunity)

### 11.4 Research Agenda

For each red/yellow cell, the synthesis will propose:
- Specific research questions
- Feasibility assessment (what would be needed to fill the gap)
- Potential impact (defense relevance, SE relevance, AI community interest)

## 12. Quality Assessment

As a scoping review, formal quality appraisal of individual studies is not required per JBI methodology. However, each included paper will be tagged with:

- **Evidence type:** Formal proof / empirical evaluation / simulation / case study / conceptual
- **Reproducibility:** Code/data available (yes/no)
- **Peer review status:** Published in peer-reviewed venue / preprint / technical report

This enables readers to assess the strength of evidence in populated cells.

## 13. Presentation of Results

The review will be reported according to PRISMA-ScR guidelines and will include:

1. PRISMA flow diagram
2. Summary table of all included papers with classification
3. The NeSy x GT classification matrix (gap map)
4. Thematic narrative synthesis organized by the five themes
5. Research agenda with prioritized opportunities
6. Supplementary material: full data extraction table, search logs, secondary corpus

## 14. Target Venues for Publication

| Venue | Type | Rationale |
|---|---|---|
| Systems Engineering (Wiley/INCOSE) | Journal | Primary SE audience, connects to SERC/INCOSE community |
| Journal of Defense Modeling and Simulation | Journal | Defense M&S community, wargaming audience |
| Artificial Intelligence Review | Journal | AI community, established survey venue |
| CSER 2026 (April, Stevens) | Conference | "Intelligent Digital Twin" theme, SERC connection |
| NDIA SME Conference 2025 (October, Tampa) | Conference | Defense SE audience, NDIA AI/ML Working Group |
| INCOSE International Symposium 2026 | Conference | Global SE audience |

## 15. Timeline

| Phase | Activity | Target Date |
|---|---|---|
| 1 | Protocol finalization | February 2026 |
| 2 | Database searches executed | March 2026 |
| 3 | Title/abstract screening | March–April 2026 |
| 4 | Full-text review and data extraction | April–May 2026 |
| 5 | Taxonomy construction and gap mapping | May 2026 |
| 6 | Synthesis and manuscript drafting | May–June 2026 |
| 7 | Internal review and revision | June–July 2026 |
| 8 | Submission | July 2026 |

## 16. Amendments

Any amendments to this protocol will be documented with date, description of change, and rationale.

| Date | Amendment | Rationale |
|---|---|---|
| — | — | — |

## 17. Protocol References

- Arksey, H. and O'Malley, L. (2005). "Scoping studies: towards a methodological framework." *International Journal of Social Research Methodology*, 8(1), 19–32.
- Levac, D., Colquhoun, H., and O'Brien, K. K. (2010). "Scoping studies: advancing the methodology." *Implementation Science*, 5, 69.
- Peters, M. D. J. et al. (2020). "Updated methodological guidance for the conduct of scoping reviews." *JBI Evidence Synthesis*, 18(10), 2119–2126.
- Tricco, A. C. et al. (2018). "PRISMA Extension for Scoping Reviews (PRISMA-ScR): Checklist and Explanation." *Annals of Internal Medicine*, 169(7), 467–473.
- Kautz, H. (2020). "The Third AI Summer." Keynote, AAAI 2020. (NeSy taxonomy origin)
