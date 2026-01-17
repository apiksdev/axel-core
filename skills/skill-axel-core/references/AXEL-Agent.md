---
name: axel-agent
description: Structure of agent definition files - objective, enforcement, registry
type: reference
---

# AXEL Agent

```xml
<document type="reference">

  <enforcement>
    <![CDATA[
    - Read `src` and `ref` attributes from agent references to locate files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
    - Agent files located in .claude/agents/agent-{name}/ directory
    - CLAUDE.md is automatically loaded by Claude Code - DO NOT add to <documents> block
    - Use Read tool to access CLAUDE.md content during execution
    ]]>
  </enforcement>

  <objective>
    Structure of agent definition files. AXEL Agent is an AI configuration format
    that runs autonomous tasks. Unlike skills, agents are goal-oriented - they work
    independently using documents to achieve a specific objective.
  </objective>

  <templates load="always" mode="context">
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/agents/AXEL-Agent-Template-Bootstrap.md"/>
    <axel-tag-structure>
      <![CDATA[
      AXEL-Agent-Tpl.md
      +-- Template Frontmatter
      +-- # AXEL Agent (title)
      +-- {{{xml}}}
      +-- <document type="agent" resumable="true|false">
      |   +-- <enforcement>
      |   |   +-- [standard rules]
      |   |   +-- RESUMABLE (if document resumable="true" OR invoke resumable="true"): continue from last incomplete stage
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
      |   +-- <archetype>
      |   +-- <system-prompt>
      |   +-- <templates name=".." load="always|on-demand|on-trigger" mode="context"> (optional)
      |   |   +-- <read src="..." ask="..."/>
      |   |   +-- <understanding>...</understanding> (required)
      |   +-- <examples> (optional)
      |   |   +-- <example name="..." language="...">
      |   +-- <variables> (optional)
      |   |   +-- <var name="..." value="..."/>
      |   |   +-- <var name="..." from="param.*|args.*"/>
      |   |   +-- <var name="..." ask="user"/>
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
      |   +-- <output format="..."> [Expected output format]
      |   +-- <understanding/>
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
    - Agent is used for autonomous, goal-driven tasks
    - Works independently using documents
    - AI invokes agent based on description field content
    - Located in .claude/agents/agent-{name}/AGENT.md
  </context>

  <requirements>
    - MUST have frontmatter with name (agent-* prefix), description, type (agent), allowed-tools
    - MAY have model, color, permissionMode in frontmatter
    - MUST have document type="agent" root element
    - MUST define objective with clear, narrowly scoped goal
    - MUST include documents registry for reference documents
    - MUST place understanding at document end
    - IF document resumable="true" OR invoke resumable="true" used THEN MUST include RESUMABLE enforcement rule
  </requirements>

  <frontmatter>
    <![CDATA[
---
name: agent-{name}                # Agent identifier (agent- prefix required)
description: Short description    # Max 200 characters, guides AI when to invoke
type: agent                       # Fixed: "agent"
model: inherit                    # inherit | sonnet | opus | haiku
color: blue                       # blue | cyan | green | yellow | magenta | red
permissionMode: default           # optional: default | acceptEdits | bypassPermissions | plan | ignore
allowed-tools:                    # Allowed tools (least privilege)
  - Read
  - Grep
  - Glob
---
    ]]>

    Color Selection:
    - blue/cyan: Analysis (review, inspect, explore)
    - green: Success-oriented (test, build)
    - yellow: Validation (lint, check)
    - red: Critical (security, audit)
    - magenta: Generation (create, write)

    Permission Mode Selection:
    - default: Standard permission handling (recommended)
    - acceptEdits: Auto-accept file edits without confirmation
    - bypassPermissions: Skip all permission checks (use with caution)
    - plan: Read-only mode, no modifications allowed
    - ignore: Silently ignore permission requests
  </frontmatter>

  <archetypes>
    <archetype type="analysis">
      Purpose: Code, PR, or data review
      Focus: Quality assessment, security analysis
      Tools: Read, Grep, Glob
      Output: Findings report with severity levels
    </archetype>

    <archetype type="generation">
      Purpose: Content, code, documentation creation
      Focus: New artifact generation
      Tools: Read, Write, Grep
      Output: Generated files
    </archetype>

    <archetype type="validation">
      Purpose: Criteria-based verification
      Focus: Standards compliance check
      Tools: Read, Grep, Glob, Bash
      Output: Pass/Fail report with fix suggestions
    </archetype>

    <archetype type="orchestration">
      Purpose: Multi-step workflow coordination
      Focus: Complex task decomposition
      Tools: All tools
      Output: Coordinated operation results
    </archetype>
  </archetypes>

  <system-prompt-design>
    Separation of Concerns:
    - system-prompt = WHO + HOW TO BEHAVE (role, responsibilities, quality standards)
    - execution = WHICH STEPS + WHEN (process flow, stages, routing)

    Content:
    - Role declaration: "You are..." format
    - Core responsibilities (3-5 items)
    - Quality standards (critical/major/minor metrics)
    - Edge case handling (brief)

    Guidelines:
    - Length: 300-2,000 characters (optimal: 300-1,500)
    - Avoid step-by-step procedures (those go in execution)
    - Focus on identity and behavior, not process
  </system-prompt-design>

  <pattern name="folder-structure">
    Location: .claude/agents/agent-{name}/
    - AGENT.md - Main agent file
  </pattern>

  <pattern name="naming-convention">
    <![CDATA[
    Agent Naming (Claude Code Style)

    Four scope levels:

    1. Plugin Level:
       Format: {plugin}:{agent-folder}:{agent-name}
       Example: axel:agent-axel-project-create:agent-axel-project-create

    2. Plugin Skill Level:
       Format: {plugin}:{skill}:agents:{agent-name}
       Example: axel:skill-axel-expert:agents:agent-axel-expert-creator

    3. User Project Level:
       Format: {project}:{agent-folder}:{agent-name}
       Example: myproject:agent-code-reviewer:agent-code-reviewer

    4. User Skill Level:
       Format: {project}:{skill}:agents:{agent-name}
       Example: myproject:skill-frontend:agents:agent-component-generator

    Usage in registries:
    - src attribute uses this naming format
    - Claude Code resolves names to actual agent files
    - Plugin agents: Defined in plugin's agents/{agent-folder}/ folder
    - Skill sub-agents: Defined in skill's agents/ folder
    ]]>
  </pattern>

  <pattern name="agent-enforcement-rules">
    Agent Enforcement Template:
    - IF document resumable="true" OR invoke resumable="true" used THEN agent MUST include in enforcement:
      - RESUMABLE: On re-invoke, continue from last incomplete stage
      - Run to completion - only user cancellation interrupts flow
  </pattern>

  <pattern name="execution-with-stages">
    <![CDATA[
    When: Agent needs multi-step execution with loops or chaining
    Purpose: Stage-based flow control within agent execution
    Location: Inside <execution> block

    Stage Usage in Agents:
    - Stages are optional in agent execution
    - Use stages for complex multi-step agent flows
    - Each stage has simple id (no prefix needed)
    - Implicit sequential flow between stages
    - Use <goto to="stage-id"/> for stage jumps and loops
    - Capture sub-agent outputs with <set var="..." from="task.output"/>

    When to Use Stages in Agents:
    - Multi-agent chaining: Call multiple agents sequentially
    - Iterative refinement: Loop until quality threshold met
    - Validation loops: Generate → validate → fix → re-validate
    - User approval flows: Generate → review → (revise) → approve

    Traditional execution flow is sufficient for:
    - Simple linear agent execution
    - Single-step analysis or generation
    - No loops or back-navigation needed

    Templates:
    - Linear: ${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/agents/AXEL-Agent-Linear-Tpl.md
    - Staged: ${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/agents/AXEL-Agent-Staged-Tpl.md

    Notes:
    - Stages are optional - use only when needed
    - Simple agents should use traditional text-based execution
    - Variable scope: set in stage, available in subsequent stages
    - Loops must have exit conditions to avoid infinite loops
    ]]>
  </pattern>

  <pattern name="project-config-lookup">
    <![CDATA[
    Project-Specific Agent Configuration

    Purpose: Agents can receive project-specific configuration via CLAUDE.md.
    This allows projects to customize agent behavior without modifying plugin files.

    IMPORTANT: CLAUDE.md is already loaded automatically by Claude Code.
    - DO NOT add CLAUDE.md to agent's <documents> block
    - Agent can directly read CLAUDE.md using Read tool
    - CLAUDE.md is always available in execution context

    Execution Flow:
    1. Agent starts execution
    2. Read project CLAUDE.md (already loaded, use Read tool)
    3. Find own ref in agents section: `ref name="agent-{name}" src="..."`
    4. Load child elements if defined:
       - `prompt` → Additional instructions
       - `documents` → Rules, checklists, standards
       - `templates` → Project-specific templates
    5. Execute with full context

    Lookup Behavior:
    - Agent MUST check CLAUDE.md for its ref definition
    - If ref has child elements → load and apply them
    - If ref is simple (no children) → use default agent behavior
    - Child elements extend, not replace, agent's base configuration

    Template Loading:
    - `template name="..." src="..." ask="..."`
    - Templates loaded on-demand when ask keywords match
    - Project templates take precedence over plugin templates

    Document Loading:
    - `read src="..." ask="..."`
    - Documents loaded on-demand when ask keywords match
    - Loaded documents add to agent's context

    Example:
    <!-- In project CLAUDE.md -->
    <agents load="on-demand">
      <ref name="agent-project-tasks" src="${CLAUDE_PLUGIN_ROOT}/agents/agent-project-tasks/AGENT.md">
        <prompt>
          When creating tasks:
          - Create DTO for each entity
          - Write unit test for each service
        </prompt>
        <documents>
          <read src=".claude/checklists/impl-checklist.md" ask="checklist"/>
        </documents>
        <templates>
          <read src=".claude/templates/dto.md" name="dto" ask="dto, request"/>
        </templates>
      </ref>
    </agents>
    ]]>
  </pattern>

  <implementation name="file-locations">
    .claude/agents/agent-{name}/
    - AGENT.md                    # Main agent file
  </implementation>

  <implementation name="creating-agent">
    Step 1 - Collect Identity:
    - Name: agent-* prefix, kebab-case (e.g., agent-code-reviewer)
    - Description: max 200 chars, guides AI when to invoke

    Step 2 - Select Archetype:
    - analysis: Code review, PR analysis, security audit
    - generation: Content creation, code generation
    - validation: Standards check, lint, verification
    - orchestration: Multi-step workflow coordination

    Step 3 - Configure:
    - Model: inherit | sonnet | opus | haiku
    - Color: blue | cyan | green | yellow | magenta | red
    - Tools: Read, Write, Edit, Grep, Glob, Bash, Task, WebFetch, WebSearch

    Step 4 - Define Behavior (system-prompt):
    - Role: "You are a [role] that [function]..."
    - Core responsibilities: 3-5 items
    - Quality standards: what defines good output

    Step 5 - Define Execution:
    - Flow: linear | staged
    - Main steps in order
    - Output format: markdown | json | text | yaml

    Step 6 - Validate:
    - Check against agent-validation checklist
    - Verify axel-tag-structure element order
    - Ensure understanding at document end

    Step 7 - Generate:
    - Map values to document elements in axel-tag-structure order
    - Save to: .claude/agents/${name}/AGENT.md

    Step 8 - AXEL Checklist:
    - MUST validate against AXEL-Checklist.md standards
    - Verify frontmatter, document-structure, element-order
    - Check execution-validation rules
  </implementation>

  <output format="markdown">
    File: AGENT.md
    Path: .claude/agents/agent-{name}/AGENT.md
    Structure:
    - YAML frontmatter (---)
    - Markdown title (# Agent Name)
    - AXEL XML in code fence (```xml ... ```)
    - Document type="agent" with registries
  </output>

  <verification>
    - Is frontmatter correct? (name: agent-*, type: agent)
    - Is document type="agent" root element present?
    - Is archetype defined?
    - Is objective specified with clear goal?
    - Is system-prompt defined?
    - Is documents registry present?
    - Is understanding at the end?
  </verification>

  <checklist name="agent-validation">
    <![CDATA[
    Frontmatter:
    - Is name prefixed with agent-?
    - Is type set to agent?
    - Is description clear (guides AI when to invoke)?
    - Is model defined (inherit, sonnet, opus, haiku)?
    - Is color defined (blue, cyan, green, yellow, red, magenta)?
    - Is allowed-tools list provided (least privilege)?
    - Is permissionMode valid if set? (default, acceptEdits, bypassPermissions, plan, ignore)

    Structure:
    - Is document type="agent" root element present?
    - Is archetype defined (analysis, generation, validation, orchestration)?
    - Is objective specified with clear goal?
    - Is system-prompt defined with second-person voice?
    - Is documents registry defined?
    - Is understanding at the end?

    System Prompt:
    - Is length between 300-2,000 characters? (focused on role/behavior)
    - Does it start with "You are..."?
    - Are core responsibilities listed briefly (3-5 items)?
    - Are quality standards defined (critical/major/minor)?
    - Are edge cases covered (concise guidelines)?
    - Does it avoid detailed step-by-step procedures? (those go in execution)
    - Does it avoid output format details? (those go in output element)

    Output (optional):
    - Is format attribute defined? (markdown, json, text, yaml, xml)
    - Does content describe expected output structure?
    - Are output sections and fields clearly defined?

    Content:
    - Is the objective narrowly scoped?
    - Is folder structure correct (.claude/agents/agent-{name}/)?

    Execution (flow="linear|staged"):
    - Is flow attribute set (linear or staged)?
    - If staged: Are stages used only when necessary?
    - Does each stage have unique id?
    - Do goto to="..." targets exist (stage ids)?
    - Are outputs captured with <tasks output="..."/> or <invoke output="..."/>?
    - Do loops have exit conditions (no infinite loops)?
    - Are stage jumps only within execution block?

    Project Config Lookup (agent execution):
    - Does agent check CLAUDE.md for its ref definition?
    - Are prompt child elements loaded and applied?
    - Are template child elements loaded on ask match?
    - Are document child elements loaded on ask match?
    - Do project templates take precedence over plugin templates?
    - Is CLAUDE.md NOT included in <documents> block? (already loaded by Claude Code)
    ]]>
  </checklist>

  <understanding/>

</document>
```
