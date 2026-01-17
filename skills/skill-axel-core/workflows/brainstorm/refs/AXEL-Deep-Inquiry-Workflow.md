---
name: inquiry-deep
description: Deep Inquiry workflow - analyze risks, explore scenarios, identify dependencies
type: workflow
triggers:
  - deep
  - risk
  - whatif
  - scenario
---

# AXEL Workflow: Deep Inquiry

```xml
<document type="workflow">

  <enforcement>
    <![CDATA[
    PATH RESOLUTION:
    - Read the `src`, `ref`, or `target` attribute from the document XML to locate referenced files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory

    - Focus on RISKS and SCENARIOS
    - Ask "What if?" and "What could go wrong?" questions
    - Identify dependencies and failure points
    - Use Pre-mortem analysis (assume failure, find causes)
    - NEVER ignore edge cases
    - Output structured findings for bootstrap consumption
    ]]>
  </enforcement>

  <objective>
    Deep Inquiry workflow for risk analysis and scenario planning.
    Answers: What could go wrong? What are the dependencies? What's the worst case?
    Uses: What-If Scenarios, Pre-mortem, Six Thinking Hats (Black Hat), Dependency Mapping.
  </objective>

  <variables>
    <var name="topic" from="params.topic" />
    <var name="context" from="params.context" default="" />
  </variables>

  <execution flow="staged">

    <!-- STAGE: INIT -->
    <stage id="init">
      <print>
        ## Deep Inquiry Phase

        Analyzing risks for: **${topic}**
      </print>
    </stage>

    <!-- STAGE: ANALYZE - Core risk analysis -->
    <stage id="analyze">
      <thinking focus="risk-analysis">
        <![CDATA[
        Apply Deep Inquiry techniques for risk analysis:

        WHAT-IF SCENARIOS:
        - What if this fails?
        - What if requirements change?
        - What if resources are cut?
        - What if timeline is shortened?
        - What if a key dependency breaks?

        PRE-MORTEM ANALYSIS:
        - Assume the project failed - why?
        - What were the warning signs?
        - What should we have done differently?
        - What was the root cause of failure?

        SIX THINKING HATS (BLACK HAT):
        - What are all the problems?
        - What are all the risks?
        - What could go wrong?
        - What are the weaknesses?

        DEPENDENCY MAPPING:
        - What does this depend on?
        - What depends on this?
        - Where are the single points of failure?
        - What's the critical path?

        SCALABILITY CONCERNS:
        - What if load increases 10x?
        - What if data grows 100x?
        - What are the bottlenecks?
        ]]>
      </thinking>
      <tasks output="deep_result">
        <![CDATA[
        Generate deep inquiry questions and findings:

        QUESTIONS TO ASK (select most relevant 3-5):
        1. "What happens if this fails? What are the consequences?"

        2. "What's the worst case scenario? How would you handle it?"

        3. "What dependencies exist? Are there single points of failure?"

        4. "Could there be scaling issues? What if 10x load?"

        5. "Are there security vulnerabilities? How could it be misused?"

        6. "What if user behaves unexpectedly?"

        7. "What if API doesn't respond? Is there a fallback?"

        8. "What if deadline is missed? What's the critical path?"

        9. "What if data is lost? Is there backup/recovery?"

        10. "Could there be race conditions?"

        ANALYZE INPUT:
        - topic: ${topic}
        - existing context: ${context}

        Identify hidden risks and dependencies.

        OUTPUT:
        - risks: List of identified risks with severity (high/medium/low)
        - mitigations: Risk mitigation strategies
        - dependencies: External and internal dependencies
        - scenarios: Key what-if scenarios and outcomes
        - failure_points: Single points of failure
        - key_questions: Most important questions to ask user
        ]]>
      </tasks>
    </stage>

    <!-- STAGE: COMPLETE -->
    <stage id="complete">
      <print>
        ## Deep Inquiry Findings

        **Risks Identified:**
        ${deep_result.risks}

        **Mitigation Strategies:**
        ${deep_result.mitigations}

        **Dependencies:**
        ${deep_result.dependencies}

        **What-If Scenarios:**
        ${deep_result.scenarios}

        **Failure Points:**
        ${deep_result.failure_points}

        **Key Questions:**
        ${deep_result.key_questions}
      </print>
      <stop kind="end" output="${deep_result}"/>
    </stage>

  </execution>

  <understanding/>

</document>
```
