---
name: brainstorm-bootstrap
description: Smart workflow bootstrap - selects and executes appropriate brainstorm workflows based on mode
type: workflow
triggers:
  - brainstorm
  - understand
  - analyze
  - todo
---

# AXEL Workflow: Brainstorm Bootstrap

```xml
<document type="workflow">

  <enforcement>
    <![CDATA[
    PATH RESOLUTION:
    - Read the `src`, `ref`, or `target` attribute from the document XML to locate referenced files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory

    - Intelligently select workflow(s) based on mode and input analysis
    - Mode determines PRIMARY goal, situation determines HELPER workflows
    - Return standardized output format for all modes
    - NEVER skip understanding phase
    - workflows_used field provides transparency on which workflows ran
    - Single workflow call = single turn (no internal loops)
    ]]>
  </enforcement>

  <objective>
    Smart inquiry bootstrap that analyzes input and selects appropriate workflow(s).
    Supports modes: understand, analysis, brainstorm, todo, review, decision.
    Returns structured output with summary, findings, questions, recommendations.
  </objective>

  <variables>
    <var name="topic" from="param.topic"/>
    <var name="mode" from="param.mode" value="understand"/>
    <var name="context" from="param.context" default=""/>
  </variables>

  <workflows name="brainstorm" load="on-demand">
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/workflows/brainstorm/refs/AXEL-Discovery-Workflow.md" ask="discover, explore, understand"/>
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/workflows/brainstorm/refs/AXEL-Elicitation-Workflow.md" ask="elicit, detail, analyze"/>
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/workflows/brainstorm/refs/AXEL-Socratic-Workflow.md" ask="socratic, validate, challenge"/>
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/workflows/brainstorm/refs/AXEL-Deep-Inquiry-Workflow.md" ask="deep, risk, review"/>
  </workflows>

  <execution flow="linear">
    <![CDATA[
    !! MANDATORY: READ → UNDERSTAND → APPLY !!
    When workflow is resolved via registry query:
    1. READ the workflow file from resolved path
    2. UNDERSTAND the workflow structure, stages, and purpose
    3. APPLY the workflow by executing its stages with given context

    Step 1 - Select Workflow(s) via Registry Query:
    Analyze mode and load PRIMARY workflow(s):
    - understand → ${workflows:brainstorm[ask=understand].src}
    - analysis   → ${workflows:brainstorm[ask=analyze].src}
    - brainstorm → ${workflows:brainstorm[ask=discover|validate].src[]}
    - todo       → ${workflows:brainstorm[ask=detail|challenge].src[]}
    - review     → ${workflows:brainstorm[ask=deep].src}
    - decision   → ${workflows:brainstorm[ask=validate|risk].src[]}

    Check if HELPER workflows needed:
    - Topic is vague      → +${workflows:brainstorm[ask=discover].src}
    - Missing details     → +${workflows:brainstorm[ask=detail].src}
    - Assumptions present → +${workflows:brainstorm[ask=validate].src}
    - Critical decision   → +${workflows:brainstorm[ask=risk].src}

    Step 2 - Execute Selected Workflow(s):
    Load resolved workflow path(s) and execute.
    Pass context: topic=${topic}, context=${context}

    Step 3 - Collect Results:
    Gather findings, questions, and recommendations from executed workflows.
    Track which workflows were used.
    ]]>
  </execution>

  <output format="markdown">
    ## Brainstorm Complete

    **Summary:** {summary}

    **Findings:**
    {findings}

    **Questions:**
    {questions}

    **Recommendations:**
    {recommendations}

    ---
    *Workflows used: {workflows_used}*
  </output>

  <understanding/>

</document>
```
