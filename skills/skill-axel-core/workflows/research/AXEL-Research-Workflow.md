---
name: research-workflow
description: Comprehensive research workflow - produces Pure Markdown research reports
type: workflow
triggers:
  - research
  - investigate
  - analyze
---

# AXEL Workflow: Research

```xml
<document type="workflow">

  <enforcement>
    <![CDATA[
    PATH RESOLUTION:
    - Read the `src`, `ref`, or `target` attribute from the document XML to locate referenced files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory

    RESEARCH RULES:
    - Topic can be new subject OR existing research file path
    - IF topic ends with .md AND file exists → continue existing research
    - ELSE → start new research
    - Output is Pure Markdown in .claude/research/{topic}.md
    - All sections MUST be present in final report
    ]]>
  </enforcement>

  <objective>
    Comprehensive research workflow that produces Pure Markdown reports.
    Supports Technical, Codebase, Web, and Best Practices research types.
    Enables iterative research via file-based checkpoint system.
  </objective>

  <documents name="references" load="always" mode="context">
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/references/AXEL-Research.md"/>
    <understanding>
      !! MANDATORY: READ → UNDERSTAND → APPLY !!
      Research reference provides structure, types, output format, and templates.
    </understanding>
  </documents>

  <variables>
    <var name="topic" from="param.topic" description="Research topic or file path"/>
    <var name="research_type" value="" description="Detected research type"/>
    <var name="is_continuation" value="false" description="Whether continuing existing research"/>
    <var name="output_path" value="" description="Final output file path"/>
  </variables>

  <execution flow="staged">

    <!-- init: Analyze parameter and determine research mode -->
    <stage id="init">
      <tasks output="init_result">
        Step 1 - Analyze Topic Parameter:
        - Check if topic ends with .md
        - IF .md extension AND file exists → set is_continuation = true
        - ELSE → set is_continuation = false

        Step 2 - Determine Research Type:
        - Analyze topic keywords to detect type:
          - "library", "framework", "comparison", "performance" → technical
          - "architecture", "pattern", "code", "design" → codebase
          - "standard", "convention", "best practice", "guideline" → best-practices
          - Default → technical

        Step 3 - Set Output Path:
        - IF continuation → use existing file path
        - ELSE → .claude/research/{topic-kebab-case}.md
      </tasks>
      <print>
        ## Research Session Started

        **Topic:** ${topic}
        **Type:** ${research_type}
        **Mode:** ${is_continuation ? "Continuing existing" : "New research"}
      </print>
      <goto when="${is_continuation} == true" to="load-existing"/>
      <goto to="gather-context"/>
    </stage>

    <!-- load-existing: Load existing research file -->
    <stage id="load-existing">
      <tasks output="existing_content">
        Step 1 - Load Existing Research:
        - Read file from ${topic}
        - Parse frontmatter for metadata
        - Extract current findings and analysis

        Step 2 - Identify Gaps:
        - Check which sections need more work
        - Identify unanswered questions
        - Note incomplete areas
      </tasks>
      <print>
        ## Continuing Research

        **File:** ${topic}
        **Current Status:** ${existing_content.status}
        **Gaps Identified:** ${existing_content.gaps}
      </print>
      <goto to="gather-context"/>
    </stage>

    <!-- gather-context: Collect information from various sources -->
    <stage id="gather-context">
      <tasks output="context_findings">
        Step 1 - Check Project Documents:
        - Read CLAUDE.md for project context
        - Scan references/ folder for related docs
        - Check existing research files

        Step 2 - Scan Codebase (if codebase type):
        - Identify relevant files and patterns
        - Note dependencies and structure
        - Document existing implementations

        Step 3 - Search External Sources (if needed):
        - Consult official documentation
        - Find authoritative articles
        - Gather community insights
      </tasks>
      <print>
        ## Context Gathered

        **Sources Consulted:**
        ${context_findings.sources}

        **Key Findings:**
        ${context_findings.summary}
      </print>
    </stage>

    <!-- formulate-questions: Define research questions -->
    <stage id="formulate-questions">
      <tasks output="questions">
        Step 1 - Define Primary Questions:
        - What must be answered?
        - Core questions for research goal

        Step 2 - Define Secondary Questions:
        - Supporting questions
        - Nice-to-have answers
      </tasks>
      <print>
        ## Research Questions

        **Primary:**
        ${questions.primary}

        **Secondary:**
        ${questions.secondary}
      </print>
    </stage>

    <!-- execute-research: Systematic research execution -->
    <stage id="execute-research">
      <tasks output="findings">
        Step 1 - Consult Sources Systematically:
        - Work through each source type
        - Document evidence and data
        - Note uncertainties

        Step 2 - Answer Questions:
        - Address primary questions first
        - Move to secondary questions
        - Document what could not be answered

        Step 3 - Collect Evidence:
        - Code examples
        - Statistics and benchmarks
        - Expert opinions
      </tasks>
      <print>
        ## Research Findings

        ${findings.summary}
      </print>
    </stage>

    <!-- analyze: Synthesize and interpret findings -->
    <stage id="analyze">
      <tasks output="analysis">
        Step 1 - Synthesize Findings:
        - Identify patterns
        - Draw connections
        - Note contradictions

        Step 2 - Evaluate Options (if applicable):
        - Compare alternatives
        - Assess trade-offs
        - Consider context factors

        Step 3 - Form Conclusions:
        - Key insights
        - Supported recommendations
      </tasks>
      <print>
        ## Analysis Complete

        **Key Insights:**
        ${analysis.insights}

        **Trade-offs:**
        ${analysis.tradeoffs}
      </print>
    </stage>

    <!-- generate-recommendations: Create actionable suggestions -->
    <stage id="generate-recommendations">
      <tasks output="recommendations">
        Step 1 - Prioritize Recommendations:
        - Must-have actions
        - Should-have improvements
        - Nice-to-have enhancements

        Step 2 - Provide Implementation Guidance:
        - How to implement recommendations
        - Potential risks and mitigations
        - Success criteria
      </tasks>
      <print>
        ## Recommendations

        ${recommendations.summary}
      </print>
    </stage>

    <!-- generate-report: Create final Markdown report -->
    <stage id="generate-report">
      <tasks output="report">
        Step 1 - Load Appropriate Template:
        - Match research_type to template
        - Prepare template variables

        Step 2 - Generate Report Content:
        - Fill all sections from gathered data
        - Format as Pure Markdown
        - Include proper frontmatter

        Step 3 - Create Research Directory:
        - Ensure .claude/research/ exists
        - Write report to ${output_path}
      </tasks>
      <print>
        ## Report Generated

        **Output:** ${output_path}
      </print>
    </stage>

    <!-- complete: Finalize and report -->
    <stage id="complete">
      <print>
        ## Research Complete

        **Topic:** ${topic}
        **Type:** ${research_type}
        **Output:** ${output_path}

        The research report has been saved. You can continue this research
        later by running: /axel:research ${output_path}
      </print>
      <stop kind="end"/>
    </stage>

  </execution>

  <output format="json">
    <![CDATA[
    {
      "status": "success",
      "topic": "${topic}",
      "research_type": "${research_type}",
      "output_path": "${output_path}",
      "is_continuation": ${is_continuation},
      "sections_completed": ["Context", "Questions", "Methodology", "Findings", "Analysis", "Recommendations", "Sources"],
      "summary": "Research completed and saved to ${output_path}"
    }
    ]]>
  </output>

  <understanding/>

</document>
```
