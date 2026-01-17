---
name: agent-staged
description: Template for agents with staged execution - supports sequential, branching, parallel, loop patterns
type: template
---

# AXEL Template: Agent - Staged

```xml
<document type="agent">

  <enforcement>
    - Read `src` and `ref` attributes from document references to locate files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
  </enforcement>

  <objective>
    Agent with staged execution flow.
    Supports sequential, branching, parallel, and loop patterns within stages.
  </objective>

  <documents name="core" load="always" mode="context">
    <read src=".claude/BOOTSTRAP.md"/>
    <understanding>
      Bootstrap provides core AXEL rules and enforcement.
      Additional documents can be added based on agent needs.
    </understanding>
  </documents>

  <archetype type="orchestration">
    <!--
    Archetype options: analysis, generation, orchestration, validation
    -->
  </archetype>

  <system-prompt voice="second-person">
    You are a [Role] specialist responsible for [core task].

    Core Responsibilities:
    1. [First responsibility]
    2. [Second responsibility]
    3. [Third responsibility]

    Edge Cases:
    - [Edge case]: [How to handle]
  </system-prompt>

  <execution flow="staged">

    <!--
    ============================================
    INPUT: Parse parameters from caller
    ============================================
    -->
    <stage id="init">
      <tasks output="params">
        Step 1 - Parse Input Parameters:
        - Extract mode from prompt (analyze | generate | validate)
        - Extract target path
        - Extract options (if provided)
        - Default mode to "analyze" if not specified
      </tasks>
      <set var="mode" from="params.mode"/>
      <set var="target" from="params.target"/>
      <set var="options" from="params.options"/>
    </stage>

    <!--
    ============================================
    MODE ROUTING: Dynamic routing based on mode
    ============================================
    -->
    <stage id="route">
      <goto to="${mode}"/>
    </stage>

    <!--
    ============================================
    MODE: analyze - Analysis operations
    ============================================
    -->
    <stage id="analyze">
      <print>Analyzing ${target}...</print>
      <tasks output="analyze_result">
        Step 1 - Read Target:
        - Load target file or directory
        - Parse content structure

        Step 2 - Analyze:
        - Apply analysis rules
        - Identify issues and patterns
      </tasks>
      <set var="result" from="analyze_result"/>
      <goto to="validate"/>
    </stage>

    <!--
    ============================================
    MODE: generate - Generation operations
    ============================================
    -->
    <stage id="generate">
      <print>Generating output for ${target}...</print>
      <tasks output="generate_result">
        Step 1 - Prepare:
        - Load templates and references
        - Gather required context

        Step 2 - Generate:
        - Create output based on input
        - Apply formatting rules
      </tasks>
      <set var="result" from="generate_result"/>
      <goto to="validate"/>
    </stage>

    <!--
    ============================================
    MODE: validate - Validation operations
    ============================================
    -->
    <stage id="validate-mode">
      <print>Validating ${target}...</print>
      <tasks output="validate_result">
        Step 1 - Check:
        - Verify structure and format
        - Check against standards
      </tasks>
      <set var="result" from="validate_result"/>
      <goto to="validate"/>
    </stage>

    <!--
    ============================================
    BRANCHING: Conditional routing with goto
    ============================================
    -->
    <stage id="conditional-route">
      <goto when="${result.type} = 'simple'" to="quick-process"/>
      <goto when="${result.type} = 'complex'" to="deep-process"/>
      <goto to="standard-process"/>
    </stage>

    <stage id="quick-process">
      <print>Quick processing...</print>
      <tasks output="quick_result">
        Step 1 - Fast Process:
        - Apply lightweight processing
        - Generate basic output
      </tasks>
      <goto to="validate"/>
    </stage>

    <stage id="standard-process">
      <print>Standard processing...</print>
      <tasks output="standard_result">
        Step 1 - Process:
        - Apply standard processing logic
        - Transform data as needed

        Step 2 - Format:
        - Structure output
        - Apply formatting rules
      </tasks>
      <goto to="validate"/>
    </stage>

    <stage id="deep-process">
      <print>Deep processing...</print>
      <tasks output="deep_result">
        Step 1 - Detailed Analysis:
        - Perform comprehensive analysis
        - Identify all edge cases

        Step 2 - Transform:
        - Apply complex transformations
        - Handle special cases

        Step 3 - Validate Intermediate:
        - Check intermediate results
        - Ensure data integrity
      </tasks>
      <goto to="validate"/>
    </stage>

    <!--
    ============================================
    PARALLEL: Multiple stages run concurrently
    ============================================
    -->
    <parallel id="concurrent-checks">
      <stage id="check-quality">
        <tasks output="quality_check">
          Step 1 - Quality Check:
          - Verify output completeness
          - Check against quality standards
        </tasks>
        <set var="quality_ok" from="quality_check.passed"/>
      </stage>
      <stage id="check-format">
        <tasks output="format_check">
          Step 1 - Format Check:
          - Validate output structure
          - Verify required fields
        </tasks>
        <set var="format_ok" from="format_check.passed"/>
      </stage>
    </parallel>

    <!--
    ============================================
    LOOP: Retry pattern with backward goto
    ============================================
    -->
    <stage id="validate">
      <set var="retry_count" value="${retry_count} + 1"/>
      <goto when="${quality_ok} = false AND ${retry_count} < 3" to="standard-process"/>
      <goto when="${quality_ok} = false AND ${retry_count} >= 3" to="fail"/>
    </stage>

    <!--
    ============================================
    WORKFLOW: Trigger a workflow with parameters
    ============================================
    -->
    <stage id="run-workflow">
      <workflow src=".claude/workflows/quality-check.md" output="workflow_result">
        <param name="project" value="${project_name}"/>
        <param name="environment" value="staging"/>
      </workflow>
      <set var="workflow_status" from="workflow_result.status"/>
      <goto when="${workflow_status} = 'failed'" to="fail"/>
    </stage>

    <!--
    ============================================
    INVOKE: Call other agents with mode parameter
    ============================================
    -->
    <stage id="delegate">
      <invoke name="Task" output="delegate_result">
        <param name="subagent_type">my-custom-agent</param>
        <param name="prompt"><![CDATA[
          - mode: analyze
          - target: ${target}
          - project: ${project_name}
          - options: detailed
        ]]></param>
      </invoke>
      <set var="delegate_summary" from="delegate_result.summary"/>
    </stage>

    <!--
    ============================================
    COMPLETION STAGES
    ============================================
    -->
    <stage id="complete">
      <print>Process completed successfully.</print>
      <stop kind="end"/>
    </stage>

    <stage id="fail">
      <print>Process failed after ${retry_count} attempts.</print>
      <stop kind="error"/>
    </stage>

  </execution>

  <output format="json">
    <![CDATA[
    {
      "status": "success|failed",
      "mode": "analyze|generate|validate",
      "target": "path/to/target",
      "result": {
        "type": "simple|standard|complex",
        "data": {}
      },
      "checks": {
        "quality_passed": true,
        "format_passed": true
      },
      "workflow_status": "success|failed",
      "delegate_summary": "Analysis findings",
      "summary": "Executed {mode} on {target}"
    }
    ]]>
  </output>

  <understanding/>

</document>
```
