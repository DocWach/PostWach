# Reproducibility Skill

## Overview

The Reproducibility skill provides comprehensive workflows for ensuring research transparency, openness, and reproducibility. This skill covers preregistration, open materials practices, code sharing, replication protocols, and adherence to open science principles throughout the research lifecycle.

## Capabilities

- Preregistration and registered reports
- Open materials and methods
- Code and analysis sharing
- Replication study design
- Transparency reporting
- Open science compliance

---

## Phase 1: Preregistration

### Preregistration Framework

```
PREREGISTRATION GUIDE

WHAT IS PREREGISTRATION
─────────────────────────────────────────
Preregistration: Specifying your research plan
in advance and registering it in a public repository
before collecting or analyzing data.

Benefits:
□ Distinguishes confirmatory from exploratory
□ Reduces p-hacking and HARKing
□ Increases transparency
□ Protects against hindsight bias
□ May improve study design
□ Signals credibility to reviewers

When to preregister:
□ Before data collection (ideal)
□ Before data analysis (second best)
□ For secondary data: Before accessing data

PREREGISTRATION PLATFORMS
─────────────────────────────────────────
OSF Registries (osf.io/registries)
- Free, flexible
- Multiple templates
- DOI assigned
- Embargo option

AsPredicted (aspredicted.org)
- Simple, quick (9 questions)
- Free
- Embargo option
- Good for straightforward studies

ClinicalTrials.gov
- Required for clinical trials
- FDA mandate for some studies
- Public database

PROSPERO
- Systematic reviews
- Free registration
- International database

Domain-specific:
- RIDIE (development economics)
- EGAP (governance/politics)
- AEA RCT Registry (economics)

PREREGISTRATION TEMPLATE
─────────────────────────────────────────
1. STUDY INFORMATION
   Title: _______________
   Authors: _______________
   Date: _______________
   Registration platform: _______________

2. RESEARCH QUESTIONS/HYPOTHESES
   RQ1: _______________
   H1: [Specific, testable hypothesis]
   H2: [Specific, testable hypothesis]

3. DESIGN
   Study type: [Experimental/Observational/Survey/etc.]
   Design: [Between/Within/Mixed/etc.]
   Conditions/Groups: _______________

4. SAMPLING
   Target population: _______________
   Sampling method: _______________
   Sample size: _______________
   Sample size rationale: _______________
   Stopping rule: _______________

5. VARIABLES
   Independent variables:
   - [Variable]: [Operationalization]

   Dependent variables:
   - [Variable]: [Operationalization]

   Covariates/Controls:
   - [Variable]: [Rationale for inclusion]

6. ANALYSIS PLAN
   Statistical model(s): _______________
   Inference criteria: _______________
   Data exclusion criteria: _______________
   Missing data handling: _______________

7. OTHER
   Known limitations: _______________
   Exploratory analyses planned: _______________

PREREGISTRATION CHECKLIST
─────────────────────────────────────────
Before registering:
□ Hypotheses are specific and testable
□ Sample size justified (power analysis)
□ Variables clearly operationalized
□ Analysis plan detailed enough to follow
□ Exclusion criteria specified in advance
□ Co-authors have reviewed and approved

After registering:
□ Save registration confirmation
□ Note registration DOI/URL
□ Follow the plan (deviations documented)
□ Report registration in manuscript
```

### Registered Reports

