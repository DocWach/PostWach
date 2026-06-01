# Scoping Review: Consolidated Extraction Table

**Status:** Phase 2 Complete (web-search + formal database search verified) — Full-text screening pending
**Date:** February 16, 2026
**Protocol:** Scoping_Review_Protocol.md v1.0
**Note:** P01-P34 from preliminary web-search pass; P35-P82 from formal database search agents

---

## PRIMARY CORPUS

Papers at the intersection of neuro-symbolic AI and game theory (meeting criteria I1, I4, I6).

### P01 — Yan, Santos, Norman, Parker, Kwiatkowska (2024)

| Field | Value |
|---|---|
| **Title** | Strategy synthesis for zero-sum neuro-symbolic concurrent stochastic games |
| **Year** | 2024 |
| **Venue** | Information and Computation |
| **DOI/URL** | https://www.sciencedirect.com/science/article/pii/S0890540124000580 |
| **Type** | Journal |
| **NeSy Type** | Type 1: Symbolic[Neural] |
| **GT Concept** | Nash Equilibrium (zero-sum) |
| **Game Info** | Perfect information, complete |
| **Players** | 2-player |
| **Domain** | General (formal methods) |
| **Neural Component** | Neural perception mechanisms (image classifiers) |
| **Symbolic Component** | PRISM-games model checker, temporal logic specifications |
| **Integration** | Neural perception feeds symbolic game model; strategies synthesized symbolically |
| **GT Property** | Strategy synthesis, equilibrium computation |
| **Evaluation** | Formal proof + empirical benchmark |
| **Maturity** | Prototype |
| **Explainability** | Yes (symbolic strategies are interpretable) |
| **Defense Relevance** | Indirect |
| **Key Contribution** | First framework for synthesizing verified strategies in games with neural perception |

### P02 — Yan, Santos, Norman, Parker, Kwiatkowska (2022)

| Field | Value |
|---|---|
| **Title** | Finite-horizon Equilibria for Neuro-symbolic Concurrent Stochastic Games |
| **Year** | 2022 |
| **Venue** | arXiv:2205.07546 |
| **Type** | Preprint |
| **NeSy Type** | Type 1: Symbolic[Neural] |
| **GT Concept** | Nash Equilibrium |
| **Game Info** | Perfect information, complete |
| **Players** | 2-player |
| **Domain** | General (formal methods) |
| **Neural Component** | Neural perception mechanisms |
| **Symbolic Component** | Formal verification, strategy synthesis algorithms |
| **Integration** | Neural perception integrated into symbolic game framework |
| **GT Property** | Equilibrium computation (finite-horizon) |
| **Evaluation** | Formal proof + empirical |
| **Maturity** | Prototype |
| **Explainability** | Yes |
| **Defense Relevance** | Indirect |
| **Key Contribution** | Establishes finite-horizon equilibria for NS-CSG model |

### P03 — Yan, Santos, Norman, Parker, Kwiatkowska (2024)

| Field | Value |
|---|---|
| **Title** | Partially Observable Stochastic Games with Neural Perception Mechanisms |
| **Year** | 2024 |
| **Venue** | FM 2024 (26th International Symposium on Formal Methods) |
| **DOI/URL** | https://link.springer.com/chapter/10.1007/978-3-031-71162-6_19 |
| **Type** | Conference |
| **NeSy Type** | Type 1: Symbolic[Neural] |
| **GT Concept** | Bayesian/POSG |
| **Game Info** | Imperfect information, incomplete |
| **Players** | 2-player |
| **Domain** | General (formal methods) |
| **Neural Component** | Neural perception mechanisms |
| **Symbolic Component** | POSG formalism, HSVI solver |
| **Integration** | Neural perception in partially observable symbolic game model |
| **GT Property** | Strategy synthesis under partial observability |
| **Evaluation** | Formal proof + empirical |
| **Maturity** | Prototype |
| **Explainability** | Yes |
| **Defense Relevance** | Indirect (fog-of-war modeling applicable) |
| **Key Contribution** | Extends NS-CSG to partial observability (NS-POSG) |

### P04 — Yan, Santos, Norman, Parker, Kwiatkowska (2024)

| Field | Value |
|---|---|
| **Title** | HSVI-based Online Minimax Strategies for Partially Observable Stochastic Games with Neural Perception Mechanisms |
| **Year** | 2024 |
| **Venue** | L4DC 2024 (6th Annual Learning for Dynamics and Control Conference) |
| **Type** | Conference |
| **NeSy Type** | Type 1: Symbolic[Neural] |
| **GT Concept** | Nash (minimax) + Bayesian/POSG |
| **Game Info** | Imperfect information |
| **Players** | 2-player |
| **Domain** | General (formal methods) |
| **Neural Component** | Neural perception mechanisms |
| **Symbolic Component** | HSVI algorithm, belief-space reasoning |
| **Integration** | Online minimax strategy computation with neural perception |
| **GT Property** | Online strategy synthesis |
| **Evaluation** | Empirical benchmark |
| **Maturity** | Prototype |
| **Explainability** | Yes |
| **Defense Relevance** | Indirect |
| **Key Contribution** | Scalable online strategy computation for NS-POSGs |

### P05 — Kwiatkowska, Norman, Parker (2020)

| Field | Value |
|---|---|
| **Title** | PRISM-games 3.0: Stochastic Game Verification with Concurrency, Equilibria and Time |
| **Year** | 2020 |
| **Venue** | CAV 2020 |
| **DOI/URL** | https://link.springer.com/chapter/10.1007/978-3-030-53291-8_25 |
| **Type** | Conference (tool paper) |
| **NeSy Type** | Type 1: Symbolic[Neural] (when used with neural perception) |
| **GT Concept** | Nash Equilibrium, correlated equilibrium |
| **Game Info** | Various (configurable) |
| **Players** | Multi-player |
| **Domain** | General (verification tool) |
| **Neural Component** | Extensible to neural components |
| **Symbolic Component** | Model checking, temporal logic, strategy synthesis |
| **Integration** | Symbolic verification framework; neural components via NS-CSG extensions |
| **GT Property** | Equilibrium verification, strategy synthesis |
| **Evaluation** | Tool + benchmarks |
| **Maturity** | Deployed |
| **Explainability** | Yes |
| **Defense Relevance** | Indirect |
| **Key Contribution** | Mature tool for stochastic game verification supporting equilibria |

### P06 — Gerstgrasser, Danino, Seuken (2023)

| Field | Value |
|---|---|
| **Title** | Oracles & Followers: Stackelberg Equilibria in Deep Multi-Agent Reinforcement Learning |
| **Year** | 2023 |
| **Venue** | ICML 2023 |
| **DOI/URL** | https://proceedings.mlr.press/v202/gerstgrasser23a.html |
| **Type** | Conference |
| **NeSy Type** | Type 2: Neural\|Symbolic |
| **GT Concept** | Stackelberg Equilibrium |
| **Game Info** | Complete information |
| **Players** | 2-player (leader-follower) |
| **Domain** | General games |
| **Neural Component** | Deep RL (policy gradient) |
| **Symbolic Component** | Stackelberg game structure, best-response oracle |
| **Integration** | Neural agents trained within symbolic Stackelberg framework |
| **GT Property** | Stackelberg equilibrium computation |
| **Evaluation** | Empirical benchmark |
| **Maturity** | Prototype |
| **Explainability** | Partial |
| **Defense Relevance** | Indirect |
| **Key Contribution** | First deep MARL method for computing Stackelberg equilibria |

### P07 — Wang, Perrault, Mate, Tambe (2020)

