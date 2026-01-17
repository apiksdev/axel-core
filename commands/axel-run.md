---
name: axel:run
description: Execute a single AXEL workflow file
type: command
allowed-tools:
  - Read
  - Write
  - Edit
  - Task
  - Glob
  - Bash
  - AskUserQuestion
---

# AXEL Command: /axel:run

```xml
<document type="command" entry="cmd:main">

  <enforcement>
    <![CDATA[
    - Read the `src`, `ref`, or `target` attribute from the document XML to locate referenced files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory

    SEMANTIC:
    - "run" = execute single workflow file
    - Fire-and-forget (stateless)
    - Workflow-only execution
    ]]>
  </enforcement>

  <objective>
    Execute a single AXEL workflow file.
    Stateless execution for workflow documents.
  </objective>

  <documents name="core" load="always" mode="context">
    <read src="${CLAUDE_PLUGIN_ROOT}/AXEL-Bootstrap.md"/>
    <understanding>
      !! MANDATORY: READ -> UNDERSTAND -> APPLY !!
      Bootstrap provides AXEL syntax and execution rules.
    </understanding>
  </documents>

  <variables>
    <var name="args" from="$ARGUMENTS"/>
    <var name="plugin_root" value="${CLAUDE_PLUGIN_ROOT}"/>
    <var name="file_path" value=""/>
  </variables>

  <command id="cmd:main">
    <goto when="args = 'help'" to="help"/>
    <goto when="args = ''" to="help"/>
    <goto to="execute"/>
  </command>

  <execution flow="staged">

    <!-- help: Show usage -->
    <stage id="help">
      <print>
        ## /axel:run

        Execute a single AXEL workflow file.

        **Usage:**
          /axel:run {workflow.md}    - Execute the workflow

        **Examples:**
          /axel:run .claude/workflows/my-workflow.md
          /axel:run .claude/workflows/build-deploy.md

        **Note:**
          - Workflow-only execution (stateless)
          - For todo management, use `/axel:todos` commands
      </print>
      <stop kind="end"/>
    </stage>

    <!-- execute: Run the workflow -->
    <stage id="execute">
      <set var="file_path" value="${args}"/>
      <print>## Running workflow: ${file_path}</print>
      <invoke name="Task" output="result">
        <param name="subagent_type">axel-core:agent-axel-runner:agent-axel-runner</param>
        <param name="description">Run: ${file_path}</param>
        <param name="prompt"><![CDATA[
          PLUGIN_ROOT: ${plugin_root}
          axel_file_path: ${file_path}
        ]]></param>
      </invoke>
      <goto to="show_result"/>
    </stage>

    <!-- show_result: Display result -->
    <stage id="show_result">
      <print>
        ## Workflow Execution Complete

        **Workflow:** ${file_path}
        **Status:** ${result.status}
      </print>
      <stop kind="end"/>
    </stage>

  </execution>

  <understanding/>

</document>
```
