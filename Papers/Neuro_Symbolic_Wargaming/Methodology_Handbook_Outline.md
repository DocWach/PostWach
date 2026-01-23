# Methodology Handbook for Neuro-Symbolic AI-Augmented Wargaming

## Document Outline

**Document Version:** 1.0 (Outline)
**Date:** 2026-01-22
**Author:** University of Arizona PostDoc Research
**Status:** Outline for NATO STO TAP Development
**Target Audience:** Wargame designers, facilitators, analysts, acquisition professionals, ME practitioners

---

## Purpose of This Handbook

This handbook provides practitioners with a **repeatable, defensible methodology** for integrating neuro-symbolic AI into wargaming to support mission engineering analysis and acquisition decision-making. It translates the technical architecture into actionable guidance for planning, executing, and exploiting AI-augmented wargames.

---

## Handbook Structure Overview

```
PART I:   FOUNDATIONS
          Understanding AI-augmented wargaming and when to use it

PART II:  PLANNING & DESIGN
          How to design AI-augmented wargames for ME gap questions

PART III: EXECUTION
          Running wargames with AI support

PART IV:  ANALYSIS & EXPLOITATION
          Extracting and validating insights

PART V:   GOVERNANCE & QUALITY
          Ensuring credibility and responsible AI use

PART VI:  REFERENCE MATERIALS
          Templates, checklists, and quick-reference guides
```

---

# PART I: FOUNDATIONS

## Chapter 1: Introduction to AI-Augmented Wargaming

### 1.1 What is Neuro-Symbolic AI?
- Definition and key concepts
- Neural capabilities: pattern learning, generation, prediction
- Symbolic capabilities: reasoning, constraints, explanation
- Why the combination matters for wargaming

### 1.2 The Case for AI Augmentation
- Limitations of traditional wargaming for acquisition
- Benefits of AI augmentation
  - Scalability: More scenarios, faster iteration
  - Consistency: Reduced adjudicator variability
  - Traceability: Complete decision chains
  - Synthesis: Cross-game learning
- Risks and limitations to understand upfront

### 1.3 AI-Augmented vs. Traditional Wargaming
- What changes with AI augmentation
- What remains the same (human judgment, decision authority)
- Comparison table: Traditional vs. AI-augmented

### 1.4 Scope of Application
- Suitable wargame types for AI augmentation
- ME gap questions addressable through wargaming
- When NOT to use AI augmentation

---

## Chapter 2: The ME-Wargame-Acquisition Triad

### 2.1 Mission Engineering Fundamentals
- ME gap questions and their structure
- MoEs and MoPs in ME context
- DOTMLPFI framework integration

### 2.2 Wargaming's Role in Capability Development
- Wargaming as hypothesis testing
- From insights to requirements
- Traceability requirements for acquisition

### 2.3 Acquisition Decision Support
- How wargame insights inform milestones
- Evidence standards for acquisition decisions
- Stakeholder expectations

### 2.4 The Integration Model
- Triad relationships diagram
- Data flow between domains
- Feedback loops and iteration

---

## Chapter 3: AI Roles in the Wargaming Lifecycle

### 3.1 Lifecycle Overview
- Five phases: Problem Framing → Design → Execution → Analysis → Exploitation
- AI touchpoints in each phase

### 3.2 AI as Facilitator Support
- Real-time synthesis
- Discussion tracking
- Participant prompting

### 3.3 AI as Challenger
- Red team augmentation
- Assumption testing
- Edge case generation

### 3.4 AI as Analyst
- Pattern detection
- Cross-game synthesis
- Insight generation

### 3.5 AI as Record Keeper
- Automated capture
- Provenance tracking
- Traceability maintenance

### 3.6 Selecting AI Roles for Your Wargame
- Decision matrix: Wargame type × AI role suitability
- Resource requirements by role
- Risk considerations

---

# PART II: PLANNING & DESIGN

## Chapter 4: Defining the Wargame Problem

### 4.1 Sponsor Engagement
- Understanding sponsor objectives
- Translating objectives to ME gap questions
- Managing expectations for AI capabilities

### 4.2 Gap Question Selection
- Using the ME-Wargame Mapping Matrix
- Prioritizing questions for a single wargame
- Scoping to achievable outcomes

### 4.3 Defining Success Criteria
- MoE/MoP specification for the wargame
- Evidence thresholds for confidence
- Minimum viable outcomes