| Field | Value |
|---|---|
| **Title** | Scalable Game-Focused Learning of Adversary Models: Data-to-Decisions in Network Security Games |
| **Year** | 2020 |
| **Venue** | AAMAS 2020 |
| **Type** | Conference |
| **NeSy Type** | Type 2: Neural\|Symbolic |
| **GT Concept** | Stackelberg Equilibrium |
| **Game Info** | Imperfect information |
| **Players** | 2-player (defender-attacker) |
| **Domain** | Security (network defense) |
| **Neural Component** | Neural network adversary model |
| **Symbolic Component** | Stackelberg game formulation, security game structure |
| **Integration** | Learned adversary models integrated into game-theoretic optimization |
| **GT Property** | Stackelberg equilibrium with learned adversary |
| **Evaluation** | Empirical (security domains) |
| **Maturity** | Prototype |
| **Explainability** | Partial |
| **Defense Relevance** | Direct (security resource allocation) |
| **Key Contribution** | Scalable data-driven approach to adversary modeling in security games |

### P08 — Fang, Stone, Tambe (2015)

| Field | Value |
|---|---|
| **Title** | When Security Games Go Green: Designing Defender Strategies to Prevent Poaching and Illegal Fishing |
| **Year** | 2015 |
| **Venue** | IJCAI 2015 |
| **Type** | Conference |
| **NeSy Type** | Type 2: Neural\|Symbolic |
| **GT Concept** | Stackelberg Equilibrium |
| **Game Info** | Imperfect information |
| **Players** | 2-player |
| **Domain** | Security (wildlife conservation) |
| **Neural Component** | Machine learning for adversary behavior prediction |
| **Symbolic Component** | Stackelberg security game formulation |
| **Integration** | ML predictions inform symbolic game-theoretic optimization |
| **GT Property** | Stackelberg equilibrium with bounded rationality |
| **Evaluation** | Field deployment (PAWS) |
| **Maturity** | Deployed |
| **Explainability** | Partial |
| **Defense Relevance** | Indirect (security resource allocation paradigm) |
| **Key Contribution** | Real-world deployed security game system (PAWS) |

### P09 — Duetting, Feng, Narasimhan, Parkes, Ravindranath (2024)

| Field | Value |
|---|---|
| **Title** | Optimal Auctions through Deep Learning: Advances in Differentiable Economics |
| **Year** | 2024 (journal), 2019 (original) |
| **Venue** | Journal of the ACM |
| **DOI/URL** | https://dl.acm.org/doi/10.1145/3630749 |
| **Type** | Journal |
| **NeSy Type** | Type 6: Symbolic∩Neural |
| **GT Concept** | Mechanism Design |
| **Game Info** | Incomplete information (valuations private) |
| **Players** | Multi-player (bidders) |
| **Domain** | Economics (auction design) |
| **Neural Component** | RegretNet neural architecture |
| **Symbolic Component** | Strategy-proofness constraints, allocation/payment rules |
| **Integration** | Differentiable mechanism design — neural network encodes auction mechanism with symbolic incentive compatibility constraints |
| **GT Property** | Mechanism design (revenue maximization, strategy-proofness) |
| **Evaluation** | Empirical benchmark |
| **Maturity** | Prototype |
| **Explainability** | Partial |
| **Defense Relevance** | Indirect (acquisition/contract design) |
| **Key Contribution** | Foundational differentiable economics framework for automated mechanism design |

### P10 — Advancing Differentiable Economics (2025)

| Field | Value |
|---|---|
| **Title** | Advancing Differentiable Economics: A Neural Network Framework for Revenue-Maximizing Combinatorial Auction Mechanisms |
| **Year** | 2025 |
| **Venue** | arXiv:2501.19219 |
| **Type** | Preprint |
| **NeSy Type** | Type 6: Symbolic∩Neural |
| **GT Concept** | Mechanism Design |
| **Game Info** | Incomplete information |
| **Players** | Multi-player |
| **Domain** | Economics (combinatorial auctions) |
| **Neural Component** | CANet, CAFormer architectures |
| **Symbolic Component** | Combinatorial constraints, strategy-proofness |
| **Integration** | Neural auction mechanisms with symbolic constraint satisfaction |
| **GT Property** | Mechanism design (combinatorial auctions) |
| **Evaluation** | Empirical benchmark |
| **Maturity** | Prototype |
| **Explainability** | Partial |
| **Defense Relevance** | Indirect |
| **Key Contribution** | Extends differentiable economics to combinatorial auctions |

### P11 — Curry, Dickerson, Schvartzman, Goldberg, Nisan, Sandholm (2024)

| Field | Value |
|---|---|
| **Title** | Automated Mechanism Design: A Survey |
| **Year** | 2024 |
| **Venue** | SIGecom Exchanges |
| **DOI/URL** | https://www.sigecom.org/exchanges/volume_22/2/CURRY.pdf |
| **Type** | Survey |
| **NeSy Type** | Type 2/6 (covers multiple) |
| **GT Concept** | Mechanism Design |
| **Game Info** | Various |
| **Players** | Multi-player |
| **Domain** | Economics/CS |
| **Neural Component** | Various (neural mechanism design landscape) |
| **Symbolic Component** | Various (classical mechanism design theory) |
| **Integration** | Survey of integration approaches |
| **GT Property** | Mechanism design |
| **Evaluation** | Literature survey |
| **Maturity** | N/A (survey) |
| **Explainability** | Addressed in survey |
| **Defense Relevance** | Indirect |
| **Key Contribution** | Comprehensive survey of automated/neural mechanism design |

### P12 — Laurière et al. (2024)

| Field | Value |
|---|---|
| **Title** | A Machine Learning Method for Stackelberg Mean Field Games |
| **Year** | 2024 |
| **Venue** | Mathematics of Operations Research |
| **DOI/URL** | https://pubsonline.informs.org/doi/abs/10.1287/moor.2023.0065 |
| **Type** | Journal |
| **NeSy Type** | Type 2: Neural\|Symbolic |
| **GT Concept** | Mean-field + Stackelberg |
| **Game Info** | Complete information, large population |
| **Players** | Population (mean-field) + leader |
| **Domain** | General (optimization) |
| **Neural Component** | Feed-forward and recurrent neural networks |
| **Symbolic Component** | Mean-field game PDE structure, Stackelberg formulation |
| **Integration** | Neural networks solve symbolically-specified MFG PDEs |
| **GT Property** | Mean-field equilibrium + Stackelberg equilibrium |
| **Evaluation** | Empirical benchmark |
| **Maturity** | Prototype |
| **Explainability** | Partial |
| **Defense Relevance** | Indirect (large-scale strategic planning) |
| **Key Contribution** | First ML method for Stackelberg MFGs |

### P13 — Ruthotto, Osher, Li, Nurbekyan, Fung (2020)

| Field | Value |
|---|---|
| **Title** | A machine learning framework for solving high-dimensional mean field game and mean field control problems |
| **Year** | 2020 |
| **Venue** | PNAS |
| **DOI/URL** | https://www.pnas.org/doi/10.1073/pnas.1922204117 |
| **Type** | Journal |
| **NeSy Type** | Type 2: Neural\|Symbolic |
| **GT Concept** | Mean-field |
| **Game Info** | Large population |
| **Players** | Population |
| **Domain** | General (applied math) |
| **Neural Component** | Neural network function approximation |
| **Symbolic Component** | Mean-field game PDE system (Hamilton-Jacobi-Bellman + Fokker-Planck) |
| **Integration** | Neural networks approximate solutions to symbolic MFG equations |
| **GT Property** | Mean-field equilibrium computation |
| **Evaluation** | Empirical (high-dimensional problems) |
| **Maturity** | Prototype |
| **Explainability** | Partial |
| **Defense Relevance** | Indirect (swarm modeling) |
| **Key Contribution** | Scalable neural approach to high-dimensional MFGs |

### P14 — Cao et al. (2023)

| Field | Value |
|---|---|
| **Title** | Deep Learning for Mean Field Games with non-separable Hamiltonians |
| **Year** | 2023 |
| **Venue** | arXiv:2301.02877 |
| **Type** | Preprint |
| **NeSy Type** | Type 2: Neural\|Symbolic |
| **GT Concept** | Mean-field |
| **Game Info** | Large population |
| **Players** | Population |
| **Domain** | General |
| **Neural Component** | Deep neural networks (single-layer, GAN variants) |
| **Symbolic Component** | MFG PDE structure with non-separable Hamiltonians |
| **Integration** | Neural solvers for symbolically-specified MFG systems |
| **GT Property** | Mean-field equilibrium |
| **Evaluation** | Empirical (up to 300 dimensions) |
| **Maturity** | Prototype |
| **Explainability** | No |
| **Defense Relevance** | Indirect |
| **Key Contribution** | Handles non-separable Hamiltonians in high dimensions |

