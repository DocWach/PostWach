# Neuro-Symbolic AI Meets Game Theory: A Scoping Review of the Literature Landscape

**White Paper — Working Draft**
**Paul F. Wach, PhD**
**University of Arizona — Systems & Industrial Engineering**
**February 16, 2026**

---

## 1. Purpose

This white paper summarizes preliminary findings from a scoping review at the intersection of three domains: **neuro-symbolic artificial intelligence (NeSy AI)**, **game theory**, and **wargaming/defense systems engineering**. The objective is to map the existing literature landscape, identify gaps, and assess the feasibility of a full scoping or systematic literature review at this intersection.

The central question motivating this review is:

> *What is the state of research integrating neuro-symbolic AI with game-theoretic reasoning, and how might such integration advance wargaming, mission engineering, and defense acquisition decision-making?*

---

## 2. Background and Motivation

### 2.1 The Integration Challenge

Wargaming is fundamentally applied game theory — it involves strategic interaction under uncertainty, adversarial reasoning, multi-agent decisions, incomplete information, and payoff structures. Yet the AI methods currently applied to wargaming (primarily deep reinforcement learning and, more recently, large language models) lack the formal game-theoretic grounding and the explainability that defense decision-makers require.

Neuro-symbolic AI offers a promising path: neural components handle pattern recognition, learning from data, and strategy discovery, while symbolic components enforce doctrinal constraints, provide formal guarantees, and produce traceable, auditable reasoning. When combined with game-theoretic foundations, this hybrid approach could yield systems that are simultaneously *capable* (through learning), *correct* (through formal reasoning), and *credible* (through game-theoretic solution concepts).

### 2.2 Scope

This scoping review spans six venue categories:

1. **Academic AI/ML venues** — NeurIPS, ICML, AAAI, IJCAI, AAMAS, ACM EC
2. **Defense research organizations** — NATO STO (SAS, MSG panels), RAND, DARPA
3. **Systems engineering venues** — INCOSE, IEEE Systems, CSER
4. **Defense industry associations** — NDIA (Systems & Mission Engineering Conference, ETI, GVSETS, Human Systems Conference)
5. **DoD University Affiliated Research Centers** — SERC, AIRC
6. **Naval Postgraduate School** — MOVES Institute, Wargaming Center, Operations Research Department

---

## 3. Findings by Domain

### 3.1 Neuro-Symbolic AI

The NeSy AI field is well-surveyed, with six or more comprehensive reviews published between 2023 and 2025:

- Colelough and Regli (2025) — PRISMA-compliant SLR of 167 papers (2020–2024), using Kautz's six-type taxonomy [1]
- Marra, Dumancic, Manhaeve, and De Raedt (2024) — traces evolution from statistical relational learning to modern NeSy [2]
- Wan et al. (2024) — positions NeSy as the path toward cognitive AI, emphasizing hardware-software co-design [3]
- Yu et al. (2023) — surveys neural-symbolic learning systems across four perspectives [4]

The dominant taxonomy is Henry Kautz's six categories of NeSy integration, ranging from loose coupling (symbolic preprocessing of neural inputs) to tight integration (differentiable symbolic reasoning within neural architectures).

**Critical observation:** None of these surveys address game-theoretic reasoning, strategic interaction, or adversarial decision-making. NeSy research has focused on perception, knowledge representation, and logical inference — not on multi-agent strategic behavior.

### 3.2 Neural Approaches to Game Theory

This is the most active area at the intersection of AI and game theory, with substantial work across several sub-fields:

**Imperfect-information game solving.** Deep RL has achieved superhuman performance in poker (Libratus [5], Pluribus [6]) and real-time strategy (AlphaStar [7]). Key methods include Neural Fictitious Self-Play (Heinrich and Silver, 2016 [8]), Deep Counterfactual Regret Minimization (Brown et al., 2019 [9]), and ReBeL (Brown et al., 2020 [10]).

**Neural equilibrium solvers.** Recent work trains neural networks to approximate Nash equilibria across families of games (Marris et al., 2022; DINES by Gemp et al., 2024 [11]).

**Differentiable economics and neural mechanism design.** RegretNet (Dutting, Feng, Parkes et al., 2019/2024 [12]) models auctions as neural networks, enabling revenue-maximizing incentive-compatible mechanism design. This area is surveyed by Curry et al. (2024) [13].

**Mean-field games.** Neural network-based solvers scale to high-dimensional stochastic mean-field games (Ruthotto et al., 2020 [14]; Angiuli et al., 2024).