```
REGISTERED REPORTS

WHAT ARE REGISTERED REPORTS
─────────────────────────────────────────
Registered Report: A publication format where
peer review occurs before data collection.
If Stage 1 is accepted (In-Principle Acceptance),
the paper is published regardless of results.

Two-stage process:
Stage 1: Review introduction, methods, analysis plan
Stage 2: Review completed study with results

Benefits:
□ Publication guaranteed (for accepted Stage 1)
□ Eliminates publication bias
□ Improves methodology through review
□ Results cannot influence publication decision
□ Strong credibility signal

STAGE 1 SUBMISSION COMPONENTS
─────────────────────────────────────────
1. Introduction
   - Background and rationale
   - Research questions
   - Hypotheses (specific, testable)

2. Methods
   - Design
   - Participants/sampling
   - Materials/measures
   - Procedure
   - Sample size justification

3. Analysis Plan
   - Statistical approach for each hypothesis
   - Inference criteria
   - Data exclusion rules
   - Assumption checks
   - Handling of violations

4. Timeline
   - Projected data collection dates
   - Expected completion

STAGE 1 REVIEW CRITERIA
─────────────────────────────────────────
Reviewers evaluate:
□ Importance of research question
□ Logic and rationale of hypotheses
□ Soundness of methodology
□ Statistical power and sample size
□ Feasibility of proposed timeline
□ Clarity of analysis plan

NOT evaluated (yet):
□ Results (don't exist yet)
□ Whether hypotheses confirmed

IN-PRINCIPLE ACCEPTANCE (IPA)
─────────────────────────────────────────
If Stage 1 accepted:
- Journal commits to publish
- Regardless of results
- As long as Stage 2 follows plan

Conditions for IPA:
□ Follow approved protocol
□ Document any deviations
□ Report all preregistered analyses
□ Do not change hypotheses

STAGE 2 SUBMISSION
─────────────────────────────────────────
Add to Stage 1:
□ Results section
□ Discussion section
□ Final method details (actual N, etc.)
□ Deviations from protocol (if any)
□ Exploratory analyses (clearly labeled)

Stage 2 review:
□ Did study follow protocol?
□ Are deviations justified?
□ Are conclusions supported by data?
□ Is reporting complete?

REGISTERED REPORTS JOURNALS
─────────────────────────────────────────
Check COS list: cos.io/rr/

Participating journals (examples):
- Nature Human Behaviour
- PLOS ONE
- Cortex
- Royal Society Open Science
- Psychological Science (some)
- Many discipline-specific journals
```

---

## Phase 2: Open Materials

### Materials Sharing Framework

```
OPEN MATERIALS GUIDE

WHAT TO SHARE
─────────────────────────────────────────
Research materials:
□ Questionnaires and surveys
□ Interview protocols/guides
□ Experimental stimuli
□ Task instructions
□ Consent forms (templates)
□ Coding schemes
□ Training materials

Instruments:
□ Custom-developed measures
□ Adapted measures (with permissions)
□ Scoring procedures
□ Psychometric information

Protocols:
□ Detailed procedures
□ Randomization procedures
□ Quality control checklists
□ Fidelity measures

MATERIALS PREPARATION
─────────────────────────────────────────
Cleaning materials:
□ Remove identifying information
□ Check for embedded metadata
□ Ensure all parts included
□ Update file formats if needed

Documentation:
□ README explaining contents
□ Version information
□ Licensing information
□ Citation guidance
□ Contact for questions

Quality check:
□ Materials are complete
□ Instructions are clear
□ Third party can use them
□ No copyright violations

MATERIALS SHARING CHECKLIST
─────────────────────────────────────────
Before sharing:
□ Permission to share (if adapted)
□ Co-author approval
□ Institutional approval (if needed)
□ No identifying information
□ Clear documentation

Sharing:
□ Repository selected (OSF, etc.)
□ Materials uploaded
□ DOI assigned
□ License specified
□ Link in manuscript

OPEN MATERIALS BADGE
─────────────────────────────────────────
COS Open Materials Badge criteria:
□ Digitally shareable materials are publicly available
□ Materials are provided in a format useful to researchers
□ Materials are described in sufficient detail
□ Materials are located at a stable URL/DOI

Badge statement (for papers):
"Materials are available at [URL/DOI]"
```

### Protocol Documentation

