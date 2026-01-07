---
name: Systematic Literature Review
version: 1.0.0
description: Rigorous methodology for identifying, analyzing, and synthesizing academic literature following established protocols
category: Academic Research Methods
difficulty: Advanced
estimatedTime: Variable (depends on scope and corpus size)
---

# Systematic Literature Review

A comprehensive methodology for conducting rigorous literature reviews that identify, evaluate, and synthesize existing research. Follows established protocols (PRISMA, Cochrane) adapted for interdisciplinary academic research.

## What This Skill Does

Systematic Literature Review enables researchers to:
- Develop comprehensive search strategies
- Apply rigorous inclusion/exclusion criteria
- Systematically extract and analyze data
- Synthesize findings across sources
- Identify gaps in existing knowledge
- Document the review process transparently

## Prerequisites

- Clear research question or objective
- Access to academic databases
- Basic understanding of the field
- Familiarity with citation management

---

## Core Methodology

### The PRISMA-Inspired Framework

```
SYSTEMATIC REVIEW PHASES

Phase 1: PLANNING
├── Define review objectives
├── Formulate research questions
├── Develop protocol
└── Register protocol (if applicable)

Phase 2: IDENTIFICATION
├── Develop search strategy
├── Select databases and sources
├── Execute searches
└── Document search results

Phase 3: SCREENING
├── Remove duplicates
├── Title/abstract screening
├── Full-text screening
└── Apply inclusion/exclusion criteria

Phase 4: EXTRACTION
├── Design extraction form
├── Extract data systematically
├── Assess quality/bias
└── Resolve discrepancies

Phase 5: SYNTHESIS
├── Analyze extracted data
├── Identify themes/patterns
├── Synthesize findings
└── Assess certainty of evidence

Phase 6: REPORTING
├── Document methodology
├── Present findings
├── Discuss limitations
└── Identify future directions
```

---

## Phase 1: Planning

### Research Question Formulation

```
QUESTION FRAMEWORKS

PICO (Intervention Studies):
- Population: Who is being studied?
- Intervention: What is being done?
- Comparison: What is the alternative?
- Outcome: What are the results?

SPIDER (Qualitative/Mixed):
- Sample: Who is being studied?
- Phenomenon of Interest: What is studied?
- Design: How is it studied?
- Evaluation: What outcomes?
- Research type: Qual/Quant/Mixed?

PEO (Exploratory):
- Population: Who?
- Exposure: What experience/condition?
- Outcome: What effects?

EXAMPLE:
Question: "How do LLMs perform in requirements engineering tasks?"
Framework: PEO
- Population: Systems engineers / SE organizations
- Exposure: Use of LLMs for RE tasks
- Outcome: Performance, accuracy, efficiency
```

### Protocol Development

```
REVIEW PROTOCOL TEMPLATE

1. TITLE
   [Descriptive title of the review]

2. BACKGROUND
   - Rationale for the review
   - Existing reviews (if any)
   - Gap this review addresses

3. OBJECTIVES
   - Primary objective
   - Secondary objectives
   - Research questions

4. ELIGIBILITY CRITERIA
   Inclusion:
   - Population criteria
   - Intervention/exposure criteria
   - Outcome criteria
   - Study design criteria
   - Time period
   - Language restrictions

   Exclusion:
   - Specific exclusion criteria
   - Justification for exclusions

5. INFORMATION SOURCES
   - Databases to search
   - Grey literature sources
   - Hand-searching plans
   - Expert consultation

6. SEARCH STRATEGY
   - Keywords and synonyms
   - Boolean operators
   - Database-specific syntax
   - Limits and filters

7. STUDY SELECTION PROCESS
   - Screening stages
   - Number of reviewers
   - Conflict resolution

8. DATA EXTRACTION
   - Variables to extract
   - Extraction form design
   - Pilot testing plan

9. QUALITY ASSESSMENT
   - Assessment tool(s)
   - Critical appraisal approach

10. SYNTHESIS APPROACH
    - Narrative synthesis plan
    - Meta-analysis plan (if applicable)
    - Subgroup analyses
```

---

## Phase 2: Identification

### Search Strategy Development

