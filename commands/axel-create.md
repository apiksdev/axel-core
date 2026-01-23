---
name: axel:create
description: Create AXEL documents (agent, workflow, skill, command)
type: command
allowed-tools:
  - Skill
---

# AXEL Command: /axel:create

```xml
<document type="command" entry="cmd:main">

  <enforcement>
    <![CDATA[
    ROUTER COMMAND:
    - Parses args to determine document type
    - Builds trigger as create:{type}
    - Sends explicit trigger and parameters to skill

    VALID TYPES:
    - agent → create:agent
    - workflow → create:workflow
    - skill → create:skill
    - command → create:command
    - bootstrap → create:bootstrap
    ]]>
  </enforcement>

  <objective>
    Router for skill-axel-core creator operations.
    Determines document type from args and delegates to appropriate creator workflow.
  </objective>

  <variables>
    <var name="doc_type" from="args.0"/>
    <var name="topic" from="args.1"/>
  </variables>

  <command id="cmd:main">
    <goto when="${doc_type} = ''" to="show-usage"/>
    <goto when="${doc_type} = agent" to="route"/>
    <goto when="${doc_type} = workflow" to="route"/>
    <goto when="${doc_type} = skill" to="route"/>
    <goto when="${doc_type} = command" to="route"/>
    <goto when="${doc_type} = bootstrap" to="route"/>
    <goto to="show-usage"/>
  </command>

  <execution flow="staged">

    <!-- show-usage: Display available types -->
    <stage id="show-usage">
      <print>
        ## /axel:create Usage

        Create AXEL documents with:

            /axel:create {type} [topic]

        **Available types:**
        - `agent` - Autonomous task executor
        - `workflow` - Multi-step process
        - `skill` - Expert role definition
        - `command` - Slash command definition
        - `bootstrap` - Project bootstrap file with document references

        **Examples:**
        - `/axel:create agent` - Create new agent
        - `/axel:create workflow data-migration` - Create workflow with topic
        - `/axel:create skill` - Create new skill
        - `/axel:create command` - Create new command
        - `/axel:create bootstrap` - Create project bootstrap file
      </print>
      <stop kind="end"/>
    </stage>

    <!-- route: Delegate to skill with create:{type} trigger -->
    <stage id="route">
      <invoke name="Skill">
        <param name="skill" value="axel-core:skill-axel-core"/>
        <param name="trigger" value="create:${doc_type}"/>
        <param name="topic" value="${topic}"/>
      </invoke>
      <stop kind="end"/>
    </stage>

  </execution>

  <understanding/>

</document>
```