```
PROTOCOL DOCUMENTATION

PROTOCOL TEMPLATE
─────────────────────────────────────────
# Study Protocol: [Title]

Version: [X.X]
Date: [YYYY-MM-DD]
Authors: [Names]

## 1. Background and Rationale
[Why this study is being conducted]

## 2. Objectives
Primary: [Main objective]
Secondary: [Additional objectives]

## 3. Study Design
Design type: [Description]
Duration: [Timeline]
Setting: [Where conducted]

## 4. Participants
Population: [Target population]
Inclusion criteria:
- [Criterion 1]
- [Criterion 2]

Exclusion criteria:
- [Criterion 1]
- [Criterion 2]

Sample size: [N with justification]
Recruitment: [Method]

## 5. Procedures
### 5.1 Screening
[Screening procedures]

### 5.2 Enrollment
[Enrollment procedures]

### 5.3 Intervention/Condition (if applicable)
[Detailed procedures]

### 5.4 Data Collection
[What, when, how]

### 5.5 Follow-up
[Follow-up procedures]

## 6. Measures
| Measure | Construct | Timing | Administration |
|---------|-----------|--------|----------------|
| [Name] | [What measured] | [When] | [How] |

## 7. Data Management
[Storage, security, handling]

## 8. Analysis Plan
[Statistical approach]

## 9. Ethical Considerations
IRB: [Approval number]
Consent: [Process]
Risks: [Assessment and mitigation]

## 10. Timeline
| Milestone | Date |
|-----------|------|
| Start | [Date] |
| End | [Date] |

## 11. Amendments
| Version | Date | Changes |
|---------|------|---------|
| 1.0 | [Date] | Original |
| 1.1 | [Date] | [Changes] |

PROTOCOLS.IO
─────────────────────────────────────────
Platform for sharing protocols:
- DOI for protocols
- Version control
- Step-by-step format
- Community feedback
- Integration with publications

Benefits:
□ Detailed step documentation
□ Troubleshooting tips
□ Multimedia support
□ Fork and adapt
```

---

## Phase 3: Code and Analysis Sharing

### Code Sharing Framework

```
CODE SHARING GUIDE

WHAT CODE TO SHARE
─────────────────────────────────────────
Essential:
□ Analysis code (produces reported results)
□ Data processing/cleaning code
□ Figure/table generation code

Recommended:
□ Data collection scripts (if applicable)
□ Simulation code
□ Custom functions/packages
□ Configuration files

Supporting:
□ Documentation
□ Example workflows
□ Test cases

CODE PREPARATION
─────────────────────────────────────────
Cleaning:
□ Remove hardcoded paths
□ Remove sensitive information
□ Remove unused code
□ Organize logically
□ Use consistent style

Documentation:
□ README with overview
□ Comments explaining logic
□ Requirements/dependencies listed
□ Installation instructions
□ Usage examples

Structure:
project/
├── README.md
├── LICENSE
├── requirements.txt (or equivalent)
├── data/
│   └── README.md (describe data)
├── src/ or scripts/
│   ├── 01_clean_data.R
│   ├── 02_analyze.R
│   └── 03_visualize.R
├── output/
│   ├── figures/
│   └── tables/
└── docs/
    └── codebook.md

CODE DOCUMENTATION TEMPLATE
─────────────────────────────────────────
# [Project Name]

## Overview
[Brief description of what the code does]

## Requirements
- [Language] version [X.X]
- [Package 1] version [X.X]
- [Package 2] version [X.X]

## Installation
```
[Installation commands]
```

## Usage
```
[Example usage]
```

## File Descriptions
- `01_clean_data.R`: [Description]
- `02_analyze.R`: [Description]

## Data
[Description of required data and where to obtain]

## Output
[Description of what code produces]

## Citation
[How to cite]

## License
[License type]

## Contact
[Contact information]

REPRODUCIBILITY CHECKLIST
─────────────────────────────────────────
□ Code runs without errors
□ Dependencies documented
□ Random seeds set for reproducibility
□ File paths are relative, not absolute
□ All necessary files included
□ Output matches reported results
□ Third party has tested running code
```

### Computational Reproducibility

```
COMPUTATIONAL REPRODUCIBILITY

LEVELS OF REPRODUCIBILITY
─────────────────────────────────────────
Level 1: Code available
- Code is shared
- May require effort to run

Level 2: Code runs
- Code executes without errors
- Dependencies available

Level 3: Results reproduce
- Running code produces same results
- Within acceptable tolerance

Level 4: Fully reproducible
- One-click reproduction
- Containerized environment
- All dependencies captured

DEPENDENCY MANAGEMENT
─────────────────────────────────────────
R:
- renv package (lockfile)
- sessionInfo() documentation
- DESCRIPTION file for packages

Python:
- requirements.txt (pip)
- environment.yml (conda)
- Pipfile (pipenv)
- pyproject.toml (poetry)

General:
- Docker container
- Binder configuration
- Makefile for workflow

Example requirements.txt:
```
pandas==1.5.0
numpy==1.23.0
scipy==1.9.0
matplotlib==3.6.0
```

CONTAINERIZATION
─────────────────────────────────────────
Docker basics:

Dockerfile example:
```dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "analysis.py"]
```

Benefits:
□ Captures entire environment
□ Runs anywhere Docker runs
□ Version-controlled
□ Shareable via Docker Hub

BINDER
─────────────────────────────────────────
mybinder.org - Free service to run code in browser

Setup:
1. Put code in GitHub repo
2. Add environment file (requirements.txt, environment.yml)
3. Add Binder badge to README
4. Anyone can run code in browser

Badge example:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/user/repo/main)

WORKFLOW AUTOMATION
─────────────────────────────────────────
Make (Makefile):
```makefile
all: results figures paper

