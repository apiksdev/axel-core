---
name: agent-creator-workflow
description: Agent document creator - collects requirements and generates AXEL agent documents
type: workflow
triggers:
  - create agent
  - agent creator
  - new agent
---

# AXEL Workflow: Agent Creator

```xml
<document type="workflow">

  <enforcement>
    <![CDATA[
    PATH RESOLUTION:
    - Read the `src`, `ref`, or `target` attribute from the document XML to locate referenced files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory

    REFERENCE-BASED CREATION:
    - ALWAYS read AXEL-Agent.md for structure, implementation steps, and validation
    - DO NOT duplicate content from reference documents
    - Reference documents are already loaded - use them as source of truth
    ]]>
  </enforcement>

  <objective>
    Create AXEL agent documents through structured inquiry using reference-based approach.
    All specifications, checklists, and patterns are read from AXEL-Agent.md.
  </objective>

  <variables>
    <var name="topic" from="param.topic"/>
    <var name="context" from="param.context" default=""/>
  </variables>

  <documents load="always" mode="context">
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/references/AXEL-Agent.md"/>
    <understanding>
      <![CDATA[
      !! MANDATORY: READ -> UNDERSTAND -> APPLY !!

      Bootstrap: Already loaded via skill-axel-core

      AXEL-Agent.md provides:
      - <axel-tag-structure>: Element order and document hierarchy
      - <implementation name="creating-agent">: Step-by-step creation process (Step 1-8)
      - <checklist name="agent-validation">: Complete validation checklist
      - <frontmatter>: Specification and color/permission guidelines
      - <archetypes>: Four agent types with purpose and tools
      - <system-prompt-design>: Content and length guidelines

      This workflow orchestrates the process - all content comes from reference.
      ]]>
    </understanding>
  </documents>

  <execution flow="linear">
    <![CDATA[
    LINEAR EXECUTION - Reference-based agent creation:

    Step 1 - Understand Document Structure:
    - Read AXEL-Agent.md <axel-tag-structure>
    - Understand element order: enforcement → objective → documents → archetype → system-prompt → variables → execution → output → understanding
    - Identify required vs optional elements
    - Know where each piece of information belongs in final structure

    Step 2 - Follow Implementation Guide:
    - Read AXEL-Agent.md <implementation name="creating-agent">
    - This defines Step 1-8 creation process
    - Each step collects specific information needed for agent document

    Step 3 - Collect Identity (Implementation Step 1):
    - Ask user for agent name (agent-* prefix, kebab-case)
    - Ask for description (max 200 chars, guides AI when to invoke)
    - Reference: AXEL-Agent.md <frontmatter> for naming rules

    Step 4 - Select Archetype (Implementation Step 2):
    - Present four archetypes from AXEL-Agent.md <archetypes>:
      * analysis: Code review, PR analysis, security audit
      * generation: Content creation, code generation
      * validation: Standards check, lint, verification
      * orchestration: Multi-step workflow coordination
    - Each archetype has recommended tools and output format

    Step 5 - Configure Agent (Implementation Step 3):
    - Model: inherit | sonnet | opus | haiku
    - Color: Reference AXEL-Agent.md <frontmatter> color selection guide
    - Tools: Based on archetype recommendations, apply least privilege
    - Permission mode (optional): default | acceptEdits | bypassPermissions | plan | ignore

    Step 6 - Define Behavior (Implementation Step 4):
    - System prompt design from AXEL-Agent.md <system-prompt-design>:
      * Role: "You are a [role] that [function]..."
      * Core responsibilities: 3-5 items
      * Quality standards: critical/major/minor
      * Edge case handling (brief)
    - Length: 300-2,000 characters (optimal: 300-1,500)
    - Focus on WHO + HOW TO BEHAVE (not step-by-step process)

    Step 7 - Define Execution (Implementation Step 5):
    - Flow: linear | staged
      * linear: Text-based instructions (RECOMMENDED for 95% of agents)
        - Sequential steps without loops
        - No skill/workflow/agent invocation
        - Simple analysis, generation, validation tasks
        - Example: Code review, documentation generation, file analysis
      * staged: ONLY for highly complex scenarios requiring:
        - Skill invocation (<invoke name="Skill">)
        - Workflow execution (<workflow src="...">)
        - Agent chaining (<invoke name="Task"> with subagent)
        - Iterative refinement loops (repeat until quality threshold met)
        - User approval flows (generate → review → revise → approve)
        - Dynamic branching based on intermediate results
        - Example: Multi-agent orchestration, complex refactoring with validation loops
    - Main steps in order (what agent does)
    - Output structure: Markdown with XML code fence (```xml ... ```)

    Step 8 - Validate Requirements (Implementation Step 6):
    - Use AXEL-Agent.md <checklist name="agent-validation">
    - Check: frontmatter, structure, system-prompt, execution
    - Verify element order matches <axel-tag-structure>
    - If missing information → ask user for clarification
    - If validation fails → return to relevant step

    Step 9 - Generate Document (Implementation Step 7):
    - Apply AXEL-Agent.md <axel-tag-structure> element order
    - Use appropriate template based on flow choice (linear/staged)
    - Map collected data to document structure
    - Frontmatter → XML document → understanding at end
    - Path: .claude/agents/${name}/AGENT.md

    Step 10 - Final Verification (Implementation Step 8):
    - Validate against AXEL-Checklist.md standards
    - Verify: frontmatter format, document structure, element order
    - Check execution-validation rules
    - Ensure understanding element at document end

    Step 11 - Save and Confirm:
    - Create directory if needed: .claude/agents/${name}/
    - Save agent document to AGENT.md
    - Display file path and creation confirmation
    - Output: {content, name, archetype, path}
    ]]>
  </execution>

  <output format="json">
    {
      "content": "generated agent document",
      "name": "agent name",
      "archetype": "selected archetype",
      "path": "file save path"
    }
  </output>

  <understanding/>

</document>
```
