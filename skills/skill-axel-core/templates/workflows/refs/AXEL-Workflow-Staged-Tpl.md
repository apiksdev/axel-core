---
name: workflow-staged
description: Template for workflows with staged execution - supports sequential, branching, parallel, loop patterns
type: template
---

# AXEL Template: Workflow - Staged

```xml
<document type="workflow">

  <enforcement>
    - Read `src` and `ref` attributes from document references to locate files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
  </enforcement>

  <objective>
    Workflow with staged execution.
    Supports sequential, branching, parallel, and loop patterns with user interaction.
  </objective>

  <documents name="core" load="always" mode="context">
    <read src=".claude/BOOTSTRAP.md"/>
    <understanding>
      Bootstrap provides core AXEL rules and enforcement.
      Staged workflows may need additional context documents.
    </understanding>
  </documents>

  <execution flow="staged">

    <!--
    ============================================
    INPUT: Parse parameters from caller
    ============================================
    -->
    <stage id="init">
      <tasks output="params">
        Step 1 - Check Input Parameters:
        - Check if project_name passed via param (from caller)
        - Check if environment passed via param (from caller)
        - Check if mode passed via param (optional)
        - Default mode to "standard" if not specified
      </tasks>
      <set var="mode" from="params.mode"/>
      <print>
        ## Workflow Started
        Initializing process...
      </print>
      <!--
      Ask only for missing parameters.
      If called via <workflow> with <param>, values already set.
      -->
      <ask when="${project_name} = null">
        - project_name: "Project name:" default="my-project"
      </ask>
      <ask when="${environment} = null">
        - environment: "Environment:" default="development"
      </ask>
    </stage>

    <!--
    ============================================
    MODE ROUTING: Dynamic routing based on mode
    ============================================
    -->
    <stage id="route">
      <goto when="${mode} = 'quick'" to="quick-deploy"/>
      <goto when="${mode} = 'full'" to="prepare"/>
      <goto to="prepare"/>
    </stage>

    <!--
    ============================================
    MODE: quick - Skip tests and lint
    ============================================
    -->
    <stage id="quick-deploy">
      <print>Quick deploy mode - skipping quality checks...</print>
      <bash run="npm run deploy:${environment}"/>
      <set var="deploy_success" from="bash.exitcode = 0"/>
      <goto when="${deploy_success} = true" to="complete"/>
      <goto to="fail"/>
    </stage>

    <!--
    ============================================
    SEQUENTIAL: Stages execute in order
    ============================================
    -->

    <stage id="prepare">
      <print>Preparing **${project_name}** for ${environment}...</print>
      <tasks output="prepare_result">
        Step 1 - Setup:
        - Validate project structure
        - Check dependencies

        Step 2 - Install:
        - Run npm install
        - Verify installation
      </tasks>
      <bash run="npm install" path="./${project_name}"/>
    </stage>

    <!--
    ============================================
    PARALLEL: Multiple stages run concurrently
    ============================================
    -->
    <parallel id="quality-checks">
      <stage id="run-tests">
        <print>Running tests...</print>
        <bash run="npm test"/>
        <set var="tests_passed" from="bash.exitcode = 0"/>
      </stage>
      <stage id="run-lint">
        <print>Running linter...</print>
        <bash run="npm run lint"/>
        <set var="lint_passed" from="bash.exitcode = 0"/>
      </stage>
    </parallel>

    <!--
    ============================================
    BRANCHING: Conditional routing
    ============================================
    -->
    <stage id="check-results">
      <goto when="${tests_passed} = false" to="fail"/>
      <goto when="${lint_passed} = false" to="fail"/>
    </stage>

    <!--
    ============================================
    CONFIRM: User approval with options
    ============================================
    -->
    <confirm id="review">
      <print>
        ## Review Results

        | Check | Status |
        |-------|--------|
        | Tests | ${tests_passed} |
        | Lint | ${lint_passed} |

        **Options:**
        1. Approve - Continue to deploy
        2. Cancel - Abort workflow
      </print>
      <ask var="action" prompt="Your choice (1/2):" default="1">
        <goto when="${action} = '1'" to="deploy"/>
        <goto when="${action} = '2'" to="cancel"/>
      </ask>
    </confirm>

    <!--
    ============================================
    LOOP: Retry pattern
    ============================================
    -->
    <stage id="deploy">
      <print>Deploying to ${environment}...</print>
      <bash run="npm run deploy:${environment}"/>
      <set var="deploy_success" from="bash.exitcode = 0"/>
      <set var="retry_count" value="${retry_count} + 1"/>
      <goto when="${deploy_success} = false AND ${retry_count} < 3" to="deploy"/>
      <goto when="${deploy_success} = false" to="fail"/>
    </stage>

    <!--
    ============================================
    WORKFLOW: Trigger another workflow
    ============================================
    -->
    <stage id="post-deploy">
      <workflow src=".claude/workflows/health-check.md" output="health_result">
        <param name="target" value="${environment}"/>
      </workflow>
      <set var="health_status" from="health_result.status"/>
      <goto when="${health_status} = 'unhealthy'" to="rollback"/>
    </stage>

    <!--
    ============================================
    INVOKE: Call agents/skills
    ============================================
    -->
    <stage id="notify">
      <invoke name="Task" output="notify_result">
        <param name="subagent_type">Explore</param>
        <param name="prompt">
          Send deployment notification for ${project_name} to ${environment}.
          Include test and lint results.
        </param>
      </invoke>
      <set var="notification_sent" from="notify_result.success"/>
    </stage>

    <!--
    ============================================
    COMPLETION STAGES
    ============================================
    -->
    <stage id="complete">
      <print>
        ## Workflow Complete

        **Project:** ${project_name}
        **Environment:** ${environment}
        **Status:** Success
      </print>
      <stop kind="end"/>
    </stage>

    <stage id="fail">
      <print>
        ## Workflow Failed

        Please check logs and try again.
      </print>
      <stop kind="error"/>
    </stage>

    <stage id="cancel">
      <print>Workflow cancelled by user.</print>
      <stop kind="end"/>
    </stage>

    <stage id="rollback">
      <print>Health check failed. Rolling back...</print>
      <bash run="npm run rollback:${environment}"/>
      <goto to="fail"/>
    </stage>

  </execution>

  <output format="json">
    <![CDATA[
    {
      "status": "success|failed|cancelled",
      "mode": "quick|full|standard",
      "project_name": "my-project",
      "environment": "development|staging|production",
      "checks": {
        "tests_passed": true,
        "lint_passed": true
      },
      "deploy_success": true,
      "health_status": "healthy|unhealthy",
      "notification_sent": true,
      "retry_count": 0,
      "summary": "Deployed {project_name} to {environment} (mode: {mode})"
    }
    ]]>
  </output>

  <understanding/>

</document>
```
