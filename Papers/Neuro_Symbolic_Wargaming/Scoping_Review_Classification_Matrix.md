# NeSy x GT Classification Matrix (Gap Map)

**Status:** Phase 2 Complete (web-search + formal database search verified)
**Date:** February 16, 2026
**Protocol Reference:** Scoping_Review_Protocol.md, Section 10.3
**Note:** Hypergame added as 9th GT concept based on formal search findings

---

## Color Legend

- **GREEN** (>=5 papers, mature work): Well-populated cell
- **YELLOW** (1-4 papers, early-stage): Emerging research
- **RED** (0 papers): Research opportunity / gap
- Paper IDs reference the Extraction Table (Pxx = primary, SAxx/SBxx/SCxx/SDxx = secondary)

---

## Classification Matrix

| NeSy Type \ GT Concept | Nash Eq. | Stackelberg | Correlated Eq. | Evolutionary | Mechanism Design | Cooperative | Bayesian/POSG | Mean-field | Hypergame |
|---|---|---|---|---|---|---|---|---|---|
| **Type 1: Symbolic[Neural]** | GREEN (5) | YELLOW (1) | YELLOW (1) | RED (0) | RED (0) | RED (0) | YELLOW (2) | RED (0) | RED (0) |
| **Type 2: Neural\|Symbolic** | GREEN (5) | YELLOW (4) | YELLOW (1) | YELLOW (3) | YELLOW (1) | YELLOW (1) | YELLOW (3) | YELLOW (3) | YELLOW (2) |
| **Type 3: Compilation** | YELLOW (3) | YELLOW (1) | RED (0) | RED (0) | RED (0) | YELLOW (1) | YELLOW (2) | RED (0) | RED (0) |
| **Type 4: Neural_{Symbolic}** | GREEN (11) | YELLOW (2) | YELLOW (1) | RED (0) | YELLOW (2) | YELLOW (1) | RED (0) | YELLOW (3) | RED (0) |
| **Type 5: Neural[Symbolic]** | GREEN (7) | YELLOW (1) | RED (0) | YELLOW (1) | RED (0) | YELLOW (1) | YELLOW (1) | RED (0) | YELLOW (1) |
| **Type 6: Symbolic-Neural** | YELLOW (1) | YELLOW (1) | RED (0) | RED (0) | YELLOW (2) | YELLOW (3) | RED (0) | RED (0) | RED (0) |

---

## Cell Details

### Type 1: Symbolic[Neural] — Symbolic system with neural subroutines

| GT Concept | Count | Key Papers | Maturity | Notes |
|---|---|---|---|---|
| **Nash** | 5 | P01 (Yan NS-CSG 2024), P02 (Yan 2022), P05 (PRISM-games), P35 (Kwiatkowska MFCS 2022), P36 (SMARL logic shields 2024) | Prototype/Deployed | Kwiatkowska group dominates; PRISM-games deployed tool |
| **Stackelberg** | 1 | P27 (StEVe 2024) | Prototype | Rational verification for SSGs |
| **Correlated** | 1 | P05/P35 (PRISM-games supports CE verification) | Deployed | CE support in PRISM-games; under-explored for NeSy |
| **Evolutionary** | 0 | — | — | GAP |
| **Mechanism Design** | 0 | — | — | GAP |
| **Cooperative** | 0 | — | — | GAP |
| **Bayesian/POSG** | 2 | P03 (Yan FM24), P04 (Yan L4DC24) | Prototype | NS-POSG formalism |
| **Mean-field** | 0 | — | — | GAP: Large-population extension of NS-CSG needed |
| **Hypergame** | 0 | — | — | GAP |

### Type 2: Neural|Symbolic — Neural informed by symbolic knowledge

