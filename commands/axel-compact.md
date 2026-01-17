---
name: axel:compact
description: Compact memories (session/learned) to archive
type: command
allowed-tools:
  - Skill
---

# AXEL Command: /axel:compact

```xml
<document type="command" entry="cmd:main">

  <enforcement>
    <![CDATA[
    ROUTER COMMAND:
    - Parses args to determine action and type
    - Sends explicit trigger and parameters to skill
    ]]>
  </enforcement>

  <objective>
    Router for skill-axel-core compact operations.
    Determines action from args and delegates to skill.
  </objective>

  <variables>
    <var name="action" from="args.0"/>
    <var name="param1" from="args.1"/>
  </variables>

  <command id="cmd:main">
    <goto when="action = ''" to="help"/>
    <goto when="action = 'memories'" to="route"/>
    <goto to="help"/>
  </command>

  <execution flow="staged">

    <!-- help: Show usage -->
    <stage id="help">
      <print>
        ## /axel:compact

        **Usage:**
          /axel:compact memories session  - Archive session memories
          /axel:compact memories learned  - Archive learned memories
      </print>
      <stop kind="end"/>
    </stage>

    <!-- route: Delegate to skill with parameters -->
    <stage id="route">
      <invoke name="Skill">
        <param name="skill" value="axel-core:skill-axel-core"/>
        <param name="trigger" value="compact"/>
        <param name="action" value="${action}"/>
        <param name="type" value="${param1}"/>
      </invoke>
      <stop kind="end"/>
    </stage>

  </execution>

  <understanding/>

</document>
```