data/clean_data.csv: data/raw_data.csv scripts/clean.R
    Rscript scripts/clean.R

results/analysis.rds: data/clean_data.csv scripts/analyze.R
    Rscript scripts/analyze.R

figures/figure1.png: results/analysis.rds scripts/plot.R
    Rscript scripts/plot.R

paper: paper/manuscript.Rmd results/analysis.rds
    Rscript -e "rmarkdown::render('paper/manuscript.Rmd')"
```

Alternatives:
- Snakemake (Python)
- targets (R)
- Nextflow (bioinformatics)
- Drake (R, older)
```

---

## Phase 4: Replication

### Replication Study Design

```
REPLICATION FRAMEWORK

TYPES OF REPLICATION
─────────────────────────────────────────
Direct replication:
- Same methods, new sample
- Tests whether effect is reproducible
- Closest to original study

Conceptual replication:
- Different methods, same construct
- Tests whether theory generalizes
- Different operationalizations

Systematic replication:
- Varies specific features
- Identifies boundary conditions
- Explores moderators

Extension:
- Replicates + extends
- Adds new conditions/measures
- Builds on original

REPLICATION STUDY DESIGN
─────────────────────────────────────────
Step 1: Select study to replicate
Criteria for selection:
□ Important finding
□ Methods clearly reported
□ Materials available (or obtainable)
□ Feasible to conduct
□ Replication would be informative

Step 2: Obtain original materials
□ Contact original authors
□ Request materials and data
□ Clarify any ambiguities
□ Get original analysis code if possible

Step 3: Design replication
□ Match original as closely as possible
□ Document any necessary changes
□ Justify any deviations
□ Plan for adequate power

Step 4: Preregister
□ Register replication plan
□ Specify criteria for "successful" replication
□ Plan analyses in advance

Step 5: Conduct study
□ Follow protocol precisely
□ Document any deviations
□ Collect data
□ Analyze as planned

Step 6: Report results
□ Compare to original
□ Report both original and replication statistics
□ Discuss consistency/inconsistency
□ Interpret appropriately

SAMPLE SIZE FOR REPLICATION
─────────────────────────────────────────
Small samples may "fail" due to noise, not because
effect doesn't exist.

Approaches:
1. Power for small effect
   - Assume effect smaller than original
   - Original may be inflated
   - Power for 50% of original effect

2. Target precision
   - Determine desired CI width
   - Calculate N for that precision

3. Small telescopes
   - Simonsohn's approach
   - What effect would original detect 33%?
   - Power replication to detect that effect

INTERPRETING REPLICATION RESULTS
─────────────────────────────────────────
Comparing results:
□ Effect in same direction?
□ Effect size similar?
□ Confidence intervals overlap?
□ Statistical significance?

Decision matrix:
| Original | Replication | Interpretation |
|----------|-------------|----------------|
| Sig + | Sig + | Replicated |
| Sig + | Sig - | Opposite! Investigate |
| Sig + | Non-sig, same direction | Uncertain |
| Sig + | Non-sig, opposite | Did not replicate |

Important:
- "Did not replicate" ≠ "Effect doesn't exist"
- Consider power, differences, context
- Multiple replications more informative
```

### Multi-Site Replication