| GT Concept | Count | Key Papers | Maturity | Notes |
|---|---|---|---|---|
| **Nash** | 5 | P18 (Li & Zhu MANSCOL), P30 (Bayesian beliefs), P42 (Cheng signaling 2023), P47 (Jacob Consensus Game ICLR24), P50 (Johansson Dynamic Shields 2025) | Prototype | MANSCOL + emergent language + equilibrium search |
| **Stackelberg** | 4 | P06 (Gerstgrasser ICML23), P07 (Tambe 2020), P08 (Fang/PAWS 2015), P26 (neuroevol. SSG) | Prototype/Deployed | Most mature Stackelberg sub-area; PAWS deployed |
| **Correlated** | 1 | P49 (Nowak Exp3-IXrl GameSec25) | Prototype | RL + game-theoretic CCE approximation |
| **Evolutionary** | 3 | P28 (EGT+RL review 2025), P29 (EGT+DRL energy 2024) + 1 | Early | Mostly RL within EGT framework |
| **Mechanism Design** | 1 | P11 (AMD survey, dual-classified) | Survey | Covers neural mechanism design landscape |
| **Cooperative** | 1 | P43 (BAMS belief map cooperative games 2024) | Prototype | Neural MARL with symbolic belief maps |
| **Bayesian** | 3 | P19 (Li & Zhu cyber), P30 (Bayesian beliefs), P42 (signaling game) | Conceptual/Prototype | Belief-based game playing |
| **Mean-field** | 3 | P12 (Lauriere MOR24), P13 (Ruthotto PNAS20), P14 (Cao 2023) | Prototype | Active neural MFG solver community |
| **Hypergame** | 2 | P51 (Trencsenyi LLM hypergame 2025), P52 (Thomas & Saad Stackelberg hypergame 2024) | Prototype | LLMs for recursive belief modeling in hypergames |

### Type 3: Neural:Symbolic-Neural — Compilation

| GT Concept | Count | Key Papers | Maturity | Notes |
|---|---|---|---|---|
| **Nash** | 3 | P54 (Yang STLGame L4DC25), P56 (Mannucci LOGAN 2025), P57 (Gutierrez Rational Verification 2021) | Prototype | Differentiable STL + adversarial self-play; logic-constrained GANs; equilibrium checking |
| **Stackelberg** | 1 | P55 (Yang Stackelberg STL 2025) | Prototype | STL specifications compiled into Stackelberg optimization |
| **Correlated** | 0 | — | — | GAP |
| **Evolutionary** | 0 | — | — | GAP |
| **Mechanism Design** | 0 | — | — | GAP |
| **Cooperative** | 1 | P58 (CICERO, Meta FAIR Science 2022) | Deployed | LM + strategic reasoning compiled into planning pipeline for cooperative-competitive Diplomacy |
| **Bayesian/POSG** | 2 | P58 (CICERO belief inference), P59 (Liu Bayesian Inverse Games WAFR24) | Prototype/Deployed | Differentiable Nash solver in VAE; CICERO belief modeling |
| **Mean-field** | 0 | — | — | GAP |
| **Hypergame** | 0 | — | — | GAP |

### Type 4: Neural_{Symbolic} — Symbolic internal representations

| GT Concept | Count | Key Papers | Maturity | Notes |
|---|---|---|---|---|
| **Nash** | 11 | P16 (Park ICML23), P60 (Marris NES NeurIPS22), P61 (Gemp EigenGame ICLR21), P62 (Wang RENES IJCAI24), P63 (Gatti GAES ICLR24), P64 (Gao implicit layers AAAI21), P67 (Baldoni 2024), P68 (Wang arbitrating AAMAS23), P69 (Balduzzi ICML18), P70 (Letcher JMLR19), P71 (Hartford NeurIPS16) | Prototype | **Largest cluster**: Differentiable equilibrium solvers; GNN-based and equivariant architectures |
| **Stackelberg** | 2 | P65 (Ling NeurIPS21 decision diagrams), P66 (Liu Riemannian Stackelberg 2025) | Prototype | Differentiable optimization over Stackelberg structure |
| **Correlated** | 1 | P60 (Marris NES 2022 covers NE + CE + CCE) | Prototype | Neural Equilibrium Solvers address all three equilibrium concepts |
| **Evolutionary** | 0 | — | — | GAP: Differentiable evolutionary dynamics unexplored |
| **Mechanism Design** | 2 | P63 (GAES covers competitive equilibrium), P68 (Wang arbitrating as reward design) | Prototype | Neural equilibrium solvers applied to mechanism design |
| **Cooperative** | 1 | P31 (NeuroGame 2024) | Prototype | GT-structured neural architecture |
| **Bayesian** | 0 | — | — | GAP |
| **Mean-field** | 3 | P15 (spatiotemporal MFG AAMAS23), P17 (neural MFG 2025) + 1 | Prototype | Physics-informed neural MFGs |
| **Hypergame** | 0 | — | — | GAP |

