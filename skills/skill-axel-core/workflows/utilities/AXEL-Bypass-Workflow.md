---
name: axel-bypass-workflow
description: Toggle Claude Code permission bypass mode on/off
type: workflow
triggers:
  - bypass
  - permissions
allowed-tools:
  - Read
  - Bash
  - AskUserQuestion
---

# AXEL Workflow: Bypass Permissions

```xml
<document type="workflow">

  <enforcement>
    <![CDATA[
    PATH RESOLUTION:
    - Read the `src`, `ref`, or `target` attribute from the document XML to locate referenced files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory

    BYPASS RULES:
    - Toggle affects settings.local.json in project .claude/ directory
    - Always confirm with user before making changes
    - Python script handles the actual toggle operation
    ]]>
  </enforcement>

  <objective>
    Toggle permission bypass mode in Claude Code settings.
    When enabled, all permission prompts are skipped.
    When disabled, normal permission flow applies.
  </objective>

  <variables>
    <var name="plugin_root" value="${CLAUDE_PLUGIN_ROOT}"/>
    <var name="script_path" value="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/scripts/axel_bypass.py"/>
    <var name="action" from="param.action" default=""/>
  </variables>

  <execution flow="staged">

    <!-- init: Route based on action parameter -->
    <stage id="init">
      <goto when="action == 'on'" to="check-enable"/>
      <goto when="action == 'off'" to="check-disable"/>
      <goto when="action == 'status'" to="show-status"/>
      <goto to="check-toggle"/>
    </stage>

    <!-- show-status: Display current bypass status -->
    <stage id="show-status">
      <bash output="status_result"><![CDATA[
PYTHONIOENCODING=utf-8 python "${script_path}" --cwd "${cwd}" --action status
      ]]></bash>
      <print>
        ## Bypass Mode Status

        ${status_result}
      </print>
      <stop kind="end"/>
    </stage>

    <!-- check-toggle: Get status and ask for toggle confirmation -->
    <stage id="check-toggle">
      <bash output="status_result"><![CDATA[
PYTHONIOENCODING=utf-8 python "${script_path}" --cwd "${cwd}" --action status
      ]]></bash>
      <goto to="confirm-toggle"/>
    </stage>

    <!-- confirm-toggle: Ask user to confirm toggle -->
    <stage id="confirm-toggle">
      <print>
        ## Toggle Bypass Mode

        Current status: ${status_result}
      </print>
      <ask var="confirm" prompt="Toggle bypass mode? (yes/no)">
        <goto when="${confirm} == 'yes'" to="execute-toggle"/>
        <goto to="cancelled"/>
      </ask>
    </stage>

    <!-- execute-toggle: Run toggle action -->
    <stage id="execute-toggle">
      <bash output="toggle_result"><![CDATA[
PYTHONIOENCODING=utf-8 python "${script_path}" --cwd "${cwd}" --action toggle
      ]]></bash>
      <goto to="done"/>
    </stage>

    <!-- check-enable: Confirm before enabling -->
    <stage id="check-enable">
      <bash output="status_result"><![CDATA[
PYTHONIOENCODING=utf-8 python "${script_path}" --cwd "${cwd}" --action status
      ]]></bash>
      <print>
        ## Enable Bypass Mode

        Current status: ${status_result}
      </print>
      <ask var="confirm" prompt="Enable bypass mode? All permission prompts will be skipped. (yes/no)">
        <goto when="${confirm} == 'yes'" to="execute-enable"/>
        <goto to="cancelled"/>
      </ask>
    </stage>

    <!-- execute-enable: Run enable action -->
    <stage id="execute-enable">
      <bash output="toggle_result"><![CDATA[
PYTHONIOENCODING=utf-8 python "${script_path}" --cwd "${cwd}" --action enable
      ]]></bash>
      <goto to="done"/>
    </stage>

    <!-- check-disable: Confirm before disabling -->
    <stage id="check-disable">
      <bash output="status_result"><![CDATA[
PYTHONIOENCODING=utf-8 python "${script_path}" --cwd "${cwd}" --action status
      ]]></bash>
      <print>
        ## Disable Bypass Mode

        Current status: ${status_result}
      </print>
      <ask var="confirm" prompt="Disable bypass mode? Permission prompts will be shown. (yes/no)">
        <goto when="${confirm} == 'yes'" to="execute-disable"/>
        <goto to="cancelled"/>
      </ask>
    </stage>

    <!-- execute-disable: Run disable action -->
    <stage id="execute-disable">
      <bash output="toggle_result"><![CDATA[
PYTHONIOENCODING=utf-8 python "${script_path}" --cwd "${cwd}" --action disable
      ]]></bash>
      <goto to="done"/>
    </stage>

    <!-- done: Show result -->
    <stage id="done">
      <print>
        ## Result

        ${toggle_result}
      </print>
      <stop kind="end"/>
    </stage>

    <!-- cancelled: User cancelled operation -->
    <stage id="cancelled">
      <print>Operation cancelled.</print>
      <stop kind="end"/>
    </stage>

  </execution>

  <understanding/>

</document>
```
