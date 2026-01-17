---
name: axel-workflow
description: Structure of workflow files - stage-based flow with tasks and parallel execution
type: reference
---

```xml
<document type="reference">

  <enforcement>
    - Read `src` and `ref` attributes from workflow references to locate files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
    - Workflow files located in .claude/workflows/ directory
  </enforcement>

  <objective>
    Structure of workflow definition files. AXEL Workflow is an XML-based configuration format that defines and manages multi-step processes. It coordinates user interaction, API calls, file operations, and AI tasks within a single flow.
  </objective>

  <frontmatter>
    <![CDATA[
---
name: workflow-deploy              # Workflow name (kebab-case)
description: Deploy notification   # Short description, max 200 characters
type: workflow                     # Always "workflow"
triggers:                          # Triggering keywords
  - deploy
  - notification
---
    ]]>
  </frontmatter>

  <templates name="templates" load="always" mode="context">
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/workflows/AXEL-Workflow-Template-Bootstrap.md"/>
    <axel-tag-structure>
      <![CDATA[
      AXEL-Workflow-{Type}-Tpl.md
      +-- Template Frontmatter
      +-- # AXEL Workflow: {Type} (title)
      +-- {{{xml}}}
      +-- <document type="workflow">
      |   +-- <enforcement>
      |   +-- <objective>
      |   +-- <documents name=".." load="always" mode="context">
      |   |   +-- <read src="..."/>
      |   |   +-- <understanding>...</understanding> (required)
      |   +-- <documents name=".." load="on-trigger" mode="context">
      |   |   +-- <read src="..." trigger="..."/>
      |   |   +-- <understanding>...</understanding> (required)
      |   +-- <documents name=".." load="on-demand" mode="context">
      |   |   +-- <read src="..." ask="..."/>
      |   |   +-- <understanding>...</understanding> (required)
      |   +-- <templates name=".." load="always|on-demand|on-trigger" mode="context"> (optional)
      |   |   +-- <read src="..." ask="..."/>
      |   |   +-- <understanding>...</understanding> (required)
      |   +-- <variables> (optional)
      |   |   +-- <var name="..." value="..."/>
      |   |   +-- <var name="..." from="param.*|args.*"/>
      |   |   +-- <var name="..." ask="user"/>
      |   +-- <skills name=".." load="on-demand"> (optional)
      |   |   +-- <ref src="..." ask="..."/>
      |   +-- <agents name=".." load="on-demand"> (optional)
      |   |   +-- <ref src="..." ask="..."/>
      |   +-- <triggers> (optional, for staged only)
      |   |   +-- <goto trigger="..." to="stage-id"/>
      |   +-- <execution flow="linear|staged">
      |   |   +-- (linear) text-based step instructions
      |   |   +-- (staged) <stage id="...">
      |   |       +-- <print>...</print>
      |   |       +-- <tasks output="...">...</tasks>
      |   |       +-- <bash run="..."/>
      |   |       +-- <workflow src="..." output="...">
      |   |       |   +-- <param name="..." value="..."/>
      |   |       +-- <call command="/..."/>
      |   |       +-- <ask var="..." prompt="...">
      |   |       |   +-- <goto when="..." to="stage-id"/>
      |   |       +-- <invoke name="Task|Skill" output="..." resumable="true|false">
      |   |       |   +-- <param name="..." value="..."/>
      |   |       +-- <set var="..." from="..."/>
      |   |       +-- <goto when="..." to="stage-id"/>
      |   |       +-- <stop kind="end|error"/>
      +-- </document>
      +-- {{{xml}}}
      ]]>
    </axel-tag-structure>
    <understanding>
      !! MANDATORY: READ → UNDERSTAND → APPLY !!
      - READ the template file first
      - UNDERSTAND the structure and patterns
      - APPLY the template structure EXACTLY
      Reference = HOW to think | Template = HOW to write
    </understanding>
  </templates>

  <context>
    - Used for defining multi-step processes
    - Coordinates user interaction, API calls, file operations
    - Stage-based flow with implicit sequential execution
    - Supports conditional jumps (goto) and parallel execution
    - Integrates with agents, skills, and commands
  </context>

  <principle name="stage-structure">
    Stage Flow: INIT → DISCOVER → ANALYZE → EXECUTE → VERIFY → COMPLETE
    - INIT: Load context, set target (required)
    - DISCOVER: Gather information, user input (optional)
    - ANALYZE: Evaluate, synthesize (optional)
    - EXECUTE: Perform action (optional)
    - VERIFY: Validate, test (optional)
    - COMPLETE: Report, finalize (required)
  </principle>

  <principle name="stage-rules">
    - Implicit flow: Stages run in definition order
    - Conditional jump: goto with to attribute jumps to different stage
    - Termination: Last stage ends with stop
    - Naming convention: Simple id without prefix (e.g., id="init" not id="stage:init")
  </principle>

  <principle name="tasks-rules">
    - Use `tasks` element for batch declarative operations
    - Tasks are defined inside CDATA block
    - Each task has target, action, and parameters
    - Use `do` element for single imperative actions
  </principle>

  <pattern name="stage"><![CDATA[
    `stage` - Workflow Stage

    Purpose: Defines a single stage in the workflow.

    Attributes:
    - `id` (mandatory): Stage identifier (simple name, no prefix)

    Child Elements:
    - `print` → Display message to user
    - `ask` → Request user input
    - `tasks` → Batch declarative operations
    - `do` → Single imperative action
    - `goto` → Conditional jump
    - `stop` → Terminate workflow

    Example:
    <stage id="init">
      <print>Starting workflow...</print>
      <ask>
        - project_name: "Enter project name:" default="${cwd.basename}"
      </ask>
    </stage>
  ]]></pattern>

  <pattern name="confirm"><![CDATA[
    `confirm` - User Confirmation Stage

    Purpose: Presents a plan/summary and asks for user confirmation.

    Attributes:
    - `id` (mandatory): Confirm identifier

    Child Elements:
    - `print` → Display plan/summary
    - `ask` → Request confirmation with goto options
    - `stop` → Stop if not confirmed

    Example:
    <confirm id="install-plan">
      <print>
        ## Installation Plan
        **Project:** ${project_name}
        Proceed with installation?
      </print>
      <ask var="confirm" prompt="Continue? (y/n):" default="y">
        <goto when="${confirm} = 'no'" to="cancelled"/>
        <goto when="${confirm} = 'yes'" to="execute"/>
      </ask>
      <stop/>
    </confirm>
  ]]></pattern>

  <pattern name="parallel"><![CDATA[
    `parallel` - Parallel Execution

    Purpose: Executes multiple stages in parallel.

    Attributes:
    - `id` (mandatory): Parallel block identifier

    Child Elements:
    - `stage` → Stages to run in parallel

    Example:
    <parallel id="execute">
      <stage id="execute-frontend">
        <tasks>
          Create files:
            - App.tsx <- Frontend-App-Tpl.tsx
            - index.ts <- Frontend-Index-Tpl.ts
        </tasks>
      </stage>
      <stage id="execute-backend">
        <tasks>
          Create files:
            - server.ts <- Backend-Server-Tpl.ts
            - routes.ts <- Backend-Routes-Tpl.ts
        </tasks>
      </stage>
    </parallel>
  ]]></pattern>

  <pattern name="tasks"><![CDATA[
    `tasks` - Batch Declarative Operations

    Purpose: Defines multiple operations in declarative format.

    Format (inside CDATA):
    Group name:
      - target (details)
      - file <- template
        - param: value
      - source -> destination

    Groups:
    - `Create folders:` → Create directories
    - `Create files:` → Create/write files from templates
    - `Copy files:` → Copy files to destination
    - `Validate:` → Validate against rules

    Syntax:
    - `(details)` → Parentheses for sub-items or description
    - `<-` → Create from template (file <- template)
    - `->` → Copy to destination (source -> target)
    - `-` → Every line starts with dash (items and parameters)

    Example:
    <tasks>
    Create folders:
      - .claude/ (commands, skills, agents, workflows, templates)
      - .claude/references/core/
      - .claude/

    Create files:
      - CLAUDE.md <- AXEL-Claude-Tpl.md
        - name: ${project_name}
        - description: ${project_desc}
      - MEMORIES.md <- AXEL-Memory-Tpl.md
      - LEARNED.md <- AXEL-Learned-Tpl.md

    Copy files:
      - understanding.md -> .claude/references/core/
      - checklist.md -> .claude/references/core/
    </tasks>
  ]]></pattern>

  <pattern name="print"><![CDATA[
    `print` - Display Message

    Purpose: Shows message to user.

    Content: Markdown-formatted text with variable interpolation.

    Example:
    <print>
      ## Project Setup Complete

      **Name:** ${project_name}
      **Path:** ${project_path}
    </print>
  ]]></pattern>

  <pattern name="ask"><![CDATA[
    `ask` - User Input Request

    Purpose: Requests input from user.

    Format 1 - Multiple variables (YAML-like):
    <ask>
      - var_name: "Prompt text" default="default_value"
      - another_var: "Another prompt"
    </ask>

    Format 2 - Single confirmation with goto:
    <ask var="confirm" prompt="Continue? (y/n):" default="y">
      <goto when="${confirm} = 'no'" to="cancelled"/>
      <goto when="${confirm} = 'yes'" to="execute"/>
    </ask>
  ]]></pattern>

  <pattern name="goto"><![CDATA[
    `goto` - Conditional Jump

    Purpose: Jumps to another stage based on condition.

    Attributes:
    - `when` (mandatory): Condition expression
    - `to` (mandatory): Target stage id

    Example:
    <goto when="${action} = 'cancel'" to="cancelled"/>
    <goto when="${tests_ok} = true AND ${lint_ok} = true" to="complete"/>
  ]]></pattern>

  <decision name="scenario-stage-selection" date="2024-12">
    When: Choosing which stages to include
    Action: Select stages based on workflow type
    - Document creation: INIT → DISCOVER → EXECUTE → COMPLETE
    - Research: INIT → DISCOVER → ANALYZE → COMPLETE
    - Code review: INIT → DISCOVER → ANALYZE → COMPLETE
    - Code development: INIT → DISCOVER → ANALYZE → EXECUTE → VERIFY → COMPLETE
    - Installation: INIT → DISCOVER → CONFIRM → EXECUTE → COMPLETE
    - Debugging: INIT → DISCOVER → ANALYZE → EXECUTE → VERIFY → (loop)
    Reason: Different workflows need different stage combinations
  </decision>

  <requirements>
    - Frontmatter must include name (kebab-case), description, type: workflow
    - Frontmatter must define triggers list
    - Document root must have type="workflow"
    - Required stages: INIT, (DISCOVER or EXECUTE), COMPLETE
    - Stage ids must be simple names (no prefix)
    - Implicit flow: stages run in definition order
    - Last stage must end with stop
    - Variables are optional (can use ask inline)
  </requirements>

  <implementation name="file-locations">
    .claude/workflows/
    - {workflow-name}.md           # Workflow file (e.g.: deploy-notification.md)
  </implementation>

  <implementation name="creating-workflow">
    Step 1 - Collect Identity:
    - Name: kebab-case (e.g., deploy-notification)
    - Description: max 200 chars
    - Triggers: keywords that activate workflow

    Step 2 - Select Workflow Type:
    - Document creation: INIT → DISCOVER → EXECUTE → COMPLETE
    - Research: INIT → DISCOVER → ANALYZE → COMPLETE
    - Code review: INIT → DISCOVER → ANALYZE → COMPLETE
    - Code development: INIT → DISCOVER → ANALYZE → EXECUTE → VERIFY → COMPLETE
    - Installation: INIT → DISCOVER → CONFIRM → EXECUTE → COMPLETE

    Step 3 - Define Stages:
    - Which stages are needed based on type
    - What each stage does
    - User confirmations (confirm element)
    - Parallel execution if needed

    Step 4 - Define Variables & Input:
    - Required variables (var element)
    - User input prompts (ask element)

    Step 5 - Define Output:
    - Final output format: markdown | json | text | yaml

    Step 6 - Validate:
    - Check against workflow-validation checklist
    - Verify axel-tag-structure element order
    - Ensure understanding at document end

    Step 7 - Generate:
    - Map values to document elements in axel-tag-structure order
    - Save to: .claude/workflows/${name}.md

    Step 8 - AXEL Checklist:
    - MUST validate against AXEL-Checklist.md standards
    - Verify frontmatter, document-structure, element-order
    - Check execution-validation rules
  </implementation>

  <output format="markdown">
    File: {workflow-name}.md
    Path: .claude/workflows/{workflow-name}.md
    Structure:
    - YAML frontmatter (---)
    - Markdown title (# Workflow Name)
    - AXEL XML in code fence (```xml ... ```)
    - Document type="workflow" with stages
  </output>

  <verification>
    - Is frontmatter correct? (name: kebab-case, type: workflow)
    - Are triggers defined?
    - Does document have type="workflow"?
    - Are stages in correct order?
    - Do required stages exist?
    - Are stage ids simple names (no prefix)?
    - Is implicit flow used (no next attribute)?
    - Does last stage end with stop?
    - Does goto use to attribute (not next)?
  </verification>

  <checklist name="workflow-validation">
    Frontmatter:
    - Is name kebab-case?
    - Is type: workflow?
    - Are description and triggers defined?

    Structure:
    - Does document type="workflow" root element exist?
    - Is execution element with flow attribute present?
    - Are stages in correct order? (INIT → DISCOVER → ANALYZE → EXECUTE → VERIFY → COMPLETE)
    - Do required stages exist? (INIT, DISCOVER or EXECUTE, COMPLETE)

    Stages:
    - Are stage ids simple names? (init, discover, execute - not stage:init)
    - Do stages run in definition order? (implicit flow)
    - Is goto used for conditional jumps with to attribute?
    - Does last stage end with stop?
    - Do goto targets reference stage id?

    Parallel:
    - Does parallel element contain stage elements?
    - Does parallel have id attribute?
    - Are parallel stages independent?

    Tasks:
    - Is tasks content inside CDATA?
    - Are groups properly named? (Create folders:, Create files:, Copy files:, Validate:)
    - Does each item use correct syntax? (<- for template, -> for copy)
    - Are parameters properly indented under items?

    User Interaction:
    - Does ask use YAML-like format for variables?
    - Does confirm have id attribute?
    - Does confirm have print and ask elements?
    - Does print contain markdown content?

    Termination:
    - Does every stage end with stop or goto?
    - Is stop kind="end" or kind="error" defined?

    Final:
    - Is understanding at document end?
  </checklist>

  <understanding/>

</document>
```
