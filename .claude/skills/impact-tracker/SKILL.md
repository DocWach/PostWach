# Impact Tracker Skill

## Overview

The Impact Tracker skill provides comprehensive workflows for monitoring, analyzing, and reporting scholarly impact across multiple dimensions. This skill helps researchers understand how their work is being received, cited, and used, informing strategic decisions about research direction and dissemination.

## Capabilities

- Citation tracking and analysis
- Altmetric monitoring
- Research profile management
- Impact reporting
- Benchmarking and comparison
- Portfolio impact assessment

---

## Phase 1: Impact Monitoring Setup

### Profile Configuration

```
RESEARCHER PROFILE SETUP

ESSENTIAL PROFILES
─────────────────────────────────────────
□ ORCID (orcid.org)
  - Universal researcher identifier
  - Links to all profiles and publications
  - Required by many funders/journals
  - Set up: Register → Claim works → Connect profiles

□ Google Scholar Profile
  - Most comprehensive citation tracking
  - Free, easy setup
  - Includes h-index, i10-index
  - Set up: Sign in → Create profile → Verify publications

□ Institutional Profile
  - University research page
  - May feed into reporting systems
  - Keep updated for visibility
  - Contact: Research office or web team

DISCIPLINE-SPECIFIC PROFILES
─────────────────────────────────────────
Sciences/Engineering:
□ Web of Science ResearcherID
□ Scopus Author ID
□ PubMed Author ID (for biomedical)

Social Sciences:
□ SSRN Author Page
□ ResearchGate Profile
□ Academia.edu Profile

Computer Science:
□ DBLP Profile
□ ACM Author Profile
□ Semantic Scholar Profile

Humanities:
□ PhilPapers Profile (philosophy)
□ Academia.edu Profile
□ Humanities Commons

PROFILE MAINTENANCE SCHEDULE
─────────────────────────────────────────
Monthly:
□ Check Google Scholar for new citations
□ Review altmetrics on recent publications
□ Claim any unclaimed publications

Quarterly:
□ Update all profiles with new publications
□ Verify ORCID completeness
□ Check for duplicate author profiles
□ Review co-author connections

Annually:
□ Audit all profiles for accuracy
□ Update professional photo if needed
□ Refresh biographical statements
□ Export metrics for reporting
□ Archive annual metrics snapshot
```

### Tracking Dashboard Setup

```
IMPACT TRACKING DASHBOARD

PUBLICATION TRACKING TABLE
─────────────────────────────────────────
For each publication, track:

| Pub | Year | Venue | GS Cites | WoS | Scopus | Altmetric |
|-----|------|-------|----------|-----|--------|-----------|
| P1  | 2023 | J1    | ##       | ##  | ##     | ##        |
| P2  | 2022 | C1    | ##       | ##  | ##     | ##        |
| ... | ...  | ...   | ...      | ... | ...    | ...       |

Update frequency: Monthly

CITATION VELOCITY TRACKING
─────────────────────────────────────────
Track citations over time for key papers:

Paper: [Title]
| Month | Cumulative | New This Month | Notes |
|-------|------------|----------------|-------|
| M1    | 0          | 0              | Published |
| M2    | 2          | 2              | |
| M3    | 5          | 3              | |
| M6    | 15         | 3 (avg)        | |
| M12   | 45         | 2.5 (avg)      | |
| M24   | 110        | 2.7 (avg)      | |

Compare against field averages:
- Top 10% in field by [month]: ## citations
- Average in field by [month]: ## citations

ALTMETRIC TRACKING
─────────────────────────────────────────
For each publication:

Social media:
□ Twitter/X mentions: ##
□ Facebook shares: ##
□ LinkedIn posts: ##

News and media:
□ News mentions: ##
□ Blog posts: ##
□ Wikipedia references: ##

Academic social:
□ Mendeley readers: ##
□ ResearchGate reads: ##
□ Downloads: ##

Policy impact:
□ Policy document citations: ##
□ Patent citations: ##

Altmetric Attention Score: ##
Percentile: Top ##%
```