**LLMs and game-theoretic reasoning.** Benchmarks such as GTBench (Huang et al., NeurIPS 2024 [15]) and TMGBench (Chen et al., 2024 [16]) consistently show that even frontier LLMs struggle with strategic reasoning beyond simple matrix games. Fan et al. (IJCAI 2025 [17]) provide the first comprehensive taxonomy of the game theory–LLM relationship.

### 3.3 Symbolic and Formal Approaches to Game Theory in AI

A mature formal methods tradition addresses game-theoretic reasoning through logic and verification:

- **Game Description Languages:** GDL (Genesereth, 2005), GDL-II (Thielscher, 2010), GDL-III (Thielscher, 2017 [18]) — logic programming languages for representing game rules declaratively
- **Alternating-Time Temporal Logic (ATL):** Alur, Henzinger, and Kupferman (2002 [19]) — enables specification and verification of strategic properties in multi-agent systems
- **Rational verification:** Gutierrez, Wooldridge et al. (2017–2022 [20]) — checks whether temporal logic formulas hold at game-theoretic equilibria of multi-agent systems
- **Symbolic strategy synthesis:** Kwiatkowska and Parker (2022 [21]) — verifies turn-based stochastic games against Nash equilibrium-based specifications

**Critical observation:** This symbolic tradition has developed independently from the neural game-solving community. The two are not integrated.

### 3.4 Game Theory in Defense and Military Contexts

**Stackelberg Security Games (SSGs).** The most mature application of computational game theory to defense, pioneered by Milind Tambe and deployed at FAMS, USCG, and LAX [22]. Reviewed comprehensively by Bauso et al. (2022 [23]).

**Defense game theory survey.** Bauso et al. (2022) classify applications into Command and Control Warfare subcategories: Resource Allocation Warfare, Information Warfare, Weapons Control Warfare, and Adversary Monitoring Warfare [23].

**Game theory in SE.** Grigoryan and Collins (2021 [24]) and Axelsson (2019 [25]) are the only surveys of game theory applied to systems engineering, covering cooperative vs. non-cooperative models in SoS contexts. Both are purely classical — no AI methods.

### 3.5 AI for Wargaming

This area is growing rapidly across multiple AI paradigms:

**Reinforcement learning.** NPS's Darken lab is a leader, with Black's PhD dissertation (2024 [26]) developing hierarchical RL for the ATLATL wargaming platform. NATO MSG-207 and MSG-217 have produced proceedings on deep RL for combat simulation, including PPO agents achieving 91% win rates in tactical air scenarios.

**Large language models.** Rivera et al. (2024 [27]) found considerable but imperfect agreement between LLM and human responses in a US–China wargame scenario. JHU APL's GenWar Lab (2025) enables AI-powered tabletop exercises.

**Institutional programs.** DARPA Gamebreaker assesses game balance using AI. DARPA SABER (2025) builds AI red teams for operational assessment. The USAF issued an RFI (Nov 2025) for AI-enabled advanced wargaming with RL adversary agents.

**RAND assessments.** Geist and Frank (2024 [28]) caution that AI is "tactically brilliant but strategically naive" and that most wargames lack digital data pipelines needed for AI integration.

### 3.6 Neuro-Symbolic AI in Defense

Only a handful of papers address this directly:

- Joshi et al. (2024 [29]) — the first paper explicitly on neuro-symbolic AI for military applications, reporting 30–100% speedup over symbolic-only baselines
- DARPA ANSR (Assured Neuro Symbolic Learning and Reasoning) — active program seeking hybrid AI algorithms with auditable symbolic traces
- Navy SBIR N251-019 (2025) — explicit call for neuro-symbolic AI agents for cybersecurity ATO development

Proto-neuro-symbolic work exists but is not labeled as such:
- NPS Soar + RL integration (2018–2019) — cognitive architecture with reinforcement learning for kill chains and logistics wargaming
- NPS LAILOW framework (Zhao et al.) — causal learning with EVE structures for multi-segment wargaming
- NPS Mission Execution Ontology (Brutzman) — formal ontological reasoning for autonomous systems
- SERC DEFII framework (Dunbar and Blackburn, 2023) — ontologies and graph data structures for digital engineering
- SERC WRT-1025 — graph embeddings combined with ML over semantic data for digital twins

### 3.7 Defense SE Venues (NDIA, SERC/AIRC, NPS)