### P15 — AAMAS 2023 Spatiotemporal MFG

| Field | Value |
|---|---|
| **Title** | Informed Deep Learning for Spatiotemporal Mean Field Games |
| **Year** | 2023 |
| **Venue** | AAMAS 2023 |
| **DOI/URL** | https://www.southampton.ac.uk/~eg/AAMAS2023/pdfs/p1079.pdf |
| **Type** | Conference |
| **NeSy Type** | Type 4: Neural_{Symbolic} |
| **GT Concept** | Mean-field |
| **Game Info** | Large population, spatiotemporal |
| **Players** | Population |
| **Domain** | General |
| **Neural Component** | Physics-informed deep learning |
| **Symbolic Component** | MFG PDE constraints embedded as physics-informed loss |
| **Integration** | Symbolic MFG structure internalized in neural architecture |
| **GT Property** | Mean-field equilibrium |
| **Evaluation** | Empirical |
| **Maturity** | Prototype |
| **Explainability** | Partial (physics-informed) |
| **Defense Relevance** | Indirect |
| **Key Contribution** | Hybrid RL + physics-informed DL for spatiotemporal MFGs |

### P16 — Park et al. (2023)

| Field | Value |
|---|---|
| **Title** | Neural Stochastic Differential Games for Time-series Analysis |
| **Year** | 2023 |
| **Venue** | ICML 2023 |
| **DOI/URL** | https://proceedings.mlr.press/v202/park23j.html |
| **Type** | Conference |
| **NeSy Type** | Type 4: Neural_{Symbolic} |
| **GT Concept** | Nash Equilibrium |
| **Game Info** | Continuous-time, differential game |
| **Players** | 2-player |
| **Domain** | Time-series analysis |
| **Neural Component** | Neural stochastic differential equations |
| **Symbolic Component** | Differential game structure (Feynman-Kac formalism) |
| **Integration** | Game-theoretic structure built into neural SDE architecture |
| **GT Property** | Nash equilibrium (deep neural fictitious play) |
| **Evaluation** | Empirical benchmark |
| **Maturity** | Prototype |
| **Explainability** | Partial |
| **Defense Relevance** | Indirect |
| **Key Contribution** | Neural SDE framework for differential games with convergence guarantees |

### P17 — Neural Mean-Field Games (2025)

| Field | Value |
|---|---|
| **Title** | Neural Mean-Field Games: Extending Mean-Field Game Theory with Neural Stochastic Differential Equations |
| **Year** | 2025 |
| **Venue** | arXiv:2504.13228 |
| **Type** | Preprint |
| **NeSy Type** | Type 4: Neural_{Symbolic} |
| **GT Concept** | Mean-field |
| **Game Info** | Large population, continuous-time |
| **Players** | Population |
| **Domain** | General |
| **Neural Component** | Neural stochastic differential equations |
| **Symbolic Component** | Mean-field game PDE structure |
| **Integration** | Neural SDEs extend MFG theory with learned dynamics |
| **GT Property** | Mean-field equilibrium |
| **Evaluation** | Empirical |
| **Maturity** | Conceptual/prototype |
| **Explainability** | Partial |
| **Defense Relevance** | Indirect |
| **Key Contribution** | Extends MFG theory using neural SDEs |

### P18 — Li, Zhu (2024)

| Field | Value |
|---|---|
| **Title** | Symbiotic Game and Foundation Models for Cyber Deception Operations in Strategic Cyber Warfare |
| **Year** | 2024 |
| **Venue** | arXiv:2403.10570 |
| **DOI/URL** | https://arxiv.org/abs/2403.10570 |
| **Type** | Preprint |
| **NeSy Type** | Type 2: Neural\|Symbolic (MANSCOL framework) |
| **GT Concept** | Multiple (Stackelberg, Bayesian, conjectural) |
| **Game Info** | Imperfect, incomplete information |
| **Players** | 2-player (defender-attacker) |
| **Domain** | Cybersecurity / defense |
| **Neural Component** | Foundation models, RL, knowledge assimilation |
| **Symbolic Component** | Game-theoretic models, conjectural learning, doctrinal knowledge |
| **Integration** | Foundation models serve as building blocks within game-theoretic framework (MANSCOL) |
| **GT Property** | Conjectural equilibrium, adaptive strategy synthesis |
| **Evaluation** | Conceptual + case study |
| **Maturity** | Conceptual |
| **Explainability** | Yes (symbolic game structure provides explanation) |
| **Defense Relevance** | Direct (cyber warfare, strategic deception) |
| **Key Contribution** | First framework integrating foundation models with game-theoretic cyber deception at operational level |

### P19 — Li, Zhu (2024)

| Field | Value |
|---|---|
| **Title** | A Multi-resolution Dynamic Game Framework for Cross-Echelon Decision-Making in Cyber Warfare |
| **Year** | 2024 |
| **Venue** | GameSec 2024 / Springer |
| **DOI/URL** | https://link.springer.com/chapter/10.1007/978-3-032-08064-6_17 |
| **Type** | Conference |
| **NeSy Type** | Type 2: Neural\|Symbolic |
| **GT Concept** | Stackelberg + dynamic games |
| **Game Info** | Imperfect information, multi-resolution |
| **Players** | Multi-player, cross-echelon |
| **Domain** | Cybersecurity / defense |
| **Neural Component** | Learning components for adversary modeling |
| **Symbolic Component** | Multi-resolution game formulation, hierarchical structure |
| **Integration** | Neural learning within symbolic multi-echelon game framework |
| **GT Property** | Dynamic game equilibrium, cross-echelon coordination |
| **Evaluation** | Case study |
| **Maturity** | Conceptual |
| **Explainability** | Yes |
| **Defense Relevance** | Direct (cyber warfare, C2) |
| **Key Contribution** | Multi-resolution game framework bridging strategic-operational-tactical levels |

### P20 — Nie (2022)

| Field | Value |
|---|---|
| **Title** | Differentiable Bilevel Programming for Stackelberg Congestion Games |
| **Year** | 2022 |
| **Venue** | Northwestern University / arXiv |
| **Type** | Preprint/workshop |
| **NeSy Type** | Type 6: Symbolic∩Neural |
| **GT Concept** | Stackelberg Equilibrium |
| **Game Info** | Complete information |
| **Players** | Leader + population |
| **Domain** | Transportation / congestion |
| **Neural Component** | Differentiable programming, automatic differentiation |
| **Symbolic Component** | Bilevel optimization, congestion game formulation |
| **Integration** | End-to-end differentiable bilevel programming over symbolic game structure |
| **GT Property** | Stackelberg equilibrium computation |
| **Evaluation** | Empirical |
| **Maturity** | Prototype |
| **Explainability** | Partial |
| **Defense Relevance** | Indirect |
| **Key Contribution** | Differentiable approach to Stackelberg congestion games |

### P21 — Game Theory Meets LLMs Survey (2025)

| Field | Value |
|---|---|
| **Title** | Game Theory Meets Large Language Models: A Systematic Survey with Taxonomy and New Frontiers |
| **Year** | 2025 |
| **Venue** | IJCAI 2025 / arXiv:2502.09053 |
| **DOI/URL** | https://arxiv.org/abs/2502.09053 |
| **Type** | Survey |
| **NeSy Type** | Type 5: Neural[Symbolic] (LLMs as neural, GT as symbolic) |
| **GT Concept** | Multiple (comprehensive survey) |
| **Game Info** | Various |
| **Players** | Various |
| **Domain** | General (AI/economics) |
| **Neural Component** | Large language models |
| **Symbolic Component** | Game-theoretic concepts and evaluation frameworks |
| **Integration** | Bidirectional: GT evaluates LLMs; LLMs advance GT |
| **GT Property** | Multiple |
| **Evaluation** | Literature survey |
| **Maturity** | N/A (survey) |
| **Explainability** | Addressed |
| **Defense Relevance** | Indirect |
| **Key Contribution** | First comprehensive bidirectional survey of GT × LLM intersection |

