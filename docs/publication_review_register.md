# Publication Review Register

*Last reviewed: 2026-02-23*
*Source folder: `02 My Outreach/00 Master Copies/`*

This register tracks which publications have been reviewed by the AI assistant and summarizes each. When new files are added to the source folder, compare against this list to identify unreviewed items.

---

## Reviewed Files (28 files, 18 distinct works)

### Legend
- **Type**: J = Journal, C = Conference, R = Report, P = Presentation/Slides, T = Tutorial, D = Dissertation
- **Duplicates**: Where multiple files represent versions of the same work, the canonical version is noted

---

## 1. Dissertation

| # | File | Type | Title | Authors | Venue/Year |
|---|---|---|---|---|---|
| 1 | `Wach_PF_D_2023.pdf` | D | Study of Equivalence in Systems Engineering within the Frame of Verification | Paul F. Wach | Virginia Tech, PhD Dissertation, Dec 2022 |

**Summary**: Foundational work for the entire research program. Establishes the Wymorian Systems Engineering (WySE) Metamodel for verification artifacts, defining how verification models should be related to system designs and requirements via systems-theoretic morphisms (homomorphism, isomorphism, identity isomorphism, parameter morphism). Demonstrated through a flashlight system exemplar with 708 proof tables. Key finding: every verification model exhibited some morphic equivalence to every system design (even counter-intuitive pairings like "pizza" for a flashlight), attributed to commonality in mathematical structure for discrete systems. Defines verification requirements as problem spaces of functions combined with verification model morphic conditions (VMMCs). Committee: Salado (chair), Beling, Kannan, Patterson, Zeigler.

**Research threads**: Morphisms, verification, WySE metamodel, T3SD, DEVS, mathematical foundations of SE.

---

## 2. Journal Articles

| # | File(s) | Type | Title | Authors | Venue/Year |
|---|---|---|---|---|---|
| 2 | `genAI_SE_expert_v2.1.pdf` (preprint), `Systems Engineering - 2025 - Topcu - Trust at Your Own Peril...pdf` (published) | J | Trust at Your Own Peril: A Mixed Methods Exploration of the Ability of Large Language Models to Generate Expert-Like Systems Engineering Artifacts and a Characterization of Failure Modes | Topcu, Husain, Ofsa, Wach | *Systems Engineering* (Wiley), 2025. DOI: 10.1002/sys.21810 |

**Summary**: Mixed-methods study testing GPT-4, GPT-3.5 Turbo, and Claude on generating SE artifacts (Capability Description Documents) for a Bulldog UGV dataset. MAUVE scores show LLMs can produce text statistically similar to human experts when prompted carefully. Qualitative analysis reveals three failure modes: premature requirements definition, unsubstantiated numerical estimates, and propensity to overspecify. These failure modes resemble novice SE behavior. Won **Best Paper Award at CSER 2024** (earlier conference version). Funded by U.S. Navy NEEC.

**Research threads**: AI4SE, LLM evaluation, SE artifact generation, prompt engineering, failure modes.

---

## 3. Conference Papers