---

## Phase 2: Citation Analysis

### Citation Metrics Reference

```
CITATION METRICS GUIDE

AUTHOR-LEVEL METRICS
─────────────────────────────────────────
h-index
- Definition: h papers with ≥h citations each
- Example: h=20 means 20 papers with ≥20 citations
- Source: Google Scholar, Web of Science, Scopus
- Strengths: Balances productivity and impact
- Limitations: Field-dependent, favors seniority

i10-index
- Definition: Number of publications with ≥10 citations
- Source: Google Scholar
- Strengths: Simple, intuitive
- Limitations: Arbitrary threshold

Total citations
- Definition: Sum of all citations received
- Source: All major databases
- Strengths: Comprehensive measure
- Limitations: Inflated by one highly-cited paper

m-quotient
- Definition: h-index / years since first publication
- Interpretation: h-index growth rate
- Strengths: Accounts for career length
- Limitations: Penalizes career breaks

g-index
- Definition: g papers with average ≥g citations
- Interpretation: Rewards highly-cited papers more
- Strengths: More sensitive to very high citations
- Limitations: Less widely used

PUBLICATION-LEVEL METRICS
─────────────────────────────────────────
Citation count
- Raw number of times cited
- Varies by database
- Accumulates over time
- Benchmark against field

Field-Weighted Citation Impact (FWCI)
- Scopus metric
- 1.0 = world average
- >1.0 = above average for field
- Accounts for field differences

Relative Citation Ratio (RCR)
- NIH metric for biomedical
- 1.0 = average for field
- Based on co-citation network
- iCite tool (NIH)

Percentile ranking
- Where paper ranks in field
- Top 1%, 10%, 25%, 50%
- More intuitive than raw counts
- Available in Scopus, WoS

INTERPRETING METRICS RESPONSIBLY
─────────────────────────────────────────
Remember:
□ Metrics vary dramatically by field
□ Compare within field, not across
□ Quality ≠ quantity
□ Gaming is possible and detected
□ Single metric never tells full story
□ Context matters (career stage, resources)
□ Negative citations still count
□ Self-citations may be excluded

Field benchmarks (very rough):
| Field | "Good" h-index at tenure |
|-------|--------------------------|
| Biomedical | 15-25 |
| Physical sciences | 12-20 |
| Engineering | 10-18 |
| Social sciences | 8-15 |
| Humanities | 5-12 |
| Computer science | 15-30 |

Note: These vary enormously by subfield
```

### Citation Analysis Workflow

```
CITATION ANALYSIS PROCESS

QUANTITATIVE ANALYSIS
─────────────────────────────────────────
Step 1: Gather citation data
Sources to check:
□ Google Scholar (most comprehensive)
□ Web of Science (more selective)
□ Scopus (broader than WoS)
□ Field-specific (DBLP, PubMed, etc.)

Note: Numbers will differ across sources

Step 2: Calculate metrics
□ Total citations (all publications)
□ h-index
□ i10-index
□ Average citations per paper
□ Citation distribution (how skewed?)

Step 3: Trend analysis
□ Year-over-year citation growth
□ Citation velocity for recent papers
□ Which papers are gaining momentum?
□ Any papers with declining citations?

Step 4: Benchmarking
□ Compare to field averages
□ Compare to peer researchers
□ Compare to career stage expectations
□ Identify over/under-performing papers

QUALITATIVE CITATION ANALYSIS
─────────────────────────────────────────
Who is citing your work?

Citation network analysis:
□ Which institutions cite you?
□ Which countries?
□ Which journals/venues?
□ Which research groups?
□ Any unexpected communities?

How is your work being cited?

Citation context analysis:
For key papers, read citing papers to understand:
□ Used as foundational reference
□ Extended/built upon
□ Methodological citation
□ Contradicted/critiqued
□ Background/context citation
□ Compared against

Impact pathways:
□ Are your concepts being adopted?
□ Are your methods being replicated?
□ Is terminology spreading?
□ Are findings influencing practice?

CITATION ANALYSIS REPORT TEMPLATE
─────────────────────────────────────────
# Citation Analysis: [Date]

## Summary Metrics
- Total publications: ##
- Total citations: ##
- h-index: ##
- i10-index: ##
- Average citations/paper: ##

## Trends
- Citations this year: ##
- Growth rate: ##% YoY
- Most cited paper: [Title] (## citations)
- Fastest growing: [Title] (## new this quarter)

## Qualitative Insights
- Primary citing communities: [list]
- Citation types: [foundational, methodological, etc.]
- Emerging impact areas: [list]

## Action Items
- Papers to promote: [list]
- Research directions gaining traction: [list]
- Potential collaborators identified: [list]
```

