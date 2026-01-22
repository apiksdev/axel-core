---
name: axel-research
description: Structure of research document files - comprehensive research process management
type: reference
---

# AXEL Research

```xml
<document type="reference">

  <enforcement>
    <![CDATA[
    PATH RESOLUTION:
    - Read `src` attribute from template references to locate research template files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
    - Research output files located in .claude/research/ directory

    RESEARCH PROCESS:
    - Topic can be a new subject OR an existing research file path
    - IF topic is file path (.md extension) → continue existing research
    - IF topic is text → start new research

    OUTPUT FORMAT:
    - Pure Markdown in .claude/research/{topic}.md
    - No XML structure in output files
    - Clean, readable research reports
    ]]>
  </enforcement>

  <objective>
    Structure of research definition files. AXEL Research is a comprehensive
    research process management system that produces structured reports.
    Supports Technical, Codebase, Web, and Best Practices research types.
    Output is Pure Markdown saved to .claude/research/ directory.
  </objective>

  <frontmatter>
    <![CDATA[
---
name: research-topic-name          # Research name (kebab-case)
description: Research description  # Short description, max 200 characters
type: research                     # Always "research"
research_type: technical           # technical | codebase | web | best-practices
status: in-progress                # in-progress | completed
created_at: YYYY-MM-DD             # Creation date
updated_at: YYYY-MM-DD             # Last update date
---
    ]]>
  </frontmatter>

  <templates load="always" mode="context">
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/research/AXEL-Research-Template-Bootstrap.md"/>
    <axel-tag-structure>
      <![CDATA[
      Research Report Structure (Pure Markdown)
      +-- Frontmatter (name, description, type: research, research_type, status, dates)
      +-- # Research: {Topic}
      +-- ## Context
      |   +-- Background information
      |   +-- Why this research is needed
      |   +-- Scope and boundaries
      +-- ## Questions
      |   +-- Primary questions to answer
      |   +-- Secondary questions
      +-- ## Methodology
      |   +-- Research approach
      |   +-- Sources to consult
      |   +-- Tools and techniques
      +-- ## Findings
      |   +-- Key discoveries
      |   +-- Data and evidence
      |   +-- Observations
      +-- ## Analysis
      |   +-- Interpretation of findings
      |   +-- Patterns and trends
      |   +-- Comparisons
      +-- ## Recommendations
      |   +-- Actionable suggestions
      |   +-- Trade-offs and considerations
      |   +-- Implementation guidance
      +-- ## Sources
      |   +-- Documentation references
      |   +-- Codebase files examined
      |   +-- External links
      ]]>
    </axel-tag-structure>
    <understanding>
      !! MANDATORY: READ -> UNDERSTAND -> APPLY !!
      - READ the template file first
      - UNDERSTAND the structure and patterns
      - APPLY the template structure EXACTLY
      Reference = HOW to think | Template = HOW to write
    </understanding>
  </templates>

  <context>
    - Used for comprehensive research and documentation
    - Supports four research types with different focuses
    - Produces clean Markdown reports in .claude/research/
    - Hybrid process: simple topics single-pass, complex topics iterative
    - File-based checkpoint: pass file path to continue existing research
  </context>

  <principle name="research-types">
    <![CDATA[
    Research Types and Focus Areas:

    1. Technical:
       - Technology comparison and evaluation
       - Library/framework analysis
       - Performance characteristics
       - Pros/cons assessment
       - Use case recommendations

    2. Codebase:
       - Code pattern discovery
       - Architecture analysis
       - Dependency mapping
       - Design decisions documentation
       - Refactoring opportunities

    3. Web:
       - External documentation research
       - Best practices from authoritative sources
       - Industry standards
       - Competitive analysis
       - Trend identification

    4. Best Practices:
       - Industry standards compilation
       - Coding conventions
       - Design patterns
       - Security guidelines
       - Performance optimization patterns
    ]]>
  </principle>

  <principle name="research-process">
    <![CDATA[
    Research Process Flow:

    1. Parameter Analysis:
       - Determine if topic is new or existing file
       - Identify research type from content/keywords
       - Set scope boundaries

    2. Context Gathering:
       - Load relevant project documents
       - Scan codebase for related patterns
       - Search web for external sources

    3. Question Formulation:
       - Define primary research questions
       - Identify secondary questions
       - Prioritize by importance

    4. Research Execution:
       - Systematic source consultation
       - Evidence collection
       - Pattern recognition

    5. Analysis:
       - Synthesize findings
       - Draw conclusions
       - Identify trade-offs

    6. Report Generation:
       - Structure findings in Markdown
       - Save to .claude/research/{topic}.md
    ]]>
  </principle>

  <decision name="hybrid-research-mode" date="2024-12">
    When: Determining research depth
    Action: Adapt based on topic complexity
    - Simple: Direct answer with brief context
    - Complex: Multi-pass iterative research
    Criteria:
    - Simple: Well-defined, single-focus topics
    - Complex: Broad scope, multiple aspects, deep analysis needed
    Reason: Efficient resource use while ensuring thorough research
  </decision>

  <decision name="file-checkpoint-system" date="2024-12">
    When: Continuing existing research
    Action: Use file path as topic parameter
    Process:
    - User passes .claude/research/topic.md as parameter
    - Load existing research content
    - Continue from current state
    - Update findings, analysis, recommendations
    Reason: Enables iterative research without losing progress
  </decision>

  <requirements>
    - Frontmatter must include name (kebab-case), description, type: research
    - Frontmatter must include research_type, status, created_at, updated_at
    - Output must be Pure Markdown (no XML in research reports)
    - Output path must be .claude/research/{topic-kebab-case}.md
    - All sections must be present: Context, Questions, Methodology, Findings, Analysis, Recommendations, Sources
    - Sources must be properly attributed and linked
  </requirements>

  <implementation name="file-locations">
    .claude/research/
    - {topic-name}.md              # Research report file (e.g.: react-state-management.md)
  </implementation>

  <implementation name="creating-research">
    Step 1 - Analyze Parameter:
    - IF topic ends with .md AND file exists → load and continue
    - ELSE → start new research

    Step 2 - Determine Research Type:
    - Analyze topic keywords
    - Match to research type (technical, codebase, web, best-practices)
    - Default to technical if unclear

    Step 3 - Gather Context:
    - Check project documents (CLAUDE.md, references)
    - Scan relevant codebase files
    - Search web for external sources

    Step 4 - Formulate Questions:
    - Define primary questions (must answer)
    - Define secondary questions (nice to answer)
    - Prioritize by importance

    Step 5 - Execute Research:
    - Consult sources systematically
    - Collect evidence and data
    - Document findings

    Step 6 - Analyze and Synthesize:
    - Interpret findings
    - Identify patterns
    - Draw conclusions

    Step 7 - Generate Recommendations:
    - Actionable suggestions
    - Trade-off analysis
    - Implementation guidance

    Step 8 - Create Report:
    - Format as Pure Markdown
    - Include all sections
    - Save to .claude/research/{topic}.md

    Step 9 - AXEL Checklist:
    - Verify all sections present
    - Check source attribution
    - Validate frontmatter
  </implementation>

  <output format="markdown">
    File: {topic-name}.md
    Path: .claude/research/{topic-name}.md
    Structure:
    - YAML frontmatter (---)
    - Markdown title (# Research: {Topic})
    - Sections: Context, Questions, Methodology, Findings, Analysis, Recommendations, Sources
  </output>

  <verification>
    - Is frontmatter correct? (name: kebab-case, type: research)
    - Is research_type defined? (technical/codebase/web/best-practices)
    - Are all sections present?
    - Are sources properly attributed?
    - Is output Pure Markdown (no XML)?
    - Is file saved to .claude/research/?
  </verification>

  <checklist name="research-validation">
    Frontmatter:
    - Is name kebab-case?
    - Is type: research?
    - Is research_type defined?
    - Is status defined?
    - Are dates (created_at, updated_at) present?

    Content:
    - Is Context section present with background?
    - Is Questions section present with clear questions?
    - Is Methodology section present with approach?
    - Is Findings section present with evidence?
    - Is Analysis section present with interpretation?
    - Is Recommendations section present with actionable items?
    - Is Sources section present with attribution?

    Quality:
    - Are findings evidence-based?
    - Are recommendations actionable?
    - Are sources properly cited?
    - Is the research comprehensive for the scope?
  </checklist>

  <understanding/>

</document>
```