| # | File(s) | Type | Title | Authors | Venue/Year |
|---|---|---|---|---|---|
| 3 | `CSER2025_Anderson_Wach_LLMBridge.pdf` (original), `CSER2025_Anderson_Wach_LLMBridge_rev1.pdf` (revision) | C | LLM-Enabled Knowledge Transfer: Modeler to SME | Anderson, Topcu, Jugan, Nerayo, Wach | CSER 2025, Long Beach, CA |
| 4 | `CSER2025_Nerayo_Wach_ToolEval_v2.pdf` | C | Fit-For-Transformation: Initial Tool Evaluation and Method for Model-Based Systems Engineering Tools | Nerayo, Wach | CSER 2025, Long Beach, CA |
| 5 | `CSER2025_Wach_etal_STcoP.pdf` (original), `CSER2025_Wach_etal_SysThCoP_rev1.pdf` (revision) | C | Systems Theoretic Co-Pilot MVP | Wach, Iyer, Shanmugam, Curran, Ashok | CSER 2025, Long Beach, CA |
| 6 | `CSER2026_WachSandmanIyer.pdf` | C | Foundations for Systems Engineering: Exploring System Morphisms | Wach, Sandmann, Iyer | CSER 2026, Arlington, VA |
| 7 | `IS2026_paper_490.pdf` | C | DEVS-Based Agentic AI Swarm Orchestration: System Entity Structure of Queens for Rapid Systems Development and Verification | [Blinded] | INCOSE IS 2026 |
| 8 | `Sandman_Wach_IS_2026_draft.pdf` | C | Structural Foundations in Systems Engineering: System Morphism Analysis | [Blinded] (Sandmann, Wach et al.) | INCOSE IS 2026 (draft) |
| 9 | `VerModConditions-V3.pdf` | C | Theoretical Underpinnings to Establish Fidelity Conditions for Defining Verification Models | Wach, Salado | INCOSE IS 2024, Dublin |
| 10 | `LLM_SE_Trades_v1.pdf` | C | The Cost of Expertise: Performance Trade-Offs in LLMs for Systems Engineering | Wach, Bell, Jugan, Longshore, Madachy | INCOSE IS 2025, Ottawa |
| 11 | `Wach_LLM-SE_CESUN_2025_v1.pdf` | C | Cautions of Leveraging LLMs for Systems Engineering: Generalist versus Specialist | Wach, Nerayo, Jugan, Anderson, Beling, Topcu | CESUN 2025 |
| 12 | `Math-Based_Data_ME-V2.pdf` | C | Math-Based Data Structures and Analysis for Mission Engineering | [Blinded, 6 authors] | INCOSE 2025 |
| 13 | `The Tale of the Broken Clock_v2.pdf` | C | The Tale of the Broken Clock: How LLMs Evaluate Requirement Quality and Where They Fail | [Blinded] | INCOSE 2025 |
| 14 | `Vision_4_RE_2035-V1.pdf` | C | Vision 2035: Exploring the Future of Requirements Specification | [Blinded, 6 authors] | INCOSE 2025 |

### Paper 3 — LLM-Enabled Knowledge Transfer
**Summary**: Tests five GPT-4o configurations (control + 4 fine-tuned variants) on converting SysMLv2 to textual descriptions. Fine-tuned "Translator" models (trained on JSON) outperform the control, achieving 91.37% BERTScore accuracy. MAUVE found unsuitable (no discriminative power). Demonstrates bidirectional bridge concept between modelers and SMEs. Rev1 adds explicit scope disclaimer and consolidates figures.

### Paper 4 — Fit-For-Transformation Tool Evaluation
**Summary**: Introduces a structured MBSE tool evaluation method organized around the 5 DoD Digital Engineering Strategy Goals. Defines Basic/Advanced/Enterprise capability levels, three standardized weighting profiles, and 1-5 scoring criteria sourced from MOSA, SEBoK, ISO/IEC 25010, DoDI 5000.97, and SERC. Demonstrated on Cameo Systems Modeler (score: 4.78/5). Also used as Virginia Tech Digital Engineering course instructional material.

### Paper 5 — Systems Theoretic Co-Pilot MVP
**Summary**: Presents the MVP architecture for a "systems theoretic co-pilot" grounded in Wymore's mathematical theory. Four components: UI (Tkinter), Systems Theoretic Algorithms (NetworkX), AI/ML (OpenAI API), Data Storage (Pandas/PostgreSQL). Introduces "degrees of homomorphism" — quantifying partial equivalence (e.g., 0.75 for a 2-state vs. 3-state flashlight). Rev1 adds a formal mathematical precepts section, expanded discussion of applications (recommender systems, morphic chains), and scaling challenges.

### Paper 6 — Foundations for SE: Exploring System Morphisms (MSD/RLC)
**Summary**: Defines six system models (three electrical, three mechanical) at physics-equation and set-theoretic levels. Shows that at 2-state abstraction, MSD-to-Series-RLC is a true isomorphism; at 4-state mechanical vs. 2-state electrical, it degrades to homomorphism (damping regime information is lost). Establishes that morphism type depends on abstraction level. MATLAB simulation confirms identical response curves.

