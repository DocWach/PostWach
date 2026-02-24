# From Rules to Agentic Swarms: The History and Current State of AI for Systems Engineering

**Paul F. Wach, PhD**
University of Arizona

**February 2026**

---

## Abstract

Artificial intelligence (AI) for systems engineering (SE) has evolved through six paradigms in five decades, from expert systems encoding static rules, through machine learning and deep learning, to large language models (LLMs), agentic AI, and now agentic swarms of coordinating specialist agents. Each paradigm expanded what AI could contribute to engineering practice, but a troubling pattern accompanies this progress: the eras are compressing. Expert systems and machine learning each lasted roughly twenty years; agentic swarms emerged within one year of single-agent AI reaching maturity. Meanwhile, defense and national security organizations, once the primary funders of AI research, now consistently trail commercial adoption by years. When adoption lag exceeds era duration, organizations risk investing in yesterday's paradigm.

This paper traces the full arc from rules to swarms through the lens of three systems the author built across the timeline: Houston (an expert system applying True Model-Based Requirements, or TMBR, to requirements definition), GenGroves (named for General Leslie Groves; an LLM/agentic co-pilot bridging SE modelers and domain experts), and MACQ (Modernized Acquisition; an agentic swarm co-pilot for defense and civil acquisition). The progression illustrates a concrete reality: each AI paradigm shift expanded the frontier of AI-assisted SE, but none eliminated the need for human engineering judgment. The paper concludes that the SE community must compress its own adoption cycles or accept permanent strategic lag, and that the window to shape the next era is measured in years, not decades.

---

## 1. Introduction

Systems engineering (SE) organizations face a widening capacity crisis. The systems they must develop, including satellites, aircraft, medical devices, and power grids, integrate more functionality, span more disciplines, and involve more stakeholders than ever before. Requirements number in the thousands, interfaces proliferate, and regulatory constraints grow more demanding. Yet engineering capacity has not grown proportionally. Talent remains scarce, budgets are constrained, and schedules compress [1, 2]. The result is an expanding gap between what must be engineered and the human capacity to engineer it.

Artificial intelligence (AI) offers a path to close this gap. Over the past five decades, AI has evolved through six distinct paradigms, each expanding what computational systems can contribute to engineering practice. This paper traces that evolution through the lens of SE application, from the earliest expert systems encoding human rules to the agentic AI swarms now emerging as collaborative engineering partners.

Two cross-cutting themes run through this history and carry urgent implications for practice:

**Accelerating cycles.** Each AI era is shorter than the last. Expert systems and machine learning each spanned roughly twenty years. Deep learning compressed to eight. Large language models (LLMs) dominated for roughly five years before agentic AI emerged. Agentic swarms are already arriving within a year of single-agent systems reaching maturity. Organizations that took five years to adopt the last wave may not have five years before the next one arrives.

**Defense adoption lag.** National security organizations have consistently adopted AI paradigms years after they emerge commercially. The Department of Defense (DoD) funded much of the original AI research in the 1960s through 1980s and adopted expert systems with relatively little lag. But as AI innovation shifted to the commercial sector, a gap opened. The transformer architecture emerged in 2017 [3]; defense organizations did not begin serious LLM adoption until after ChatGPT's release in late 2022, a five-year lag. As cycles compress, this lag becomes a strategic risk: organizations may find themselves investing heavily in one paradigm just as the next one arrives.

This paper grounds each era in concrete SE practice through three systems the author has developed across the AI timeline: **Houston**, an expert system leveraging hard-coded rules and True Model-Based Requirements (TMBR) for requirements definition; **GenGroves** (named for General Leslie Groves), an LLM/agentic AI co-pilot bridging SE modelers and domain subject matter experts (SMEs); and **MACQ (Modernized Acquisition)**, an agentic swarm co-pilot for defense, National Nuclear Security Administration (NNSA), National Aeronautics and Space Administration (NASA), and generic acquisition processes. Together, these systems illustrate what each AI paradigm made possible, and where each reached its ceiling.

