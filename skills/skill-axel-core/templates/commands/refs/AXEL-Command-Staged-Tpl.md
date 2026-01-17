---
name: command-staged
description: Template for commands with staged execution - supports sequential, branching, loop patterns
type: template
---

# AXEL Template: Command - Staged

```xml
<document type="command" entry="cmd:main">

  <enforcement>
    - Read `src` and `ref` attributes from document references to locate files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
  </enforcement>

  <objective>
    Command with staged execution flow.
    Supports sequential, branching, and loop patterns within stages.
  </objective>

  <documents load="always" mode="context">
    <read src=".claude/BOOTSTRAP.md"/>
    <understanding>
      Bootstrap provides core AXEL rules and enforcement.
      Additional documents can be added based on command needs.
    </understanding>
  </documents>

  <variables>
    <var name="project" from="args.0"/>
    <var name="action" from="args.1"/>
    <var name="target" from="args.2"/>
  </variables>

  <!--
  ═══════════════════════════════════════════════════════════════
       ROUTING - Entry point
  ═══════════════════════════════════════════════════════════════
  -->

  <command id="cmd:main">
    <goto when="project == ''" to="help"/>
    <goto when="action == ''" to="list"/>
    <goto when="action == 'list'" to="list"/>
    <goto when="action == 'create'" to="init"/>
    <goto when="action == 'analyze'" to="analyze"/>
    <goto when="action == 'check'" to="run-workflow"/>
    <goto to="help"/>
  </command>

  <!--
  ═══════════════════════════════════════════════════════════════
       EXECUTION - All stages here
  ═══════════════════════════════════════════════════════════════
  -->

  <execution flow="staged">

    <!--
    ============================================
    HELP: Display usage information
    ============================================
    -->
    <stage id="help">
      <print>
        ## /axel:command-name

        Usage: /axel:command-name {project} {action} [target]

        Actions:
        - list              : List items
        - create {name}     : Create new item
        - analyze {name}    : Analyze item
        - check             : Run quality check workflow

        Examples:
          /axel:command-name myapp list
          /axel:command-name myapp create auth
          /axel:command-name myapp analyze api
          /axel:command-name myapp check
      </print>
      <stop kind="end"/>
    </stage>

    <!--
    ============================================
    SEQUENTIAL: List items
    ============================================
    -->
    <stage id="list">
      <tasks output="items">
        Step 1 - Find Items:
        - Glob for .claude/projects/${project}/items/*.md
        - Extract name and description from each

        Step 2 - Format Output:
        - Create numbered list
        - Show status if available
      </tasks>
      <print>
        ## Items - ${project}

        ${items}
      </print>
      <stop kind="end"/>
    </stage>

    <!--
    ============================================
    INPUT: Initialize with user input
    ============================================
    -->
    <stage id="init">
      <print>## Create New Item</print>
      <ask>
        - name: "Enter name:" default="${target}"
        - description: "Enter description:" default=""
      </ask>
      <set var="retry_count" value="0"/>
    </stage>

    <!--
    ============================================
    BRANCHING: Review and decide
    ============================================
    -->
    <stage id="review">
      <print>
        ## Review Configuration

        | Field | Value |
        |-------|-------|
        | Project | ${project} |
        | Name  | ${name} |
        | Description | ${description} |
      </print>
      <ask id="choice" prompt="What would you like to do?">
        <choice key="1" value="create" label="Create item"/>
        <choice key="2" value="edit" label="Edit values"/>
        <choice key="3" value="cancel" label="Cancel"/>
      </ask>
      <goto when="${choice.value} == 'create'" to="create"/>
      <goto when="${choice.value} == 'edit'" to="edit"/>
      <goto to="cancel"/>
    </stage>

    <stage id="edit">
      <print>Enter new values (leave empty to keep current):</print>
      <ask>
        - name: "New name:" default="${name}"
        - description: "New description:" default="${description}"
      </ask>
      <goto to="review"/>
    </stage>

    <!--
    ============================================
    INVOKE: Call agent for creation
    ============================================
    -->
    <stage id="create">
      <print>Creating ${name}...</print>
      <invoke name="Task" output="create_result">
        <param name="subagent_type">my-custom-agent</param>
        <param name="prompt"><![CDATA[
          - mode: create
          - project: ${project}
          - name: ${name}
          - description: ${description}
        ]]></param>
      </invoke>
      <set var="create_status" from="create_result.status"/>
      <goto when="${create_status} == 'failed'" to="fail"/>
      <goto to="complete"/>
    </stage>

    <!--
    ============================================
    ANALYZE: Multi-step analysis with agent chain
    ============================================
    -->
    <stage id="analyze">
      <print>## Analyzing ${target}...</print>
      <invoke name="Task" output="analysis">
        <param name="subagent_type">axel:agent-project-analysis</param>
        <param name="prompt"><![CDATA[
          - mode: analyze
          - project: ${project}
          - target: ${target}
        ]]></param>
      </invoke>
      <set var="findings" from="analysis.findings"/>
    </stage>

    <stage id="show-analysis">
      <print>
        ## Analysis Results

        ${findings}

        ---
      </print>
      <ask id="next_action" prompt="What would you like to do?">
        <choice key="1" value="tasks" label="Create implementation tasks"/>
        <choice key="2" value="done" label="Done"/>
      </ask>
      <goto when="${next_action.value} == 'tasks'" to="create-tasks"/>
      <goto to="complete"/>
    </stage>

    <stage id="create-tasks">
      <invoke name="Task" output="tasks_result">
        <param name="subagent_type">axel:agent-project-tasks</param>
        <param name="prompt"><![CDATA[
          - mode: generate
          - project: ${project}
          - analysis: ${findings}
        ]]></param>
      </invoke>
      <print>Tasks created successfully.</print>
      <goto to="complete"/>
    </stage>

    <!--
    ============================================
    WORKFLOW: Run external workflow
    ============================================
    -->
    <stage id="run-workflow">
      <print>Running quality check workflow...</print>
      <workflow src=".claude/workflows/quality-check.md" output="workflow_result">
        <param name="project" value="${project}"/>
        <param name="environment" value="staging"/>
      </workflow>
      <set var="workflow_status" from="workflow_result.status"/>
      <goto when="${workflow_status} == 'failed'" to="fail"/>
      <goto to="complete"/>
    </stage>

    <!--
    ============================================
    LOOP: Retry pattern
    ============================================
    -->
    <stage id="validate">
      <tasks output="validation">
        Step 1 - Check:
        - Verify created item exists
        - Validate structure
      </tasks>
      <set var="is_valid" from="validation.passed"/>
      <set var="retry_count" value="${retry_count} + 1"/>
      <goto when="${is_valid} == false AND ${retry_count} < 3" to="create"/>
      <goto when="${is_valid} == false" to="fail"/>
      <goto to="complete"/>
    </stage>

    <!--
    ============================================
    COMPLETION STAGES
    ============================================
    -->
    <stage id="complete">
      <print>
        ## Completed

        Operation finished successfully.
      </print>
      <stop kind="end"/>
    </stage>

    <stage id="fail">
      <print>
        ## Failed

        Operation failed after ${retry_count} attempts.
      </print>
      <stop kind="error"/>
    </stage>

    <stage id="cancel">
      <print>Operation cancelled.</print>
      <stop kind="end"/>
    </stage>

  </execution>

  <understanding/>

</document>
```
