# Section 2: Background

**Target length:** ~1,500 words
**Status:** Draft v0.1

---

## 2. Background

This section establishes the foundations underlying agentic AI swarms for systems engineering, tracing the evolution of AI capabilities and defining the systems engineering process framework to which swarm capabilities will be mapped.

### 2.1 Evolution of AI Capabilities

Artificial intelligence capabilities relevant to systems engineering have evolved through distinct generations, each offering new possibilities for engineering support.

**Expert systems (1970s-1980s)** encoded human expertise as rule-based knowledge systems [3]. Early SE applications included configuration management assistants, fault diagnosis systems, and design rule checkers. These systems demonstrated AI value for structured engineering tasks but required extensive knowledge engineering and could not adapt beyond their encoded rules.

**Machine learning (1990s-2010s)** introduced statistical learning from data [4]. SE applications expanded to include defect prediction, cost estimation, and requirements classification. ML enabled pattern recognition beyond explicit programming but required substantial training data and remained narrow in capability.

**Deep learning (2012-2020)** achieved breakthroughs in perception and representation learning [5]. Foundation architectures including transformers [6] enabled processing of sequential data including natural language. SE applications emerged in requirements analysis, design pattern recognition, and automated code generation.

**Large language models (2018-2023)** demonstrated emergent capabilities in language understanding, reasoning, and generation [7, 8]. Models trained on massive text corpora exhibited in-context learning—adapting to new tasks from examples without parameter updates. SE applications proliferated: documentation generation, requirements analysis, code completion, and technical question answering.

**Agentic AI (2023-2024)** augmented LLMs with capabilities for autonomous action [9, 10]. Tool use enables LLMs to invoke external capabilities—calculators, search engines, APIs, code interpreters. Memory systems provide persistence beyond context windows. Planning approaches enable multi-step reasoning toward goals. Agentic AI can pursue objectives through extended sequences of reasoning and action.

**Agentic swarms (2024-present)** coordinate multiple agentic AI systems to address complex tasks [11, 12, 13]. Specialized agents collaborate, bringing diverse capabilities to problems exceeding individual agent capacity. Swarm architectures enable parallelism, perspective diversity, and collective intelligence. This generation offers the potential for comprehensive SE lifecycle support through human-AI collaboration.

### 2.2 From LLMs to Agentic Swarms

The transition from LLMs to agentic swarms involves progressive capability augmentation:

**Tool use** extends LLM capabilities beyond text generation. Agents can retrieve information from databases, execute code, query APIs, and interact with engineering tools. For SE, tool use enables agents to access requirements repositories, execute analyses, and update system models.

**Memory systems** provide persistent context:
- *Short-term memory* maintains recent interaction context
- *Long-term memory* accumulates knowledge across sessions
- *Episodic memory* records past interactions and outcomes

Memory enables agents to accumulate project knowledge, learn from experience, and maintain continuity across extended engineering activities.

**Planning and reasoning** approaches enable complex task decomposition:
- *Chain-of-thought* prompting elicits step-by-step reasoning [14]
- *ReAct* interleaves reasoning with actions [9]
- *Tree-of-thought* explores alternative reasoning paths [15]

These approaches enable agents to tackle multi-step engineering tasks requiring analysis, synthesis, and judgment.

**Multi-agent coordination** enables collective capability:
- *Role specialization* assigns distinct capabilities to different agents
- *Conversation* enables agents to discuss, debate, and refine
- *Shared memory* provides common context across agents
- *Orchestration* coordinates agent activities toward objectives

Multi-agent architectures enable swarms to address SE's inherently multi-disciplinary, collaborative nature.

### 2.3 Systems Engineering Process Framework

Systems engineering provides disciplined processes for developing complex systems across the lifecycle [1, 16]. ISO/IEC/IEEE 15288:2023 [2] defines the international standard framework, organizing lifecycle processes into technical processes, technical management processes, and organizational project-enabling processes.

The **technical processes** directly realize and support the system:

| Process | ISO 15288 Ref | Description |
|---------|---------------|-------------|
| Stakeholder Needs and Requirements Definition | 6.4.1 | Elicit and define stakeholder needs |
| System Requirements Definition | 6.4.2 | Transform needs into system requirements |
| Architecture Definition | 6.4.3 | Define system architecture |
| Design Definition | 6.4.4 | Detailed design of system elements |
| System Analysis | 6.4.5 | Trade studies, effectiveness analysis |
| Implementation | 6.4.6 | Realize system elements |
| Integration | 6.4.7 | Assemble system from elements |
| Verification | 6.4.8 | Confirm system meets requirements |
| Validation | 6.4.9 | Confirm system meets stakeholder needs |
| Transition | 6.4.10 | Establish in operational environment |
| Operation | 6.4.11 | Use system to deliver services |
| Maintenance | 6.4.12 | Sustain system capability |
| Disposal | 6.4.13 | End of life management |

These processes apply across domains—aerospace, defense, healthcare, energy, transportation—making SE inherently domain-agnostic while requiring domain-specific knowledge for application.

The INCOSE Systems Engineering Handbook [1] and NASA Systems Engineering Handbook [16] provide guidance on applying these processes. Model-Based Systems Engineering (MBSE) establishes formal system models as the authoritative source of truth, creating structured representations that AI systems can process and analyze [17, 18].

### 2.4 The Case for Multi-Agent Approaches in SE

Several characteristics of systems engineering motivate multi-agent rather than single-agent AI approaches:

**Multi-disciplinary nature.** SE integrates contributions from diverse disciplines—mechanical, electrical, software, human factors, logistics. No single agent can embody deep expertise across all disciplines. Multi-agent architectures enable discipline specialization with cross-discipline coordination.

**Collaborative practice.** SE is inherently collaborative, involving teams of engineers, stakeholders, and organizations. Multi-agent systems mirror this collaborative structure, with agents representing different perspectives, roles, or organizational entities.

**Artifact complexity.** SE produces complex, interrelated artifacts—requirements, architectures, designs, test cases—with consistency and traceability requirements across thousands of elements. Agent swarms can achieve comprehensive coverage that individual analysis cannot.

**Perspective diversity.** Engineering quality benefits from multiple viewpoints examining artifacts. Agent swarms provide perspective diversity—different specializations, different analysis approaches—that surface issues single-point analysis misses.

**Parallelism potential.** Many SE activities can proceed concurrently. Agent swarms can exploit parallelism, analyzing multiple alternatives, checking multiple requirements, or evaluating multiple test cases simultaneously.

**Lifecycle span.** SE spans extended lifecycles from concept through disposal. Persistent agent systems can maintain continuity, accumulating knowledge and adapting to evolving system states across lifecycle phases.

These characteristics suggest that multi-agent architectures—agentic AI swarms—offer a natural fit for SE support, motivating the framework developed in subsequent sections.

---

**Word count:** ~1,100 words
**Subsections:** 4
**Tables:** 1
**References cited:** [1]-[18]

---

## Revision Notes

- [ ] Add figure showing AI evolution timeline
- [ ] Consider expanding MBSE connection
- [ ] Verify reference numbers align with final bibliography