**NDIA** has strong coverage of AI4SE (annual Systems & Mission Engineering Conference tracks, AI/ML Working Group) and human-AI teaming (Human Systems Conference series). No explicit NeSy or game theory papers, but two proto-NeSy papers combining knowledge graphs with neural methods (MacPherson, ETI 2024; Hoang et al., GVSETS 2025).

**SERC** has extensive ontology and digital engineering work providing symbolic foundations, plus the annual AI4SE/SE4AI workshop series (2020–2025). The 2024 workshop included multi-agent RL and graph neural networks. **AIRC** has one explicit game theory project (Shittu and Szajnfarber on DoD IP transactions, $812K), plus gamified acquisition training (Finkenstadt and Handfield).

**NPS** has the richest output: world-class RL wargaming (Darken lab, 10+ theses since 2022), applied game theory for defense (Fox, Zhao, Kress), the WRAID conceptual system design (SE Capstone 2022), and hybrid symbolic-neural work (Soar + RL, causal learning with EVE structures).

---

## 4. Gap Analysis

### 4.1 Two-Way Intersections

| Intersection | Existing Work |
|---|---|
| NeSy + Game Theory | **Zero surveys.** ~2 early papers (DICELAB autoformalization project at Royal Holloway). |
| NeSy + Wargaming | **Zero papers.** Community uses neural OR symbolic, never integrated. |
| Game Theory + AI Wargaming | **Near-zero.** NPS WRAID concept is the closest. No papers formally bridge computational GT with RL wargame agents. |
| Mechanism Design + Defense SE | **Absent** despite obvious relevance to acquisition and contract design. |

### 4.2 Three-Way Intersection

The intersection of **neuro-symbolic AI + game theory + wargaming/defense SE** is **entirely absent** from the literature. No paper, technical report, or survey occupies this space across any of the six venue categories searched.

### 4.3 Specific Gaps

1. **Game-theoretic foundations for AI wargaming.** RL wargame agents are not verified against equilibrium concepts (Nash, Stackelberg, correlated equilibrium). No formal connection between the wargaming AI and computational game theory communities.

2. **Neuro-symbolic wargaming agents.** A system combining neural strategy learning with symbolic doctrinal reasoning and game-theoretic optimality guarantees does not exist.

3. **Mechanism design for defense acquisition.** The "inverse game theory" for designing incentive-compatible procurement mechanisms is virtually absent from defense SE literature.

4. **Coalition game theory for alliance wargaming.** NATO coalition wargaming inherently involves cooperative game theory among allies and non-cooperative game theory against adversaries, but no published work formalizes this.

5. **Formal verification of AI wargame agent behavior.** Game-theoretic properties (strategy domination, equilibrium bounds, regret minimization) are not applied to verify learned wargaming strategies.

6. **LLM game-theoretic behavior analysis.** Benchmarks exist but no frameworks bound or verify LLM strategic behavior in wargaming contexts.

7. **Game-theoretic requirements engineering for AI-enabled defense systems.** Multi-stakeholder tensions (capability vs. explainability vs. autonomy vs. oversight) are not modeled game-theoretically.

8. **Multi-agent game-theoretic wargaming at scale.** True multi-player coalition wargaming with information asymmetry and mechanism design is absent.

---

## 5. Existing Surveys and Positioning

The following table maps existing surveys against the planned review's scope:

| Survey | Year | Covers NeSy? | Covers GT? | Covers Wargaming? | Covers SE? |
|---|---|---|---|---|---|
| Colelough & Regli [1] | 2025 | Yes | No | No | No |
| Marra et al. [2] | 2024 | Yes | No | No | No |
| Fan et al. (IJCAI) [17] | 2025 | No | Yes (LLM) | No | No |
| Wellman et al. (EGTA) | 2025 | No | Yes | No | No |
| Bauso et al. [23] | 2022 | No | Yes | Partial | No |
| Geist & Frank (RAND) [28] | 2024 | No | No | Yes | No |
| Grigoryan & Collins [24] | 2021 | No | Yes | No | Yes |
| Curry et al. [13] | 2024 | No | Yes (mech. design) | No | No |
| **Planned review** | **2026** | **Yes** | **Yes** | **Yes** | **Yes** |

No existing survey spans more than two of the four columns.

---

## 6. Proposed Review Framing

Based on these findings, the planned scoping review could be framed as:

> **"Neuro-Symbolic AI Meets Game Theory: A Scoping Review with Applications to Wargaming and Systems Engineering"**

