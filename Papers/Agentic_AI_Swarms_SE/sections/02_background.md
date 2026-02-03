# Section 2: Background — Evolution of AI Capabilities

**Target length:** ~1,500 words
**Status:** Draft v0.1

---

## 2. Background: Evolution of AI Capabilities

The application of artificial intelligence to engineering problems has evolved through six distinct capability tiers over the past five decades. Each tier introduced new capabilities while retaining the strengths of previous approaches, creating a cumulative technological foundation. Understanding this evolution provides essential context for positioning agentic AI swarms as the current frontier of AI-augmented systems engineering.

![Evolution of AI: From Rules to Swarms](../../docs/ai_history_timeline.png)

### 2.1 Expert Systems (1970s–1980s)

The first generation of AI systems applied to engineering problems were expert systems—software that encoded human expert knowledge as explicit "if-then" rules [1]. These systems represented domain expertise in symbolic form, enabling consistent application of established practices without requiring the human expert's presence.

In systems engineering contexts, expert systems found early application in configuration management, fault diagnosis, and design rule checking. XCON (also known as R1), developed at Digital Equipment Corporation, configured VAX computer systems by applying thousands of rules encoding expert knowledge about component compatibility and spatial constraints [ref]. NASA employed expert systems for spacecraft fault diagnosis and mission planning support [ref].

The limitations of expert systems became apparent as system complexity increased. Knowledge acquisition proved expensive and time-consuming, requiring extensive interviews with domain experts. The systems were brittle—performing well within their encoded knowledge but failing unpredictably when encountering situations outside their rule base. They could not learn from experience or adapt to new situations without manual rule updates. Despite these limitations, the paradigm established the principle of encoding domain expertise in computational form, a concept that persists in modern AI systems.

### 2.2 Machine Learning (1990s–2010s)

The second tier shifted from explicit knowledge encoding to learning patterns from data. Machine learning algorithms—including support vector machines, random forests, and early neural networks—could generalize from training examples to new inputs, reducing dependence on manual knowledge engineering [2].

For systems engineering, machine learning enabled new capabilities in cost estimation, defect prediction, and risk assessment. Statistical models trained on historical project data could predict development effort, identify high-risk components, and support resource allocation decisions. The approach proved particularly valuable where explicit rules were difficult to articulate but historical data was available.

However, machine learning required careful feature engineering—human experts still needed to identify relevant input variables. Models were typically narrow, trained for single tasks, and struggled to transfer knowledge across domains. The "black box" nature of many algorithms made it difficult to explain predictions to stakeholders, limiting adoption in safety-critical systems engineering contexts where traceability and justification are essential.

### 2.3 Deep Learning (2012–2020)

Deep learning extended machine learning through multi-layer neural networks capable of automatically learning hierarchical feature representations from raw data [17]. The 2012 AlexNet breakthrough in image classification triggered rapid adoption across perception tasks, enabling capabilities previously considered intractable.

In engineering applications, deep learning enabled automatic feature extraction from complex data sources—satellite imagery analysis, sensor signal processing, natural language processing of requirements documents, and pattern recognition in design repositories. The technology reduced dependence on manual feature engineering, allowing systems to learn relevant representations directly from data.

For systems engineering specifically, deep learning supported requirements classification, design pattern recognition, and anomaly detection in operational systems. Research explored applications in automated document analysis, extracting structured information from unstructured technical specifications and identifying potential conflicts or gaps.

Yet deep learning models remained specialized—one model per task—and required large labeled datasets for training. The computational demands were substantial, and the "black box" criticism intensified as model complexity increased. Transfer learning emerged as a partial solution, enabling pre-trained models to be adapted to new domains with less data, foreshadowing the foundation model paradigm that would follow.

### 2.4 Large Language Models (2018–2023)

The fourth tier emerged with transformer-based language models trained on internet-scale text corpora [17]. Beginning with BERT (2018) and accelerating through the GPT series and Claude, these large language models (LLMs) demonstrated emergent capabilities that qualitatively exceeded their predecessors [18, 19].

LLMs introduced several capabilities relevant to systems engineering:

- **Zero-shot and few-shot learning**: Performing tasks without task-specific training, guided only by natural language instructions
- **General-purpose reasoning**: Applying logical inference across diverse problem types
- **Code generation and analysis**: Producing and reviewing software artifacts
- **Natural language understanding**: Processing technical documents, specifications, and requirements at scale
- **Multi-step reasoning**: Decomposing complex problems into sequential steps

For systems engineering practice, LLMs enabled new applications in documentation generation, requirements analysis, interface specification review, and decision support. Systems engineers could query models about standards compliance, explore design trade-offs through natural language dialogue, and generate initial drafts of technical documents.