### Self-Citation Guidelines

```
SELF-CITATION BEST PRACTICES

LEGITIMATE SELF-CITATION
─────────────────────────────────────────
Appropriate when:
□ Building directly on prior work
□ Avoiding redundancy in methods/theory
□ Directing readers to fuller treatments
□ Establishing research program coherence
□ Citing relevant prior findings

CONCERNING PATTERNS
─────────────────────────────────────────
Red flags:
□ Self-citations >30% of references
□ Citing tangentially related own work
□ Citation circles with collaborators
□ Strategic citation to boost metrics
□ Citing own work when better alternatives exist

BEST PRACTICES
─────────────────────────────────────────
□ Self-cite only when genuinely relevant
□ Consider: Would reviewer question this?
□ Balance self-citation with others' work
□ Don't avoid legitimate self-citation
□ Be aware some metrics exclude self-citations

SELF-CITATION AUDIT
─────────────────────────────────────────
For each of your papers:
- Total references: ##
- Self-citations: ##
- Self-citation rate: ##%
- Justifiable self-citations: ##
- Could be replaced: ##

Target: <15-20% self-citation rate is typical
```

---

## Phase 3: Altmetric Monitoring

### Altmetric Tracking Framework

```
ALTMETRIC MONITORING

WHAT ALTMETRICS CAPTURE
─────────────────────────────────────────
Social media attention:
├── Twitter/X mentions and retweets
├── Facebook shares and posts
├── LinkedIn posts
├── Reddit discussions
└── YouTube references

News and media:
├── News outlet mentions
├── Magazine articles
├── Blog posts
└── Newsletter features

Academic social:
├── Mendeley readers
├── CiteULike bookmarks
├── ResearchGate engagement
└── Academia.edu views

Policy and practice:
├── Policy document citations
├── Clinical guideline references
├── Patent citations
└── Syllabi mentions

Reference management:
├── Mendeley reader counts
├── F1000 recommendations
└── Wikipedia references

ALTMETRIC TOOLS
─────────────────────────────────────────
Altmetric.com
- Tracks attention across sources
- Provides attention score
- Contextual percentiles
- Free bookmarklet for checking papers

PlumX (Plum Analytics)
- Five categories: Citations, Usage, Captures,
  Mentions, Social Media
- Institutional dashboards
- Integrated with Scopus

Dimensions
- Combines citations with altmetrics
- Free version available
- Policy citations tracking

ImpactStory
- Open source
- ORCID integration
- Personal profile dashboards

ALTMETRIC MONITORING WORKFLOW
─────────────────────────────────────────
Set up alerts:
□ Google Alerts for paper titles
□ Twitter notifications for mentions
□ Altmetric alerts for DOIs
□ Google Scholar alerts

Weekly check:
□ Review new mentions
□ Engage with meaningful discussions
□ Correct misinformation if needed
□ Thank promoters when appropriate

Monthly analysis:
□ Which papers getting attention?
□ What types of attention?
□ Any viral moments?
□ Patterns in who's sharing?

INTERPRETING ALTMETRICS
─────────────────────────────────────────
High altmetrics may indicate:
+ Broad accessibility/interest
+ Policy relevance
+ Teaching utility
+ Media newsworthiness
+ Public engagement

Low altmetrics don't necessarily mean:
- Low quality
- Low academic impact
- Irrelevance
(Some excellent work has niche audiences)

Altmetrics vs. citations:
- Altmetrics: Early attention (days-weeks)
- Citations: Academic impact (months-years)
- Both valuable, measure different things
```

