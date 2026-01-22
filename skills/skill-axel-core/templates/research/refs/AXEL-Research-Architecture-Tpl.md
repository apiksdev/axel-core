---
name: research-architecture
description: Template for architecture research - codebase analysis, design patterns, and structure
type: template
---

# AXEL Template: Research - Architecture

```xml
<document type="template">

  <enforcement>
    <![CDATA[
    - Output is Pure Markdown (no XML in generated file)
    - Save to .claude/research/{topic-kebab-case}.md
    - Include all required sections
    - Reference codebase files with @ prefix
    ]]>
  </enforcement>

  <objective>
    Template for architecture and codebase research.
    Analyzes code patterns, design decisions, and structure.
    Provides insights for refactoring and improvement.
  </objective>

  <output-template>
    <![CDATA[
---
name: {topic-kebab-case}
description: {brief description}
type: research
research_type: codebase
status: in-progress
created_at: {YYYY-MM-DD}
updated_at: {YYYY-MM-DD}
---

# Research: {Topic Title}

## Context

**Background:**
{Why this architecture research is needed}

**Scope:**
- {Components/modules to analyze}
- {Boundaries and exclusions}

**Goals:**
- {What insights we want to gain}
- {Decisions to inform}

## Questions

**Primary Questions:**
1. {Main architectural question}
2. {Second main question}

**Secondary Questions:**
- {Supporting question}
- {Detail question}

## Methodology

**Analysis Approach:**
- Static code analysis
- Dependency mapping
- Pattern recognition
- Design document review

**Tools Used:**
- {Tool 1}
- {Tool 2}

## Findings

### Current Architecture Overview

**High-Level Structure:**
{Description of the overall architecture}

{{{mermaid}}}
graph TD
    A[Component A] --> B[Component B]
    B --> C[Component C]
{{{mermaid}}}

**Key Components:**

| Component | Purpose | Dependencies |
|-----------|---------|--------------|
| {Name} | {What it does} | {What it depends on} |

### Design Patterns Identified

**Pattern 1: {Pattern Name}**
- Location: `{file/folder path}`
- Usage: {How it's used}
- Effectiveness: {Assessment}

**Pattern 2: {Pattern Name}**
- Location: `{path}`
- Usage: {Description}
- Effectiveness: {Assessment}

### Dependency Analysis

**Internal Dependencies:**
{Description of how components depend on each other}

**External Dependencies:**
| Package | Version | Purpose | Risk Level |
|---------|---------|---------|------------|
| {name} | {ver} | {why needed} | {L/M/H} |

### Code Quality Observations

**Strengths:**
- {Positive observation 1}
- {Positive observation 2}

**Areas for Improvement:**
- {Issue 1}
- {Issue 2}

**Technical Debt:**
- {Debt item 1}
- {Debt item 2}

## Analysis

**Architectural Insights:**
1. {Key insight about the architecture}
2. {Another important finding}

**Design Decision Rationale:**
- {Why certain decisions were made}
- {Trade-offs accepted}

**Scalability Assessment:**
- {How well the architecture scales}
- {Bottlenecks identified}

**Maintainability Assessment:**
- {Ease of making changes}
- {Areas of concern}

## Recommendations

**Short-term Improvements:**
1. {Quick win 1}
2. {Quick win 2}

**Long-term Refactoring:**
1. {Major improvement 1}
   - Impact: {What it affects}
   - Effort: {Estimated effort}
2. {Major improvement 2}

**Architectural Changes:**
- {Proposed structural change}
- {Rationale}

**Priority Matrix:**

| Recommendation | Impact | Effort | Priority |
|----------------|--------|--------|----------|
| {Item 1} | {H/M/L} | {H/M/L} | {1-5} |

## Sources

**Codebase Files Analyzed:**
- `{@path/to/file1}`
- `{@path/to/file2}`

**Design Documents:**
- {Reference to design docs}

**Related Documentation:**
- [{Doc name}]({path or URL})

**Reference Architectures:**
- [{Name}]({URL})
    ]]>
  </output-template>

  <understanding/>

</document>
```
