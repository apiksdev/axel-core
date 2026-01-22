---
name: axel:research
description: Start AXEL research session - comprehensive research with Pure Markdown output
type: command
allowed-tools:
  - Skill
---

# AXEL Command: /axel:research

```xml
<document type="command" entry="cmd:main">

  <enforcement>
    <![CDATA[
    ROUTER COMMAND:
    - Parses args to determine topic or file path
    - Sends explicit trigger and parameters to skill
    - Topic can be new subject OR existing research file path
    ]]>
  </enforcement>

  <objective>
    Router for skill-axel-core research operations.
    Delegates to skill with research trigger.
    Supports new research or continuing existing research via file path.
  </objective>

  <variables>
    <var name="topic" from="args.*"/>
  </variables>

  <command id="cmd:main">
    <goto to="route"/>
  </command>

  <execution flow="staged">

    <!-- route: Delegate to skill with research trigger -->
    <stage id="route">
      <invoke name="Skill">
        <param name="skill" value="axel-core:skill-axel-core"/>
        <param name="trigger" value="research"/>
        <param name="topic" value="${topic}"/>
      </invoke>
      <stop kind="end"/>
    </stage>

  </execution>

  <understanding/>

</document>
```