### Social Media for Research

```
RESEARCH SOCIAL MEDIA STRATEGY

PLATFORM SELECTION
─────────────────────────────────────────
Twitter/X (Academic Twitter)
- Best for: Real-time discussion, networking
- Content: Paper threads, commentary, live-tweeting
- Audience: Academics, journalists, public

LinkedIn
- Best for: Professional networking, industry reach
- Content: Publications, career news, insights
- Audience: Professional, cross-sector

ResearchGate
- Best for: Academic networking, paper sharing
- Content: Publications, questions, projects
- Audience: Researchers specifically

Mastodon (Academic instances)
- Best for: Twitter alternative
- Content: Similar to Twitter
- Audience: Growing academic community

YouTube/TikTok
- Best for: Explainer content
- Content: Video abstracts, tutorials
- Audience: Broader public, students

PAPER PROMOTION TEMPLATE
─────────────────────────────────────────
Twitter thread format:

Tweet 1 (Hook):
"New paper out! We found [key finding] 🧵

[Engaging summary of main result]

[Link to paper]"

Tweet 2 (Problem):
"The problem: [What question we addressed]"

Tweet 3 (Approach):
"We [methodology] using [data/approach]"

Tweet 4-5 (Key findings):
"Key finding 1: [result]"
"Key finding 2: [result]"

Tweet 6 (Implications):
"This means [so what?]"

Tweet 7 (Call to action):
"Paper is open access here: [link]
Would love to hear your thoughts!

Thanks to [coauthors, funders]"

Best practices:
□ Include visual (figure, graphical abstract)
□ Tag co-authors
□ Use relevant hashtags (not too many)
□ Post when audience is active
□ Engage with replies
□ Thread for longer content

ENGAGEMENT GUIDELINES
─────────────────────────────────────────
Do:
✓ Share others' work generously
✓ Engage substantively with discussions
✓ Acknowledge limitations in your work
✓ Be collegial and professional
✓ Give credit appropriately
✓ Correct errors graciously

Don't:
✗ Only self-promote
✗ Engage in flame wars
✗ Overstate findings
✗ Post angry or political rants (on research account)
✗ Ignore legitimate critique
✗ Ghost after posting
```

---

## Phase 4: Impact Reporting

### Impact Report Templates

```
IMPACT REPORT FORMATS

ANNUAL IMPACT SUMMARY
─────────────────────────────────────────
# Annual Research Impact Report: [Year]

## Publication Metrics
- Papers published: ##
- Total citations (all time): ##
- New citations this year: ##
- h-index: ## (Δ+# from last year)

## Impact Highlights

### Most Cited Papers
1. [Title] – ## citations (## new this year)
2. [Title] – ## citations
3. [Title] – ## citations

### Emerging Impact
- [Paper] gaining traction in [community]
- [Paper] cited in [policy document/media]
- [Paper] used in [practical application]

### Broader Impact
- Media mentions: ##
- Policy citations: ##
- Teaching uses: ##
- Industry applications: [describe]

## Research Influence
- New collaborations established: ##
- Invited talks: ##
- Keynote addresses: ##
- Editorial roles: [list]

## Goals for Next Year
1. [Goal 1]
2. [Goal 2]
3. [Goal 3]

GRANT REPORTING FORMAT
─────────────────────────────────────────
# Research Outputs and Impact: [Grant Name]

## Publications
| # | Authors | Year | Title | Venue | Status | DOI |
|---|---------|------|-------|-------|--------|-----|
| 1 | | | | | Published | |
| 2 | | | | | In press | |
| 3 | | | | | Under review | |

## Citation Impact
- Total citations from grant publications: ##
- Average citations per paper: ##
- Most cited: [Title] (## citations)

## Broader Impacts
- Students trained: ##
- Presentations: ##
- Media coverage: [list]
- Practice/policy influence: [describe]
- Data/tools released: [list]
- Community engagement: [describe]

## Intellectual Merit Evidence
- Novel contributions: [describe]
- Field advancement: [describe]
- Future research enabled: [describe]

TENURE/PROMOTION DOSSIER FORMAT
─────────────────────────────────────────
# Research Impact Statement

## Publication Record
- Total peer-reviewed publications: ##
- First-authored publications: ##
- Publications since [appointment/last review]: ##

## Citation Impact
- Total citations: ## (Source: Google Scholar/WoS)
- h-index: ##
- i10-index: ##

## Evidence of Impact

### Highly Cited Works
[List top 5-10 with citation counts and significance]

### Invited Contributions
- Review articles: ##
- Book chapters: ##
- Encyclopedia entries: ##

### Recognition
- Awards: [list]
- Invited talks: ## (international: ##)
- Keynotes: ##

### Influence on Field
- [Description of how work has shaped the field]
- [Evidence: citations to specific papers, adoptions]

### Broader Impact
- Policy influence: [describe]
- Practice adoption: [describe]
- Media coverage: [describe]
- Public engagement: [describe]

## External Validation
[Letters from field leaders addressing impact]
```