### Type 5: Neural[Symbolic] — Neural calling symbolic solvers

| GT Concept | Count | Key Papers | Maturity | Notes |
|---|---|---|---|---|
| **Nash** | 7 | P21 (GT-LLM survey), P22 (LLM strategic reasoning), P23 (Nature SR 2024), P24 (Nature HB 2025), P25 (Neurocomputing 2025), P72 (G-CTR 2026), P73 (Xie Nash Q-Net GameSec25) | Prototype | LLM + GT evaluation cluster; G-CTR lifts cyber-range success 20%->43% |
| **Stackelberg** | 1 | P74 (Zhu GT+LLM cybersecurity 2025) | Conceptual | LLMs as strategic planners in leader-follower settings |
| **Correlated** | 0 | — | — | GAP |
| **Evolutionary** | 1 | P75 (Lanctot Neural Replicator Dynamics AAMAS20) | Prototype | Neural policy + replicator dynamics convergence |
| **Mechanism Design** | 0 | — | — | GAP: LLM-based mechanism design unexplored |
| **Cooperative** | 1 | P76 (Kublashvili NeSy Shapley 2025) | Prototype | NeSy pipeline with Shapley allocation |
| **Bayesian/POSG** | 1 | P77 (Lei & Zhu ADAPT MILCOM24) | Prototype | Game-theoretic NeSy penetration testing |
| **Mean-field** | 0 | — | — | GAP |
| **Hypergame** | 1 | P78 (Trencsenyi Hypergame Rationalisability 2025) | Prototype | Logic-based DSL + ASP for hypergame reasoning |

### Type 6: Symbolic-Neural — Tightly integrated

| GT Concept | Count | Key Papers | Maturity | Notes |
|---|---|---|---|---|
| **Nash** | 1 | P32 (generative AI equilibria 2024) | Prototype | Flow-based equilibrium computation |
| **Stackelberg** | 1 | P20 (differentiable bilevel 2022) | Prototype | End-to-end differentiable Stackelberg |
| **Correlated** | 0 | — | — | GAP |
| **Evolutionary** | 0 | — | — | GAP |
| **Mechanism Design** | 2 | P09 (Duetting RegretNet), P10 (CANet 2025) | Prototype | Differentiable economics cluster |
| **Cooperative** | 3 | P79 (Abbasi CQD-SHAP 2025), P80 (Mastropietro GStarX NeurIPS22), P81 (Tan counterfactual GNN AAAI24) | Prototype | Game-theoretic XAI for neural-symbolic reasoning (Shapley/Banzhaf values) |
| **Bayesian** | 0 | — | — | GAP |
| **Mean-field** | 0 | — | — | GAP |
| **Hypergame** | 0 | — | — | GAP |

---

## Summary Statistics

### Population Counts

| Metric | Value | Change from Preliminary |
|---|---|---|
| Total cells in matrix | 54 (6 types x 9 concepts) | +6 (Hypergame column added) |
| GREEN cells (>=5) | 4 (7.4%) | +3 |
| YELLOW cells (1-4) | 26 (48.1%) | +10 |
| RED cells (0) | 24 (44.4%) | -7 (from 31) |
| Total primary papers classified | 82 | +48 |

### By NeSy Type

| Type | Papers | Coverage | Assessment |
|---|---|---|---|
| Type 1: Symbolic[Neural] | 9 | 4/9 GT concepts | Narrow but deep (Kwiatkowska group); verification strength |
| Type 2: Neural\|Symbolic | 23 | 9/9 GT concepts | **Only type covering all GT concepts**; broadest coverage |
| Type 3: Compilation | 7 | 4/9 GT concepts | **No longer empty** (STLGame, LOGAN, CICERO, rational verification) |
| Type 4: Neural_{Symbolic} | 20 | 6/9 GT concepts | **Largest cluster**; differentiable equilibrium solvers dominate |
| Type 5: Neural[Symbolic] | 12 | 6/9 GT concepts | LLM+GT evaluation + emerging defense applications |
| Type 6: Symbolic-Neural | 7 | 4/9 GT concepts | Differentiable economics + game-theoretic XAI |

