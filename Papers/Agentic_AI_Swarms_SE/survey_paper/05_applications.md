# Section 5: Applications to Systems Engineering

**Target length:** ~2,000 words
**Status:** Draft v0.1

---

## 5. Applications to Systems Engineering

This section surveys multi-agent AI applications across systems engineering process areas, assessing maturity and identifying gaps in current research and practice.

### 5.1 Mapping Framework

We organize applications according to ISO/IEC/IEEE 15288:2023 technical processes [26], providing a systematic framework for coverage assessment. For each process area, we examine:
- Reported applications in literature
- Agent architectures employed
- Maturity level (research prototype, pilot deployment, production use)
- Evidence quality (laboratory study, field trial, case study)

### 5.2 Requirements Engineering Applications

Requirements engineering—encompassing stakeholder needs definition and system requirements definition—has received substantial attention from AI and multi-agent researchers.

**Requirements elicitation** applications use agents to support stakeholder interaction and needs capture. **Elicitron** exemplifies this class: a multi-agent framework that conducts simulated stakeholder interviews, with distinct agents representing different user roles, domain experts, and regulatory perspectives to surface requirements that might otherwise be missed [112]. Multi-agent approaches include:
- Stakeholder-representative agents embodying different user perspectives [55]
- Interview assistant agents generating questions and probing for completeness, such as IBM Watson-based requirements analysis assistants [113]
- Multi-perspective analysis where agents identify conflicting stakeholder needs
- Dialogue-driven elicitation where LLM agents simulate diverse end-user populations to stress-test requirements coverage [112]

**Requirements analysis** applications examine requirements quality. Tools such as **ARTE** (Automated Requirements Traceability Engine) and NLP-based frameworks like **REGAL** demonstrate the growing sophistication of automated analysis pipelines [114]. Specific capabilities include:
- Completeness checking agents identifying missing requirements based on domain templates [56]
- Consistency checking agents detecting conflicts between requirements [57]
- Ambiguity detection agents flagging unclear language, increasingly leveraging transformer-based NLP models [58]
- Multi-agent argumentation for resolving requirement conflicts, where agents advocate for competing stakeholder priorities and negotiate compromises [59]
- Automated classification of functional versus non-functional requirements using ensemble agent architectures [114]

**Requirements specification** applications generate requirements artifacts:
- Natural language generation of requirements from models
- Formalization agents translating natural language to formal specifications
- Template-based generation with multi-agent review

**Requirements traceability** applications maintain relationships:
- Trace link generation agents identifying relationships between artifacts [60]
- Impact analysis agents assessing change propagation
- Traceability verification agents checking link completeness

**Maturity assessment:** Requirements applications are among the most mature, with research spanning decades and recent LLM-based tools reaching pilot deployment. Single-agent LLM approaches (e.g., GPT-4 for requirements classification) have demonstrated strong performance on isolated tasks, but true multi-agent systems that coordinate across elicitation, analysis, and traceability remain largely at the research prototype stage [115]. Evidence includes controlled experiments and industrial case studies, though most multi-agent evaluations are limited to laboratory settings.

### 5.3 Architecture and Design Applications

Architecture definition and design processes have seen growing multi-agent application:

**Architecture exploration** employs agents for systematic alternative evaluation. AI-assisted SysML modeling is an emerging capability, where LLM agents generate and refine SysML block definition and internal block diagrams from natural language descriptions [116]. Integration with MBSE tools such as Cameo Systems Modeler and DOORS enables agents to operate within established model repositories rather than generating standalone artifacts [117]. Specific approaches include:
- Multi-objective optimization agents exploring architecture trade spaces [61]
- Pattern-matching agents suggesting applicable architecture patterns drawn from catalogues
- Constraint-checking agents verifying architecture decisions against requirements
- LLM-based agents generating candidate SysML models from stakeholder intent descriptions [116]

**View generation** applications produce architecture representations:
- Viewpoint-specialized agents generating views per ISO 42010 [62]
- Diagram generation agents creating visual representations
- Consistency-checking agents verifying cross-view alignment

**Interface definition** applications manage system boundaries:
- Interface identification agents detecting needed interfaces from architectures
- Interface specification agents generating ICD content
- Conflict detection agents identifying interface mismatches

**Trade study support** coordinates multi-criteria analysis:
- Alternative generation agents proposing design options
- Evaluation agents assessing alternatives against criteria
- Sensitivity analysis agents exploring parameter variations
- Multi-agent deliberation aggregating assessments [63]

