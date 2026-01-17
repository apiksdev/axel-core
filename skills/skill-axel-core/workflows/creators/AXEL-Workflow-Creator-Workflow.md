---
name: workflow-creator-workflow
description: Workflow document creator - collects requirements and generates AXEL workflow documents
type: workflow
triggers:
  - create workflow
  - workflow creator
  - new workflow
---

# AXEL Workflow: Workflow Creator

```xml
<document type="workflow">

  <enforcement>
    <![CDATA[
    PATH RESOLUTION:
    - Read the `src`, `ref`, or `target` attribute from the document XML to locate referenced files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory

    REFERENCE-BASED CREATION:
    - ALWAYS read AXEL-Workflow.md for structure, implementation steps, and validation
    - DO NOT duplicate content from reference documents
    - Reference documents are already loaded - use them as source of truth
    ]]>
  </enforcement>

  <objective>
    Create AXEL workflow documents through structured inquiry using reference-based approach.
    All specifications, patterns, and stage structures are read from AXEL-Workflow.md.
  </objective>

  <variables>
    <var name="topic" from="param.topic"/>
    <var name="context" from="param.context" default=""/>
  </variables>

  <documents load="always" mode="context">
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/references/AXEL-Workflow.md"/>
    <understanding>
      <![CDATA[
      !! MANDATORY: READ -> UNDERSTAND -> APPLY !!

      Bootstrap: Already loaded via skill-axel-core

      AXEL-Workflow.md provides:
      - <axel-tag-structure>: Element order and document hierarchy
      - <implementation name="creating-workflow">: Step-by-step creation process (Step 1-8)
      - <checklist name="workflow-validation">: Complete validation checklist
      - <frontmatter>: Specification and format
      - <principle>: stage-structure, stage-rules, tasks-rules
      - <pattern>: stage, confirm, parallel, tasks, print, ask, goto
      - <decision name="scenario-stage-selection">: Workflow type patterns

      Workflows use STAGED flow with stage progression:
      INIT → DISCOVER → ANALYZE → EXECUTE → VERIFY → COMPLETE

      This workflow orchestrates the process - all content comes from reference.
      ]]>
    </understanding>
  </documents>

  <execution flow="linear">
    <![CDATA[
    LINEAR EXECUTION - Reference-based workflow creation:

    Step 1 - Understand Document Structure:
    - Read AXEL-Workflow.md <axel-tag-structure>
    - Understand element order: frontmatter → objective → documents → variables → execution (stages)
    - Identify required vs optional elements
    - Know stage-based flow structure

    Step 2 - Follow Implementation Guide:
    - Read AXEL-Workflow.md <implementation name="creating-workflow">
    - This defines Step 1-8 creation process
    - Each step collects specific information needed for workflow document

    Step 3 - Collect Identity (Implementation Step 1):
    - Ask user for workflow name (kebab-case, e.g., deploy-notification)
    - Ask for description (max 200 chars)
    - Ask for triggers (keywords that activate workflow)
    - Reference: AXEL-Workflow.md <frontmatter> for format

    Step 4 - Select Workflow Type (Implementation Step 2):
    - Reference: AXEL-Workflow.md <decision name="scenario-stage-selection">
    - Present workflow types:
      * Document creation: INIT → DISCOVER → EXECUTE → COMPLETE
      * Research: INIT → DISCOVER → ANALYZE → COMPLETE
      * Code review: INIT → DISCOVER → ANALYZE → COMPLETE
      * Code development: INIT → DISCOVER → ANALYZE → EXECUTE → VERIFY → COMPLETE
      * Installation: INIT → DISCOVER → CONFIRM → EXECUTE → COMPLETE
      * Debugging: INIT → DISCOVER → ANALYZE → EXECUTE → VERIFY → (loop)
    - Each type determines stage pattern

    Step 5 - Understand Stage Principles (Implementation Step 3):
    - Reference: AXEL-Workflow.md <principle name="stage-structure">
    - Stage progression: INIT → DISCOVER → ANALYZE → EXECUTE → VERIFY → COMPLETE
      * INIT: Load context, set target (required)
      * DISCOVER: Gather information, user input (optional)
      * ANALYZE: Evaluate, synthesize (optional)
      * EXECUTE: Perform action (optional)
      * VERIFY: Validate, test (optional)
      * COMPLETE: Report, finalize (required)
    - Reference: AXEL-Workflow.md <principle name="stage-rules">
      * Implicit flow: stages run in definition order
      * Conditional jump: goto with when + to attributes
      * Termination: last stage ends with stop
      * Naming: simple id (e.g., "init" not "stage:init")

    Step 6 - Define Stages Based on Type:
    - For each stage needed (from selected workflow type):
      * What does stage do?
      * Any user confirmations? (use <confirm> pattern)
      * Any parallel execution? (use <parallel> pattern)
    - Reference: AXEL-Workflow.md <pattern>:
      * stage: Basic workflow stage
      * confirm: User confirmation stage
      * parallel: Parallel execution
      * tasks: Batch declarative operations
      * print: Display message
      * ask: User input request
      * goto: Conditional jump (ONLY with when condition)

    Step 7 - Define Tasks Operations:
    - Reference: AXEL-Workflow.md <pattern name="tasks">
    - Tasks use declarative format inside CDATA:
      * Create folders: - folder/path/ (description)
      * Create files: - file.md <- Template.md
      * Copy files: - source.txt -> destination/
      * Validate: - target (validation rule)
    - Reference: AXEL-Workflow.md <principle name="tasks-rules">

    Step 8 - Define Variables & Input (Implementation Step 4):
    - Identify required variables (var element)
    - User input prompts (ask element with YAML-like format)
    - Variable sources: from="param.*" or ask="user"
    - Set defaults with value="..."

    Step 9 - Choose Execution Flow (linear vs staged):
    - Flow: linear | staged
      * linear: Text-based instructions (for simple workflows only)
        - Sequential steps without loops
        - No skill/workflow/agent invocation
        - Simple document creation, basic automation
        - Example: Memory save, simple file operations
      * staged: ONLY for highly complex scenarios requiring (RECOMMENDED for 95% of workflows):
        - Skill invocation (<invoke name="Skill">)
        - Workflow execution (<workflow src="...">)
        - Agent chaining (<invoke name="Task"> with subagent)
        - User confirmations (<confirm> pattern)
        - Parallel execution (<parallel> pattern)
        - Tasks operations (Create folders/files, Copy files, Validate)
        - Iterative refinement loops (repeat until quality threshold met)
        - Dynamic branching based on intermediate results
        - Example: Installation workflows, code development flows, deployment pipelines
    - Main stages in order (what workflow does)
    - Output structure: Markdown with XML code fence (```xml ... ```)

    Step 11 - Validate Requirements (Implementation Step 6):
    - Use AXEL-Workflow.md <checklist name="workflow-validation">
    - Check: frontmatter, structure, stages, parallel, tasks, user interaction, termination
    - Verify:
      * Frontmatter format (name kebab-case, type: workflow, triggers defined)
      * Required stages exist (INIT, DISCOVER or EXECUTE, COMPLETE)
      * Stage ids are simple names (no prefix)
      * Implicit flow (stages run in order)
      * Last stage ends with stop
      * Goto uses when + to attributes (NO when-less goto)
      * Element order matches <axel-tag-structure>
    - If missing information → ask user for clarification
    - If validation fails → return to relevant step

    Step 12 - Generate Document (Implementation Step 7):
    - Apply AXEL-Workflow.md <axel-tag-structure> element order
    - Use appropriate template based on workflow type
    - Map collected data to document structure:
      * Frontmatter (name, description, type, triggers)
      * XML document start (type="workflow")
      * Objective
      * Documents registry (if external docs needed)
      * Variables (if any)
      * Execution block with stages
      * Understanding (empty, at end)
    - Path: .claude/workflows/${name}.md

    Step 13 - Final Verification (Implementation Step 8):
    - Validate against AXEL-Checklist.md standards
    - Verify: frontmatter format, document structure, element order
    - Check execution-validation rules
    - Ensure understanding element at document end
    - Verify stage compliance:
      * Required stages present
      * Stage order correct
      * Simple stage ids
      * Implicit flow used
      * Goto has when conditions (no default goto)

    Step 14 - Save and Confirm:
    - Create file: .claude/workflows/${name}.md
    - Display file path and creation confirmation
    - Output: {content, name, path}
    ]]>
  </execution>

  <output format="json">
    {
      "content": "generated workflow document",
      "name": "workflow name",
      "path": "file save path"
    }
  </output>

  <understanding/>

</document>
```
