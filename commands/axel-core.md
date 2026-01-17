---
name: axel:core
description: Execute skill-axel-core with trigger-based workflow dispatch
type: command
model: inherit
allowed-tools: []
---

# AXEL Command: Core

```xml
<document type="command" entry="cmd:main">

  <enforcement>
    <![CDATA[
    PATH RESOLUTION:
    - Read the `src`, `ref`, or `target` attribute from the document XML to locate referenced files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory

    DELEGATION:
    - This command delegates all work to skill-axel-core
    - skill-axel-core handles trigger-based workflow dispatch
    - No direct tool usage in this command
    ]]>
  </enforcement>

  <objective>
    Execute skill-axel-core for AXEL core operations.
    Delegates to skill-axel-core which routes to appropriate workflows based on trigger.
  </objective>

  <variables>
    <var name="arguments" from="args.*"/>
  </variables>

  <command id="cmd:main">
    <goto to="execute"/>
  </command>

  <execution flow="staged">
    <!-- execute: Invoke skill-axel-core with arguments -->
    <stage id="execute">
      <invoke name="Skill">
        <param name="skill">axel-core:skill-axel-core</param>
        <param name="args">${arguments}</param>
      </invoke>
      <stop kind="end"/>
    </stage>
  </execution>

  <understanding/>

</document>
```
