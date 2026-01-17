---
name: command-creator-workflow
description: Command document creator - collects requirements and generates AXEL command documents
type: workflow
triggers:
  - create command
  - command creator
  - new command
---

# AXEL Workflow: Command Creator

```xml
<document type="workflow">

  <enforcement>
    <![CDATA[
    PATH RESOLUTION:
    - Read the `src`, `ref`, or `target` attribute from the document XML to locate referenced files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory

    REFERENCE-BASED CREATION:
    - ALWAYS read AXEL-Command.md for structure, implementation steps, and validation
    - DO NOT duplicate content from reference documents
    - Reference documents are already loaded - use them as source of truth
    ]]>
  </enforcement>

  <objective>
    Create AXEL command documents through structured inquiry using reference-based approach.
    All specifications, principles, and patterns are read from AXEL-Command.md.
  </objective>

  <variables>
    <var name="topic" from="param.topic"/>
    <var name="context" from="param.context" default=""/>
  </variables>

  <documents load="always" mode="context">
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/references/AXEL-Command.md"/>
    <understanding>
      <![CDATA[
      !! MANDATORY: READ -> UNDERSTAND -> APPLY !!

      Bootstrap: Already loaded via skill-axel-core

      AXEL-Command.md provides:
      - <axel-tag-structure>: Element order and document hierarchy
      - <implementation name="steps">: Step-by-step creation process (Step 1-8)
      - <checklist name="command-creation">: Complete validation checklist
      - <frontmatter>: Specification and naming conventions
      - <principle>: routing-vs-execution, entry-first, explicit-termination, enforcement-clarity
      - <pattern>: simple-command, interactive-command
      - <decision>: plugin-root-variable, argument-access-pattern, goto-stage-only

      Commands have TWO PARTS:
      - ROUTING: cmd:main block (only goto tags)
      - EXECUTION: stages block (actual work)

      This workflow orchestrates the process - all content comes from reference.
      ]]>
    </understanding>
  </documents>

  <execution flow="linear">
    <![CDATA[
    LINEAR EXECUTION - Reference-based command creation:

    Step 1 - Understand Document Structure:
    - Read AXEL-Command.md <axel-tag-structure>
    - Understand element order: frontmatter → objective → variables → command (routing) → execution (stages)
    - Identify required vs optional elements
    - Know TWO PARTS separation: routing (cmd:main) vs execution (stages)

    Step 2 - Follow Implementation Guide:
    - Read AXEL-Command.md <implementation name="steps">
    - This defines Step 1-8 creation process
    - Each step collects specific information needed for command document

    Step 3 - Collect Identity (Implementation Step 1):
    - Ask user for command name:
      * Plugin commands: plugin:command-name format
      * Project commands: kebab-case format
    - Ask for description (max 200 chars)
    - Reference: AXEL-Command.md <frontmatter> for naming rules

    Step 4 - Configure Command (Implementation Step 2-3):
    - Model: inherit | sonnet | opus | haiku
    - Allowed tools: Read, Write, Edit, Glob, Grep, Bash, Task, WebFetch, WebSearch
    - Document type="command" and entry="cmd:main"
    - Objective: 1-3 sentences describing what command does

    Step 5 - Define Variables (Implementation Step 4):
    - Identify command arguments needed
    - Use AXEL-Command.md <decision name="argument-access-pattern">:
      * args.0, args.1, args.* (AXEL pattern)
      * $1, $2, $ARGUMENTS (native pattern)
    - Set variable sources: from="args.N" or ask="prompt"
    - Set defaults with value="..."

    Step 6 - Design Routing (Implementation Step 5):
    - Reference: AXEL-Command.md <principle name="routing-vs-execution">
    - cmd:main contains ONLY <goto> tags for branching
    - Route to appropriate stage based on arguments
    - NO business logic in routing
    - Example structure (routing in cmd:main):
      * <goto when="args.0 == 'help'" to="help"/>
      * <goto when="args.0 == 'list'" to="list"/>
      * <goto when="args.0 == 'create'" to="create"/>

    Step 7 - Design Execution Stages (Implementation Step 6):
    - Reference: AXEL-Command.md <pattern>
    - Choose pattern:
      * simple-command: Basic list/create/edit without loops
      * interactive-command: With loops (approval, validation, agent chaining)
    - Identify stages needed
    - Each stage must end with <stop> or <goto>
    - Principle: <principle name="explicit-termination">
      * stop kind="end" for success
      * stop kind="error" for errors
    - All stages must be inside <execution> wrapper

    Step 8 - Map Pattern to Stages:
    - If simple pattern:
      * routing → stage → stop
      * Each stage does one thing
      * Example: <stage id="list">...<stop kind="end"/></stage>
    - If interactive pattern:
      * Approval flow: init → review ↔ edit → execute
      * Agent chain: analyze → plan → approve ↔ revise → execute
      * Validation loop: generate → validate ↔ fix → verify
      * Example with when conditions in stages:
        <stage id="review">
          <ask var="action" prompt="Approve?"/>
          <goto when="${action} == 'edit'" to="edit"/>
          <goto when="${action} == 'approve'" to="execute"/>
        </stage>

    Step 9 - Validate Requirements (Implementation Step 7):
    - Use AXEL-Command.md <checklist name="command-creation">
    - Check: frontmatter, structure, routing, stages, variables
    - Verify:
      * Single cmd:main for routing only
      * All stages inside <execution> wrapper
      * Each stage has unique id
      * Every stage ends with stop or goto
      * All goto targets exist as stage ids
    - If missing information → ask user for clarification
    - If validation fails → return to relevant step

    Step 10 - Generate Document (Implementation Step 8):
    - Apply AXEL-Command.md <axel-tag-structure> element order
    - Use appropriate template based on pattern choice (simple/interactive)
    - Map collected data to document structure:
      * Frontmatter (name, description, type, model, allowed-tools)
      * XML document start (type="command" entry="cmd:main")
      * Objective
      * Variables (if any)
      * Command block (routing only)
      * Execution block (all stages)
      * Understanding (empty, at end)
    - Path: .claude/commands/${name}.md

    Step 11 - Final Verification:
    - Validate against AXEL-Checklist.md standards
    - Verify: frontmatter format, document structure, element order
    - Check execution-validation rules
    - Ensure understanding element at document end
    - Verify principle compliance:
      * routing-vs-execution: cmd:main has only goto, stages have work
      * entry-first: entry="cmd:main" is set
      * explicit-termination: all paths end with stop

    Step 12 - Save and Confirm:
    - Create file: .claude/commands/${name}.md
    - Display file path and creation confirmation
    - Output: {content, name, path}
    ]]>
  </execution>

  <output format="json">
    {
      "content": "generated command document",
      "name": "command name",
      "path": "file save path"
    }
  </output>

  <understanding/>

</document>
```