However, LLMs exhibited significant limitations. They were fundamentally reactive—responding to prompts but lacking persistent goals or memory across sessions. Hallucination—generating plausible but factually incorrect content—posed risks in engineering contexts where accuracy is critical. Knowledge cutoffs meant models lacked information about recent developments, and context window limitations constrained the size of documents they could process in a single interaction.

### 2.5 Agentic AI (2023–2024)

The fifth tier addressed LLM limitations by augmenting language models with tools, persistent memory, and goal-directed control loops [23, 24]. Agentic AI systems could browse the web, execute code, call APIs, and maintain state across interactions—enabling autonomous multi-step task execution.

The ReAct framework (Reasoning + Acting) demonstrated that interleaving reasoning traces with action execution improved task completion on complex problems [23]. Systems could now observe their environment, reason about observations, take actions, and adapt based on feedback—a fundamental shift from reactive query-response to proactive goal pursuit.

For systems engineering, agentic AI opened possibilities for automated trade study execution, design space exploration, and requirements verification workflows. An agent could be tasked with evaluating alternative architectures, gathering relevant data from multiple sources, performing analyses, and synthesizing recommendations—all without step-by-step human guidance.

Yet single-agent systems faced scalability limits. Complex systems engineering tasks require diverse expertise—requirements engineering, multiple design disciplines, verification and validation, project management—that exceeded the capability of any single agent. Sequential execution created bottlenecks, and the absence of checks and balances increased the risk of errors propagating through extended workflows.

### 2.6 Agentic Swarms (2024–Present)

The current frontier extends agentic AI to coordinated multi-agent systems—swarms of specialized agents working collectively on complex problems [29–34]. Rather than a single agent attempting all tasks, swarms implement division of labor analogous to human engineering teams.

Key characteristics of agentic AI swarms include:

- **Agent specialization**: Individual agents optimized for specific roles (requirements analysis, architecture, domain expertise, verification)
- **Parallel execution**: Multiple agents working simultaneously on independent subtasks
- **Shared memory**: Common knowledge repositories enabling information exchange without direct communication
- **Coordination mechanisms**: Protocols for managing dependencies, resolving conflicts, and achieving consensus
- **Emergent capabilities**: Collective behaviors exceeding the sum of individual agent capabilities

For systems engineering, swarms offer the potential to support full lifecycle activities with appropriate expertise at each phase. A swarm might include agents specializing in stakeholder needs elicitation, requirements derivation, architecture definition, domain-specific design (mechanical, electrical, software, human factors), integration planning, and verification—mirroring the structure of integrated product teams in traditional systems engineering organizations.

The emergence of agentic swarms coincides with the digital engineering transformation in systems engineering practice [48, 57]. As organizations increasingly rely on model-based approaches and authoritative sources of truth, AI swarms could serve as intelligent participants in the digital thread—consuming, producing, and validating engineering artifacts in coordination with human engineers.

However, swarm systems introduce new challenges: coordination overhead, emergent unpredictable behaviors, governance and accountability questions, and the need for robust human oversight mechanisms. These challenges, and potential approaches to addressing them, are explored in Section 7.

### 2.7 Summary

Table 1 summarizes the six tiers of AI capability evolution with their characteristics and systems engineering applications.

| Tier | Era | Core Capability | SE Applications | Limitations |
|------|-----|-----------------|-----------------|-------------|
| 1. Expert Systems | 1970s–1980s | Rule-based reasoning | Configuration, fault diagnosis | Brittle, no learning |
| 2. Machine Learning | 1990s–2010s | Pattern learning from data | Cost estimation, defect prediction | Feature engineering required |
| 3. Deep Learning | 2012–2020 | Automatic feature learning | Document analysis, anomaly detection | Single-task, data-hungry |
| 4. LLMs | 2018–2023 | General-purpose language | Documentation, requirements analysis | Reactive, hallucination |
| 5. Agentic AI | 2023–2024 | Tool use, goal-directed | Trade studies, design exploration | Single-agent limits |
| 6. Agentic Swarms | 2024–present | Multi-agent coordination | Full lifecycle support | Coordination, governance |

Each tier builds upon rather than replaces its predecessors. Modern agentic swarms incorporate rule-based constraints (Tier 1), learned models (Tiers 2–3), language understanding (Tier 4), and autonomous action (Tier 5) within a coordinated multi-agent architecture. This cumulative foundation enables capabilities that no single tier could achieve in isolation.

---

**Word count:** ~1,480 words
**References cited:** [1], [2], [17], [18], [19], [23], [24], [29–34], [48], [57]
**Figures:** 1 (AI Evolution Timeline)
**Tables:** 1 (Tier Summary)

---

## Revision Notes

- [ ] Add specific citation numbers from reference list
- [ ] Verify NASA expert systems reference
- [ ] Add XCON/R1 citation
- [ ] Consider adding brief mention of symbolic AI vs. connectionist debate
- [ ] Verify word count after final edits