### Benchmarking Framework

```
IMPACT BENCHMARKING

PEER COMPARISON ANALYSIS
─────────────────────────────────────────
Select 5-10 peer researchers:
- Similar career stage
- Similar research area
- Mix of institutions

For each peer, gather:
□ h-index
□ Total citations
□ Publications in past 5 years
□ Citations in past 5 years

Comparison table:
| Name | h-index | Total Cites | Pubs (5yr) | Cites (5yr) |
|------|---------|-------------|------------|-------------|
| Self | ## | ## | ## | ## |
| Peer 1 | ## | ## | ## | ## |
| Peer 2 | ## | ## | ## | ## |
| ... | ... | ... | ... | ... |
| Average | ## | ## | ## | ## |
| Median | ## | ## | ## | ## |

Interpretation:
- Above median: [which metrics]
- Below median: [which metrics]
- Unique strengths: [describe]

FIELD BENCHMARKING
─────────────────────────────────────────
Use field-normalized metrics:
□ FWCI (Field-Weighted Citation Impact)
□ Percentile rankings
□ Field-specific indices

Resources:
- Scopus SciVal (institutional access)
- Web of Science InCites (institutional access)
- NIH iCite (biomedical)
- Google Scholar field rankings

Benchmark questions:
□ What h-index is typical for tenure in my field?
□ What citations does a "successful" paper get?
□ How does my productivity compare?
□ How does my impact compare?

CAREER TRAJECTORY ANALYSIS
─────────────────────────────────────────
Track your metrics over time:

Year | h-index | Total Cites | Pubs | Notes
-----|---------|-------------|------|------
Y1   | #       | #           | #    |
Y2   | #       | #           | #    |
Y3   | #       | #           | #    |
...  | ...     | ...         | ...  |

Calculate:
- Average h-index growth per year
- Average citations per year
- Productivity trend
- Impact trend

Project forward:
- At current rate, h-index in 5 years: ##
- Needed rate for target: ## per year
```

---

## Phase 5: Strategic Impact Enhancement

### Impact Optimization Strategies

