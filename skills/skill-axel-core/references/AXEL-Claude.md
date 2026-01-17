---
name: axel-claude
description: CLAUDE.md reference - project configuration guide and best practices
type: reference
---

# AXEL Claude (Project Configuration Guide)

```xml
<document type="reference">

  <enforcement>
    - Read `src` and `ref` attributes from project references to locate files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
    - Project configuration located in CLAUDE.md (project root)
    - All project references use relative paths from project root
  </enforcement>

  <objective>
    CLAUDE.md project configuration guide. Defines how to create and structure
    the central configuration file for AXEL-powered projects. Focuses on design
    principles, best practices, and decision-making.
  </objective>

  <templates name="core" load="always" mode="context">
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/claude/AXEL-Claude-Tpl.md"/>
    <axel-tag-structure>
      <![CDATA[
      AXEL-Claude-Tpl.md
      +-- Template Frontmatter
      +-- # AXEL Claude (title)
      +-- {{{xml}}}
      +-- <document type="project">
      |   +-- <enforcement> (project-specific rules only)
      |   +-- <project>
      |   +-- <locale>
      |   +-- <configurations> (required, single instance)
      |   |   +-- <var name="AXEL_CORE_PLUGIN_ROOT" value="..."/> (required)
      |   |   +-- <var name="COMMIT_MESSAGE_FORMAT" value="..."/> (required)
      |   |   +-- <var name="..." value="..."/>
      |   +-- <documents name="axel-bootstrap" load="always" mode="context"> (optional)
      |   |   +-- <read src="${CLAUDE_PLUGIN_ROOT}/AXEL-Bootstrap.md"/>
      |   |   +-- <understanding>...</understanding> (required if block exists)
      |   +-- <documents name=".." load="on-demand" mode="context">
      |   |   +-- <read src="..." ask="..."/>
      |   |   +-- <understanding>...</understanding> (required)
      |   +-- <memories name=".." load="always" mode="context">
      |   |   +-- <read src="..."/>
      |   |   +-- <understanding>...</understanding> (required)
      |   +-- <templates name=".." load="always|on-demand|on-trigger" mode="context"> (optional)
      |   |   +-- <read src="..." ask="..."/>
      |   |   +-- <understanding>...</understanding> (required)
      |   +-- <examples> (optional)
      |   |   +-- <example name="..." language="...">
      |   +-- <skills name=".." load="on-demand"> (optional)
      |   |   +-- <ref src="..." ask="..."/>
      |   +-- <agents name=".." load="on-demand"> (optional)
      |   |   +-- <ref src="..." ask="..."/>
      |   +-- <commands> (optional)
      |   |   +-- <ref name="/...">
      |   |   |   +-- - sub-command - description
      |   +-- <understanding/> (empty, rules from Bootstrap)
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
    - CLAUDE.md is the central brain of your project
    - Single source of truth for AI configuration
    - Connects all skills, agents, commands, and workflows
    - Defines project context, stack, and conventions
    - Controls what AI knows and how it behaves
    - Think of it as the "main()" function of AI-assisted development
  </context>

  <requirements>
    - Must be placed in project root directory
    - Must have document type="project"
    - Must define project name and stack
    - Must include project-specific enforcement rules
    - May reference plugin's AXEL-Bootstrap.md for core rules (optional)
    - Must define locale settings
    - Must include configurations block with:
      - AXEL_CORE_PLUGIN_ROOT variable
      - COMMIT_MESSAGE_FORMAT variable
  </requirements>

  <frontmatter>
    <![CDATA[
---
name: {project-name}
description: {project description}  # Max 200 characters
type: project
version: {version}
---
    ]]>
  </frontmatter>

  <implementation name="folder-structure">
    Folder Structure:
    - CLAUDE.md
    - .claude/commands/
    - .claude/skills/
    - .claude/agents/
    - .claude/workflows/
    - .claude/references/
    - .claude/references/understanding.md
    - .claude/references/thinking.md
    - .claude/references/enforcement.md
    - .claude/references/checklist.md
    - .claude/references/standards.md
    - .claude/templates/
    - .claude/MEMORIES.md
    - .claude/LEARNED.md
    - .claude/memories/
    - .claude/workspaces/
    - .claude/workspaces/default/           # Default workspace
    - .claude/workspaces/default/todos/     # Todos in default workspace
    - .claude/workspaces/{workspace}/       # Named workspaces
    - .claude/workspaces/{workspace}/todos/ # Todos in named workspaces
  </implementation>

  <implementation name="creating-claude">
    Step 1 - Define Project Identity:
    - Name: kebab-case (e.g., my-project)
    - Description: max 200 chars
    - Version: semantic versioning

    Step 2 - Define Stack:
    - Language(s): e.g., TypeScript, C#
    - Platform: e.g., Node.js, .NET
    - Framework(s): e.g., React, ASP.NET

    Step 3 - Configure Enforcement Rules:
    - Define project-specific rules
    - Reference core enforcement files
    - Set coding standards

    Step 4 - Configure Locale:
    - Set default language (e.g., en, tr)
    - Define output language for AI responses

    Step 5 - Set Up Registries:
    - documents: References and standards (load="on-demand")
    - memories: Session and learned data (load="always")
    - templates: Code patterns (load="on-demand") - optional
    - skills: Expert roles (load="on-demand") - optional
    - agents: Autonomous tasks (load="on-demand") - optional
    - commands: Slash commands (no load attribute) - optional

    Step 6 - Create Folder Structure:
    - Create .claude/ folder with sub-folders
    - Create .claude/ folder structure for runtime data
    - Add core reference files

    Step 7 - Validate Configuration:
    - No circular references
    - Minimal load="always" usage
    - Clear component responsibilities

    Step 8 - AXEL Checklist:
    - MUST validate against AXEL-Checklist.md standards
    - Verify claude-md-creation checklist
  </implementation>

  <principle name="minimal-configuration">
    - Only add what you actually need
    - Start small, grow organically
    - Empty registries are acceptable
    - Less is more for context management
  </principle>

  <principle name="explicit-over-implicit">
    - Declare dependencies clearly
    - Use load="always" sparingly
    - Let on-demand be the default
    - Avoid hidden assumptions
  </principle>

  <principle name="single-responsibility">
    - One skill = one expertise area
    - One agent = one autonomous task
    - One command = one domain (with sub-actions)
    - Clear boundaries between components
  </principle>

  <principle name="context-awareness">
    - AI reads what it needs, when it needs it
    - Don't overload with unnecessary context
    - Use triggers and ask attributes wisely
    - Respect token limits
  </principle>

  <decision name="documents-load-always" date="2024-12">
    When to use load="always":
    - Enforcement rules (MUST follow)
    - Understanding rules (interpretation)
    - Critical learned lessons
    - Nothing else - be selective
  </decision>

  <decision name="documents-load-on-demand" date="2024-12">
    When to use load="on-demand":
    - Architecture references
    - Coding standards
    - API documentation
    - Feature-specific guides
  </decision>

  <decision name="skills-vs-agents" date="2024-12">
    Use SKILL when:
    - Ongoing expertise needed (Frontend Developer)
    - Multiple related tasks over time
    - Context switching between domains

    Use AGENT when:
    - One-time autonomous task (Code Reviewer)
    - Specific goal with clear end state
    - Delegation without supervision
  </decision>

  <pattern name="backend-project">
    Essential components:
    - skill-backend (API development)
    - agent-code-reviewer (quality)
    - templates: entity, service, controller
    - enforcement: coding standards
  </pattern>

  <pattern name="frontend-project">
    Essential components:
    - skill-frontend (UI development)
    - templates: component, hook, page
    - enforcement: accessibility, styling
  </pattern>

  <pattern name="fullstack-project">
    Essential components:
    - skill-backend + skill-frontend
    - agent-code-reviewer
    - templates for both layers
    - shared enforcement rules
  </pattern>

  <pattern name="anti-pattern-context-overflow">
    Problem: Too much load="always"
    Symptom: Slow responses, confused AI
    Fix: Move to on-demand, use triggers
  </pattern>

  <pattern name="anti-pattern-circular-refs">
    Problem: Circular references between files
    Symptom: Infinite loading loops
    Fix: Review dependency graph, break cycles
  </pattern>

  <pattern name="anti-pattern-duplicate-defs">
    Problem: Same rule defined in multiple places
    Symptom: Conflicting behavior
    Fix: Single source of truth per concept
  </pattern>

  <pattern name="anti-pattern-missing-enforcement">
    Problem: No enforcement rules defined
    Symptom: Inconsistent AI behavior
    Fix: Always define core rules first
  </pattern>

  <pattern name="bootstrap-reference">
    <![CDATA[
    Bootstrap Reference Pattern (Optional)

    CLAUDE.md can optionally reference plugin's AXEL-Bootstrap.md:
    - CLAUDE.md contains project-specific enforcement
    - Core AXEL rules can come from referenced AXEL-Bootstrap.md (if needed)

    When to use:
    - When using advanced AXEL features (skills, agents, workflows)
    - When you want centralized AXEL rule updates

    When NOT needed:
    - Simple projects with only CLAUDE.md configuration
    - Projects not using AXEL DSL features

    Structure (if used):
    <documents name="axel-bootstrap" load="always" mode="context">
      <read src="${CLAUDE_PLUGIN_ROOT}/AXEL-Bootstrap.md"/>
    </documents>
    ]]>
  </pattern>

  <pattern name="agents-section-structure">
    <![CDATA[
    Extended Agent Configuration - project-specific settings without modifying plugin files.

    Naming Convention (Claude Code Style):
    - Plugin Level: {plugin}:{agent-folder}:{agent-name}
      Example: axel:agent-axel-project-create:agent-axel-project-create
    - Skill Sub-agent: {plugin}:{skill}:agents:{agent-name}
      Example: axel:skill-axel-expert:agents:agent-axel-expert-creator

    Structure:
    <agents name="project-agents" load="on-demand">
      <ref src="axel:agent-axel-project-create:agent-axel-project-create" ask="init, project"/>
      <ref src="axel:agent-code-reviewer:agent-code-reviewer" ask="review">
        <prompt>Additional project-specific instructions</prompt>
        <documents>
          <read src=".claude/checklists/review-checklist.md" ask="checklist"/>
        </documents>
      </ref>
    </agents>

    References:
    - Naming details: AXEL-Agent.md → naming-convention pattern
    - Extended config: AXEL-Agent.md → project-config-lookup pattern
    ]]>
  </pattern>

  <output format="markdown">
    File: CLAUDE.md
    Path: {project-root}/CLAUDE.md
    Structure:
    - YAML frontmatter (---)
    - Markdown title (# Project Name) [optional]
    - AXEL XML in code fence (```xml ... ```)
    - Document type="project" with registries and commands
  </output>

  <verification>
    - Is document type="project"?
    - Does project tag have name attribute?
    - Is stack defined with technologies?
    - Is locale defined with default?
    - Is configurations block present?
    - Is AXEL_CORE_PLUGIN_ROOT variable defined?
    - Is COMMIT_MESSAGE_FORMAT variable defined?
    - Are all variable names UPPERCASE?
    - Are enforcement rules loaded first?
    - Is understanding reference included?
    - No circular references?
    - Minimal load="always" usage?
  </verification>

  <pattern name="configurations-element">
    <![CDATA[
    `configurations` - Project-Level Key-Value Settings (REQUIRED)

    Purpose: Define project-wide configuration settings for CLAUDE.md.
    Only ONE <configurations> block per CLAUDE.md (project-level).
    This element is REQUIRED in every CLAUDE.md file.

    Structure:
    <configurations>
      <var name="AXEL_CORE_PLUGIN_ROOT" value="..."/>  <!-- REQUIRED -->
      <var name="COMMIT_MESSAGE_FORMAT" value="..."/>  <!-- REQUIRED -->
      <var name="KEY" value="value"/>
    </configurations>

    Attributes (for <var> children):
    - name: Configuration key in UPPERCASE (required)
    - value: Configuration value (required)
    - No type attribute needed (values are self-descriptive)

    Required Variables:
    - AXEL_CORE_PLUGIN_ROOT: Path to AXEL core plugin (required)
    - COMMIT_MESSAGE_FORMAT: Git commit message style (required)
      - Values: "single-line", "conventional", "detailed"

    Example - Project Configuration:
    <configurations>
      <var name="AXEL_CORE_PLUGIN_ROOT" value="${CLAUDE_PLUGIN_ROOT}"/>
      <var name="COMMIT_MESSAGE_FORMAT" value="conventional"/>
      <var name="DEFAULT_WORKSPACE" value="default"/>
      <var name="AUTO_SAVE" value="true"/>
      <var name="LOG_LEVEL" value="info"/>
    </configurations>

    Usage Guidelines:
    - Place after <locale> and before registries (documents, templates, etc.)
    - Use for project-wide settings that affect AI behavior
    - Variable names MUST be UPPERCASE with underscores (SCREAMING_SNAKE_CASE)
    - Values are strings (boolean/numeric values as strings)

    Common Configuration Keys:
    - AXEL_CORE_PLUGIN_ROOT: Path to AXEL core plugin (REQUIRED)
    - COMMIT_MESSAGE_FORMAT: Git commit style (REQUIRED)
    - DEFAULT_WORKSPACE: Default workspace name for todos
    - AUTO_SAVE: Enable/disable automatic session saving
    - LOG_LEVEL: Logging verbosity (debug, info, warn, error)
    ]]>
  </pattern>

  <checklist name="claude-md-creation">
    Structure:
    - Is CLAUDE.md in project root?
    - Does .claude/ folder structure exist?
    - Does .claude/ folder exist with proper structure?

    Required Elements:
    - Is document type="project"?
    - Does project tag have name?
    - Is stack defined?
    - Is locale defined?

    Bootstrap Reference (optional):
    - If using AXEL features, reference plugin's AXEL-Bootstrap.md
    - If referencing, use <documents name="axel-bootstrap" load="always">
    - CLAUDE.md should contain project-specific enforcement rules

    Configuration (required):
    - Is configurations block present and single instance?
    - Is AXEL_CORE_PLUGIN_ROOT variable defined?
    - Is COMMIT_MESSAGE_FORMAT variable defined?
    - Do var elements have name and value attributes?
    - Are configuration keys UPPERCASE (SCREAMING_SNAKE_CASE)?

    Quality:
    - No circular references?
    - No duplicate definitions?
    - Minimal load="always" usage?
    - Skills/agents have clear responsibilities?

    Registries:
    - documents: load="on-demand" default, references and standards
    - memories: load="always", session and learned data
    - templates: load="on-demand", code patterns (optional)
    - skills: load="on-demand", expert roles (optional)
    - agents: load="on-demand", autonomous tasks (optional)
    - commands: no load attribute, slash commands (optional)

    Agent Extended Config (optional):
    - Is prompt content clear and actionable?
    - Do documents have src and ask attributes?
    - Do templates have src, name, and ask attributes?
    - Are ask keywords comma-separated?
    - Does config extend (not replace) agent behavior?
  </checklist>

  <understanding/>

</document>
```