### 4.4 Resource Assessment
- Personnel requirements (SMEs, facilitators, AI operators)
- Technology requirements
- Time and budget constraints

**Deliverables:**
- [ ] Wargame Charter
- [ ] Selected ME Gap Questions
- [ ] Success Criteria Document

---

## Chapter 5: Designing the Wargame

### 5.1 Selecting Wargame Type
- Type taxonomy review (Seminar, Tabletop, Matrix, Computational, etc.)
- Matching type to gap questions
- Hybrid approaches

### 5.2 Scenario Development
#### 5.2.1 Human-Led Scenario Development
- Traditional scenario design process
- SME input requirements
- Doctrinal grounding

#### 5.2.2 AI-Assisted Scenario Generation
- Using the Scenario Generator
- Specifying constraints and parameters
- Reviewing and validating AI-generated scenarios
- Iteration and refinement

#### 5.2.3 Scenario Validation Checklist
- Doctrinal plausibility
- Operational realism
- Gap question alignment
- Stress test coverage

### 5.3 ORBAT and Force Structure
- AI-assisted ORBAT generation
- Capability mapping
- Coalition force considerations

### 5.4 Inject Design
- Purpose and timing of injects
- AI-generated vs. pre-planned injects
- Stress testing through injects

### 5.5 Adjudication Framework
- Rules-based vs. judgment-based adjudication
- AI support for adjudication
- Consistency and transparency requirements

### 5.6 Data Collection Plan
- What data to capture
- Capture mechanisms (automated vs. manual)
- Privacy and classification considerations

### 5.7 AI Configuration
- Selecting AI components to activate
- Configuring constraints and guardrails
- Testing AI setup before execution

**Deliverables:**
- [ ] Scenario Document
- [ ] ORBAT
- [ ] Inject Schedule
- [ ] Adjudication Rules
- [ ] Data Collection Plan
- [ ] AI Configuration Specification

---

## Chapter 6: Participant Preparation

### 6.1 Role Definitions
- Player roles and responsibilities
- Facilitator roles
- AI operator role
- Observer/analyst roles

### 6.2 Pre-Wargame Training
- Familiarization with AI capabilities
- Trust calibration briefing
- Interaction protocols

### 6.3 Briefing Materials
- Scenario read-ahead
- AI capability brief
- Rules of engagement for AI interaction

### 6.4 Managing Expectations
- What AI can and cannot do
- How to interpret AI outputs
- When to override or question AI

**Deliverables:**
- [ ] Role Assignment Matrix
- [ ] Pre-Wargame Training Package
- [ ] Participant Briefing Slides

---

# PART III: EXECUTION

## Chapter 7: Wargame Execution Protocols

### 7.1 Pre-Execution Checklist
- System readiness verification
- AI component testing
- Participant confirmation
- Fallback procedures

### 7.2 Opening Procedures
- Welcome and orientation
- AI capability demonstration
- Ground rules establishment

### 7.3 Turn/Phase Structure
- Standard turn sequence
- AI integration points in each turn
- Time management

### 7.4 Facilitator Protocols
- Managing AI-human interaction
- Handling AI failures gracefully
- Maintaining engagement

### 7.5 Real-Time AI Support
#### 7.5.1 Scenario Adaptation
- Dynamic inject triggering
- Scenario branching based on play

#### 7.5.2 Adjudication Support
- AI-assisted outcome determination
- Consistency checking
- Explanation provision

#### 7.5.3 Discussion Synthesis
- Real-time summarization
- Key point tracking
- Gap coverage monitoring

### 7.6 Data Capture During Execution
- Automated capture mechanisms
- Manual annotation protocols
- Quality assurance checks

### 7.7 Closing Procedures
- Hot wash facilitation
- Initial insight capture
- Participant feedback collection

**Deliverables:**
- [ ] Execution Log
- [ ] Raw Data Capture
- [ ] Hot Wash Notes
- [ ] Participant Feedback

---

## Chapter 8: Human-AI Teaming During Execution

### 8.1 Interaction Patterns
- Query patterns: How to ask AI for support
- Response interpretation: Understanding AI outputs
- Override protocols: When and how to override AI

### 8.2 Trust Calibration in Practice
- Recognizing appropriate trust levels
- Indicators of AI uncertainty
- Verification strategies

