---
name: axel:brainstorm
description: Start AXEL brainstorming session for discovery and ideation
type: command
allowed-tools:
  - Skill
---

# AXEL Command: /axel:brainstorm

```xml
<document type="command" entry="cmd:main">

  <enforcement>
    <![CDATA[
    ROUTER COMMAND:
    - Parses args to determine topic
    - Sends explicit trigger and parameters to skill
    ]]>
  </enforcement>

  <objective>
    Router for skill-axel-core brainstorm operations.
    Delegates to skill with brainstorm trigger.
  </objective>

  <variables>
    <var name="topic" from="args.0"/>
  </variables>

  <command id="cmd:main">
    <goto to="route"/>
  </command>

  <execution flow="staged">

    <!-- route: Delegate to skill with brainstorm trigger -->
    <stage id="route">
      <invoke name="Skill">
        <param name="skill" value="axel-core:skill-axel-core"/>
        <param name="trigger" value="create:brainstorm"/>
        <param name="topic" value="${topic}"/>
      </invoke>
      <stop kind="end"/>
    </stage>

  </execution>

  <understanding/>

</document>
```
