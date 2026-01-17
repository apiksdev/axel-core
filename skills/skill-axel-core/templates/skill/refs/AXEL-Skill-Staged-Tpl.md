---
name: skill-staged
description: Template for skills with staged execution - supports sequential, branching, triggers, invoke patterns
type: template
---

# AXEL Template: Skill - Staged

```xml
<document type="skill">

  <enforcement>
    - Read the `target`, `src`, or `ref` attribute from document references to locate files
    - Extract plugin root directory from paths (${CLAUDE_PLUGIN_ROOT} or explicit paths)
    - Resolve relative paths (.claude/) against current working directory
    - Validate all referenced files exist before execution
  </enforcement>

  <objective>
    Skill with staged execution flow.
    Supports sequential stages, branching, trigger-based routing, and external invocations.
  </objective>

  <documents load="always" mode="context">
    <read src=".claude/BOOTSTRAP.md"/>
    <understanding>
      Bootstrap provides core AXEL rules and enforcement.
      Additional documents loaded based on skill domain.
    </understanding>
  </documents>

  <documents load="on-trigger" mode="context">
    <read src=".claude/references/domain-guide.md" triggers="[keyword1, keyword2]"/>
    <understanding>
      Domain-specific guides loaded when trigger keywords detected.
    </understanding>
  </documents>

  <role>
    As a [Role Name], you [core responsibility description].
    Expertise in [domain1], [domain2], and [domain3].
  </role>

  <capabilities>
    - [Capability 1]
    - [Capability 2]
    - [Capability 3]
  </capabilities>

  <templates load="on-trigger" mode="context">
    <read src="${CLAUDE_PLUGIN_ROOT}/templates/domain/template1.md" triggers="[trigger1]"/>
    <understanding>
      Templates provide output structure patterns.
      Loaded when specific triggers match user request.
    </understanding>
  </templates>

  <workflows load="on-trigger" mode="map">
    <read src=".claude/workflows/workflow1.md" triggers="[trigger1]"/>
    <understanding>
      Workflows provide step-by-step execution plans.
      Loaded when trigger keywords detected in user request.
    </understanding>
  </workflows>

  <!--
  ============================================
  TRIGGERS: Automatic stage routing
  ============================================
  When skill activates, check user message against triggers.
  If match found, jump directly to target stage.
  If no match, start from "init" stage.
  -->
  <triggers>
    <goto trigger="create component" to="component-create"/>
    <goto trigger="test coverage" to="test-stage"/>
    <goto trigger="[a11y, accessibility, wcag]" to="a11y-check"/>
  </triggers>

  <execution flow="staged">

    <!--
    ============================================
    INIT: Entry point (default if no trigger match)
    ============================================
    -->
    <stage id="init">
      <tasks output="params">
        Step 1 - Analyze Request:
        - Parse user message for intent
        - Extract key parameters
        - Determine appropriate action path
      </tasks>
      <set var="action" from="params.action"/>
      <print>
        ## Skill Activated
        Processing request...
      </print>
    </stage>

    <!--
    ============================================
    ROUTE: Dynamic routing based on analysis
    ============================================
    -->
    <stage id="route">
      <goto when="${action} = 'create'" to="component-create"/>
      <goto when="${action} = 'test'" to="test-stage"/>
      <goto when="${action} = 'accessibility'" to="a11y-check"/>
      <goto to="general-process"/>
    </stage>

    <!--
    ============================================
    COMPONENT CREATE: Specific action stage
    ============================================
    -->
    <stage id="component-create">
      <print>Creating component...</print>
      <tasks output="create_result">
        Step 1 - Gather Requirements:
        - Component name and type
        - Props interface
        - State requirements

        Step 2 - Generate Component:
        - Create component file
        - Apply patterns from templates
        - Add TypeScript types
      </tasks>
      <goto to="validate"/>
    </stage>

    <!--
    ============================================
    TEST STAGE: Testing operations
    ============================================
    -->
    <stage id="test-stage">
      <print>Running tests...</print>
      <tasks output="test_result">
        Step 1 - Identify Test Targets:
        - Find related test files
        - Determine coverage gaps

        Step 2 - Execute Tests:
        - Run test suite
        - Collect results
      </tasks>
      <set var="tests_passed" from="test_result.passed"/>
      <goto when="${tests_passed} = false" to="fail"/>
      <goto to="complete"/>
    </stage>

    <!--
    ============================================
    A11Y CHECK: Accessibility audit
    ============================================
    -->
    <stage id="a11y-check">
      <print>Running accessibility audit...</print>
      <tasks output="a11y_result">
        Step 1 - Audit:
        - Check ARIA attributes
        - Verify keyboard navigation
        - Test color contrast

        Step 2 - Report:
        - List issues found
        - Suggest fixes
      </tasks>
      <goto to="complete"/>
    </stage>

    <!--
    ============================================
    GENERAL PROCESS: Default processing path
    ============================================
    -->
    <stage id="general-process">
      <tasks output="process_result">
        Step 1 - Process Request:
        - Apply skill capabilities
        - Follow domain guidelines
        - Generate output
      </tasks>
      <goto to="validate"/>
    </stage>

    <!--
    ============================================
    VALIDATE: Quality check
    ============================================
    -->
    <stage id="validate">
      <tasks output="validation">
        Step 1 - Validate Output:
        - Check against requirements
        - Verify completeness
        - Ensure quality standards met
      </tasks>
      <set var="valid" from="validation.passed"/>
      <goto when="${valid} = false" to="fail"/>
      <goto to="complete"/>
    </stage>

    <!--
    ============================================
    WORKFLOW INVOCATION: Call external workflow
    ============================================
    -->
    <stage id="invoke-workflow">
      <workflow src=".claude/workflows/quality-check.md" output="workflow_result">
        <param name="target" value="${target}"/>
      </workflow>
      <set var="workflow_status" from="workflow_result.status"/>
      <goto when="${workflow_status} = 'failed'" to="fail"/>
      <goto to="complete"/>
    </stage>

    <!--
    ============================================
    AGENT INVOCATION: Delegate to another agent
    ============================================
    -->
    <stage id="invoke-agent">
      <invoke name="Task" output="agent_result">
        <param name="subagent_type">my-agent</param>
        <param name="prompt"><![CDATA[
          - mode: analyze
          - target: ${target}
        ]]></param>
      </invoke>
      <set var="agent_output" from="agent_result.output"/>
      <goto to="complete"/>
    </stage>

    <!--
    ============================================
    COMPLETION STAGES
    ============================================
    -->
    <stage id="complete">
      <print>
        ## Task Complete
        Successfully processed request.
      </print>
      <stop kind="end"/>
    </stage>

    <stage id="fail">
      <print>
        ## Task Failed
        Unable to complete request. Please review and try again.
      </print>
      <stop kind="error"/>
    </stage>

  </execution>

  <understanding/>

</document>
```
