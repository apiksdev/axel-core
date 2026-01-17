---
name: workflow-linear
description: Template for workflows with linear execution - no stages, simple sequential steps
type: template
---

# AXEL Template: Workflow - Linear

```xml
<document type="workflow">

  <enforcement>
    - Read `src` and `ref` attributes from document references to locate files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
  </enforcement>

  <objective>
    Workflow with linear execution.
    Simple sequential process without stages, branching, or parallel execution.
  </objective>

  <documents name="core" load="always" mode="context">
    <read src=".claude/BOOTSTRAP.md"/>
    <understanding>
      Bootstrap provides core AXEL rules and enforcement.
      Linear workflows need minimal document context.
    </understanding>
  </documents>

  <execution flow="linear">
    <![CDATA[
    LINEAR WORKFLOW (no stages, text-based):

    Step 1 - Initialize:
    - Set up required variables
    - Validate prerequisites

    Step 2 - Execute:
    - Perform main task
    - Process input data

    Step 3 - Finalize:
    - Generate output
    - Clean up resources

    Example use cases:
    - Simple data transformation
    - Single-step automation
    - Basic file processing
    ]]>
  </execution>

  <understanding/>

</document>
```