```
SEARCH STRATEGY COMPONENTS

1. KEY CONCEPTS
   Identify main concepts from research question
   Example: "LLM performance in requirements engineering"
   Concepts: [LLM/AI], [performance/evaluation], [requirements engineering]

2. SYNONYMS AND VARIANTS
   For each concept, list:
   - Synonyms
   - Related terms
   - Abbreviations
   - Alternative spellings

   Example for "LLM":
   - Large Language Model*
   - LLM*
   - GPT*
   - ChatGPT
   - Generative AI
   - Foundation model*
   - Transformer model*
   - Natural language processing
   - NLP

3. BOOLEAN CONSTRUCTION
   Combine with operators:
   - OR: within concept groups (synonyms)
   - AND: between concept groups
   - NOT: exclude irrelevant (use sparingly)

   Example:
   ("Large Language Model*" OR "LLM" OR "GPT*" OR "ChatGPT"
    OR "generative AI" OR "foundation model*")
   AND
   ("requirements engineering" OR "requirements analysis"
    OR "requirements quality" OR "RE")
   AND
   ("performance" OR "evaluation" OR "assessment"
    OR "accuracy" OR "effectiveness")

4. DATABASE ADAPTATION
   Adapt syntax for each database:
   - Scopus: TITLE-ABS-KEY()
   - Web of Science: TS=()
   - IEEE Xplore: ("Abstract":)
   - ACM DL: [[Abstract:]]
```

### Source Selection Matrix

| Source Type | Examples | Purpose |
|-------------|----------|---------|
| **Academic Databases** | Scopus, WoS, IEEE, ACM | Peer-reviewed literature |
| **Preprint Servers** | arXiv, SSRN, OSF | Cutting-edge research |
| **Grey Literature** | Theses, reports, white papers | Unpublished insights |
| **Citation Chaining** | Forward/backward citation | Comprehensive coverage |
| **Expert Consultation** | Domain experts | Gap identification |
| **Conference Proceedings** | INCOSE, ICSE, RE | Current developments |

### Search Documentation

```
SEARCH LOG TEMPLATE

Database: [Name]
Date Searched: [YYYY-MM-DD]
Search String: [Full query]
Limits Applied: [Date range, language, etc.]
Results Retrieved: [Number]
Notes: [Any issues or observations]

EXAMPLE:
Database: Scopus
Date Searched: 2026-01-07
Search String: TITLE-ABS-KEY(("Large Language Model*" OR "LLM"
              OR "GPT*") AND ("requirements engineering" OR
              "requirements analysis") AND ("performance" OR
              "evaluation"))
Limits Applied: 2020-2026, English, Article/Conference Paper
Results Retrieved: 247
Notes: High noise from software requirements (non-SE context)
```

---

## Phase 3: Screening

### Screening Protocol

```
TWO-STAGE SCREENING PROCESS

STAGE 1: TITLE/ABSTRACT SCREENING
┌────────────────────────────────────────────┐
│ For each record, determine:               │
│                                            │
│ INCLUDE if:                                │
│ - Clearly relevant to research question   │
│ - Meets population criteria               │
│ - Addresses phenomenon of interest        │
│                                            │
│ EXCLUDE if:                                │
│ - Clearly irrelevant topic                │
│ - Wrong population                        │
│ - Wrong study type                        │
│ - Wrong language                          │
│                                            │
│ UNCERTAIN → Proceed to full-text          │
└────────────────────────────────────────────┘

STAGE 2: FULL-TEXT SCREENING
┌────────────────────────────────────────────┐
│ For each full-text, verify:               │
│                                            │
│ □ Meets all inclusion criteria            │
│ □ Does not meet any exclusion criteria    │
│ □ Sufficient methodological detail        │
│ □ Relevant outcomes reported              │
│                                            │
│ Document exclusion reasons                │
└────────────────────────────────────────────┘
```

### Inclusion/Exclusion Criteria Template

