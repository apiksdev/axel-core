---
name: axel:bypass-permissions
description: Toggle Claude Code permission bypass mode on/off
type: command
allowed-tools:
  - Skill
---

# AXEL Command: /axel:bypass-permissions

```xml
<document type="command" entry="cmd:main">

  <enforcement>
    <![CDATA[
    ROUTER COMMAND:
    - Parses args to determine action
    - Sends explicit trigger and parameters to skill
    ]]>
  </enforcement>

  <objective>
    Router for skill-axel-core bypass operations.
    Determines action from args and delegates to skill.
  </objective>

  <variables>
    <var name="action" from="args.0"/>
  </variables>

  <command id="cmd:main">
    <goto to="route"/>
  </command>

  <execution flow="staged">

    <!-- route: Delegate to skill with action parameter -->
    <stage id="route">
      <invoke name="Skill">
        <param name="skill" value="axel-core:skill-axel-core"/>
        <param name="trigger" value="bypass"/>
        <param name="action" value="${action}"/>
      </invoke>
      <stop kind="end"/>
    </stage>

  </execution>

  <understanding/>

</document>
```
