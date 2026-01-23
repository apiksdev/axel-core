---
name: axel-command
description: Structure of slash command definition files - routing, execution, AI integration
type: reference
---

# AXEL Command

```xml
<document type="reference">

  <enforcement>
    - Read `src` attribute from command references to locate files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
    - Command files located in .claude/commands/ directory
    - Commands with file I/O must document path resolution strategy
  </enforcement>

  <objective>
    How to create slash commands in AXEL DSL - step-by-step guide.
    Commands have two parts: routing (command block) and execution (stages).
  </objective>

  <templates load="always" mode="context">
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/commands/AXEL-Command-Template-Bootstrap.md"/>
    <axel-tag-structure>
      <![CDATA[
      Command Document Structure (NEW)
      +-- Frontmatter (name, description, type: command, allowed-tools)
      +-- # Command Name (title)
      +-- {{{xml}}}
      +-- <document type="command" entry="cmd:main">
      |   +-- <enforcement> (recommended)
      |   |   +-- [standard rules]
      |   |   +-- RESUMABLE (if invoke resumable="true"): continue from last incomplete stage
      |   +-- <objective> (recommended) [NEW]
      |   +-- <documents name=".." load="always" mode="context">
      |   |   +-- <read src="..."/>
      |   |   +-- <understanding>...</understanding> (required)
      |   +-- <documents name=".." load="on-trigger" mode="context">
      |   |   +-- <read src="..." trigger="..."/>
      |   |   +-- <understanding>...</understanding> (required)
      |   +-- <documents name=".." load="on-demand" mode="context">
      |   |   +-- <read src="..." ask="..."/>
      |   |   +-- <understanding>...</understanding> (required)
      |   +-- <variables> (optional)
      |   |   +-- <var name="..." value="..."/>
      |   |   +-- <var name="..." from="args.0|args.*"/>
      |   |   +-- <var name="..." ask="user"/>
      |   +-- <command id="cmd:main"> [ROUTING ONLY]
      |   |   +-- <goto when="..." to="stage-id"/>
      |   |   +-- <goto to="default-stage"/>
      |   +-- <execution flow="linear|staged"> [Stage Container]
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
    - Commands are slash-triggered interactive flows (/command-name args)
    - Used for automating repetitive tasks (git commits, memory saves, deployments)
    - Commands have two parts: ROUTING (cmd:main) and EXECUTION (stages)
    - Commands can delegate to skills, agents, or workflows
    - Commands live in .claude/commands/ folder
  </context>

  <principle name="routing-vs-execution">
    Commands are split into two distinct parts:

    ROUTING (command block):
    - Single <command id="cmd:main"> block
    - Contains ONLY <goto> tags for branching
    - Routes to appropriate stage based on arguments
    - No business logic here

    EXECUTION (stages):
    - <execution> wrapper contains all <stage> blocks
    - Each stage has its own id
    - Stages contain the actual work (print, tasks, invoke, etc.)
    - Every stage must end with <stop> or <goto>

    Example:
    <![CDATA[
    <command id="cmd:main">
      <goto when="target == ''" to="help"/>
      <goto when="target == 'list'" to="list"/>
      <goto when="target == 'create'" to="create"/>
      <goto to="list"/>
    </command>

    <execution>
      <stage id="help">...</stage>
      <stage id="list">...</stage>
      <stage id="create">...</stage>
    </execution>
    ]]>
  </principle>

  <principle name="entry-first">
    - Entry attribute defines the starting command block
    - Always use entry="cmd:main"
    - Clear entry point prevents execution confusion
  </principle>

  <principle name="explicit-termination">
    - Every execution path must end with stop
    - stop kind="end" for successful completion
    - stop kind="error" for error conditions
    - No implicit flow endings
  </principle>

  <principle name="enforcement-clarity">
    - Enforcement defines HOW to execute read/write operations
    - Must specify file locations via src attribute interpretation
    - Must clarify ${CLAUDE_PLUGIN_ROOT} vs relative path resolution
    - Must state format/mode requirements
    - Essential for commands with file I/O operations
  </principle>


  <decision name="plugin-root-variable" date="2024-12">
    <![CDATA[
    When: Referencing plugin files in commands (PLUGIN ONLY)
    Pattern: Use ${CLAUDE_PLUGIN_ROOT} for plugin-relative paths
    - ${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/... (template files)
    - ${CLAUDE_PLUGIN_ROOT}/references/... (reference docs)
    - ${CLAUDE_PLUGIN_ROOT}/skills/... (skill definitions)

    IMPORTANT: This variable is ONLY for plugin commands!
    - Plugin commands: Use ${CLAUDE_PLUGIN_ROOT}
    - Project commands (.claude/commands/): Use relative paths from project root

    Reason: Portable paths that work regardless of plugin installation location
    ]]>
  </decision>

  <decision name="argument-access-pattern" date="2024-12">
    When: Accessing command arguments
    Pattern: Use var from="args.N" where N is zero-indexed
    - args.0 = first argument
    - args.* = all arguments (array)
    - args.length = argument count
    Reason: Consistent, predictable argument access
  </decision>

  <decision name="native-arguments-syntax" date="2024-12">
    When: Using Claude Code native argument variables
    Pattern: Use $ARGUMENTS, $1, $2, etc.
    - $ARGUMENTS = all arguments as single string
    - $1 = first argument
    - $2 = second argument
    - $N = Nth argument
    Note: This is Claude Code native syntax, alternative to args.N
    Reason: Direct compatibility with Claude Code command system
  </decision>

  <decision name="goto-stage-only" date="2024-12">
    When: Using goto for flow control
    Pattern: Use to="stage-id" for all jumps

    Routing happens in cmd:main, execution uses stage jumps:
    <![CDATA[
    <!-- In cmd:main (routing) -->
    <goto when="action == 'create'" to="create"/>
    <goto to="list"/>

    <!-- In stages (loops/flow) -->
    <goto when="${action.value} == 'edit'" to="edit"/>
    <goto to="review"/>
    ]]>

    Note: goto command="..." is deprecated. Use single cmd:main for routing.
  </decision>

  <decision name="write-mode-selection" date="2024-12">
    When: Writing files in commands
    Modes:
    - create = overwrite (one-time files)
    - append = add to end (logs, history)
    - prepend = add to beginning (headers)
    - merge = merge content (JSON/YAML configs)
    Reason: Explicit intent prevents accidental data loss
  </decision>

  <decision name="claude-md-command-index" date="2024-12">
    <![CDATA[
    When: Adding or updating slash commands
    Requirement: CLAUDE.md <commands> section MUST be updated

    Format:
    <commands>
      <ref name="/plugin:command-name">
        - sub-command - Short description
        - another-sub - Another description
      </ref>
    </commands>

    Example:
    <ref name="/axel:axel-todos">
      - list - List todo items
      - add - Add new todo
      - done - Mark todo as done
    </ref>

    Rules:
    - name attribute: Slash command path starting with /
    - Content: Bullet list of sub-commands with descriptions
    - Single action commands: One bullet with description
    - No src attribute - purely index/documentation

    When to Update:
    - New command created → Add <ref> entry to CLAUDE.md
    - Command renamed → Update name attribute
    - Sub-commands changed → Update bullet list
    - Command deleted → Remove <ref> entry

    Why This Matters:
    - CLAUDE.md serves as command index/quick reference
    - AI reads CLAUDE.md to understand available commands
    - Keeps documentation in sync with actual commands
    ]]>
  </decision>

  <pattern name="simple-command">
    When: Basic list/create/edit commands without loops
    Structure: cmd:main routes to stages, each stage does one thing
    Flow: routing → stage → stop
    Template: AXEL-Command-Simple-Tpl.md
  </pattern>

  <pattern name="interactive-command">
    When: Commands with loops (approval, validation, agent chaining)
    Structure: cmd:main routes, execution has loops between stages
    Flows:
    - Approval: init → review ↔ edit → execute
    - Agent Chain: analyze → plan → approve ↔ revise → execute
    Template: AXEL-Command-Interactive-Tpl.md
  </pattern>

  <pattern name="direct-tool-invocation">
    <![CDATA[
    When: Direct invocation of Claude Code native tools
    Purpose: Call skills and agents from commands

    <!-- Agent invocation -->
    <invoke name="Task">
      <param name="subagent_type">axel:agent-xyz</param>
      <param name="prompt">${prompt}</param>
    </invoke>

    <!-- Skill invocation -->
    <invoke name="Skill">
      <param name="skill">skill-axel-expert</param>
    </invoke>

    Note:
    - invoke is for Task/Skill tools
    - Use <tasks> for simple AI tasks
    - Use <call command="/..."> for slash commands
    ]]>
  </pattern>

  <pattern name="command-enforcement-rules">
    Command Enforcement Template:
    - IF invoke resumable="true" used THEN command MUST include in enforcement:
      - RESUMABLE: On re-invoke, continue from last incomplete stage
      - Run to completion - only user cancellation interrupts flow
  </pattern>

  <requirements>
    - Frontmatter must have name, description, type: command
    - Document root must have type="command" and entry="cmd:main"
    - Must include locale compliance enforcement rule (chat vs docs/code language)
    - Single <command id="cmd:main"> for routing only
    - All stages inside <execution> wrapper
    - Every stage must end with <stop> or <goto>
    - Variables must have explicit source (value/from/ask)
    - IF invoke resumable="true" used THEN MUST include RESUMABLE enforcement rule
  </requirements>

  <frontmatter>
    <![CDATA[
---
name: memory-save               # Command name format:
                                #   Plugin commands: plugin:command (e.g., axel:install)
                                #   Project commands: kebab-case (e.g., memory-save)
description: Memory kaydetme    # Short description, max 200 characters
type: command                   # Always "command"
model: sonnet                   # Model selection: inherit | sonnet | opus | haiku
allowed-tools:                  # Tools that can be used
  - Read
  - Write
  - Bash
---
    ]]>
  </frontmatter>

  <implementation name="steps">
    Step 1 - Define Frontmatter:
    - Set name (plugin:command for plugins, kebab-case for projects)
    - Write clear description (max 200 chars)
    - Set type: command
    - List allowed-tools

    Step 2 - Create Document Root:
    - Set type="command"
    - Set entry="cmd:main"

    Step 3 - Add Objective:
    - Describe what command does (1-3 sentences)

    Step 4 - Define Variables:
    - Capture arguments with from="args.N"
    - Set defaults with value="..."
    - Request input with ask="prompt"

    Step 5 - Build Routing (cmd:main):
    - Add <goto when="..." to="stage"/> for each branch
    - Add default <goto to="default-stage"/>
    - NO business logic here

    Step 6 - Build Execution Stages:
    - Wrap all stages in <execution>
    - Each stage: <stage id="...">
    - Use <print>, <tasks>, <bash>, <workflow>, <invoke>
    - End with <stop> or <goto>

    Step 7 - Generate:
    - Map values to document elements in axel-tag-structure order
    - Save to: .claude/commands/${name}.md

    Step 8 - AXEL Checklist:
    - MUST validate against AXEL-Checklist.md standards
    - Verify frontmatter, document-structure, element-order
    - Check execution-validation rules
  </implementation>

  <output format="markdown">
    File: {command-name}.md
    Path: .claude/commands/{command-name}.md
    Structure:
    - YAML frontmatter (---)
    - Markdown title (# Command Name)
    - AXEL XML in code fence (```xml ... ```)
    - Document type="command" with cmd:main and execution
  </output>

  <verification>
    Structure:
    - Does document have type="command" and entry="cmd:main"?
    - Is there a single <command id="cmd:main"> block?
    - Is there an <execution> wrapper?
    - Are all stages inside <execution>?
    - Is locale compliance rule in enforcement (chat vs docs/code)?

    Routing:
    - Does cmd:main contain ONLY <goto> tags?
    - Do all goto to="..." targets exist as stages?
    - Is there a default goto (no when condition)?

    Stages:
    - Does each stage have unique id?
    - Does every stage end with <stop> or <goto>?
    - Do loops have exit conditions?

    Elements:
    - Does <tasks> have output attribute?
    - Does <bash> have run or content?
    - Does <workflow> have target?
    - Does <call> have command?
    - Does <invoke> have name (Task or Skill)?

    Variables:
    - Do all variables have source (value/from/ask)?
    - Are args.N references correct?
  </verification>

  <checklist name="command-creation">
    Frontmatter:
    - [ ] name format correct? (plugin:command or kebab-case)
    - [ ] description under 200 characters?
    - [ ] type set to "command"?
    - [ ] allowed-tools listed?

    Structure:
    - [ ] document type="command" entry="cmd:main"?
    - [ ] single <command id="cmd:main"> for routing?
    - [ ] <execution> wrapper present?
    - [ ] all stages inside execution?
    - [ ] locale compliance rule in enforcement (chat vs docs/code)?

    Routing (cmd:main):
    - [ ] only <goto> tags?
    - [ ] all targets are valid stage ids?
    - [ ] default goto present?

    Stages:
    - [ ] each stage has unique id?
    - [ ] each stage ends with stop or goto?
    - [ ] loops have exit conditions?

    Variables:
    - [ ] <objective> present?
    - [ ] variables have source (value/from/ask)?
    - [ ] args.N or $1 used consistently?
  </checklist>

  <understanding/>

</document>
```