```
ELIGIBILITY CRITERIA SPECIFICATION

INCLUSION CRITERIA:
┌─────────────────┬──────────────────────────────────────┐
│ Criterion       │ Specification                        │
├─────────────────┼──────────────────────────────────────┤
│ Population      │ [Specific population definition]     │
│ Exposure/       │ [What must be studied]               │
│ Intervention    │                                      │
│ Outcome         │ [Required outcomes]                  │
│ Study Design    │ [Acceptable designs]                 │
│ Time Period     │ [Date range]                         │
│ Language        │ [Accepted languages]                 │
│ Publication     │ [Peer-reviewed, grey lit, etc.]      │
└─────────────────┴──────────────────────────────────────┘

EXCLUSION CRITERIA:
┌─────────────────┬──────────────────────────────────────┐
│ Criterion       │ Justification                        │
├─────────────────┼──────────────────────────────────────┤
│ [Criterion 1]   │ [Why excluded]                       │
│ [Criterion 2]   │ [Why excluded]                       │
│ [Criterion 3]   │ [Why excluded]                       │
└─────────────────┴──────────────────────────────────────┘
```

### PRISMA Flow Diagram

```
PRISMA 2020 FLOW DIAGRAM

IDENTIFICATION
┌─────────────────────────────────────────────────────────┐
│ Records identified from databases (n = )                │
│   Database 1 (n = )                                     │
│   Database 2 (n = )                                     │
│   Database 3 (n = )                                     │
├─────────────────────────────────────────────────────────┤
│ Records identified from other sources (n = )           │
│   Citation searching (n = )                             │
│   Expert recommendations (n = )                         │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│ Records after duplicates removed (n = )                │
└─────────────────────────────────────────────────────────┘
                          │
SCREENING                 ▼
┌─────────────────────────────────────────────────────────┐
│ Records screened (n = )                                │
│                                     Excluded (n = )    │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│ Full-text articles assessed (n = )                     │
│                                     Excluded (n = )    │
│                                       Reason 1 (n = )  │
│                                       Reason 2 (n = )  │
│                                       Reason 3 (n = )  │
└─────────────────────────────────────────────────────────┘
                          │
INCLUDED                  ▼
┌─────────────────────────────────────────────────────────┐
│ Studies included in review (n = )                      │
│   Quantitative (n = )                                   │
│   Qualitative (n = )                                    │
│   Mixed methods (n = )                                  │
└─────────────────────────────────────────────────────────┘
```

---

## Phase 4: Data Extraction

### Extraction Form Design

```
DATA EXTRACTION FORM

STUDY IDENTIFICATION
- Author(s):
- Year:
- Title:
- Journal/Conference:
- DOI:

STUDY CHARACTERISTICS
- Country/Setting:
- Study Design:
- Time Period:
- Sample Size:
- Funding Source:

POPULATION
- Description:
- Inclusion Criteria:
- Recruitment Method:

INTERVENTION/EXPOSURE
- Description:
- Duration:
- Comparison/Control:

OUTCOMES
- Primary Outcome(s):
- Secondary Outcome(s):
- Measurement Method:
- Timing of Assessment:

RESULTS
- Main Findings:
- Effect Sizes (if applicable):
- Statistical Significance:
- Confidence Intervals:

QUALITY INDICATORS
- Risk of Bias:
- Limitations Noted:
- Generalizability:

REVIEWER NOTES
- Key Contributions:
- Methodological Concerns:
- Relevance to Review Questions:
```

### Quality Assessment Tools

```
QUALITY ASSESSMENT SELECTION

For Quantitative Studies:
├── RCTs → Cochrane Risk of Bias Tool
├── Cohort → Newcastle-Ottawa Scale
├── Cross-sectional → AXIS Tool
└── Case-control → Newcastle-Ottawa Scale

For Qualitative Studies:
├── General → CASP Qualitative Checklist
├── Grounded Theory → CASP + specific criteria
└── Case Study → Joanna Briggs Institute Checklist

For Mixed Methods:
└── MMAT (Mixed Methods Appraisal Tool)

For Technical/Engineering Studies:
├── Empirical SE → Guidelines by Kitchenham
└── Design Science → Hevner's Guidelines
```

### Quality Assessment Template