**Maturity assessment:** Architecture applications are moderately mature. Optimization-based approaches have production use in specific domains (e.g., aerospace trade studies); LLM-based architecture agents remain largely research prototypes with limited industrial validation. The gap between single-agent assistants (which can draft individual diagrams) and multi-agent systems (which would coordinate across viewpoints and maintain cross-view consistency) remains substantial [117].

### 5.4 Verification and Validation Applications

V&V processes have substantial multi-agent application, particularly for software-intensive systems:

**Test case generation** employs agents for systematic test development. Several specialized tools have emerged: **KaneAI** provides AI-powered end-to-end test automation with natural language test authoring [118]; **Diffblue Cover** uses reinforcement learning to automatically generate unit tests for Java codebases [119]; **TestPilot** leverages LLMs to generate test cases from code context and documentation [120]; and **EvoSuite**, originally a search-based test generator, has been augmented with LLM-driven seed generation to improve coverage in complex scenarios [121]. Specific multi-agent strategies include:
- Requirements-based test generation agents deriving tests from specifications [64]
- Coverage-directed agents generating tests to maximize coverage criteria
- Adversarial agents generating challenging test cases through mutation-based and boundary-probing strategies
- Multi-agent approaches combining coverage, boundary, and fault-based strategies, where specialized agents focus on distinct testing concerns and a coordinator agent merges results [118]

**Test execution and analysis** coordinates automated testing:
- Test orchestration agents managing test execution
- Result analysis agents interpreting test outcomes
- Regression analysis agents identifying failure patterns

**Formal verification** applications support rigorous analysis. **Lean Copilot** integrates LLMs with the Lean theorem prover to suggest proof steps and lemma applications, reducing the manual effort of formal proofs [122]. DeepMind's **AlphaProof** demonstrated that reinforcement learning combined with formal reasoning can solve competition-level mathematical problems, suggesting pathways toward automated verification of system properties [123]. Specific approaches include:
- Model checking agents exploring state spaces with intelligent state pruning
- Theorem proving agents assisting formal proofs through tactic suggestion and proof search [122]
- Abstraction agents managing complexity through model reduction
- Multi-agent verification pipelines where decomposition agents partition verification tasks and specialist agents apply domain-appropriate methods [123]

**Review and inspection** applications support human review processes:
- Pre-review analysis agents identifying potential issues for human attention
- Checklist verification agents assessing completeness against criteria
- Multi-perspective review agents examining artifacts from different viewpoints [65]

**Maturity assessment:** V&V applications, particularly test generation, are relatively mature with commercial tools such as Diffblue Cover and KaneAI incorporating AI capabilities and achieving production deployment [119]. Formal verification agents remain research-focused, though tools like Lean Copilot represent significant progress toward practical usability [122]. LLM-based review support is emerging rapidly, with single-agent code review tools reaching pilot deployment while multi-agent review orchestration remains experimental.

### 5.5 Integration and Lifecycle Applications

Later lifecycle phases have received less attention but offer significant opportunities:

**Integration planning** applications support assembly sequencing:
- Dependency analysis agents identifying integration constraints
- Sequence optimization agents generating build orders
- Resource allocation agents managing integration facilities

**Transition support** applications facilitate deployment:
- Procedure generation agents creating transition plans
- Training material agents generating user documentation
- Readiness assessment agents evaluating transition prerequisites

**Operations support** applications assist in-service systems:
- Anomaly detection agents identifying unexpected behaviors
- Diagnostic agents supporting fault isolation
- Operational optimization agents suggesting efficiency improvements

**Maintenance support** applications sustain system capability:
- Failure prediction agents anticipating maintenance needs
- Sustainment planning agents optimizing maintenance schedules
- Technical refresh agents assessing modernization options

**Maturity assessment:** Lifecycle applications lag requirements and V&V in maturity. Operations and maintenance applications exist for specific domains (predictive maintenance in manufacturing) but general SE applications remain limited.

### 5.6 Cross-Cutting Applications

Some applications span multiple process areas:

**Documentation generation** produces engineering artifacts:
- Report generation agents synthesizing technical documents
- Specification writing agents creating standards-compliant documents
- Update propagation agents maintaining document consistency

**Traceability management** maintains artifact relationships:
- Link discovery agents identifying implicit relationships
- Impact analysis agents propagating changes through trace networks
- Compliance verification agents checking traceability completeness

**Configuration management** tracks artifact versions and baselines:
- Change detection agents identifying modifications
- Baseline comparison agents assessing evolution
- Configuration audit agents verifying consistency

**Project management support** assists technical management:
- Progress assessment agents evaluating completion status
- Risk identification agents surfacing technical risks
- Resource estimation agents predicting effort requirements