Figure 1 provides a companion timeline of the six AI eras discussed in this paper.

\begin{figure}[h]
\centering
\makebox[\textwidth][c]{\includegraphics[width=1.3\textwidth]{AI_history_overview_v4.png}}
\caption{Six eras of AI evolution, from expert systems to agentic swarms.}
\end{figure}

---

## 2. Expert Systems (1970s–1980s)

**Era span: ~20 years** | Defense adoption lag: minimal, as DoD funded much of the original research

The first generation of AI systems applied to engineering problems encoded human expert knowledge as explicit "if-then" rules. These expert systems represented domain expertise in symbolic form, enabling consistent application of established practices without requiring the human expert's physical presence. Landmark systems included MYCIN for medical diagnosis [4] and XCON (R1) for computer configuration at Digital Equipment Corporation [5], among numerous other systems for spacecraft fault diagnosis and mission planning.

Expert systems offered clear strengths: they codified expertise into deterministic, auditable decision procedures. When the problem fell within the encoded rule base, performance was reliable and explainable. For SE, this was a natural fit, as many SE activities involve systematic application of standards, checklists, and established heuristics.

However, expert systems proved brittle. They performed well within their encoded knowledge but failed unpredictably when encountering situations outside their rule base. The knowledge acquisition bottleneck, meaning the expensive and time-consuming process of eliciting and encoding expert knowledge, limited scalability [6]. They could not learn from experience or adapt without manual rule updates.

**Case Study: Houston.** The author's Houston system applied the expert systems paradigm to requirements definition, leveraging hard-coded rules and True Model-Based Requirements (TMBR) to assist SE practitioners in producing consistent, standards-compliant requirements artifacts [7, 8, 9]. Houston demonstrated the value proposition of rule-based AI for SE: encoding TMBR patterns enabled repeatable, template-driven requirements generation that reduced manual effort and enforced consistency. These well-documented strengths of the expert systems paradigm, deterministic behavior, auditability, and domain-specific codification, translated directly to requirements engineering practice. Equally, the well-documented limitations of expert systems applied: the requirements engineering domain demands contextual judgment, stakeholder negotiation, and cross-domain reasoning that static rules cannot capture. As an expert system, Houston inherited these constraints. Every novel project context demanded new rules, and the system could not generalize beyond what was explicitly encoded.

Houston proved the value proposition of AI-assisted SE while also demonstrating why the expert systems paradigm alone, with its inherent brittleness and inability to learn, was insufficient to address the broader capacity crisis.

---

## 3. Machine Learning (1990s–2010s)

**Era span: ~20 years** | Defense adoption: gradual, primarily in intelligence and signals analysis

The second era shifted from hand-coded rules to learning patterns from data. Machine learning (ML) algorithms, including support vector machines, random forests, decision trees, and early neural networks, could generalize from training examples to new inputs, fundamentally reducing dependence on manual knowledge engineering [10].

For SE, machine learning enabled cost estimation from historical project data, defect prediction in software-intensive systems, and risk assessment based on project characteristics. The approach proved particularly valuable where explicit rules were difficult to articulate but historical data was available.

However, machine learning required careful feature engineering; human experts still needed to identify and select relevant input variables. Models were typically narrow, trained for a single task, and struggled to transfer knowledge across domains. The "black box" nature of many algorithms limited adoption in safety-critical SE contexts where traceability and justification are essential. Most critically, the SE domain suffered from a chronic shortage of labeled training data, constraining what could be learned.

---

## 4. Deep Learning (2012–2020)

**Era span: ~8 years**, cycle compression begins | Defense adoption: DoD invested (Project Maven, JAIC) but SE-specific adoption remained minimal