The review would be the first to:

1. **Map NeSy integration types** (Kautz taxonomy) against **game-theoretic solution concepts** (Nash, Stackelberg, evolutionary, mechanism design) — creating a two-dimensional classification framework
2. **Position wargaming as a unifying application domain** that naturally requires all three: multi-agent strategic reasoning (game theory), doctrine and rule-based constraints (symbolic AI), and pattern recognition under uncertainty (neural AI)
3. **Bridge the formal verification tradition** (ATL, rational verification, symbolic strategy synthesis) with **neural game solvers** (Deep CFR, ReBeL, neural equilibrium solvers)
4. **Propose a research agenda** for hybrid NeSy-GT architectures applied to defense and SE decision-making

### 6.1 Target Venues

- **Primary (general SE):** Systems Engineering (Wiley/INCOSE), Journal of Defense Modeling and Simulation, IEEE Systems Journal
- **Application domain (NATO/Defense):** NATO STO SAS/MSG panels, CSER, NDIA Systems & Mission Engineering Conference
- **AI community:** AAMAS, AAAI (for algorithmic novelty)

### 6.2 Connections to Ongoing Work

This review connects to and extends several existing research threads:

- The SERC AI4SE/SE4AI roadmap (McDermott et al., 2020/2023) — extending toward game-theoretic and neuro-symbolic methods
- The DARPA ANSR program — providing a literature foundation for assured neuro-symbolic reasoning in game-theoretic defense contexts
- NPS wargaming AI research (Darken lab) — bridging their empirical RL work with formal game-theoretic and symbolic reasoning foundations
- AIRC game theory for acquisition (Shittu/Szajnfarber) — extending from acquisition IP to broader defense decision-making

---

## 7. Key Researchers

| Domain | Researchers |
|---|---|
| Neural game solving | Noam Brown (Meta), Tuomas Sandholm (CMU), Marc Lanctot (DeepMind) |
| Neural mechanism design | David Parkes (Harvard), Paul Dutting (Google/LSE) |
| Formal game verification | Michael Wooldridge (Oxford), Julian Gutierrez (Monash), Marta Kwiatkowska (Oxford) |
| Game description languages | Michael Thielscher (UNSW), Michael Genesereth (Stanford) |
| NeSy foundations | Luc De Raedt (KU Leuven), Pascal Hitzler, Artur d'Avila Garcez |
| Security games | Milind Tambe (Harvard) |
| AI wargaming | Christian Darken (NPS), Ying Zhao (NPS), Scotty Black (NPS) |
| Defense game theory | William Fox (NPS), Moshe Kress (NPS) |
| AI4SE | Tom McDermott (SERC/Stevens), Peter Beling (Virginia Tech) |
| GT for defense acquisition | Ekundayo Shittu (GWU/AIRC), Andreas Tolk (MITRE) |
| Autoformalization | DICELAB (Royal Holloway) |

---

## 8. Next Steps

1. **Formalize the scoping review protocol** — research questions, search strategy (databases, search strings), inclusion/exclusion criteria, data extraction template
2. **Conduct systematic searches** across IEEE Xplore, ACM DL, Scopus, Web of Science, arXiv, DTIC, and NATO STO publications
3. **Apply the proposed two-dimensional taxonomy** (NeSy type x GT solution concept) to classify identified papers
4. **Synthesize gaps** into a concrete research agenda with prioritized research questions
5. **Draft the full scoping review manuscript** targeting INCOSE Systems Engineering or a comparable venue

---

## References

[1] B. C. Colelough and W. Regli, "Neuro-Symbolic AI in 2024: A Systematic Review," arXiv:2501.05435, 2025.

[2] G. Marra, S. Dumancic, R. Manhaeve, and L. De Raedt, "From Statistical Relational to Neurosymbolic Artificial Intelligence: A Survey," *Artificial Intelligence*, vol. 328, art. 104062, 2024.

[3] Z. Wan et al., "Towards Cognitive AI Systems: A Survey and Prospective on Neuro-Symbolic AI," arXiv:2401.01040, 2024.

[4] D. Yu, B. Yang, D. Liu, H. Wang, and S. Pan, "A Survey on Neural-Symbolic Learning Systems," *Neural Networks*, vol. 166, pp. 105–126, 2023.

[5] N. Brown and T. Sandholm, "Superhuman AI for heads-up no-limit poker: Libratus beats top professionals," *Science*, vol. 359, no. 6374, pp. 418–424, 2017.

