---
name: skill-creator-workflow
description: Skill document creator - collects requirements and generates AXEL skill documents
type: workflow
triggers:
  - create skill
  - skill creator
  - new skill
---

# AXEL Workflow: Skill Creator

```xml
<document type="workflow">

  <enforcement>
    <![CDATA[
    PATH RESOLUTION:
    - Read the `src`, `ref`, or `target` attribute from the document XML to locate referenced files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory

    REFERENCE-BASED CREATION:
    - ALWAYS read AXEL-Skill.md for structure, implementation steps, and validation
    - DO NOT duplicate content from reference documents
    - Reference documents are already loaded - use them as source of truth
    ]]>
  </enforcement>

  <objective>
    Create AXEL skill documents through structured inquiry using reference-based approach.
    All specifications, principles, and patterns are read from AXEL-Skill.md.
  </objective>

  <variables>
    <var name="topic" from="param.topic"/>
    <var name="context" from="param.context" default=""/>
  </variables>

  <documents load="always" mode="context">
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/references/AXEL-Skill.md"/>
    <understanding>
      <![CDATA[
      !! MANDATORY: READ -> UNDERSTAND -> APPLY !!

      Bootstrap: Already loaded via skill-axel-core

      AXEL-Skill.md provides:
      - <axel-tag-structure>: Element order and document hierarchy
      - <implementation name="creating-skill">: Step-by-step creation process (Step 1-8)
      - <checklist name="skill-validation">: Complete validation checklist
      - <frontmatter>: Specification and allowed-tools
      - <principle>: skill-structure, staged-execution, trigger-routing, registry-loading
      - <pattern>: naming-convention, agents-registry
      - <decision>: trigger-based-loading, enforcement-placement

      Skills specialize AI in specific domains with role, capabilities, and execution.

      This workflow orchestrates the process - all content comes from reference.
      ]]>
    </understanding>
  </documents>

  <execution flow="linear">
    <![CDATA[
    LINEAR EXECUTION - Reference-based skill creation:

    Step 1 - Understand Document Structure:
    - Read AXEL-Skill.md <axel-tag-structure>
    - Understand element order: frontmatter → objective → documents → role → capabilities → templates → workflows → triggers → execution → understanding
    - Identify required vs optional elements
    - Know skill's purpose: Specialize AI in a domain

    Step 2 - Follow Implementation Guide:
    - Read AXEL-Skill.md <implementation name="creating-skill">
    - This defines Step 1-8 creation process
    - Each step collects specific information needed for skill document

    Step 3 - Collect Identity (Implementation Step 1):
    - Ask user for skill name (skill-* prefix, kebab-case, e.g., skill-frontend)
    - Ask for description (max 200 chars)
    - Reference: AXEL-Skill.md <frontmatter> for naming rules
    - Reference: AXEL-Skill.md <principle name="trigger-description"> for detailed description format

    Step 4 - Define Role & Objective (Implementation Step 2):
    - Reference: AXEL-Skill.md <principle name="skill-structure">
    - Role: Who is the AI? (persona, expertise level)
      * Example: "Frontend development specialist with expertise in React, TypeScript, and modern web patterns"
    - Objective: Main goal and purpose of the skill
      * What problem does this skill solve?
      * What is the skill's primary function?

    Step 5 - Define Capabilities (Implementation Step 3):
    - Reference: AXEL-Skill.md <principle name="skill-structure">
    - What can this skill do? (bullet list format)
    - List 3-7 core capabilities
    - Focus on specific, actionable capabilities
    - Example: "Create React components with TypeScript", "Implement state management patterns"

    Step 6 - Configure Tools (Implementation Step 4):
    - Reference: AXEL-Skill.md <frontmatter>
    - Allowed tools: Read, Write, Edit, Glob, Grep, Bash, Task, WebFetch, WebSearch, AskUserQuestion
    - Apply least privilege principle (only needed tools)
    - Disable model invocation: true | false (default: false)
      * true = manual-only skill, no auto-invoke
      * false = can be automatically invoked based on description

    Step 7 - Choose Execution Flow (Implementation Step 5):
    - Reference: AXEL-Skill.md <principle name="staged-execution">
    - Flow: linear | staged
      * linear: Text-based instructions (RECOMMENDED for 95% of skills)
        - Sequential steps without loops
        - No skill/workflow/agent invocation
        - Guidance-focused skills
        - Simple context provision
        - Trigger-based workflow dispatch (if using workflows registry with load="on-trigger")
        - Example: Code style guides, pattern libraries, best practices, workflow dispatchers
      * staged: ONLY for highly complex scenarios requiring:
        - Skill invocation (<invoke name="Skill">)
        - Workflow execution (<workflow src="...">)
        - Agent chaining (<invoke name="Task"> with subagent)
        - User confirmation checkpoints
        - Multi-step processing with branching logic
        - Example: Complex code generation, multi-step refactoring, deployment orchestration
    - If staged: Define stages needed
    - Triggers for stage routing (optional, Reference: AXEL-Skill.md <principle name="trigger-routing">)
      * Format: trigger="create component" or trigger="[test, testing]"
      * Automatic routing based on user input keywords

    Step 8 - Define Registries (Optional):
    - Reference: AXEL-Skill.md <principle name="registry-loading">
    - Documents registry: Reference documents for the skill
      * load="always": Always in context
      * load="on-demand": Load when ask keywords match
      * load="on-trigger": Load when triggers match
    - Templates registry: Output templates
    - Workflows registry: Step-by-step processes
      * load="on-trigger": Each workflow has trigger="..." attribute
      * IMPORTANT: If using workflows with load="on-trigger", execution MUST use trigger-based dispatch pattern:
        - Step 1: Receive parameters (trigger, prompt, etc.)
        - Step 2: Resolve trigger (from parameter or detect from prompt)
        - Step 3: Dispatch (Match trigger → workflows registry → execute workflow)
      * Example: See skill-axel-core SKILL.md execution pattern
    - Skills registry: Sub-skills (Reference: AXEL-Skill.md <pattern name="naming-convention">)
    - Agents registry: Sub-agents (Reference: AXEL-Skill.md <pattern name="agents-registry">)

    Step 9 - Validate Requirements (Implementation Step 6):
    - Use AXEL-Skill.md <checklist name="skill-validation">
    - Check: frontmatter, structure, registries, execution, triggers
    - Verify:
      * Frontmatter format (name: skill-*, type: skill, allowed-tools defined)
      * Role and objective defined
      * Capabilities in bullet list format
      * Documents registry defined (AXEL-Bootstrap.md FIRST with load="always")
      * If staged: init and complete stages exist
      * If triggers: all target stage ids exist
      * Element order matches <axel-tag-structure>
    - If missing information → ask user for clarification
    - If validation fails → return to relevant step

    Step 10 - Generate Document (Implementation Step 7):
    - Apply AXEL-Skill.md <axel-tag-structure> element order
    - Use appropriate template based on flow choice (linear/staged)
    - Map collected data to document structure:
      * Frontmatter (name, description, type, allowed-tools, disable-model-invocation)
      * XML document start (type="skill")
      * Objective
      * Documents registry (AXEL-Bootstrap.md FIRST)
      * Role
      * Capabilities
      * Templates/Workflows/Skills/Agents registries (if any)
      * Triggers (if staged with routing)
      * Execution block
      * Understanding (empty, at end)
    - Path: .claude/skills/${name}/SKILL.md
    - Output structure: Markdown with XML code fence (```xml ... ```)

    Step 11 - Final Verification (Implementation Step 8):
    - Validate against AXEL-Checklist.md standards
    - Verify: frontmatter format, document structure, element order
    - Check execution-validation rules
    - Ensure understanding element at document end
    - Reference: AXEL-Skill.md <principle name="writing-style">
      * Use imperative form in instructions
      * Use third-person in descriptions
      * Avoid "you" in instructions
    - Verify compliance:
      * AXEL-Bootstrap.md is FIRST in documents registry
      * Goto uses when conditions (NO when-less goto)
      * If staged: all stages have unique ids, last stage ends with stop
      * If workflows registry load="on-trigger": execution uses trigger-based dispatch pattern
        - Step 1: Receive parameters
        - Step 2: Resolve trigger
        - Step 3: Match and dispatch to workflow

    Step 12 - Save and Confirm:
    - Create directory if needed: .claude/skills/${name}/
    - Save skill document to SKILL.md
    - Display file path and creation confirmation
    - Output: {content, name, path}
    ]]>
  </execution>

  <output format="json">
    {
      "content": "generated skill document",
      "name": "skill name",
      "path": "file save path"
    }
  </output>

  <understanding/>

</document>
```