Deep learning extended machine learning through multi-layer neural networks capable of automatically learning hierarchical feature representations from raw data [11]. The 2012 AlexNet breakthrough in image classification demonstrated that deep networks could match or exceed human performance on perception tasks, triggering rapid adoption across computer vision, speech recognition, and game-playing (AlphaGo) [12].

Architecturally, deep learning introduced convolutional neural networks (CNNs) for spatial data, recurrent neural networks (RNNs) for sequential data, and eventually attention mechanisms that would seed the next revolution. The key advance was automatic feature learning: rather than requiring human engineers to specify what to look for, networks learned relevant representations directly from data.

For SE, deep learning supported natural language processing of requirements documents, image-based inspection in manufacturing and test, and anomaly detection in operational systems. Yet deep learning models remained fundamentally single-task (one trained model per problem) and required large labeled datasets that were rarely available in SE practice. The models could classify and predict, but they could not reason, plan, or generate coherent engineering artifacts.

---

## 5. Large Language Models (2018–2023)

**Era span: ~5 years** | The transformer architecture emerged in 2017 [3], but defense and SE adoption did not begin until post-ChatGPT (late 2022/2023), a five-year lag

The transformer architecture [3] and the scaling laws it enabled produced LLMs trained on internet-scale text corpora. Beginning with BERT (2018) and accelerating through the GPT series and Claude, LLMs demonstrated emergent capabilities qualitatively beyond their predecessors: zero-shot and few-shot learning, general-purpose reasoning, code generation, and multi-step problem decomposition [13, 14].

For SE, LLMs introduced the possibility of generating, not merely classifying, engineering artifacts. Requirements documents, design descriptions, trade study analyses, and code could be drafted from natural language instructions. A single model could address many SE tasks without task-specific training, dramatically lowering the barrier to AI-assisted engineering.

Empirical research validated this promise while revealing important caveats. Topcu, Husain, Ofsa, and Wach [15] demonstrated that LLMs can produce SE artifacts (Capability Description Documents) with text statistically similar to human expert output when prompted carefully, a finding that won Best Paper at CSER 2024. However, qualitative analysis uncovered three characteristic failure modes: premature requirements definition, unsubstantiated numerical estimates, and propensity to overspecify. These patterns resemble novice SE behavior rather than expert practice.

This work laid the foundation for **GenGroves** (described in Section 6) by establishing that LLMs could serve as a viable generation engine for SE artifacts, provided that appropriate validation, specialization, and human oversight mechanisms were in place.

Further research by Wach et al. [16] revealed a counter-intuitive finding with significant implications: unmodified ChatGPT-4o outperformed fine-tuned and fine-tuned+RAG variants on the SysEngBench benchmark of 1,144 SE multiple-choice questions. Specializing LLMs on SysMLv2 *degraded* general SE knowledge. This specialist-versus-generalist trade-off, that as we specialize AI on one SE subdomain we may lose the broad transdisciplinary understanding that SE demands, remains a central challenge in the field [17].

---

## 6. Agentic AI (2023–2024)

**Era span: ~1–2 years**, cycle compression accelerating rapidly | Defense adoption: beginning now, but most organizations are still in the LLM adoption phase

Agentic AI addressed the fundamental limitations of stand-alone LLMs by augmenting language models with tools, persistent memory, and goal-directed control loops [18]. Where LLMs were reactive, responding to prompts and then forgetting, agentic systems could plan, act, observe results, and self-correct across multi-step workflows. The ReAct framework [19] demonstrated that interleaving reasoning traces with tool execution substantially improved task completion on complex problems.

For SE, agentic AI opened the door to automated trade study execution, design space exploration, and continuous verification workflows. An agent could be tasked with evaluating architectural alternatives, gathering relevant data, performing analyses, and synthesizing recommendations, all without step-by-step human guidance.

