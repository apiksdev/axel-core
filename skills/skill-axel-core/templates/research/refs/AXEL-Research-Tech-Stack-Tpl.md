---
name: research-tech-stack
description: Template for technology stack research - library/framework comparison and evaluation
type: template
---

# AXEL Template: Research - Tech Stack

```xml
<document type="template">

  <enforcement>
    <![CDATA[
    - Output is Pure Markdown (no XML in generated file)
    - Save to .claude/research/{topic-kebab-case}.md
    - Include all required sections
    - Cite sources properly
    ]]>
  </enforcement>

  <objective>
    Template for technology stack research.
    Compares libraries, frameworks, and technologies.
    Provides pros/cons analysis and recommendations.
  </objective>

  <output-template>
    <![CDATA[
---
name: {topic-kebab-case}
description: {brief description}
type: research
research_type: technical
status: in-progress
created_at: {YYYY-MM-DD}
updated_at: {YYYY-MM-DD}
---

# Research: {Topic Title}

## Context

**Background:**
{Why this research is needed}

**Scope:**
- {What is included in this research}
- {Boundaries and limitations}

**Stakeholders:**
- {Who will benefit from this research}

## Questions

**Primary Questions:**
1. {Main question to answer}
2. {Second main question}

**Secondary Questions:**
- {Additional question}
- {Supporting question}

## Methodology

**Research Approach:**
- {How the research will be conducted}
- {Sources to consult}

**Evaluation Criteria:**
| Criteria | Weight | Description |
|----------|--------|-------------|
| {Criteria 1} | {High/Medium/Low} | {What it measures} |
| {Criteria 2} | {Weight} | {Description} |

## Findings

### Option A: {Technology/Library Name}

**Overview:**
{Brief description of the technology}

**Pros:**
- {Advantage 1}
- {Advantage 2}

**Cons:**
- {Disadvantage 1}
- {Disadvantage 2}

**Best For:**
{Use cases where this option excels}

### Option B: {Technology/Library Name}

**Overview:**
{Brief description}

**Pros:**
- {Advantage 1}
- {Advantage 2}

**Cons:**
- {Disadvantage 1}
- {Disadvantage 2}

**Best For:**
{Use cases}

### Comparison Matrix

| Feature | Option A | Option B | Option C |
|---------|----------|----------|----------|
| {Feature 1} | {Value} | {Value} | {Value} |
| {Feature 2} | {Value} | {Value} | {Value} |

## Analysis

**Key Insights:**
1. {Major finding 1}
2. {Major finding 2}

**Trade-offs:**
- {Trade-off consideration 1}
- {Trade-off consideration 2}

**Risk Assessment:**
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| {Risk 1} | {L/M/H} | {L/M/H} | {Strategy} |

## Recommendations

**Primary Recommendation:**
{Recommended option with rationale}

**Alternative Recommendation:**
{When to choose a different option}

**Implementation Guidance:**
1. {Step 1}
2. {Step 2}
3. {Step 3}

**Migration Path (if applicable):**
- {How to migrate from current to recommended}

## Sources

**Official Documentation:**
- [{Name}]({URL})

**Articles & Tutorials:**
- [{Title}]({URL})

**Benchmarks & Comparisons:**
- [{Source}]({URL})

**Community Resources:**
- [{Resource}]({URL})
    ]]>
  </output-template>

  <understanding/>

</document>
```