### 5.7 Cross-Application Integration

A critical observation from the preceding subsections is that most multi-agent SE applications operate within a single process area. Requirements agents do not communicate with architecture agents, which in turn are disconnected from V&V agents. Yet the central promise of multi-agent orchestration in systems engineering lies precisely in cross-phase integration: a requirements change should propagate automatically to affected architecture elements, trigger re-verification of impacted test cases, and update traceability links throughout.

The concept of a **digital thread**---a continuously maintained, model-based representation linking all engineering artifacts across the lifecycle---provides a natural integration substrate for multi-agent SE systems [124]. In a fully realized digital thread, requirements agents would feed structured outputs into architecture agents, which would in turn trigger V&V agents to assess the impact of design decisions on verification plans. Multi-agent orchestration frameworks could manage this flow, with coordinator agents routing artifacts between specialist agents and monitoring cross-phase consistency [125].

Current model-based systems engineering (MBSE) tools such as Cameo Systems Modeler, IBM Engineering Lifecycle Management, and Siemens Teamcenter provide partial infrastructure for this vision, offering shared data repositories and standardized exchange formats (SysML, OSLC). However, integrating autonomous agents into these environments---enabling agents to read, modify, and create model elements while respecting access controls and process governance---remains a significant engineering challenge [124].

The state of practice is largely siloed: individual multi-agent applications achieve strong results within their process area but lack the interfaces and protocols needed for cross-application coordination. Bridging this gap represents a key research frontier. Efforts in digital engineering and the Department of Defense Digital Engineering Strategy [126] provide institutional momentum, but the agent interoperability standards and coordination protocols needed for seamless cross-phase multi-agent integration have yet to be developed.

### 5.8 Application Maturity Assessment

Table 3 summarizes application maturity across process areas.

| Process Area | Research Activity | Representative Tools | Tool Availability | Industrial Adoption | Multi-Agent Maturity | Evidence Quality |
|--------------|-------------------|---------------------|-------------------|---------------------|---------------------|------------------|
| Requirements elicitation | High | Elicitron, IBM Watson | Moderate | Low-Moderate | Research prototype | Case studies |
| Requirements analysis | High | ARTE, REGAL | Moderate | Moderate | Pilot deployment | Experiments + cases |
| Architecture exploration | Moderate | AI-SysML agents, MBSE integrations | Low | Low | Research prototype | Prototypes |
| Trade studies | Moderate | Multi-objective optimization agents | Low | Low | Research prototype | Laboratory |
| Test generation | High | KaneAI, Diffblue Cover, TestPilot, EvoSuite+LLM | High | Moderate | Pilot deployment | Experiments + field |
| Formal verification | Moderate | Lean Copilot, AlphaProof | Moderate | Low | Research prototype | Laboratory |
| Review support | Emerging | LLM-based review agents | Low | Very low | Concept | Prototypes |
| Integration | Low | --- | Very low | Very low | Concept | Limited |
| Operations/maintenance | Moderate | Domain-specific predictive agents | Moderate (domain-specific) | Moderate (specific domains) | Pilot (narrow domains) | Case studies |
| Documentation | Emerging | LLM generation agents | Emerging | Very low | Concept | Prototypes |
| Cross-phase integration | Low | Digital thread prototypes | Very low | Very low | Concept | Limited |

### 5.9 Summary: Applications × Process × Evidence

Key observations from the application survey:

**Concentrated maturity:** Application maturity concentrates in requirements analysis and test generation, with other process areas substantially less developed.

**LLM acceleration:** LLM-based approaches are rapidly advancing across process areas, but with limited industrial validation. Most LLM applications remain research prototypes or early pilots.

**Domain specificity:** Many mature applications are domain-specific (aerospace V&V, manufacturing maintenance) rather than general SE tools.

**Multi-agent gap:** Most applications employ single agents or simple agent pairs; true multi-agent swarm approaches remain rare except in optimization contexts.

**Evidence limitations:** Rigorous empirical evaluation is limited. Many papers report prototype demonstrations without controlled experiments or industrial validation.

---

**Word count:** ~2,000 words
**Subsections:** 9
**Tables:** 1 (expanded)
**References cited:** [55]-[65], [112]-[126]

---

## Revision Notes

- [x] Expand with specific tool and framework names
- [x] Add more citations for each application area
- [x] Consider splitting into two sections if length grows — retained as single section; ~2,000 words is within target and subsections provide sufficient internal navigation
- [x] Add discussion of cross-application integration