### Paper 7 — DEVS-Based Agentic AI Swarm Orchestration
**Summary**: Formalizes AI agent swarms as DEVS coupled models with an SES-based "Queen Hierarchy" architecture. Three theoretical results: (1) Emergent Behavior Prediction Theorem (SES structure bounds emergent behaviors), (2) V&V Complexity Reduction Theorem (hierarchical verification reduces from O(|S|^n) to O(n*k), >10^10x improvement), (3) Safety Case Generation Theorem (DEVS traces map to GSN/ISO 26262). Implemented in C++20 with Anthropic API; demonstrated on a wargaming scenario with 292 entities.

### Paper 8 — Structural Foundations: Capacitor/Hydraulic Morphism
**Summary**: Companion to Paper 6, extending morphism analysis to electrical capacitor vs. micro-scale hydraulic bubble systems. Proves isomorphism at 2-state set-theoretic level. Establishes variable mapping: Capacitance (C) <-> Hydraulic Compliance (C_H), Voltage (V) <-> Pressure (p), Current (I) <-> Flow Rate change.

### Paper 9 — Verification Model Fidelity Conditions (INCOSE IS 2024)
**Summary**: Compares three approaches to defining verification models: text-based practice, MBSE/SysML, and Wymorian mathematical underpinning. Shows text-based and MBSE approaches yield implicit/qualitative relationships; the mathematical approach yields explicit/quantitative relationships in all three categories (VM-to-SR, VM-to-VR, VM-to-SD). SysML notably has *no* relationship between verification model and system design. Introduces the WySE metamodel in a concise conference format.

### Paper 10 — Cost of Expertise: LLM Performance Trade-Offs
**Summary**: Counter-intuitive finding: unmodified ChatGPT-4o (96%) outperforms fine-tuned (95%) and fine-tuned+RAG (94%) variants on the SysEngBench benchmark (1,144 SE MCQs). SysMLv2 specialization degrades general SE knowledge. Raises the provocative question of whether this reflects LLM limitations or a disconnect between SysMLv2 and broader SE knowledge.

### Paper 11 — Cautions of LLMs for SE: Generalist vs. Specialist
**Summary**: Synthesis/position paper combining results from three empirical studies (MAUVE artifact similarity, BERTScore SysML translation, SysEngBench benchmarking). Central thesis: as we specialize LLMs on SE, we lose the generalizability that SE's transdisciplinary nature demands. Raises questions about SE's maturity as a discipline.

### Paper 12 — Math-Based Data Structures for Mission Engineering
**Summary**: Positions DEVS as a foundational data structure (not just simulation formalism) for mission engineering. Develops a DEVS ontology (Protege) deployed to graph databases (Neo4j, ArcadeDB). Demonstrates parameter morphisms linking physics-based satellite models to DEVS-Markov mission models. Space systems exemplar: 8-satellite constellation with solar flare disruption. Achieves DE strategy goals of interoperability and reuse.

### Paper 13 — The Broken Clock: LLMs for Requirement Quality
**Summary**: First quantitative benchmarking of off-the-shelf ChatGPT-4o for requirements quality evaluation. Asymmetric performance: good at avoiding false alarms (TNR=0.83) but misses ~65% of actual quality issues (TPR=0.35). Performs best on linguistic issues (ambiguity, verifiability) and worst on SE-judgment issues (conciseness, necessity, correctness). 100 runs show high variability. Conclusion: not suitable for autonomous use; best as assistive tool with human-in-the-loop.

### Paper 14 — Vision 2035: Future of Requirements Specification
**Summary**: Strategic roadmap for requirements specification evolution. Near-term (2025-2028): NLP-based quality automation, data governance, AI sandboxes. Mid-term (2028-2032): model-linked specifications, knowledge graphs, AI-assisted change impact analysis. Long-term (2032-2035): executable requirements, closed-loop requirement-to-test-to-evidence workflows, multi-agent context-aware AI. Derived from stakeholder interviews and literature synthesis.

---

## 4. Technical Reports

| # | File | Type | Title | Authors | Venue/Year |
|---|---|---|---|---|---|
| 15 | `SERC_A013_WRT-2406_Final Technical Report_20250924.pdf` | R | WRT-2406: Optimized Portfolio Digital Engineering (Base Year) | Wach (PI), Topcu, Esser, Hutchison, Beling, Jurczyk, Florez, Sandman | SERC, Sep 2025 |

