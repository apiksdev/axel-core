---
name: inquiry-discovery
description: Discovery workflow - explore new topics, gather broad context, identify stakeholders
type: workflow
triggers:
  - discover
  - explore
  - what
---

# AXEL Workflow: Discovery

```xml
<document type="workflow">

  <enforcement>
    <![CDATA[
    PATH RESOLUTION:
    - Read the `src`, `ref`, or `target` attribute from the document XML to locate referenced files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory

    - Focus on BROAD understanding, not details
    - Ask "What?" questions, not "How?" questions
    - Identify stakeholders and scope boundaries
    - NEVER assume context - always ask
    - Output structured findings for bootstrap consumption
    ]]>
  </enforcement>

  <objective>
    Discovery workflow for exploring new topics and gathering broad context.
    Answers: What is this about? Who is involved? What's the big picture?
    Uses: Mind Mapping, Stakeholder View, Scope Identification techniques.
  </objective>

  <variables>
    <var name="topic" from="params.topic" />
    <var name="context" from="params.context" default="" />
  </variables>

  <execution flow="staged">

    <!-- STAGE: INIT -->
    <stage id="init">
    <print>
      ## Discovery Phase

      Exploring: **${topic}**
    </print>
  </stage>

  <!-- STAGE: DISCOVER - Core discovery questions -->
  <stage id="discover">
    <thinking focus="discovery-analysis">
      <![CDATA[
      Apply Discovery techniques to understand the topic:

      MIND MAPPING:
      - What is the central concept?
      - What are the main branches/aspects?
      - How do they connect?

      STAKEHOLDER VIEW:
      - Who will use this?
      - Who will be affected?
      - Who needs to approve?
      - Who provides input?

      SCOPE IDENTIFICATION:
      - What's definitely included?
      - What's definitely excluded?
      - What's unclear/borderline?

      CONTEXT GATHERING:
      - Where did this idea come from?
      - What triggered this need?
      - What's the ideal outcome?
      - Has something similar been tried before?
      ]]>
    </thinking>
    <tasks output="discovery_result">
      <![CDATA[
      Generate discovery questions and initial findings:

      QUESTIONS TO ASK (select most relevant 3-5):
      1. "What exactly are you trying to do?"

      2. "Where did this idea come from? What triggered it?"

      3. "Who will be affected? Who will use it?"

      4. "What does the ideal outcome look like?"

      5. "Has something similar been tried before?"

      6. "What's the scope? What's in, what's out?"

      7. "What's the most important success criterion?"

      ANALYZE INPUT:
      - topic: ${topic}
      - existing context: ${context}

      OUTPUT:
      - topic_summary: Brief understanding of the topic
      - stakeholders: List of identified stakeholders
      - scope_hints: Initial scope boundaries
      - unknowns: List of things we don't know yet
      - key_questions: Most important questions to ask user
      ]]>
    </tasks>
  </stage>

  <!-- STAGE: COMPLETE -->
  <stage id="complete">
    <print>
      ## Discovery Findings

      **Topic Summary:**
      ${discovery_result.topic_summary}

      **Stakeholders Identified:**
      ${discovery_result.stakeholders}

      **Scope Hints:**
      ${discovery_result.scope_hints}

      **Unknowns:**
      ${discovery_result.unknowns}

      **Key Questions:**
      ${discovery_result.key_questions}
    </print>
    <stop kind="end" output="${discovery_result}"/>
    </stage>

  </execution>

  <understanding/>

</document>
```