```
QUALITY APPRAISAL CHECKLIST

Study: [Citation]
Assessor: [Name]
Date: [Date]

DOMAIN 1: RESEARCH DESIGN
□ Clear research question/objective
□ Appropriate study design for question
□ Adequate sample/case selection
Score: [ ] High [ ] Medium [ ] Low [ ] Unclear

DOMAIN 2: METHODOLOGY
□ Methods clearly described
□ Data collection appropriate
□ Analysis approach justified
Score: [ ] High [ ] Medium [ ] Low [ ] Unclear

DOMAIN 3: VALIDITY
□ Internal validity addressed
□ External validity discussed
□ Limitations acknowledged
Score: [ ] High [ ] Medium [ ] Low [ ] Unclear

DOMAIN 4: REPORTING
□ Results clearly presented
□ Findings support conclusions
□ Sufficient detail for replication
Score: [ ] High [ ] Medium [ ] Low [ ] Unclear

OVERALL QUALITY: [ ] High [ ] Medium [ ] Low

Notes:
```

---

## Phase 5: Synthesis

### Synthesis Approaches

```
SYNTHESIS METHOD SELECTION

NARRATIVE SYNTHESIS
When to use:
- Heterogeneous studies
- Qualitative or mixed evidence
- Conceptual/theoretical review

Techniques:
- Thematic analysis
- Content analysis
- Framework synthesis
- Critical interpretive synthesis

META-ANALYSIS
When to use:
- Homogeneous quantitative studies
- Comparable outcomes
- Sufficient number of studies

Requirements:
- Similar study designs
- Common effect measures
- Statistical data available

MIXED METHODS SYNTHESIS
When to use:
- Both qual and quant studies
- Complementary perspectives needed

Approaches:
- Segregated (separate then integrate)
- Integrated (transform and combine)
- Contingent (sequential, building)
```

### Thematic Synthesis Protocol

```
THEMATIC SYNTHESIS STEPS

1. CODING
   - Read extracted data thoroughly
   - Apply line-by-line coding
   - Use both inductive and deductive codes
   - Maintain coding consistency

2. DESCRIPTIVE THEMES
   - Group related codes
   - Develop descriptive themes
   - Stay close to primary data
   - Create theme definitions

3. ANALYTICAL THEMES
   - Go beyond primary studies
   - Generate new interpretations
   - Address review questions
   - Develop theoretical insights

THEME DOCUMENTATION:
┌────────────────────────────────────────────────────────┐
│ Theme: [Name]                                          │
│ Definition: [Clear definition]                         │
│ Codes included: [List of codes]                        │
│ Studies contributing: [Citations]                      │
│ Illustrative quotes: [Key quotes]                      │
│ Analytical insight: [Interpretation]                   │
└────────────────────────────────────────────────────────┘
```

### Evidence Mapping

```
EVIDENCE MAP TEMPLATE

Research Question: [RQ]

┌─────────────────────┬────────┬────────┬────────┬────────┐
│ Finding/Theme       │ Strong │ Moderate│ Limited│ Gap    │
├─────────────────────┼────────┼────────┼────────┼────────┤
│ [Finding 1]         │   X    │        │        │        │
│ [Finding 2]         │        │   X    │        │        │
│ [Finding 3]         │        │        │   X    │        │
│ [Finding 4]         │        │        │        │   X    │
└─────────────────────┴────────┴────────┴────────┴────────┘

Evidence Strength Criteria:
- Strong: Multiple high-quality studies, consistent findings
- Moderate: Several studies, mostly consistent
- Limited: Few studies or inconsistent findings
- Gap: No studies identified
```

---

## Phase 6: Reporting

### Review Report Structure

```
SYSTEMATIC REVIEW REPORT OUTLINE

1. ABSTRACT
   - Background
   - Objectives
   - Methods
   - Results
   - Conclusions

2. INTRODUCTION
   - Rationale
   - Objectives
   - Research questions

3. METHODS
   - Protocol and registration
   - Eligibility criteria
   - Information sources
   - Search strategy
   - Selection process
   - Data collection process
   - Data items
   - Quality assessment
   - Synthesis methods

4. RESULTS
   - Study selection (PRISMA flow)
   - Study characteristics
   - Quality assessment results
   - Synthesis findings
   - Additional analyses

5. DISCUSSION
   - Summary of evidence
   - Limitations
   - Implications
   - Future research

6. CONCLUSIONS
   - Key findings
   - Recommendations

APPENDICES
   - Full search strategies
   - Excluded studies list
   - Data extraction forms
   - Quality assessments
```