```
MULTI-SITE REPLICATION

MANY LABS APPROACH
─────────────────────────────────────────
Concept: Multiple independent labs conduct
same replication simultaneously.

Benefits:
□ Tests replicability across contexts
□ High statistical power (pooled)
□ Identifies site-level moderators
□ Strong evidence either way
□ Efficient use of resources

Design considerations:
□ Standardized protocol essential
□ Central coordination
□ Training for all sites
□ Quality control procedures
□ Pre-specified analysis plan

COORDINATION STRUCTURE
─────────────────────────────────────────
Central team:
- Protocol development
- Materials distribution
- Training provision
- Data management
- Analysis and reporting

Site requirements:
- Local ethics approval
- Certified staff
- Protocol adherence
- Data submission
- Quality standards

PROTOCOL STANDARDIZATION
─────────────────────────────────────────
What must be identical:
□ Core procedures
□ Key measures
□ Essential instructions
□ Critical timing

What may vary:
□ Language (translation protocol)
□ Local consent procedures
□ Participant compensation
□ Setting details

Documentation:
□ Master protocol
□ Site-specific adaptations
□ Translation procedures
□ Training materials
□ Fidelity checklists

ANALYSIS APPROACH
─────────────────────────────────────────
Pooled analysis:
- Combine data across sites
- Meta-analytic approach
- Random effects for site

Site-level analysis:
- Estimate effect per site
- Compare across sites
- Heterogeneity assessment

Moderator analysis:
- Site-level characteristics
- Sample characteristics
- Procedural variations
```

---

## Phase 5: Transparency Reporting

### Transparency Checklist

```
TRANSPARENCY STANDARDS

21-WORD SOLUTION
─────────────────────────────────────────
Include in every empirical paper:
"We report how we determined our sample size,
all data exclusions (if any), all manipulations,
and all measures in the study."

TRANSPARENCY CHECKLIST
─────────────────────────────────────────
Study Design:
□ Design clearly described
□ Sample size determination explained
□ Data collection stopping rule stated
□ All conditions/groups reported

Data:
□ Data exclusions reported with rationale
□ All exclusion criteria stated in advance
□ Missing data handling explained
□ Data available or explanation for restrictions

Materials:
□ All materials available or described
□ All measures reported
□ All manipulations described
□ Stimuli available or described

Analysis:
□ All analyses reported (including non-significant)
□ Analysis approach justified
□ Deviations from preregistration noted
□ Exploratory analyses labeled as such

Disclosure:
□ Preregistration status stated
□ Prior presentations/publications noted
□ Funding sources disclosed
□ Conflicts of interest disclosed

DISCLOSURE STATEMENT TEMPLATE
─────────────────────────────────────────
"We report all measures, manipulations, and
exclusions in this study. Sample size was
determined [before/after] data collection based
on [power analysis/practical constraints/etc.].
[This study was/was not] preregistered at [URL].
[Data/Materials/Code] are available at [URL].
[The authors have no/The following] conflicts
of interest to disclose: [list]."

REPORTING GUIDELINES BY FIELD
─────────────────────────────────────────
Psychology:
- JARS (APA)
- TOP Guidelines

Medicine/Health:
- CONSORT (trials)
- STROBE (observational)
- PRISMA (systematic reviews)
- SPIRIT (protocols)

Qualitative:
- COREQ
- SRQR

General:
- EQUATOR Network (equator-network.org)
- Check journal requirements
```

### Open Science Badges

```
OPEN SCIENCE BADGES

COS BADGES
─────────────────────────────────────────
Open Data Badge:
□ Data publicly available
□ Sufficient for reproducing results
□ Available at persistent URL
□ Described in sufficient detail

Open Materials Badge:
□ Materials publicly available
□ Sufficient for replication
□ Available at persistent URL
□ Described in sufficient detail

Preregistered Badge:
□ Study preregistered
□ Preregistration at recognized registry
□ Registration preceded data collection
□ Full report matches preregistration

Preregistered + Analysis Plan Badge:
□ All above, plus
□ Analysis plan in preregistration
□ Results follow plan
□ Deviations documented

HOW TO EARN BADGES
─────────────────────────────────────────
Step 1: Meet criteria
- Share data/materials at stable location
- Use recognized platform
- Ensure accessibility

Step 2: Self-certify
- Complete disclosure form
- Provide URLs/DOIs
- Attest to meeting criteria

Step 3: Journal verification
- Editor/reviewer confirms
- Badge awarded at publication

Badge URL locations:
- OSF projects
- Zenodo
- Figshare
- Institutional repositories
- Dataverse

BADGE STATEMENT EXAMPLES
─────────────────────────────────────────
Open Data:
"Data are available at [DOI]. [Codebook/documentation]
is provided at [DOI]."

Open Materials:
"All materials necessary for replication are
available at [DOI]."

Preregistration:
"This study was preregistered at [registry] on
[date] prior to data collection. The registration
is available at [DOI]."

BENEFITS OF BADGES
─────────────────────────────────────────
For researchers:
□ Signal rigor and transparency
□ Increase citations (evidence suggests)
□ Build reputation for openness

For science:
□ Normalize open practices
□ Enable verification
□ Accelerate progress
□ Reduce waste
```

