---
name: inquiry-elicitation
description: Elicitation workflow - extract details, clarify ambiguities, identify constraints
type: workflow
triggers:
  - elicit
  - clarify
  - detail
  - how
---

# AXEL Workflow: Elicitation

```xml
<document type="workflow">

  <enforcement>
    <![CDATA[
    PATH RESOLUTION:
    - Read the `src`, `ref`, or `target` attribute from the document XML to locate referenced files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory

    - Focus on DETAILS and CLARIFICATION
    - Ask "How?" and "What exactly?" questions
    - Identify constraints, priorities, success criteria
    - Use Five Whys to find root causes
    - NEVER accept vague answers - dig deeper
    - Output structured findings for bootstrap consumption
    ]]>
  </enforcement>

  <objective>
    Elicitation workflow for extracting detailed information and clarifying ambiguities.
    Answers: How exactly? What are the constraints? What's the priority?
    Uses: Five Whys, Constraint Mapping, Expand/Contract techniques.
  </objective>

  <variables>
    <var name="topic" from="params.topic" />
    <var name="context" from="params.context" default="" />
  </variables>

  <execution flow="staged">

    <!-- STAGE: INIT -->
    <stage id="init">
    <print>
      ## Elicitation Phase

      Clarifying: **${topic}**
    </print>
  </stage>

  <!-- STAGE: ELICIT - Core elicitation questions -->
  <stage id="elicit">
    <thinking focus="elicitation-analysis">
      <![CDATA[
      Apply Elicitation techniques to extract details:

      FIVE WHYS (Root Cause):
      - Why is this needed?
      - Why now?
      - Why this approach?
      - Why these constraints?
      - Why this priority?

      CONSTRAINT MAPPING:
      - Technical constraints (tech stack, performance, security)
      - Business constraints (budget, timeline, resources)
      - Process constraints (approvals, compliance, standards)
      - Integration constraints (APIs, dependencies, compatibility)

      EXPAND/CONTRACT:
      - Where do we need MORE detail?
      - Where can we SIMPLIFY?
      - What level of detail is appropriate?

      PRIORITY IDENTIFICATION:
      - What's must-have vs nice-to-have?
      - What's the order of importance?
      - What can be deferred?
      ]]>
    </thinking>
    <tasks output="elicitation_result">
      <![CDATA[
      Generate elicitation questions and findings:

      QUESTIONS TO ASK (select most relevant 3-5):
      1. "Can you explain this in more detail?"

      2. "What exactly do you mean by X?"

      3. "What constraints exist? (technical, time, budget)"

      4. "What are success criteria? What will we measure?"

      5. "What's the priority order? Which is most critical?"

      6. "Why is this needed now? What triggered it?"

      7. "What dependencies exist? What's it waiting for?"

      8. "What would be an unacceptable outcome?"

      ANALYZE INPUT:
      - topic: ${topic}
      - existing context: ${context}

      OUTPUT:
      - clarifications: List of clarified points
      - constraints: Identified constraints (technical, business, process)
      - priorities: Priority order of requirements
      - success_criteria: Defined success metrics
      - gaps: Information still missing
      - key_questions: Most important questions to ask user
      ]]>
    </tasks>
  </stage>

  <!-- STAGE: COMPLETE -->
  <stage id="complete">
    <print>
      ## Elicitation Findings

      **Clarifications:**
      ${elicitation_result.clarifications}

      **Constraints:**
      ${elicitation_result.constraints}

      **Priorities:**
      ${elicitation_result.priorities}

      **Success Criteria:**
      ${elicitation_result.success_criteria}

      **Gaps:**
      ${elicitation_result.gaps}

      **Key Questions:**
      ${elicitation_result.key_questions}
    </print>
    <stop kind="end" output="${elicitation_result}"/>
    </stage>

  </execution>

  <understanding/>

</document>
```