### By GT Concept

| Concept | Papers | NeSy Types | Assessment |
|---|---|---|---|
| Nash Equilibrium | 32 | 6/6 types | Best-covered concept; GREEN in 4 types |
| Stackelberg | 10 | 5/6 types | Deployed systems exist (PAWS); differentiable approaches emerging |
| Correlated Equilibrium | 3 | 3/6 types | **No longer empty** (NES, Exp3-IXrl, PRISM-games) |
| Evolutionary | 4 | 2/6 types | Under-served; RL+EGT and neural replicator dynamics |
| Mechanism Design | 5 | 3/6 types | Differentiable economics + neural equilibrium solvers |
| Cooperative | 7 | 5/6 types | Game-theoretic XAI (Shapley values) drives Type 6 coverage |
| Bayesian/POSG | 8 | 4/6 types | Kwiatkowska POSG + CICERO beliefs + ADAPT |
| Mean-field | 6 | 2/6 types | Physics-informed neural MFG solvers; Type 2 and Type 4 |
| Hypergame | 3 | 2/6 types | **New category**: Misperception modeling; LLM+hypergame emerging |

---

## Changes from Preliminary Matrix

### Cells Changed from RED to YELLOW (10 cells)

| Cell | Papers Found | Key Finding |
|---|---|---|
| Type 1 x Correlated | 1 | PRISM-games supports CE verification |
| Type 2 x Correlated | 1 | Exp3-IXrl blends RL with CCE approximation |
| Type 2 x Cooperative | 1 | BAMS neuro-symbolic belief maps for cooperative games |
| Type 3 x Nash | 3 | STLGame, LOGAN, Rational Verification |
| Type 3 x Stackelberg | 1 | Stackelberg STL control synthesis |
| Type 3 x Cooperative | 1 | CICERO (Diplomacy) |
| Type 3 x Bayesian | 2 | CICERO beliefs + Bayesian Inverse Games |
| Type 4 x Stackelberg | 2 | Differentiable equilibrium via decision diagrams, Riemannian flows |
| Type 4 x Correlated | 1 | Neural Equilibrium Solvers (NES) |
| Type 6 x Cooperative | 3 | Shapley/Banzhaf-based GNN explanations |

### Cells Changed from YELLOW to GREEN (3 cells)

| Cell | New Count | Key Addition |
|---|---|---|
| Type 2 x Nash | 5 (was 2) | Consensus Game, Dynamic Shields, signaling games |
| Type 4 x Nash | 11 (was 1) | Differentiable equilibrium solver cluster (NES, EigenGame, GAES, RENES, etc.) |
| Type 5 x Nash | 7 (was 5) | G-CTR, Nash Q-Network |

### New Column: Hypergame (3 papers)

| Type | Papers | Notes |
|---|---|---|
| Type 2 | 2 | LLM recursive reasoning in hypergames; Stackelberg hypergame for semantic comms |
| Type 5 | 1 | Logic-based DSL + ASP for hypergame rationalisability |

---

## Top Research Opportunities (Prioritized)

### Priority 1: High Impact, High Feasibility

| Gap | Rationale | Approach |
|---|---|---|
| **Type 3 x Mechanism Design** | Compilation approaches (STLGame, LOGAN) proven for Nash/Stackelberg; mechanism design is the natural next application | Compile auction/mechanism rules into differentiable neural architectures |
| **Type 5 x Bayesian (expand)** | LLMs are natural belief-reasoning engines; only 1 paper exists | Evaluate LLMs on Bayesian games; develop LLM+Bayesian game solver pipelines |
| **Type 4 x Bayesian** | Differentiable equilibrium solvers (NES, GAES) proven for Nash; Bayesian extension natural | Extend neural equilibrium solvers to Bayesian incomplete-information settings |
| **Correlated Eq. (expand all types)** | Only 3 papers across 3 types; CE is computationally easier than Nash | Any NeSy approach to CE computation/verification |
| **Type 5 x Mechanism Design** | LLMs unexplored for mechanism design; natural synergy with auction/contract design | LLM-based auction design, procurement mechanism optimization |