```
IMPACT ENHANCEMENT TACTICS

PRE-PUBLICATION
─────────────────────────────────────────
□ Post preprint for early visibility
□ Present at conferences before publication
□ Build anticipation in research community
□ Prepare promotional materials

AT PUBLICATION
─────────────────────────────────────────
□ Social media announcement (threaded)
□ Email to key contacts
□ Add to all profiles immediately
□ Notify institutional communications
□ Visual abstract or infographic
□ Blog post or lay summary
□ Video abstract (if platform supports)

POST-PUBLICATION
─────────────────────────────────────────
□ Conference presentations
□ Webinars and invited talks
□ Engage with citing authors
□ Respond to questions/comments
□ Update Wikipedia if appropriate
□ Write for practitioner outlets
□ Media outreach (if newsworthy)

ONGOING
─────────────────────────────────────────
□ Cite your own work appropriately
□ Build on published work (creates citations)
□ Collaborate with researchers who might cite
□ Make work accessible (OA, repositories)
□ Keep profiles updated
□ Network at conferences

TITLE AND ABSTRACT OPTIMIZATION
─────────────────────────────────────────
For discoverability:
□ Keywords in title
□ Searchable abstract
□ Clear contribution statement
□ Avoid excessive jargon
□ Descriptive over clever

COLLABORATION FOR IMPACT
─────────────────────────────────────────
Strategic collaboration benefits:
+ Access to different networks
+ Cross-citation potential
+ Broader dissemination reach
+ Different expertise areas
+ Geographic diversity

Consider collaborators':
□ Citation networks
□ Social media presence
□ Field connections
□ Institutional reach
```

### Impact Narrative Development

```
CRAFTING YOUR IMPACT STORY

BEYOND THE NUMBERS
─────────────────────────────────────────
Metrics alone don't tell the story.
Develop narrative around:

Research significance:
- What problems does your work address?
- What has changed because of your research?
- Who has benefited and how?

Intellectual contribution:
- How has the field been shaped by your work?
- What new directions have opened?
- What debates has your work influenced?

Practical impact:
- How has practice changed?
- What tools/methods have been adopted?
- What policies have been influenced?

Training impact:
- Students and postdocs mentored
- Skills and methods transmitted
- Academic placements of mentees

EVIDENCE COLLECTION
─────────────────────────────────────────
Document evidence of impact:
□ Testimonials from users of your work
□ Adoption documentation
□ Policy citations
□ Media coverage clips
□ Invitation letters (talks, reviews)
□ Award nominations and letters
□ Course syllabi featuring your work
□ Practitioner implementations

IMPACT STATEMENT TEMPLATE
─────────────────────────────────────────
My research on [topic] has contributed to [field]
by [key contribution].

This work has been recognized through [# citations,
awards, etc.].

Beyond academic impact, this research has [practical
impact]: [specific examples].

Looking forward, this work enables [future directions]
and positions [research group/institution] as [status].
```

---

## Integration Patterns

### With Research Agents

- **publication-strategist**: Uses impact data for venue selection
- **peer-review-responder**: Cites impact in revision responses
- **literature-reviewer**: Identifies highly-cited relevant works

### With Other Skills

- **research-roadmapping**: Integrates impact goals into planning
- **grant-writing**: Provides impact evidence for proposals
- **research-writing**: Informs writing for discoverability

---

## Output Artifacts

1. **Profile Audit Report**: Status of all research profiles
2. **Citation Analysis**: Detailed metrics and trends
3. **Altmetric Dashboard**: Attention tracking across sources
4. **Impact Report**: Formatted reports for various purposes
5. **Benchmark Analysis**: Comparison with peers and field
6. **Impact Narrative**: Qualitative impact story

---

## Quality Criteria

Impact tracking is successful when:

1. **Comprehensive**: All publications tracked across sources
2. **Accurate**: Data verified and current
3. **Contextualized**: Metrics interpreted appropriately
4. **Actionable**: Insights inform strategic decisions
5. **Honest**: Limitations acknowledged
6. **Sustainable**: Regular monitoring without obsession

---

## Warnings

- Don't obsess over metrics daily—check monthly
- Recognize that metrics are imperfect proxies
- Don't compare across fields
- Be cautious about gaming metrics
- Remember: Not all valuable work is highly cited
- Impact takes time—be patient with new work
- Quality and significance matter more than numbers

---

## Learn More

- Sugimoto, C.R. & Larivière, V. (2018). Measuring Research
- Hicks, D. et al. (2015). Bibliometrics: The Leiden Manifesto
- DORA Declaration: sfdora.org
- Responsible Metrics: responsiblemetrics.org
- Altmetric: altmetric.com/about-altmetrics