### P22 — LLM Strategic Reasoning (2025)

| Field | Value |
|---|---|
| **Title** | LLM Strategic Reasoning: Agentic Study through Behavioral Game Theory |
| **Year** | 2025 |
| **Venue** | arXiv:2502.20432 |
| **Type** | Preprint |
| **NeSy Type** | Type 5: Neural[Symbolic] |
| **GT Concept** | Nash Equilibrium (behavioral GT) |
| **Game Info** | Various |
| **Players** | Multi-player |
| **Domain** | General (AI evaluation) |
| **Neural Component** | 22 state-of-the-art LLMs |
| **Symbolic Component** | Game-theoretic evaluation framework, behavioral game theory |
| **Integration** | LLMs evaluated on symbolic game-theoretic tasks |
| **GT Property** | Strategic reasoning, Nash equilibrium play |
| **Evaluation** | Empirical (behavioral experiments) |
| **Maturity** | Prototype |
| **Explainability** | Partial |
| **Defense Relevance** | Indirect |
| **Key Contribution** | Systematic behavioral GT evaluation of LLM strategic capabilities |

### P23 — Strategic Behavior of LLMs (2024)

| Field | Value |
|---|---|
| **Title** | Strategic behavior of large language models and the role of game structure versus contextual framing |
| **Year** | 2024 |
| **Venue** | Nature Scientific Reports |
| **DOI/URL** | https://www.nature.com/articles/s41598-024-69032-z |
| **Type** | Journal |
| **NeSy Type** | Type 5: Neural[Symbolic] |
| **GT Concept** | Nash Equilibrium |
| **Game Info** | Complete information |
| **Players** | 2-player |
| **Domain** | General (behavioral economics) |
| **Neural Component** | Large language models |
| **Symbolic Component** | Classical game theory (Prisoner's Dilemma, Ultimatum Game) |
| **Integration** | LLMs play symbolically-defined games |
| **GT Property** | Equilibrium behavior analysis |
| **Evaluation** | Empirical |
| **Maturity** | Prototype |
| **Explainability** | Partial |
| **Defense Relevance** | Indirect |
| **Key Contribution** | Game structure matters more than framing for LLM strategic behavior |

### P24 — Playing Repeated Games with LLMs (2025)

| Field | Value |
|---|---|
| **Title** | Playing repeated games with large language models |
| **Year** | 2025 |
| **Venue** | Nature Human Behaviour |
| **DOI/URL** | https://www.nature.com/articles/s41562-025-02172-y |
| **Type** | Journal |
| **NeSy Type** | Type 5: Neural[Symbolic] |
| **GT Concept** | Nash + Cooperative (repeated games) |
| **Game Info** | Complete information, repeated |
| **Players** | 2-player |
| **Domain** | General (behavioral economics) |
| **Neural Component** | Large language models |
| **Symbolic Component** | Repeated game theory, cooperation analysis |
| **Integration** | LLMs in repeated game settings |
| **GT Property** | Cooperation emergence, equilibrium in repeated games |
| **Evaluation** | Empirical |
| **Maturity** | Prototype |
| **Explainability** | Partial |
| **Defense Relevance** | Indirect |
| **Key Contribution** | LLMs show higher cooperation than humans in social dilemmas |

### P25 — Game-theoretic Evaluation of LLM Strategic Reasoning (2025)

| Field | Value |
|---|---|
| **Title** | Game-theoretic evaluation of strategic reasoning in large language models: From complete coverage to compositional complexity |
| **Year** | 2025 |
| **Venue** | Neurocomputing / ScienceDirect |
| **Type** | Journal |
| **NeSy Type** | Type 5: Neural[Symbolic] |
| **GT Concept** | Nash Equilibrium |
| **Game Info** | Various |
| **Players** | 2-player |
| **Domain** | General (AI evaluation) |
| **Neural Component** | Large language models |
| **Symbolic Component** | Game-theoretic evaluation framework |
| **Integration** | Systematic evaluation of LLM game-theoretic reasoning |
| **GT Property** | Strategic reasoning quality |
| **Evaluation** | Empirical |
| **Maturity** | Prototype |
| **Explainability** | Addressed |
| **Defense Relevance** | Indirect |
| **Key Contribution** | Reveals critical limitations in LLM strategic reasoning |

### P26 — Duel-based Neuroevolution for SSGs (2023)

| Field | Value |
|---|---|
| **Title** | Duel-based neuroevolutionary method for Stackelberg Security Games with boundedly rational Attacker |
| **Year** | 2023 |
| **Venue** | Applied Soft Computing |
| **DOI/URL** | https://www.sciencedirect.com/science/article/pii/S1568494623006919 |
| **Type** | Journal |
| **NeSy Type** | Type 2: Neural\|Symbolic |
| **GT Concept** | Stackelberg Equilibrium |
| **Game Info** | Imperfect information, bounded rationality |
| **Players** | 2-player |
| **Domain** | Security |
| **Neural Component** | Neuroevolutionary methods |
| **Symbolic Component** | Stackelberg security game structure |
| **Integration** | Neural evolution within symbolic game framework |
| **GT Property** | Stackelberg equilibrium with bounded rationality |
| **Evaluation** | Empirical |
| **Maturity** | Prototype |
| **Explainability** | Partial |
| **Defense Relevance** | Direct (security resource allocation) |
| **Key Contribution** | Neuroevolutionary approach to SSGs handling attacker bounded rationality |

### P27 — StEVe Verification Tool (2024)

| Field | Value |
|---|---|
| **Title** | StEVe: A Rational Verification Tool for Stackelberg Security Games |
| **Year** | 2024 |
| **Venue** | Springer |
| **DOI/URL** | https://link.springer.com/chapter/10.1007/978-3-031-76554-4_15 |
| **Type** | Conference (tool paper) |
| **NeSy Type** | Type 1: Symbolic[Neural] |
| **GT Concept** | Stackelberg Equilibrium |
| **Game Info** | Complete information |
| **Players** | 2-player |
| **Domain** | Security |
| **Neural Component** | Verification of strategies (potentially learned) |
| **Symbolic Component** | Rational verification, model checking |
| **Integration** | Symbolic verification of game strategies |
| **GT Property** | Rational verification of Stackelberg strategies |
| **Evaluation** | Tool + benchmarks |
| **Maturity** | Prototype |
| **Explainability** | Yes |
| **Defense Relevance** | Indirect |
| **Key Contribution** | First rational verification tool specifically for Stackelberg security games |

### P28 — Evolutionary GT + Deep RL Review (2025)

| Field | Value |
|---|---|
| **Title** | Reinforcement learning in evolutionary game theory: A brief review of recent developments |
| **Year** | 2025 |
| **Venue** | Applied Mathematics and Computation |
| **DOI/URL** | https://www.sciencedirect.com/science/article/abs/pii/S0096300325004114 |
| **Type** | Survey |
| **NeSy Type** | Type 2: Neural\|Symbolic |
| **GT Concept** | Evolutionary |
| **Game Info** | Population dynamics |
| **Players** | Population |
| **Domain** | General |
| **Neural Component** | Deep RL (DQN, policy gradient) |
| **Symbolic Component** | Evolutionary game dynamics, replicator equation |
| **Integration** | RL algorithms applied within evolutionary game framework |
| **GT Property** | Evolutionary stable strategy, population dynamics |
| **Evaluation** | Literature survey |
| **Maturity** | N/A (survey) |
| **Explainability** | Addressed |
| **Defense Relevance** | Indirect |
| **Key Contribution** | Reviews RL-EGT integration, identifies open problems |

### P29 — EGT + Deep RL for Energy Markets (2024)

| Field | Value |
|---|---|
| **Title** | Integrating Evolutionary Game-Theoretical Methods and Deep Reinforcement Learning for Adaptive Strategy Optimization in User-Side Electricity Markets |
| **Year** | 2024 |
| **Venue** | Mathematics (MDPI) |
| **Type** | Journal |
| **NeSy Type** | Type 2: Neural\|Symbolic |
| **GT Concept** | Evolutionary |
| **Game Info** | Population dynamics |
| **Players** | Population |
| **Domain** | Energy markets |
| **Neural Component** | Deep RL (DQN) |
| **Symbolic Component** | Evolutionary game dynamics |
| **Integration** | DRL addresses limitations of classical EGT in dynamic settings |
| **GT Property** | Evolutionary stable strategy |
| **Evaluation** | Review + empirical |
| **Maturity** | Prototype |
| **Explainability** | Partial |
| **Defense Relevance** | None |
| **Key Contribution** | Systematic review of DRL-EGT integration in energy markets |

### P30 — Bayesian Beliefs in Games (2024)

| Field | Value |
|---|---|
| **Title** | Modeling Other Players with Bayesian Beliefs for Games with Incomplete Information |
| **Year** | 2024 |
| **Venue** | arXiv:2405.14122 |
| **Type** | Preprint |
| **NeSy Type** | Type 2: Neural\|Symbolic |
| **GT Concept** | Bayesian Game |
| **Game Info** | Incomplete information |
| **Players** | Multi-player |
| **Domain** | General games |
| **Neural Component** | Neural network belief models |
| **Symbolic Component** | Bayesian game formulation, belief updating |
| **Integration** | Neural belief models within symbolic Bayesian game framework |
| **GT Property** | Bayesian Nash equilibrium |
| **Evaluation** | Empirical |
| **Maturity** | Prototype |
| **Explainability** | Partial |
| **Defense Relevance** | Indirect (fog-of-war, intelligence analysis) |
| **Key Contribution** | Explicit Bayesian belief modeling for neural game-playing agents |

### P31 — NeuroGame Framework (2024)

| Field | Value |
|---|---|
| **Title** | Game Theory Meets Statistical Mechanics in Deep Learning Design |
| **Year** | 2024 |
| **Venue** | arXiv:2410.12264 |
| **Type** | Preprint |
| **NeSy Type** | Type 4: Neural_{Symbolic} |
| **GT Concept** | Cooperative (Shapley value) |
| **Game Info** | Cooperative game among neurons |
| **Players** | Multi-player (neurons as players) |
| **Domain** | Neural architecture design |
| **Neural Component** | Deep neural networks |
| **Symbolic Component** | Cooperative game theory (Shapley value), statistical mechanics |
| **Integration** | Game-theoretic structure internalized in neural network design |
| **GT Property** | Coalition formation, Shapley value |
| **Evaluation** | Empirical |
| **Maturity** | Prototype |
| **Explainability** | Yes (Shapley-based interpretability) |
| **Defense Relevance** | None |
| **Key Contribution** | Novel architecture using cooperative GT for neural network design |

### P32 — Generative AI for Network Game Equilibria (2024)

| Field | Value |
|---|---|
| **Title** | Exploring Equilibrium Strategies in Network Games with Generative AI |
| **Year** | 2024 |
| **Venue** | arXiv:2405.08289 |
| **Type** | Preprint |
| **NeSy Type** | Type 6: Symbolic∩Neural |
| **GT Concept** | Nash Equilibrium |
| **Game Info** | Network games |
| **Players** | Multi-player (network) |
| **Domain** | General |
| **Neural Component** | Generative AI models (flow-based) |
| **Symbolic Component** | Network game equilibrium structure |
| **Integration** | Generative models directly compute equilibria |
| **GT Property** | Nash equilibrium computation |
| **Evaluation** | Empirical |
| **Maturity** | Prototype |
| **Explainability** | Partial |
| **Defense Relevance** | Indirect |
| **Key Contribution** | Generative AI approach to equilibrium computation with convergence guarantees |

### P33 — Colbert, Kott, Knachel (2020)

| Field | Value |
|---|---|
| **Title** | The game-theoretic model and experimental investigation of cyber wargaming |
| **Year** | 2020 |
| **Venue** | Journal of Defense Modeling and Simulation |
| **DOI/URL** | https://journals.sagepub.com/doi/abs/10.1177/1548512918795061 |
| **Type** | Journal |
| **NeSy Type** | Proto-NeSy (rule-based + computational) |
| **GT Concept** | Multiple (extensive-form games) |
| **Game Info** | Imperfect information |
| **Players** | 2-player |
| **Domain** | Cyber wargaming |
| **Neural Component** | Computational agents |
| **Symbolic Component** | Game-theoretic framework, rule-based wargame model |
| **Integration** | Computational agents in symbolic game-theoretic wargame |
| **GT Property** | Experimental game theory |
| **Evaluation** | Experimental (human subjects) |
| **Maturity** | Prototype |
| **Explainability** | Yes |
| **Defense Relevance** | Direct (cyber wargaming) |
| **Key Contribution** | Experimental validation of game-theoretic cyber wargame model |

### P34 — LLMs for Open-ended Wargames (2025)

| Field | Value |
|---|---|
| **Title** | Shall We Play a Game? Language Models for Open-ended Wargames |
| **Year** | 2025 |
| **Venue** | arXiv:2509.17192 |
| **Type** | Preprint |
| **NeSy Type** | Type 5: Neural[Symbolic] |
| **GT Concept** | Strategic interaction (informal) |
| **Game Info** | Imperfect information |
| **Players** | Multi-player |
| **Domain** | Wargaming / defense |
| **Neural Component** | Large language models |
| **Symbolic Component** | Wargame rules, scenario structure |
| **Integration** | LLMs play within symbolic wargame structure |
| **GT Property** | Strategic decision-making |
| **Evaluation** | Case study |
| **Maturity** | Prototype |
| **Explainability** | Partial (LLM reasoning traces) |
| **Defense Relevance** | Direct (wargaming) |
| **Key Contribution** | Demonstrates LLM capabilities in open-ended wargaming |

---

## FORMAL SEARCH ADDITIONS (Phase 2 — Database Search Agents)

Papers identified by formal database search agents (S1-S6), citation tracking, and grey literature search. Listed in condensed format; full extraction forms to be created during Phase 4 (full-text review).

### Type 1: Symbolic[Neural] — New Papers

| ID | Authors | Title | Year | Venue | GT Concept | Key Contribution |
|---|---|---|---|---|---|---|
| P35 | Kwiatkowska, Norman, Parker, Santos, Yan | Probabilistic Model Checking for Strategic Equilibria-Based Decision Making | 2022 | MFCS 2022 (LIPIcs) | Nash + Correlated | Overview of PRISM-games equilibria verification including CE; outlines neural extensions |
| P36 | Chatterji, Acar | Think Smart, Act SMARL! Probabilistic Logic Shields for Multi-Agent RL | 2024 | ECAI 2024 | Nash (n-player) | Probabilistic logic shields for safe MARL with formal guarantees on game-theoretic benchmarks |
| P37 | Kouvaros | Towards Formal Verification of Neuro-symbolic Multi-agent Systems | 2023 | IJCAI 2023 (Early Career) | Multi-agent strategic (ATL) | Verification of NeSy MAS covering adversarial robustness and strategic properties |
| P38 | Kouvaros, Botoeva, De Bonis-Campbell | Formal Verification of Parameterised Neural-symbolic Multi-agent Systems | 2024 | IJCAI 2024 | Multi-agent (parameterised) | Extends NeSy MAS verification to arbitrary numbers of agents; CTL verification + emergence |
| P39 | Bacci, Parker | Verified Probabilistic Policies for Deep Reinforcement Learning | 2022 | NFM 2022 | Verified strategies | PRISM-based verification of deep RL policies; finite- and infinite-horizon |
| P40 | Jin, Tian, Zhi, Wen, Zhang | Trainify: CEGAR-Driven Training and Verification for Safe Deep RL | 2022 | CAV 2022 | Verified strategies | CEGAR verification-in-the-loop DRL training on coarsely abstracted state spaces |
| P41 | Xie, Kersting, Neider | Neuro-Symbolic Verification of Deep Neural Networks | 2022 | IJCAI 2022 | Adversarial (verification) | Reference networks for concept-level DNN verification |

### Type 2: Neural|Symbolic — New Papers

| ID | Authors | Title | Year | Venue | GT Concept | Key Contribution |
|---|---|---|---|---|---|---|
| P42 | Cheng, Knoll, Liao | Neuro-Symbolic Causal Reasoning Meets Signaling Game for Emergent Semantic Communications | 2023 | IEEE JSAC | Signaling game (Nash) | NeSy causal reasoning + signaling game for emergent language design |
| P43 | Luo, Huang et al. | Multi-agent Cooperative Games Using Belief Map Assisted Training (BAMS) | 2024 | ECAI 2023 | Cooperative | Neuro-symbolic belief map for interpretable cooperative MARL |
| P44 | Amador, Gierasimczuk | SymDQN: Symbolic Knowledge and Reasoning in Neural Network-based RL | 2025 | NeSy 2025 | Sequential games | Logic Tensor Networks + DuelDQN for symbolic-augmented RL |
| P45 | Kimura et al. | A Hybrid Neuro-Symbolic Approach for Text-Based Games Using ILP | 2022 | AAAI 2022 Workshop | Sequential games | Answer Set Programming rules learned via ILP guide neural RL in text games |
| P46 | Dong, Mao, Lin, Wang, Li, Zhou | Neural Logic Machines | 2019 | ICLR 2019 | Sequential games | Differentiable neural operators on tensor predicates for relational reasoning |
| P47 | Jacob, Shen, Farina, Andreas | The Consensus Game: Language Model Generation via Equilibrium Search | 2024 | ICLR 2024 | Signaling game (Nash) | LM decoding as game between generator/discriminator; equilibrium-ranking outperforms much larger models |
| P48 | Wellman, Tuyls, Greenwald | Empirical Game-Theoretic Analysis: A Survey | 2025 | JAIR | Nash (empirical) | Neural payoff approximation within symbolic meta-game models |
| P49 | Nowak, Xie et al. | Explore Reinforced: Equilibrium Approximation with Reinforcement Learning | 2025 | GameSec 2025 | Coarse Correlated Eq. | Exp3-IXrl blends RL action selection with game-theoretic CCE approximation |
| P50 | Johansson et al. | Dynamic Shields: Game-Theoretic RL Framework for APT Mitigation | 2025 | GameSec 2025 | Nash (POMDP game) | PPO reduces attack success by 65%; proves equilibrium existence in attacker-defender game |
| P51 | Trencsenyi, Mensfelt, Stathis | Approximating Human Strategic Reasoning with LLM-Enhanced Recursive Reasoners Leveraging Multi-agent Hypergames | 2025 | arXiv:2502.07443 | Hypergame | LLMs for recursive strategic reasoning in beauty contest games within hypergame belief hierarchy |
| P52 | Thomas, Saad | Hypergame Theory for Decentralized Resource Allocation in Multi-user Semantic Communications | 2024 | arXiv:2409.17985 | Stackelberg Hypergame | ~45% reduction in physical bits via Stackelberg hypergame with misperception modeling |

### Type 3: Compilation — New Papers

| ID | Authors | Title | Year | Venue | GT Concept | Key Contribution |
|---|---|---|---|---|---|---|
| P54 | Yang et al. | STLGame: Signal Temporal Logic Games in Adversarial Multi-Agent Systems | 2025 | L4DC 2025 | Nash (fictitious self-play) | Differentiable STL formulas compiled into neural policy optimization for adversarial multi-agent control |
| P55 | Yang et al. | Stackelberg Game Approach for STL Control Synthesis with Uncontrollable Agents | 2025 | arXiv:2502.14585 | Stackelberg | STL specifications + counter-example guided synthesis in leader-follower settings |
| P56 | Mannucci | Logical GANs: Adversarial Learning through Ehrenfeucht-Fraisse Games (LOGAN) | 2025 | arXiv:2510.22824 | Adversarial (Nash-seeking) | Logic-constrained adversarial training; first-order logic equivalence via EF games |
| P57 | Gutierrez, Hammond, Wooldridge et al. | Rational Verification: Game-Theoretic Verification of Multi-Agent Systems | 2021 | Applied Intelligence | Nash (equilibrium checking) | Temporal logic + equilibrium checking framework for multi-agent system verification |
| P58 | Meta FAIR (Bakhtin, Brown et al.) | Human-Level Play in the Game of Diplomacy by Combining Language Models with Strategic Reasoning (CICERO) | 2022 | Science 378(6624) | Cooperative + Bayesian | LM + planning + RL for cooperative-competitive Diplomacy; top 10% of human players |
| P59 | Liu, Peters, Alonso-Mora | Auto-Encoding Bayesian Inverse Games | 2024 | WAFR 2024 | Bayesian Nash (differentiable) | Differentiable Nash game solver embedded in VAE for multi-modal Bayesian inference; autonomous driving |

### Type 4: Neural_{Symbolic} — New Papers

| ID | Authors | Title | Year | Venue | GT Concept | Key Contribution |
|---|---|---|---|---|---|---|
| P60 | Marris, Lanctot, Gemp, Piliouras, Tuyls | Turbocharging Solution Concepts: Solving NEs, CEs and CCEs with Neural Equilibrium Solvers | 2022 | NeurIPS 2022 | Nash + Correlated + CCE | Equivariant neural network outputs symbolic equilibrium strategies; covers all three equilibrium concepts |
| P61 | Gemp, McWilliams, Vernade, Graepel | EigenGame: PCA as a Nash Equilibrium | 2021 | ICLR 2021 (Oral) | Nash (competitive) | Game-theoretic formulation of PCA as multi-player Nash; Oja's rule + Gram-Schmidt |
| P62 | Wang, Yang, Li et al. | Reinforcement Nash Equilibrium Solver (RENES) | 2024 | IJCAI 2024 | Nash | GNN encodes game structure + PPO solves for symbolic equilibrium |
| P63 | Gatti, Gemp, Graepel et al. | Generative Adversarial Equilibrium Solvers (GAES) | 2024 | ICLR 2024 | Generalized Nash + Competitive Eq. | GAN architecture outputs symbolic equilibrium solutions; pseudo-games, Arrow-Debreu economies |
| P64 | Gao et al. | Learning Game-Theoretic Models of Multiagent Trajectories Using Implicit Layers | 2021 | AAAI 2021 | Nash (potential games) | Neural preference learning + differentiable Nash implicit layer; autonomous driving |
| P65 | Ling, Fang, Kolter | Differentiable Equilibrium Computation with Decision Diagrams for Stackelberg | 2021 | NeurIPS 2021 | Stackelberg (combinatorial) | ZDD-based differentiable optimization over combinatorial congestion games |
| P66 | Liu, Rasul, Chao, Etesami | Riemannian Manifold Learning for Stackelberg Games with Neural Flow Representations | 2025 | arXiv:2502.05498 | Stackelberg | Neural normalizing flows learn Stackelberg manifold; cybersecurity, supply chains |
| P67 | Baldoni et al. | A General Framework for Optimizing and Learning Nash Equilibrium | 2024 | arXiv:2408.16260 | Nash | GNN learns cost functions + variational inequality for Nash computation |
| P68 | Wang, Song, Gao et al. | Differentiable Arbitrating in Zero-sum Markov Games | 2023 | AAMAS 2023 | Nash (mechanism design) | Backpropagation through Nash equilibrium for reward perturbation / mechanism design |
| P69 | Balduzzi, Racaniere, Martens, Foerster, Tuyls, Graepel | The Mechanics of n-Player Differentiable Games | 2018 | ICML 2018 | Nash (potential + Hamiltonian) | Symplectic Gradient Adjustment; Jacobian decomposition of differentiable games |
| P70 | Letcher, Balduzzi et al. | Differentiable Game Mechanics | 2019 | JMLR | Nash (potential + Hamiltonian) | Fixed point analysis and convergence guarantees for differentiable game dynamics |
| P71 | Hartford, Wright, Leyton-Brown | Deep Learning for Predicting Human Strategic Behavior | 2016 | NeurIPS 2016 | Nash (behavioral, level-k) | Neural network encodes behavioral game theory for predicting human play |

### Type 5: Neural[Symbolic] — New Papers

| ID | Authors | Title | Year | Venue | GT Concept | Key Contribution |
|---|---|---|---|---|---|---|
| P72 | Mayoral-Vilches, Sanz-Gomez, Balassone, Rass et al. | Cybersecurity AI: G-CTR — A Game-Theoretic AI for Guiding Attack and Defense | 2026 | arXiv:2601.05887 | Nash (attack graphs) | G-CTR layer extracts attack graphs, computes Nash, feeds digest to LLM; 52.4% win rate vs 28.6% baseline |
| P73 | Xie et al. | Nash Q-Network for Multi-Agent Cybersecurity Simulation | 2025 | GameSec 2025 | Nash (Markov game) | Deep Q-Network + PPO with symbolic Nash-Q algorithm for cyber defense |
| P74 | Zhu | Game Theory Meets LLM and Agentic AI: Reimagining Cybersecurity | 2025 | arXiv:2507.10621 | Multiple (Stackelberg, Bayesian) | Position paper: LLM agents operationalize game-theoretic strategies for cybersecurity |
| P75 | Lanctot et al. | Neural Replicator Dynamics | 2020 | AAMAS 2020 | Evolutionary (replicator) | Neural policy parameterization + replicator dynamics convergence for imperfect-info games |
| P76 | Kublashvili | Probabilistic Neuro-Symbolic Reasoning for Sparse Historical Data with Game-Theoretic Allocation | 2025 | arXiv:2512.01723 | Cooperative (Shapley) | Attention + causal models + Shapley allocation for historical territorial analysis |
| P77 | Lei, Ge, Zhu | ADAPT: A Game-Theoretic and Neuro-Symbolic Framework for Automated Distributed Adaptive Penetration Testing | 2024 | IEEE MILCOM 2024 | Game-theoretic meta-game | Integrates game-theoretic security modeling with NeSy adaptive knowledge exploration for pen-testing |
| P78 | Trencsenyi | Hypergame Rationalisability: Solving Agent Misalignment in Strategic Play | 2025 | arXiv:2512.11942 | Hypergame | Logic-based DSL + answer-set programming for automated hypergame rationalisation |
| P53 | Al Bari, Zhu | A Gestalt Game-Theoretic Framework for Designing Agentic AI Workflows in Cyber Deception | 2025 | GameSec 2025 | Gestalt Nash Eq. (Stackelberg + signaling) | Novel "Gestalt Equilibrium" concept; LLM agents orchestrated by game-theoretic workflow for cyber deception |

### Type 6: Symbolic-Neural — New Papers

| ID | Authors | Title | Year | Venue | GT Concept | Key Contribution |
|---|---|---|---|---|---|---|
| P79 | Abbasi et al. | CQD-SHAP: Explainable Complex Query Answering via Shapley Values | 2025 | arXiv:2510.15623 | Cooperative (Shapley) | Shapley-based explanation of NeSy knowledge graph reasoning |
| P80 | Mastropietro, Pasculli et al. | GStarX: Explaining Graph Neural Networks with Structure-Aware Cooperative Games | 2022 | NeurIPS 2022 | Cooperative (Shapley-like) | Structure-aware cooperative game for GNN explanation |
| P81 | Tan et al. | Game-theoretic Counterfactual Explanation for Graph Neural Networks | 2024 | AAAI 2024 | Cooperative (Banzhaf) | Banzhaf values for counterfactual GNN explanations |
| P82 | Zhang et al. | Knowledge Graph Query and Reasoning Based on Game Theory | 2020 | IEEE IAEAC 2020 | Strategic aggregation | Game-theoretic correlation reasoning for sparse KG data |

---

## SECONDARY CORPUS

Papers in borderline categories per Protocol Section 5.3.

### Category A: Foundational Neural Game Solvers

| ID | Citation | Year | Venue | Game Type | Key Contribution |
|---|---|---|---|---|---|
| SA01 | Brown, Sandholm. "Deep Counterfactual Regret Minimization" | 2019 | ICML | Poker (imperfect info) | Neural function approximation for CFR in full game |
| SA02 | Brown et al. "ReBeL: Combining Online/Offline RL" | 2020 | NeurIPS/Science | General imperfect info | Sound RL+search for imperfect-information games |
| SA03 | Moravčík et al. "DeepStack: Expert-Level AI in HUNL Poker" | 2017 | Science | Poker | Continual re-solving with neural value networks |
| SA04 | Silver et al. "Mastering Chess and Shogi by Self-Play (AlphaZero)" | 2018 | Science | Chess, shogi, Go | Self-play RL with MCTS for perfect-info games |
| SA05 | Vinyals et al. "Grandmaster Level in StarCraft II (AlphaStar)" | 2019 | Nature | StarCraft II | Multi-agent RL for complex imperfect-info game |
| SA06 | Meta FAIR. "Human-level play in Diplomacy (CICERO)" | 2022 | Science | Diplomacy | LLM + strategic reasoning for negotiation game |
| SA07 | Lanctot et al. "OpenSpiel: A Framework for RL in Games" | 2019 | arXiv | Framework | Multi-game evaluation framework |
| SA08 | Heinrich, Silver. "Deep RL from Self-Play (NFSP)" | 2016 | NeurIPS | Imperfect info | Neural fictitious self-play |
| SA09 | Brown, Sandholm. "Superhuman AI for HUNL Poker (Pluribus)" | 2019 | Science | 6-player poker | First superhuman multiplayer poker AI |

### Category B: Symbolic Game Formalisms

| ID | Citation | Year | Venue | Key Contribution |
|---|---|---|---|---|
| SB01 | Love et al. "General Game Playing: Game Description Language (GDL)" | 2008 | AI Magazine | Standard language for game specification |
| SB02 | Alur, Henzinger, Kupferman. "Alternating-time Temporal Logic (ATL)" | 2002 | JACM | Temporal logic for strategic reasoning |
| SB03 | Kwiatkowska et al. "PRISM-games model checker" | 2013-2020 | CAV/STTT | Probabilistic model checking for stochastic games |

### Category C: Proto-Neuro-Symbolic

| ID | Citation | Year | Domain | Hybrid Characteristics |
|---|---|---|---|---|
| SC01 | Laird. "The Soar Cognitive Architecture" + RL extensions | 2012+ | Military simulation | Symbolic cognitive architecture + RL learning |
| SC02 | Lockheed-Martin/Cycorp team (DARPA Gamebreaker) | 2020 | Wargaming | Symbolic AI (Cyc ontology) + ML for game balance |
| SC03 | CyQuaPro framework | 2024 | Cybersecurity | Stackelberg game + computational agents |

### Category D: Key Surveys and Reviews

| ID | Citation | Year | Venue | Scope |
|---|---|---|---|---|
| SD01 | Garcez, Lamb. "Neurosymbolic AI: The 3rd Wave" | 2023 | Artificial Intelligence Review | NeSy taxonomy and landscape |
| SD02 | Gibaut et al. "Neurosymbolic AI and its taxonomy: a survey" | 2023 | arXiv:2305.08876 | Comprehensive NeSy taxonomy |
| SD03 | "Neuro-Symbolic AI in 2024: A Systematic Review" | 2024 | CEUR-WS Vol. 3819 | Annual NeSy landscape |
| SD04 | "Applications of game theory in deep learning: a survey" | 2022 | PMC | GT applied to DL (inverse direction) |
| SD05 | Hagos, Rawat. "Game Theory in Defence Applications: A Review" | 2022 | Games (MDPI) / PMC | GT for defense (no NeSy focus) |
| SD06 | De La Fuente et al. "Game Theory and Multi-Agent RL: Nash to Evolutionary" | 2025 | SSRN | MARL + GT convergence |
| SD07 | Curry et al. "Automated Mechanism Design: A Survey" | 2024 | SIGecom Exchanges | Neural mechanism design landscape |
| SD08 | "Towards Cognitive AI Systems: A Survey on Neuro-Symbolic AI" | 2024 | arXiv:2401.01040 | Cognitive NeSy perspective |
| SD09 | Trencsenyi, Mensfelt, Stathis. "Hypergames: Modeling Misaligned Perceptions for MAS" | 2025 | arXiv:2507.19593 | Hypergame theory survey (44 studies) |
| SD10 | Landers, Doryab. "Deep Reinforcement Learning Verification: A Survey" | 2023 | ACM Computing Surveys | DRL verification methods |
| SD11 | Hagos, Rawat. "Neuro-Symbolic AI for Military Applications" | 2024 | IEEE Access | NeSy for defense survey |
| SD12 | Hakim et al. "Neuro-Symbolic AI for Cybersecurity: State of the Art" | 2025 | arXiv:2509.06921 | 127-publication NeSy cybersecurity survey |
| SD13 | Bizzarri et al. "Neurosymbolic AI for Network Intrusion Detection: A Survey" | 2025 | J. Info. Security & Apps | NeSy for NIDS survey |
| SD14 | Condorelli, Furlan. "Deep Learning Across Games" | 2024 | arXiv:2409.15197 | Emergent NE from adversarial neural training |
| SD15 | Chen, Zhu. "Security Investment under Cognitive Constraints: Gestalt Nash Eq." | 2018 | IEEE CISS | Foundational Gestalt NE concept (pure GT) |

### Category E: Foundational Formal Verification for Games

| ID | Citation | Year | Venue | Key Contribution |
|---|---|---|---|---|
| SE01 | Gutierrez, Harrenstein, Wooldridge. "From Model Checking to Equilibrium Checking" | 2017 | Artificial Intelligence | Foundational "equilibrium checking" framework |
| SE02 | Bastani, Pu, Solar-Lezama. "Verifiable RL via Policy Extraction (VIPER)" | 2018 | NeurIPS | Decision tree policy extraction from DNN oracle |
| SE03 | Bacci, Parker. "Probabilistic Guarantees for Safe Deep RL" | 2020 | FORMATS | Probabilistic verification for deep RL via PRISM |

---

## DEFENSE-SPECIFIC SOURCES (Meeting I2, I3, I7)

### DARPA Programs

| ID | Program | Years | Focus | NeSy Relevance |
|---|---|---|---|---|
| DP01 | Gamebreaker | 2020-2023 | AI game balance analysis for wargaming | Multiple teams including symbolic AI (Cycorp) |
| DP02 | SABER | 2022+ | Strategic adaptive behaviors | AI adversary modeling |
| DP03 | ANSR | 2021+ | Assured Neuro-Symbolic Learning and Reasoning | Core NeSy program |
| DP04 | ACE | 2019+ | Air Combat Evolution | AI dogfighting |
| DP05 | XAI | 2017-2021 | Explainable AI | Explainability techniques |
| DP06 | ITM | 2023+ | In the Moment | Trust in AI decision-making |

### Institutional Reports and Grey Literature

| ID | Source | Year | Focus |
|---|---|---|---|
| IR01 | RAND Corporation reports on AI for wargaming | Various | Policy-level AI wargaming assessments |
| IR02 | MITRE technical reports on AI/ML for defense | Various | Systems-level AI defense applications |
| IR03 | NPS Calhoun repository — wargaming theses | Various | Naval wargaming research |
| IR04 | NATO STO publications (SAS/MSG panels) | Various | Alliance AI and wargaming research |
| IR05 | NATO STO-MP-SAS-192: "Leveraging LLMs for Enhanced Wargaming" | 2024 | NATO assessment of LLM integration in wargaming |
| IR06 | NATO STO-MP-MSG-207: Black & Darken, "Scaling AI for Digital Wargaming" | 2024 | Hierarchical RL with dimension-invariant abstractions for wargaming |
| IR07 | JHU APL publications on AI + game theory for defense | Various | Applied defense AI research |
| IR08 | SERC/AIRC publications on AI for systems engineering | Various | Defense SE research |

### Defense-Relevant NeSy Papers (Not Meeting Primary GT Criterion)

Papers from S2 search that apply NeSy to defense but lack explicit game-theoretic formulation. Retained for RQ3 (defense application mapping).

| ID | Authors | Title | Year | Venue | NeSy Type | Domain |
|---|---|---|---|---|---|---|
| DF01 | Bae, Hwang, Lee, Lee | LLM-based Wargame Scenario Generation with Domain Ontology and ECA Rules | 2026 | Simulation (SAGE) | Type 5 | Wargaming |
| DF02 | Hogan, Brennen | Open-Ended Wargames with Large Language Models (Snow Globe) | 2024 | arXiv:2404.11446 | Type 4 | Wargaming |
| DF03 | Lamparth et al. | Human vs. Machine: Behavioral Differences in Wargame Simulations | 2024 | arXiv:2403.03407 | Type 4 | Wargaming |
| DF04 | Goecks, Waytowich | COA-GPT: Generative Transformers for Course of Action Development | 2024 | NATO IST/ICMCIS | Type 5 | Military C2 |
| DF05 | ReaDS-KG authors | ReaDS-KG: LLM-KG Framework for Reasoned Decision Support | 2025 | TechRxiv/IEEE | Type 5 | Military C2 |
| DF06 | Command-Agent authors | Command-Agent: Reconstructing Warfare Simulation with LLMs | 2025 | Defence Technology | Type 5 | Military C2 |
| DF07 | Imanov et al. | Strategic Doctrine Language Models (sdLM) | 2026 | arXiv:2601.14862 | Type 5 | Military planning |
| DF08 | Rawat | Towards NeSy AI for Assured and Trustworthy Human-Autonomy Teaming | 2023 | IEEE TPS-ISA | Type 1 | Military C2 |
| DF09 | Rawat | Towards NeSy RL for Trustworthy Human-Autonomy Teaming | 2024 | SPIE Defense | Type 3 | Military C2 |
| DF10 | Grov et al. | On the Use of Neurosymbolic AI for Defending Against Cyber Attacks | 2024 | NeSy 2024 | Type 1 | Cybersecurity |
| DF11 | Bizzarri et al. | A Synergistic Approach in Network Intrusion Detection by NeSy AI | 2024 | arXiv:2406.00938 | Type 3 | Cybersecurity |
| DF12 | Kohaut et al. | Probabilistic Mission Design in Neuro-Symbolic Systems (ProMis) | 2025 | arXiv:2501.01439 | Type 5 | Mission engineering |
| DF13 | Grosvenor et al. | Hierarchical Neuro-Symbolic AI for Autonomous Space Operations | 2025 | AMOS 2025 | Type 5 | Space defense |
| DF14 | Nie, Zeng, Meng | Knowledge Reasoning for Military Decision Support KG | 2020 | IEEE CAC | Type 2 | Military C2 |
| DF15 | KG Wargame Coordination authors | A KG Based Approach to Operational Coordination Recognition in Wargame | 2022 | AsiaSim | Type 2 | Wargaming |
| DF16 | Maathuis, Cools | Collateral Damage Assessment Model for AI System Target Engagement | 2025 | MILCOM 2025 | Type 1 | Targeting |
| DF17 | Deep AI Military Staff authors | Deep AI Military Staff: Cooperative Battlefield Situation Awareness | 2022 | J. Supercomputing | Type 3 | Battlefield SA |

---

**Total Primary Corpus:** 82 papers (Phase 2 complete — full-text screening pending)
**Total Secondary Corpus:** 30 entries (9 foundational game solvers + 3 symbolic formalisms + 3 proto-NeSy + 15 surveys/foundations)
**Total Defense-Specific (non-GT):** 17 papers + 8 institutional sources + 6 DARPA programs
**Estimated Total After Full Screening:** 200-250+ papers