[6] N. Brown and T. Sandholm, "Superhuman AI for multiplayer poker," *Science*, vol. 365, no. 6456, pp. 885–890, 2019.

[7] O. Vinyals et al., "Grandmaster level in StarCraft II using multi-agent reinforcement learning," *Nature*, vol. 575, pp. 350–354, 2019.

[8] J. Heinrich and D. Silver, "Deep Reinforcement Learning from Self-Play in Imperfect-Information Games," in *Proc. NeurIPS*, 2016.

[9] N. Brown, A. Lerer, S. Gross, and T. Sandholm, "Deep Counterfactual Regret Minimization," in *Proc. ICML*, 2019.

[10] N. Brown et al., "Combining Deep Reinforcement Learning and Search for Imperfect-Information Games," in *Proc. NeurIPS*, 2020.

[11] I. Gemp et al., "Solving Nash Equilibrium Scalably via Deep-Learning-Augmented Iterative Algorithms (DINES)," 2024.

[12] P. Dutting, Z. Feng, H. Narasimhan, D. Parkes, and S. S. Ravindranath, "Optimal Auctions through Deep Learning: Advances in Differentiable Economics," *J. ACM*, vol. 71, no. 1, 2024.

[13] M. Curry et al., "Deep Learning Meets Mechanism Design: A Survey," arXiv:2401.05683, 2024.

[14] L. Ruthotto et al., "A Machine Learning Framework for Solving High-Dimensional Mean Field Game and Mean Field Control Problems," *PNAS*, vol. 117, no. 17, pp. 9183–9193, 2020.

[15] Z. Huang et al., "GTBench: Uncovering the Strategic Reasoning Capabilities of LLMs via Game-Theoretic Evaluations," in *Proc. NeurIPS*, 2024.

[16] Y. Chen et al., "TMGBench: A Systematic Game Benchmark for Evaluating Strategic Reasoning Abilities of LLMs," arXiv:2410.10479, 2024.

[17] H. Sun, Y. Wu, Y. Cheng, and X. Chu, "Game Theory Meets Large Language Models: A Systematic Survey with Taxonomy and New Frontiers," in *Proc. IJCAI*, 2025.

[18] M. Thielscher, "GDL-III: A Description Language for Epistemic General Game Playing," in *Proc. IJCAI*, 2017.

[19] R. Alur, T. A. Henzinger, and O. Kupferman, "Alternating-Time Temporal Logic," *J. ACM*, vol. 49, no. 5, pp. 672–713, 2002.

[20] J. Gutierrez, P. Harrenstein, and M. Wooldridge, "Rational Verification: Game-Theoretic Verification of Multi-Agent Systems," *Applied Intelligence*, vol. 51, pp. 6569–6584, 2021.

[21] M. Kwiatkowska, D. Parker, et al., "Symbolic Verification and Strategy Synthesis for Turn-Based Stochastic Games," in *Festschrift for T. Henzinger*, Springer, 2022.

[22] J. Pita, M. Jain, M. Tambe, et al., "Deployed ARMOR Protection: The Application of a Game Theoretic Model for Security at the Los Angeles International Airport," in *Proc. AAMAS*, 2008.

[23] D. Bauso et al., "Game Theory in Defence Applications: A Review," *Sensors*, vol. 22, no. 3, art. 1032, 2022.

[24] G. Grigoryan and A. J. Collins, "Game Theory for Systems Engineering: A Survey," *Int. J. System of Systems Engineering*, vol. 11, no. 2, pp. 121–158, 2021.

[25] J. Axelsson, "Game Theory Applications in Systems-of-Systems Engineering: A Literature Review and Synthesis," *Procedia Computer Science*, vol. 153, pp. 154–165, 2019.

[26] S. Black, "Mastering the Digital Art of War: Developing Intelligent Combat Simulation Agents for Wargaming Using Hierarchical Reinforcement Learning," PhD dissertation, Naval Postgraduate School, 2024.

[27] J. P. Rivera et al., "Human vs. Machine: Language Models and Wargames," arXiv:2403.03407, 2024.

[28] E. Geist, A. B. Frank, and L. Menthe, "Understanding the Limits of Artificial Intelligence for Warfighters: Volume 4, Wargames," RAND Corporation, RR-A1722-4, 2024.

[29] A. Joshi et al., "Neuro-Symbolic AI for Military Applications," arXiv:2408.09224, 2024.