**Case Study: GenGroves.** GenGroves (named for General Leslie Groves) is an agentic AI co-pilot designed to bridge the communication gap between SE modelers and domain SMEs [20, 21, 22]. The system architecture comprises four specialized language models: an orchestrator that manages workflow, a text-to-SysMLv2 generator, an image-to-SysMLv2 generator, and a SysMLv2-to-text translator. These models coordinate through LangGraph and Model Context Protocol (MCP) pipelines, with verification and validation (V&V) feedback loops ensuring generated SysMLv2 artifacts are validated before delivery.

Anderson et al. [20] demonstrated that fine-tuned "Translator" models achieved 91.37% BERTScore accuracy in converting SysMLv2 to natural language descriptions, establishing a bidirectional bridge: modelers can generate formal models from informal descriptions, and SMEs can read and validate formal models in natural language. The bridge concept spans the full spectrum of stakeholders, from executives requiring high-level summaries to electrical engineers needing component-level specifications.

GenGroves represents the transition from LLMs as text generators to agentic systems that coordinate multiple specialized models in pursuit of an engineering goal. It also illustrates a key architectural lesson: rather than building one monolithic SE agent, decomposing the problem into specialized models with clearly defined interfaces produces more reliable results.

---

## 7. Agentic Swarms (2024–Present)

**Era span: ~1 year and emerging**, the lag problem intensifies as organizations still adopting LLMs while swarms are already here

The current frontier extends agentic AI from single-agent systems to coordinated multi-agent swarms, meaning teams of specialized agents working collectively on problems too complex for any individual agent. Where GenGroves coordinates four models within a single pipeline, agentic swarms deploy multiple autonomous agents with specialized roles, shared memory, consensus protocols, and collective intelligence [23, 24].

Key characteristics distinguish swarms from single-agent systems:

- **Agent specialization**: individual agents optimized for specific roles (requirements analysis, architecture, domain expertise, verification)
- **Parallel execution**: multiple agents working simultaneously on independent subtasks
- **Shared memory**: common knowledge repositories enabling information exchange
- **Coordination mechanisms**: protocols for managing dependencies, resolving conflicts, and achieving consensus
- **Emergent capabilities**: collective behaviors exceeding the sum of individual agent capabilities

This architecture mirrors the multi-disciplinary, collaborative nature of SE itself. SE is not a solo activity; it requires requirements engineers, systems architects, domain specialists, integration engineers, and V&V engineers working in concert. Agentic swarms can operate the same way.

**Case Study: MACQ (Modernized Acquisition).** MACQ is an agentic swarm co-pilot designed for acquisition processes across multiple organizational frameworks: the Department of War (DoW), NNSA, NASA, and generic acquisition. Multiple specialized agents coordinate across acquisition lifecycle phases, with current capabilities including milestone review support and Systems Engineering Plan (SEP) generation.

MACQ's architecture assigns distinct agents to distinct acquisition concerns, including regulatory compliance, technical assessment, schedule analysis, and stakeholder coordination, and enables them to share context through shared memory and structured communication protocols. When conducting a milestone review, for instance, agents independently assess their respective domains and then synthesize findings into a coordinated review package that identifies cross-cutting risks no single agent would catch in isolation.

The progression from Houston (single expert system, one domain) through GenGroves (coordinated specialized models, one workflow) to MACQ (autonomous specialized agents, full acquisition lifecycle) traces the expanding frontier of AI-assisted SE in concrete terms.

---

## 8. The Compression Problem

The two cross-cutting themes of this paper, accelerating cycles and defense adoption lag, converge into a strategic problem that demands attention.