**Summary**: Comprehensive DE transformation assessment for a DoD sponsor. Identifies 49 sociotechnical barriers across 6 dimensions. Tradespace analysis of 29 DE capabilities across organizational feasibility, TRL, and governance risk. Phased roadmap: Year 1 (high-TRL DE tech), Year 2 (requirements/architecture draft generators), Year 3+ (organizational knowledge infusion, Gen-AI for concepts). 10-year requirements specification roadmap through 2035. Introduces GenGroves agentic AI framework. Key recommendation: invest in agentic AI. Only ~2% of DoD ETM personnel hold DE or AI credentials.

---

## 5. Presentations and Tutorials

| # | File | Type | Title | Authors | Venue/Year |
|---|---|---|---|---|---|
| 16a | `Track+2+AI4SE_06.+Paul+Wach+++Mohammed+Husain (2).pdf` | P | Large Language Model Enabled Generation of Systems Engineering Artifacts | Wach, Husain, Topcu | AI4SE Workshop, 2023 |
| 16b | `Jugan_Wach_SERC_AIws_2024-09-18.pdf` | P | Using Large Language Models to Accelerate Development of Complex Systems | Wach, Jugan, Lucero | SERC AI Workshop, Sep 2024 |
| 16c | `Wach_NDIA_2024-10-31.pdf` | P | Using Large Language Models to Accelerate Development of Complex Systems | Wach, Jugan, Lucero | NDIA, Oct 2024 |
| 16d | `WRT-2406 Outbrief 2025-10_FINAL.pdf` | P | WRT-2406: Optimized Portfolio Digital Engineering Transformation — Final Outbrief | Wach, Topcu, Hutchison, Sandman | SERC Outbrief, Oct 2025 |
| 17a | `Wach_GenGroves_2025-09-17.pdf` | P | GenGroves: A Bridge Between Systems Engineers and Domain Experts | Wach, Nerayo, Beling, Jugan, Anderson, Anand | SERC AI4SE Workshop, Sep 2025 |
| 17b | `Wach_GenGroves_Abstract_AIworkshop_2025.pdf` | P | GenGroves: A Bridge Between Systems Engineers and Domain Experts (Abstract) | Wach, Nerayo, Beling, Jugan, Anderson, Anand | SERC AI4SE Workshop, 2025 |
| 17c | `Wach_STA_2025-09-16.pdf` | P | Advancing SE through a Mathematically-Rigorous Co-Pilot: From GPS Systems to Satellite Constellation Revectoring | Wach, Iyer, Nerayo, Beling, Jugan, Anderson | SERC AI4SE Workshop, Sep 2025 |
| 17d | `Wach_STcP_Abstract_AIworkshop_2025.pdf` | P | Advancing SE through a Mathematically-Rigorous Co-Pilot (Abstract) | Wach, Iyer, Nerayo, Beling, Jugan, Anderson | SERC AI4SE Workshop, 2025 |
| 18 | `Wach_SE-AI_Riddle_IW_2026-02-01.pdf` | P | Speak Friend and Enter: Is the Future of SE and AI a Riddle? | Wach | Invited Workshop, Feb 2026 |
| 19 | `dTE_mini-tutorial_2025-04-23_v2.pdf` | T | Digital Engineering and Test & Evaluation: How DE Impacts T&E — Mini-Tutorial | Salado, Gregory, Wach, Kerr, Sandman, Sherburne | AIRC Mini-Tutorial, Apr 2025 |

### 16a — AI4SE Workshop 2023 (Foundational LLM Study)
**Summary**: Earliest work in the LLM-for-SE program. Developed 6-step test framework for evaluating LLM-generated SE artifacts. Two datasets: Bulldog (synthetic UGV) and Silverfish (perimeter security). Prompt specificity is the dominant factor — Claude went from MAUVE 0.0000 (generic) to 0.9932 (most specific). Establishes the plausibility of LLMs for SE artifact generation.

### 16b/16c — SERC and NDIA Presentations (2024)
**Summary**: Presentations of the three-thrust research program (text-to-text, text/image-to-SysMLv2, SysML-to-text) to SERC and defense industry audiences. GPT-4o optimized outperforms fine-tuned and control. SysML Generator tool demonstrated. NDIA version adds future directions: STEDE scaling, LLM vs. SLM comparison, teams of agents.

