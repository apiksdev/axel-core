---
name: command-linear
description: Template for commands with linear execution - single purpose, no stages, no subcommands
type: template
---

# AXEL Template: Command - Linear

```xml
<document type="command">

  <enforcement>
    - Read `src` and `ref` attributes from document references to locate files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
  </enforcement>

  <objective>
    Single-purpose command with linear execution.
    No subcommands, no stages - just one action.
  </objective>

  <documents load="always" mode="context">
    <read src=".claude/BOOTSTRAP.md"/>
    <understanding>
      Bootstrap provides core AXEL rules and enforcement.
      Linear commands need minimal document context.
    </understanding>
  </documents>

  <variables>
    <var name="target" from="args.0"/>
  </variables>

  <execution flow="linear">
    <![CDATA[
    LINEAR COMMAND (single purpose, text-based):

    Step 1 - Validate Input:
    - Check if target provided
    - Verify target exists and is valid format

    Step 2 - Execute:
    - Perform the single action
    - Process target as needed

    Step 3 - Output:
    - Display results to user
    - Show success/failure message

    Example:
    /axel:command-name target.md
    ]]>
  </execution>

  <understanding/>

</document>
```