\begin{table}[h]
\small
\centering
\caption{AI era durations and the compression of paradigm cycles.}
\begin{tabular}{p{4cm} l l p{5.5cm}}
\hline
\textbf{Era} & \textbf{Approx. Span} & \textbf{Duration} & \textbf{Approx. Defense Adoption Lag} \\
\hline
Expert Systems & 1970s--1980s & \textasciitilde 20 years & Minimal (DoD-funded) \\
Machine Learning & 1990s--2010s & \textasciitilde 20 years & Moderate (intel/signals) \\
Deep Learning & 2012--2020 & \textasciitilde 8 years & Moderate (Project Maven, JAIC) \\
Large Language Models & 2018--2023 & \textasciitilde 5 years & \textasciitilde 5 years (2017 $\rightarrow$ 2022/23) \\
Agentic AI & 2023--2024 & \textasciitilde 1--2 years & Beginning now \\
Agentic Swarms & 2024--present & \textasciitilde 1 year & Not yet started \\
\hline
\end{tabular}
\end{table}

The pattern is unmistakable: era durations have compressed from decades to a single year. Meanwhile, defense and national security organizations have seen their adoption lag remain roughly constant or grow. The critical inflection point occurs when the adoption lag exceeds the era duration. At that point, organizations risk investing heavily in a paradigm (e.g., standing up LLM programs) just as the next paradigm (agentic swarms) arrives, or skipping an era entirely without ever realizing its benefits.

This is not merely an academic observation. Organizations today are establishing LLM centers of excellence, developing LLM governance frameworks, and training their workforce on LLM tools. These are valuable investments. But if those programs take three to five years to mature, the AI landscape will have shifted beneath them twice over.

Across all six eras, a consistent evolutionary pattern emerges: increasing autonomy (from static rules to self-directed agents), decreasing brittleness (from rigid rule bases to adaptive learned behaviors), and growing coordination (from isolated systems to collaborative swarms). The throughline from Houston to GenGroves to MACQ illustrates that each AI paradigm shift expanded what was possible in SE practice, but none eliminated the need for human engineering judgment.

What remains constant across every era:

- **Human judgment**: value-laden trade-off decisions that reflect stakeholder priorities and engineering experience
- **Accountability**: when systems fail, humans bear responsibility; AI systems are tools, however sophisticated
- **Stakeholder relationships**: the interpersonal dimensions of engineering that resist computational mediation
- **Creative insight**: redefining the problem space itself, recognizing when the wrong question is being answered

AI augments engineering capacity. It does not replace engineering judgment.

---

## 9. Looking Forward

Several convergence points define the near-term frontier:

**Agentic swarms and digital engineering.** As organizations transition to model-based systems engineering (MBSE), digital threads, and digital twins, they are building the infrastructure on which AI swarms will operate. MBSE provides formal, machine-readable representations of system architecture. Digital threads maintain traceability across the lifecycle. Digital twins bridge development and operations. AI swarms can consume, produce, and validate engineering artifacts across this entire digital ecosystem [1, 2, 25].

**The strategic imperative.** The compression problem described in Section 8 means that organizations cannot afford multi-year adoption cycles for each new AI paradigm. Instead, they must develop the organizational agility to evaluate, pilot, and scale AI capabilities on compressed timescales, or accept permanent lag as a strategic risk. This requires investment not only in technology but in workforce AI literacy, governance frameworks, and organizational learning capacity.

**A call to action.** The SE community faces a choice. It can react to AI advancement as it unfolds, adapting after the fact to capabilities others develop for other purposes. Or it can actively shape how AI is applied to engineering practice, ensuring that the resulting systems serve engineering needs, preserve engineering values, and amplify the capacity that the discipline so urgently requires [2].

The time between paradigm shifts is no longer measured in decades. The window to shape the next era is open now.

---

## References

[1] INCOSE, *Systems Engineering Handbook*, 5th ed., Wiley, 2023.

[2] INCOSE, *Systems Engineering Vision 2035*, 2022.

[3] A. Vaswani et al., "Attention is all you need," *Advances in Neural Information Processing Systems*, vol. 30, 2017.

[4] E. H. Shortliffe, *Computer-Based Medical Consultations: MYCIN*. New York, NY: Elsevier, 1976.