### 8.3 Managing AI Failures
- Common failure modes
- Graceful degradation procedures
- Recovery protocols

### 8.4 Bias Awareness
- Recognizing potential AI bias
- Human bias interaction with AI
- Mitigation strategies during execution

### 8.5 Documentation of AI Contributions
- Marking AI-generated content
- Recording AI-human interactions
- Provenance maintenance

---

# PART IV: ANALYSIS & EXPLOITATION

## Chapter 9: Post-Wargame Analysis

### 9.1 Data Consolidation
- Aggregating capture data
- Quality review and cleaning
- Gap identification in captured data

### 9.2 AI-Assisted Pattern Analysis
#### 9.2.1 Within-Game Pattern Detection
- Recurring decision patterns
- Outcome clusters
- Anomalies and outliers

#### 9.2.2 Cross-Game Synthesis
- Comparison with historical wargames
- Emerging patterns across games
- Cumulative knowledge building

### 9.3 Insight Generation
#### 9.3.1 AI-Generated Insights
- Using the Pattern Learner
- Confidence interpretation
- Validation requirements

#### 9.3.2 Human-AI Collaborative Analysis
- SME review of AI insights
- Challenging and refining insights
- Consensus building

### 9.4 Traceability Verification
- Completeness checking
- Chain validation
- Gap identification

### 9.5 Confidence Assessment
- Evidence strength evaluation
- Uncertainty quantification
- Limitation documentation

**Deliverables:**
- [ ] Consolidated Data Package
- [ ] Pattern Analysis Report
- [ ] Draft Insights with Confidence Levels

---

## Chapter 10: Insight Validation

### 10.1 Validation Framework
- Validation criteria
- Evidence thresholds
- SME validation protocols

### 10.2 Internal Validation
- Cross-checking with wargame data
- Consistency with doctrine
- Plausibility assessment

### 10.3 External Validation
- SME panel review
- Comparison with other evidence sources
- Red team challenge

### 10.4 Confidence Calibration
- Interpreting AI confidence scores
- Adjusting based on validation
- Communicating uncertainty

### 10.5 Documentation of Validation
- Validation record structure
- Dissenting views capture
- Final confidence assignment

**Deliverables:**
- [ ] Validation Record
- [ ] Validated Insight Set
- [ ] Confidence Summary

---

## Chapter 11: Exploitation and Transition

### 11.1 Insight Packaging for Decision-Makers
- Executive summary development
- Visualization of key findings
- Confidence communication

### 11.2 Traceability Documentation
- Complete chains: Gap → Wargame → Insight → Requirement
- Audit trail preparation
- Evidence package assembly

### 11.3 Requirement Linkage
- Mapping insights to capability gaps
- Supporting requirement definition
- DOTMLPFI implications

### 11.4 Acquisition Decision Support
- Milestone-specific packaging
- Alternatives analysis support
- Risk characterization

### 11.5 Knowledge Persistence
- Adding to organizational knowledge base
- Updating the Knowledge Graph
- Preparing for future wargames

### 11.6 Reporting
- Sponsor report structure
- Technical report structure
- Lessons learned documentation

**Deliverables:**
- [ ] Executive Summary
- [ ] Full Analysis Report
- [ ] Traceability Package
- [ ] Knowledge Base Updates
- [ ] Lessons Learned Report

---

# PART V: GOVERNANCE & QUALITY

## Chapter 12: Analytical Credibility

### 12.1 Credibility Framework
- Definition of analytical credibility
- Credibility dimensions
- Assessment criteria

### 12.2 Achieving Credibility
- Methodological rigor requirements
- Documentation standards
- Transparency obligations

### 12.3 Credibility Threats
- Common threats to credibility
- AI-specific credibility risks
- Mitigation strategies

### 12.4 Credibility Assessment
- Self-assessment checklist
- Peer review protocols
- External audit preparation

### 12.5 Communicating Credibility
- Credibility statements in reports
- Handling credibility challenges
- Building stakeholder confidence

---

## Chapter 13: Responsible AI Governance

### 13.1 Governance Framework Overview
- NATO Responsible AI principles
- Organizational policy alignment
- Role-based responsibilities

### 13.2 Human Oversight Requirements
- Mandatory human checkpoints
- Override authority and procedures
- Accountability assignment

### 13.3 Transparency and Explainability
- Explanation requirements by output type
- Audience-appropriate explanations
- Documentation of AI reasoning

