---
name: research-best-practices
description: Template for best practices research - industry standards, conventions, and guidelines
type: template
---

# AXEL Template: Research - Best Practices

```xml
<document type="template">

  <enforcement>
    <![CDATA[
    - Output is Pure Markdown (no XML in generated file)
    - Save to .claude/research/{topic-kebab-case}.md
    - Include all required sections
    - Cite authoritative sources
    ]]>
  </enforcement>

  <objective>
    Template for best practices research.
    Compiles industry standards, coding conventions, and guidelines.
    Provides actionable recommendations for implementation.
  </objective>

  <output-template>
    <![CDATA[
---
name: {topic-kebab-case}
description: {brief description}
type: research
research_type: best-practices
status: in-progress
created_at: {YYYY-MM-DD}
updated_at: {YYYY-MM-DD}
---

# Research: {Topic Title}

## Context

**Background:**
{Why these best practices are being researched}

**Scope:**
- {What areas are covered}
- {What is excluded}

**Target Audience:**
- {Who will use these practices}

## Questions

**Primary Questions:**
1. {Main question about best practices}
2. {Second question}

**Secondary Questions:**
- {Supporting question}
- {Detail question}

## Methodology

**Research Approach:**
- Official documentation review
- Industry standard analysis
- Expert recommendations compilation
- Community consensus gathering

**Sources Prioritization:**
1. Official language/framework documentation
2. Industry standards bodies (OWASP, IEEE, etc.)
3. Recognized experts and thought leaders
4. Community best practices

## Findings

### Category 1: {Practice Category}

**Best Practice 1.1: {Practice Name}**

*Description:*
{What this practice entails}

*Rationale:*
{Why this practice matters}

*Implementation:*
{{{lang}}}
// Example code
{{{lang}}}

*Common Mistakes:*
- {Mistake to avoid}

---

**Best Practice 1.2: {Practice Name}**

*Description:*
{Description}

*Rationale:*
{Why it matters}

*Implementation:*
{How to implement}

---

### Category 2: {Practice Category}

**Best Practice 2.1: {Practice Name}**

*Description:*
{Description}

*Rationale:*
{Rationale}

*Implementation:*
{Implementation guidance}

---

### Summary Table

| Category | Practice | Priority | Difficulty |
|----------|----------|----------|------------|
| {Cat 1} | {Practice} | {High/Medium/Low} | {Easy/Medium/Hard} |
| {Cat 2} | {Practice} | {Priority} | {Difficulty} |

## Analysis

**Industry Consensus:**
- {What most sources agree on}
- {Areas of strong agreement}

**Emerging Trends:**
- {New practices gaining adoption}
- {Evolving standards}

**Context Considerations:**
- {When practices may vary}
- {Project-specific factors}

**Trade-offs:**
| Practice | Benefit | Cost |
|----------|---------|------|
| {Practice} | {What you gain} | {What you give up} |

## Recommendations

**Must-Have Practices:**
1. {Critical practice}
2. {Essential practice}

**Should-Have Practices:**
1. {Important practice}
2. {Recommended practice}

**Nice-to-Have Practices:**
1. {Optional improvement}
2. {Advanced practice}

**Implementation Roadmap:**

| Phase | Practices | Timeline |
|-------|-----------|----------|
| Phase 1 | {Critical practices} | {Immediate} |
| Phase 2 | {Important practices} | {Short-term} |
| Phase 3 | {Advanced practices} | {Long-term} |

**Checklist for Adoption:**
- [ ] {First step}
- [ ] {Second step}
- [ ] {Third step}

## Sources

**Official Documentation:**
- [{Name}]({URL})

**Industry Standards:**
- [{Standard Name}]({URL})

**Expert Resources:**
- [{Author/Source}]({URL})

**Books & Publications:**
- {Book title} by {Author}

**Community Resources:**
- [{Resource}]({URL})
    ]]>
  </output-template>

  <understanding/>

</document>
```