[5] J. McDermott, "R1: A rule-based configurer of computer systems," *Artificial Intelligence*, vol. 19, no. 1, pp. 39–88, 1982.

[6] E. A. Feigenbaum, "The art of artificial intelligence: Themes and case studies of knowledge engineering," in *Proc. International Joint Conference on Artificial Intelligence*, 1977.

[7] P. F. Wach and A. Salado, "Template/model-based requirements: A framework for structured requirements definition," in *Proc. INCOSE International Symposium*, 2019.

[8] P. F. Wach and A. Salado, "A systems theoretic metamodel for verification model definition," *Systems Engineering*, vol. 24, no. 6, pp. 396–413, 2021. DOI: 10.1002/sys.21781.

[9] P. F. Wach and A. Salado, "Theoretical underpinnings to establish fidelity conditions for defining verification models," in *Proc. INCOSE International Symposium*, Dublin, 2024.

[10] T. M. Mitchell, *Machine Learning*. New York, NY: McGraw-Hill, 1997.

[11] A. Krizhevsky, I. Sutskever, and G. E. Hinton, "ImageNet classification with deep convolutional neural networks," *Advances in Neural Information Processing Systems*, vol. 25, 2012.

[12] D. Silver et al., "Mastering the game of Go with deep neural networks and tree search," *Nature*, vol. 529, pp. 484–489, 2016.

[13] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, "BERT: Pre-training of deep bidirectional transformers for language understanding," in *Proc. NAACL-HLT*, 2019.

[14] T. Brown et al., "Language models are few-shot learners," *Advances in Neural Information Processing Systems*, vol. 33, 2020.

[15] G. Topcu, M. Husain, C. Ofsa, and P. F. Wach, "Trust at your own peril: A mixed methods exploration of the ability of large language models to generate expert-like systems engineering artifacts and a characterization of failure modes," *Systems Engineering*, Wiley, 2025. DOI: 10.1002/sys.21810.

[16] P. F. Wach, G. Bell, K. Jugan, E. Longshore, and R. Madachy, "The cost of expertise: Performance trade-offs in LLMs for systems engineering," in *Proc. INCOSE International Symposium*, Ottawa, 2025.

[17] P. F. Wach, S. Nerayo, K. Jugan, T. Anderson, P. Beling, and G. Topcu, "Cautions of leveraging LLMs for systems engineering: Generalist versus specialist," in *Proc. CESUN*, 2025.

[18] S. Yao et al., "ReAct: Synergizing reasoning and acting in language models," in *Proc. ICLR*, 2023.

[19] A. Shinn et al., "Reflexion: Language agents with verbal reinforcement learning," *Advances in Neural Information Processing Systems*, vol. 36, 2023.

[20] T. Anderson, G. Topcu, K. Jugan, S. Nerayo, and P. F. Wach, "LLM-enabled knowledge transfer: Modeler to SME," in *Proc. CSER*, Long Beach, CA, 2025.

[21] P. F. Wach, S. Nerayo, P. Beling, K. Jugan, T. Anderson, and V. Anand, "GenGroves: A bridge between systems engineers and domain experts," SERC AI4SE Workshop, 2025.

[22] P. F. Wach, K. Jugan, and J. Lucero, "Using large language models to accelerate development of complex systems," SERC AI Workshop, 2024.

[23] ISO/IEC/IEEE 15288:2023, *Systems and software engineering — System life cycle processes*.

[24] DoD, *Digital Engineering Strategy*, Office of the Deputy Assistant Secretary of Defense for Systems Engineering, 2018.

[25] NASA, *Systems Engineering Handbook*, Rev. 2, NASA/SP-2016-6105, 2016.

---

*This white paper is part of a research program at the University of Arizona on agentic AI for systems engineering. For deeper treatment of swarm architectures and their mapping to SE processes, see the companion executive summary white paper, survey paper, and vision paper available from the author.*

**Contact:** Paul F. Wach, PhD — University of Arizona
