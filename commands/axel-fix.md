---
name: axel:fix
description: Validate AXEL document against Bootstrap rules, show numbered inconsistencies, and apply user-selected fixes
type: command
allowed-tools:
  - Skill
---

# AXEL Command: /axel:fix

```xml
<document type="command" entry="cmd:main">

  <enforcement>
    <![CDATA[
    ROUTER COMMAND:
    - Parses args to get target path
    - Sends explicit trigger and parameters to skill
    ]]>
  </enforcement>

  <objective>
    Router for skill-axel-core validate operations.
    Determines target from args and delegates to skill.
  </objective>

  <variables>
    <var name="target_path" from="args.0"/>
  </variables>

  <command id="cmd:main">
    <goto when="target_path = ''" to="help"/>
    <goto to="route_validate"/>
  </command>

  <execution flow="staged">

    <!-- help: Show usage -->
    <stage id="help">
      <print>
        ## /axel:fix

        **Usage:**
          /axel:fix {path}  - Validate and fix AXEL document

        **Example:**
          /axel:fix skills/my-skill/SKILL.md
      </print>
      <stop kind="end"/>
    </stage>

    <!-- route_validate: Delegate to skill -->
    <stage id="route_validate">
      <invoke name="Skill">
        <param name="skill" value="axel-core:skill-axel-core"/>
        <param name="trigger" value="fix"/>
        <param name="target_path" value="${target_path}"/>
      </invoke>
      <stop kind="end"/>
    </stage>

  </execution>

  <understanding/>

</document>
```