### 13.4 Bias Management
- Bias detection procedures
- Mitigation strategies
- Monitoring and reporting

### 13.5 Data Governance
- Data quality requirements
- Classification handling
- Privacy protection

### 13.6 Risk Management
- AI risk register
- Risk monitoring procedures
- Incident response

### 13.7 Audit and Compliance
- Audit trail requirements
- Compliance verification
- External audit support

---

## Chapter 14: Quality Assurance

### 14.1 Quality Framework
- Quality dimensions for AI-augmented wargaming
- Quality metrics and targets
- Continuous improvement cycle

### 14.2 Pre-Wargame Quality Gates
- Design review checklist
- AI configuration verification
- Participant readiness assessment

### 14.3 During-Wargame Quality Monitoring
- Real-time quality indicators
- Intervention triggers
- Issue escalation procedures

### 14.4 Post-Wargame Quality Review
- Execution quality assessment
- Analysis quality verification
- Deliverable quality check

### 14.5 Lessons Learned Process
- Capture mechanisms
- Analysis and categorization
- Implementation tracking

### 14.6 Continuous Improvement
- Methodology updates
- AI model improvement
- Training program updates

---

## Chapter 15: Security and Classification

### 15.1 Classification Framework
- NATO classification levels
- National caveats handling
- Cross-domain considerations

### 15.2 AI-Specific Security
- Model security
- Input/output security
- Prompt injection prevention

### 15.3 Data Handling
- Classified data procedures
- Data minimization
- Secure destruction

### 15.4 Multinational Considerations
- Information sharing agreements
- Release authority
- Coalition operations

### 15.5 Incident Response
- Security incident procedures
- Breach notification
- Recovery protocols

---

# PART VI: REFERENCE MATERIALS

## Chapter 16: Templates and Forms

### 16.1 Planning Templates
- Wargame Charter Template
- ME Gap Question Selection Worksheet
- Success Criteria Template
- Resource Assessment Form

### 16.2 Design Templates
- Scenario Development Template
- ORBAT Template
- Inject Design Template
- Adjudication Rules Template
- Data Collection Plan Template
- AI Configuration Checklist

### 16.3 Execution Templates
- Pre-Execution Checklist
- Facilitator Protocol Guide
- Data Capture Forms
- Hot Wash Template

### 16.4 Analysis Templates
- Pattern Analysis Worksheet
- Insight Documentation Template
- Validation Record Template
- Traceability Matrix Template

### 16.5 Reporting Templates
- Executive Summary Template
- Full Report Template
- Lessons Learned Template

---

## Chapter 17: Checklists

### 17.1 Planning Phase Checklist
- Sponsor engagement complete
- Gap questions selected and prioritized
- Success criteria defined
- Resources assessed and allocated
- Wargame charter approved

### 17.2 Design Phase Checklist
- Wargame type selected
- Scenario developed and validated
- ORBAT complete
- Injects designed
- Adjudication framework established
- Data collection plan approved
- AI configuration tested
- Participant preparation complete

### 17.3 Execution Phase Checklist
- Pre-execution verification complete
- Opening procedures followed
- Data capture operational
- AI systems functioning
- Closing procedures complete
- Hot wash conducted

### 17.4 Analysis Phase Checklist
- Data consolidated and cleaned
- Pattern analysis complete
- Insights generated
- Traceability verified
- Confidence assessed
- Validation complete

### 17.5 Exploitation Phase Checklist
- Insights packaged for decision-makers
- Traceability documentation complete
- Requirements linkage established
- Reports delivered
- Knowledge base updated
- Lessons learned captured

### 17.6 Quality and Governance Checklist
- Credibility assessment passed
- Responsible AI compliance verified
- Security requirements met
- Audit trail complete

---

## Chapter 18: Quick Reference Guides

### 18.1 AI Capability Quick Reference
- One-page summary of each AI component
- Input/output specifications
- Common use cases
- Limitations and caveats

### 18.2 Wargame Type Quick Reference
- One-page summary of each wargame type
- AI suitability ratings
- Best practices
- Common pitfalls

### 18.3 ME Gap Area Quick Reference
- One-page summary of each gap area
- Recommended wargame approaches
- Key questions to address
- DOTMLPFI mapping

### 18.4 Troubleshooting Guide
- Common issues and solutions
- AI failure recovery procedures
- Escalation contacts

