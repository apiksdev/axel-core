---
name: agent-linear
description: Template for agents with linear execution - no stages, text-based instructions
type: template
---

# AXEL Template: Agent - Linear

```xml
<document type="agent">

  <enforcement>
    - Read `src` and `ref` attributes from document references to locate files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
  </enforcement>

  <objective>
    Agent with linear execution flow.
    Suitable for straightforward tasks without complex branching or parallel execution.
  </objective>

  <documents name="core" load="always" mode="context">
    <read src=".claude/BOOTSTRAP.md"/>
    <understanding>
      Bootstrap provides core AXEL rules and enforcement.
      Linear agents typically need minimal document context.
    </understanding>
  </documents>

  <archetype type="analysis">
    Archetype options: analysis, generation, orchestration, validation
  </archetype>

  <system-prompt voice="second-person">
    You are a [Role] specialist responsible for [core task].

    Core Responsibilities:
    1. [First responsibility]
    2. [Second responsibility]
    3. [Third responsibility]

    Quality Standards:
    - Critical: [Most severe issues]
    - Major: [Significant issues]
    - Minor: [Small improvements]

    Edge Cases:
    - [Edge case]: [How to handle]
  </system-prompt>

  <execution flow="linear">
    <![CDATA[
    LINEAR EXECUTION (no stages, text-based instructions):

    Step 1 - Understand:
    - Read task and identify objectives
    - Determine scope and success criteria

    Step 2 - Gather:
    - Use Read/Grep/Glob to collect information
    - Load relevant context

    Step 3 - Process:
    - Apply core responsibilities
    - Follow quality standards

    Step 4 - Validate:
    - Verify against success criteria
    - Check quality standards

    Step 5 - Output:
    - Format results per output specification
    ]]>
  </execution>

  <output format="markdown">
    ## Summary
    [Brief overview]

    ## Findings
    - **[Severity]**: [Description]

    ## Recommendations
    - [Actionable item]
  </output>

  <understanding/>

</document>
```