### 16d — WRT-2406 Outbrief
**Summary**: Executive briefing version of the SERC technical report. BLUF: invest in agentic AI. Summarizes tradespace analysis, phased roadmap, and 2025-2035 requirements specification evolution across methods, infrastructure, and workforce.

### 17a/17b — GenGroves
**Summary**: Agentic AI framework using four LLMs (orchestrator + text-to-SysMLv2 + image-to-SysMLv2 + SysML-to-text) to bridge SE modelers and domain SMEs. Built on LangGraph + MCP. Deployed on STEDE Kubernetes GPU cluster. Benchmarked open-source models (Gemma best overall). V&V feedback loops for generated SysMLv2.

### 17c/17d — Systems Theoretic Co-Pilot (STA)
**Summary**: Operationalizes Wymorian theory into a software co-pilot for mathematically rigorous verification. Key innovation: "degrees of homomorphism" as a quantitative metric. Three phases: GPS (simple), defense systems (complex), satellite constellations (SDA scale). Growing library of known homomorphisms. Integration with DEVS/RTSync (~90% dev time reduction). Hybrid agentic architecture (LangGraph + Strands + MCP). Neo4j for scalable graph analytics.

### 18 — SE-AI Riddle (IW 2026)
**Summary**: Invited talk using the Tolkien "Door of Durin" metaphor. Core message: the SE community is overthinking AI integration — the answer is binding AI to clear intent, constraints, and evidence ("make AI a friend"). Presents four co-pilot tools: Houston (requirements), GenGroves (SysMLv2), ACQbar (acquisition), PLMr (PLM). Maturity spectrum: document-based -> model-based -> data-centric. NATO panel on neuro-symbolic AI for wargaming.

### 19 — dTE Mini-Tutorial (AIRC 2025)
**Summary**: Comprehensive tutorial on transforming T&E through digital engineering. Three-phase vision: document-based TEMPs -> model-based dashboards -> full mission-fidelity digital T&E with AI/ML. Operation Safe Passage (OSP) testbed using Lego robots as UGV proxies. MB TEMP built on UA Ontology Stack (OWL/SWRL/SPARQL) with VIOLET platform. IDSK five-pillar framework. Sponsored by DOT&E. Partners: JHU-APL, GTRI. Future vision: holistic mathematically-underpinned data and models with known fidelity from inception to retirement.

---

## Research Thread Map

| Thread | Publications |
|---|---|
| **Morphisms & Mathematical Foundations of SE** | 1 (dissertation), 5, 6, 8, 9, 12, 17c/d |
| **LLM Evaluation for SE** | 2, 3, 10, 11, 13, 16a |
| **Agentic AI for SE** | 7, 15, 16d, 17a/b, 18 |
| **MBSE Tools & Digital Transformation** | 4, 14, 15, 16b/c, 19 |
| **Verification & T&E** | 1, 9, 19 |
| **DEVS for SE** | 7, 12 |
| **GenGroves (SysMLv2 Bridge)** | 3, 17a/b |
| **Systems Theoretic Co-Pilot** | 5, 17c/d |

---

## Version/Duplicate Map

| Canonical Work | Files |
|---|---|
| Trust at Your Own Peril (journal) | `genAI_SE_expert_v2.1.pdf`, `Systems Engineering - 2025 - Topcu...pdf` |
| LLM-Enabled Knowledge Transfer | `CSER2025_Anderson_Wach_LLMBridge.pdf`, `CSER2025_Anderson_Wach_LLMBridge_rev1.pdf` |
| Systems Theoretic Co-Pilot MVP | `CSER2025_Wach_etal_STcoP.pdf`, `CSER2025_Wach_etal_SysThCoP_rev1.pdf` |
| LLMs to Accelerate Complex Systems | `Jugan_Wach_SERC_AIws_2024-09-18.pdf`, `Wach_NDIA_2024-10-31.pdf` |
| GenGroves | `Wach_GenGroves_2025-09-17.pdf`, `Wach_GenGroves_Abstract_AIworkshop_2025.pdf` |
| STA Co-Pilot | `Wach_STA_2025-09-16.pdf`, `Wach_STcP_Abstract_AIworkshop_2025.pdf` |
