---
name: axel:install
description: Initialize AXEL structure with folders and configuration files
type: command
allowed-tools:
  - Skill
---

# AXEL Command: /axel:install

```xml
<document type="command" entry="cmd:main">

  <enforcement>
    <![CDATA[
    ROUTER COMMAND:
    - Delegates directly to skill
    - Skill handles parameter collection and installation
    ]]>
  </enforcement>

  <objective>
    Router for skill-axel-core install operations.
    Delegates to skill for parameter collection and execution.
  </objective>

  <command id="cmd:main">
    <goto to="route_install"/>
  </command>

  <execution flow="staged">

    <!-- route_install: Delegate to skill -->
    <stage id="route_install">
      <invoke name="Skill">
        <param name="skill" value="axel-core:skill-axel-core"/>
        <param name="trigger" value="install"/>
      </invoke>
      <stop kind="end"/>
    </stage>

  </execution>

  <understanding/>

</document>
```