### 18.5 Glossary
- Key terms and definitions
- Acronyms
- Cross-references

---

## Chapter 19: Case Studies

### 19.1 Case Study 1: Coalition Operations Matrix Game
- Context and objectives
- AI components used
- Execution summary
- Insights generated
- Lessons learned

### 19.2 Case Study 2: Communications-Denied Computational Wargame
- Context and objectives
- AI components used
- Execution summary
- Insights generated
- Lessons learned

### 19.3 Case Study 3: Human-Machine Teaming Simulation
- Context and objectives
- AI components used
- Execution summary
- Insights generated
- Lessons learned

### 19.4 Case Study 4: Ethics and Authority Boundaries Seminar
- Context and objectives
- AI components used
- Execution summary
- Insights generated
- Lessons learned

### 19.5 Anti-Patterns: What Not to Do
- Common mistakes
- Warning signs
- Recovery strategies

---

## Chapter 20: Training Curriculum

### 20.1 Training Program Overview
- Training objectives
- Target audiences
- Program structure

### 20.2 Module 1: AI Fundamentals for Wargaming (4 hours)
- Learning objectives
- Content outline
- Exercises
- Assessment

### 20.3 Module 2: Designing AI-Augmented Wargames (8 hours)
- Learning objectives
- Content outline
- Exercises
- Assessment

### 20.4 Module 3: Facilitating AI-Augmented Wargames (8 hours)
- Learning objectives
- Content outline
- Exercises
- Assessment

### 20.5 Module 4: Analyzing AI-Augmented Wargames (8 hours)
- Learning objectives
- Content outline
- Exercises
- Assessment

### 20.6 Module 5: Responsible AI in Wargaming (4 hours)
- Learning objectives
- Content outline
- Exercises
- Assessment

### 20.7 Practicum: Capstone Exercise (16 hours)
- Exercise description
- Team roles
- Assessment criteria
- Certification requirements

---

# APPENDICES

## Appendix A: ME Gap Question Catalog
- Complete listing of 42 ME gap questions
- Gap area assignments
- Recommended wargame types
- Priority ratings

## Appendix B: Wargame Type Specifications
- Detailed specifications for each wargame type
- AI integration guidance
- Resource requirements

## Appendix C: AI Component Technical Reference
- Detailed technical specifications
- API reference
- Configuration parameters

## Appendix D: Knowledge Graph Schema Reference
- Ontology documentation
- Entity and relationship definitions
- Query examples

## Appendix E: DOTMLPFI Reference
- Domain definitions
- Implication categories
- Assessment guidance

## Appendix F: NATO Responsible AI Principles
- Full text of applicable principles
- Implementation guidance
- Compliance checklist

## Appendix G: Security Classification Guide
- NATO classification definitions
- Handling procedures
- Marking requirements

## Appendix H: Sample Wargame Materials
- Sample scenario
- Sample ORBAT
- Sample injects
- Sample analysis report

## Appendix I: Acronyms and Abbreviations

## Appendix J: Bibliography and References

---

# INDEX

---

## Document Development Notes

### Handbook Development Phases

| Phase | Content | Timeline |
|-------|---------|----------|
| **Phase 1** | Part I (Foundations), Part V (Governance), Part VI Ch 17-18 (Checklists, Quick Ref) | Year 1 |
| **Phase 2** | Part II (Planning), Part III (Execution), Part VI Ch 16 (Templates) | Year 2 |
| **Phase 3** | Part IV (Analysis), Part VI Ch 19-20 (Case Studies, Training), Appendices | Year 3 |

### Review and Validation

| Review Type | Reviewers | Timing |
|-------------|-----------|--------|
| Technical Review | AI/ML experts, Systems engineers | Each phase |
| Operational Review | Wargaming practitioners, ME analysts | Each phase |
| Governance Review | Legal, Ethics, Security | Each phase |
| User Testing | Pilot wargame participants | Phase 2-3 |
| Final Validation | NATO STO stakeholders | End Phase 3 |

### Version Control

| Version | Description | Date |
|---------|-------------|------|
| 0.1 | Initial outline | 2026-01-22 |
| 1.0 | Phase 1 content complete | TBD |
| 2.0 | Phase 2 content complete | TBD |
| 3.0 | Full handbook release | TBD |

---

*Outline prepared for NATO STO TAP development.*
*Version 0.1 - 2026-01-22*