### Open Access

```
OPEN ACCESS PUBLISHING

OA TYPES
─────────────────────────────────────────
Gold OA:
- Published openly by journal
- Usually with Article Processing Charge (APC)
- Immediate access

Green OA:
- Self-archiving
- Preprint or postprint
- May have embargo

Diamond OA:
- No APC, fully open
- Funded by institutions/societies

Hybrid:
- Subscription journal
- OA option for extra fee
- Controversial ("double dipping")

PREPRINT STRATEGY
─────────────────────────────────────────
What is a preprint:
- Manuscript posted before peer review
- Typically on preprint server
- Not yet peer-reviewed

Benefits:
□ Immediate dissemination
□ Establishes priority
□ Enables feedback
□ Increases citations
□ Satisfies some funder requirements

Preprint servers:
- arXiv (physics, math, CS)
- bioRxiv (biology)
- medRxiv (medicine)
- PsyArXiv (psychology)
- SocArXiv (social sciences)
- OSF Preprints (general)
- SSRN (social sciences)

FUNDER REQUIREMENTS
─────────────────────────────────────────
Many funders now require OA:

NIH:
- Public Access Policy
- Must be in PubMed Central
- Within 12 months of publication

NSF:
- Public access required
- Various mechanisms acceptable

Plan S (Europe):
- Immediate OA required
- No embargo period
- Specific journal compliance

Check:
□ Funder policy
□ Institution policy
□ Journal policy
□ Compliance mechanism

RIGHTS RETENTION
─────────────────────────────────────────
Retain rights to share your work:
□ Author addendum to publishing agreement
□ Rights retention statement in paper
□ Know what rights you're signing away
□ Consider OA-friendly journals

Rights retention statement:
"For the purpose of open access, the author has
applied a CC BY public copyright license to any
Author Accepted Manuscript version arising from
this submission."
```

---

## Integration Patterns

### With Research Agents

- **research-architect**: Integrates preregistration into design
- **methodology-advisor**: Ensures analysis plan is complete
- **publication-strategist**: Coordinates OA and sharing strategy
- **peer-review-responder**: Addresses transparency in revisions

### With Other Skills

- **data-management**: Coordinates data sharing
- **research-writing**: Integrates disclosure statements
- **grant-writing**: Addresses reproducibility in proposals

---

## Output Artifacts

1. **Preregistration Document**: Complete study plan
2. **Materials Package**: Shareable research materials
3. **Code Repository**: Documented, runnable code
4. **Replication Protocol**: Detailed replication design
5. **Transparency Statement**: Disclosure documentation
6. **Open Science Checklist**: Compliance verification

---

## Quality Criteria

Reproducibility practices are successful when:

1. **Transparent**: All decisions documented
2. **Accessible**: Materials available to others
3. **Complete**: All necessary components shared
4. **Usable**: Others can actually reproduce
5. **Credible**: Practices signal rigor
6. **Sustainable**: Practices are maintainable

---

## Warnings

- Preregistration requires planning—start early
- Sharing takes preparation time—budget for it
- Not all data can be shared—know the limits
- Reproducibility ≠ correctness
- Perfect is enemy of good—share what you can
- Keep updated as standards evolve

---

## Learn More

- Open Science Framework: osf.io
- Center for Open Science: cos.io
- TOP Guidelines: cos.io/top
- Reproducibility guides: reproducibleresearch.net
- The Turing Way: the-turing-way.netlify.app
- FORRT: forrt.org