---

## Integration with Claude Flow

### Spawning Literature Review

```bash
# Run systematic literature review
claude-flow hive-mind spawn "Conduct systematic review on [topic]" \
  --queen epistemic \
  --workers empiricist-gatherer,skeptical-challenger,dialectical-synthesizer
```

### Memory Patterns

```javascript
// Store review protocol
mcp__claude-flow__memory_usage({
  action: "store",
  key: "research/literature-review/protocol",
  namespace: "academic",
  value: JSON.stringify({
    title: reviewTitle,
    objectives: reviewObjectives,
    eligibilityCriteria: criteria,
    searchStrategy: searchStrings,
    synthesisApproach: approach
  })
})

// Store screening results
mcp__claude-flow__memory_usage({
  action: "store",
  key: "research/literature-review/screening",
  namespace: "academic",
  value: JSON.stringify({
    identified: totalRecords,
    duplicatesRemoved: duplicates,
    screened: screenedRecords,
    excluded: excludedRecords,
    included: includedStudies,
    prismaFlow: flowDiagram
  })
})

// Store synthesis findings
mcp__claude-flow__memory_usage({
  action: "store",
  key: "research/literature-review/synthesis",
  namespace: "academic",
  value: JSON.stringify({
    themes: identifiedThemes,
    evidenceMap: evidenceStrengths,
    gaps: identifiedGaps,
    conclusions: mainFindings
  })
})
```

---

## Output Templates

### Literature Review Summary

```
SYSTEMATIC LITERATURE REVIEW: [Topic]
Date: [Date]
Reviewer(s): [Names]

OVERVIEW
Objective: [Review objective]
Databases: [List]
Date Range: [Period covered]
Studies Included: [Number]

SEARCH RESULTS
Total Identified: [N]
Duplicates Removed: [N]
Title/Abstract Screened: [N]
Full-Text Assessed: [N]
Final Included: [N]

KEY FINDINGS
Theme 1: [Theme name]
- [Finding summary]
- Evidence strength: [Strong/Moderate/Limited]
- Contributing studies: [N]

Theme 2: [Theme name]
- [Finding summary]
- Evidence strength: [Strong/Moderate/Limited]
- Contributing studies: [N]

GAPS IDENTIFIED
1. [Gap description]
2. [Gap description]
3. [Gap description]

QUALITY OF EVIDENCE
- High quality studies: [N]
- Moderate quality: [N]
- Low quality: [N]

LIMITATIONS
- [Limitation 1]
- [Limitation 2]

CONCLUSIONS
[Summary of main conclusions]

IMPLICATIONS FOR RESEARCH
[Future research directions]
```

---

## Quality Criteria

A systematic literature review is successful when:

1. **Comprehensive**: Thorough search across relevant sources
2. **Transparent**: All decisions documented and reproducible
3. **Rigorous**: Systematic application of criteria
4. **Unbiased**: Minimizes selection and interpretation bias
5. **Synthesized**: Findings meaningfully integrated
6. **Actionable**: Clear implications identified

---

## Troubleshooting

### "Too many results"
- Narrow search terms
- Add specific filters
- Use more precise Boolean logic
- Consider focused sub-reviews

### "Too few results"
- Broaden search terms
- Add synonyms and variants
- Search additional databases
- Include grey literature

### "Heterogeneous studies"
- Use narrative synthesis
- Group by study type
- Conduct subgroup analyses
- Acknowledge heterogeneity

### "Quality concerns"
- Document quality issues
- Conduct sensitivity analyses
- Weight by quality in synthesis
- Discuss implications for findings

---

## Learn More

- Moher, D. et al. (2009). PRISMA Statement
- Higgins, J.P.T. & Green, S. (2011). Cochrane Handbook
- Kitchenham, B. & Charters, S. (2007). Guidelines for SE Systematic Reviews
- Booth, A. et al. (2016). Systematic Approaches to Successful Literature Review