### Priority 2: High Impact, Moderate Feasibility

| Gap | Rationale | Approach |
|---|---|---|
| **Type 1 x Mean-field** | Extend NS-CSG to large populations; symbolic verification of MFG strategies | Scale Kwiatkowska framework to mean-field settings |
| **Type 4 x Evolutionary** | Differentiable game mechanics (Balduzzi, Letcher) applicable to evolutionary dynamics | Differentiable replicator dynamics; neural evolutionary game solvers |
| **Type 6 x Bayesian** | End-to-end differentiable Bayesian game solving | Differentiable belief updating + equilibrium computation |
| **Hypergame (expand all types)** | Only 3 papers; misperception modeling critical for defense | Extend hypergame formalisms to all NeSy types |

### Priority 3: Defense-Specific Opportunities

| Gap | Rationale | Approach |
|---|---|---|
| **NeSy + GT + Wargaming (Triple intersection)** | Only 5-6 papers at true triple intersection; Zhu group dominates | Develop NS-CSG or MANSCOL-style frameworks for wargaming |
| **Type 3 x Defense** | Compiling doctrine/rules-of-engagement into neural wargame agents | STLGame-style approach with military temporal logic specifications |
| **Type 1 x Cooperative (defense)** | Alliance burden-sharing, coalition operations need formal frameworks | Symbolic verification of cooperative game strategies for coalitions |
| **Type 5 x Defense wargaming** | LLMs used for wargaming but lack GT foundations | Add formal game-theoretic structure to LLM wargaming (extend G-CTR approach) |
| **Hypergame x Defense** | Hypergames model fog-of-war and deception natively | NeSy agents in military hypergame scenarios |

---

## Key Research Groups

| Group | Affiliation | Focus | NeSy Types | GT Concepts |
|---|---|---|---|---|
| Kwiatkowska, Norman, Parker, Yan, Santos | Oxford / Glasgow | NS-CSG, formal verification | Type 1 | Nash, Bayesian/POSG, Correlated |
| Tambe, Fang, Perrault | Harvard/Google | Security games | Type 2 | Stackelberg |
| Brown, Sandholm | CMU/Meta | Game solving | Secondary (neural-only) | Nash (imperfect info) |
| Li, Zhu, Al Bari, Lei | NYU | MANSCOL, Gestalt NE, cyber deception, ADAPT | Type 2/5 | Stackelberg, Bayesian, Hypergame |
| Duetting, Parkes | Harvard | Differentiable economics | Type 6 | Mechanism Design |
| Lauriere et al. | Various | Neural MFG solvers | Type 2/4 | Mean-field |
| Marris, Lanctot, Gemp, Tuyls | DeepMind | Neural equilibrium solvers | Type 4 | Nash, Correlated, Evolutionary |
| Balduzzi, Letcher, Foerster | Various | Differentiable game mechanics | Type 4 | Nash |
| Yang et al. | Various | STL games | Type 3 | Nash, Stackelberg |
| Gutierrez, Wooldridge | Oxford | Rational verification | Type 3 | Nash |
| Trencsenyi, Stathis | Royal Holloway | Hypergame theory + AI | Type 2/5 | Hypergame |
| Rawat, Hagos, Jalaian, Bastian | Howard/ARL | NeSy for military | Type 1/5 | Defense survey |

---

## Notes on Phase 2 Completion

This matrix integrates results from:
1. Preliminary web-search pass (34 papers, February 16 2026)
2. Formal database search agents S1-S6 (47 + 39 + 28 new papers)
3. Citation tracking (15 new primary papers)
4. Grey literature search (34 institutional sources)

Refinements expected during full-text screening (Phase 4):
1. **Paper counts may shift** as dual-classified papers are resolved to primary NeSy type
2. **Type 3 papers need careful scrutiny** — several are borderline between Type 3 (compilation) and other types
3. **Hypergame column needs protocol amendment** — original protocol lists 8 GT concepts; formal search warrants adding Hypergame as 9th
4. **Defense relevance will deepen** with full-text review of grey literature and institutional reports
5. **The 24 RED cells represent confirmed research opportunities** — most expected to remain empty after screening
