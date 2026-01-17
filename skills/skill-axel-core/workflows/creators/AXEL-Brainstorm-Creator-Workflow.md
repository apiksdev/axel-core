---
name: brainstorm-creator-workflow
description: Brainstorm document creator with inquiry workflow selection - linear execution flow for creating AXEL brainstorm documents (5 types)
type: workflow
triggers:
  - create brainstorm
  - brainstorm creator
  - new brainstorm
---

# AXEL Workflow: Brainstorm Creator

```xml
<document type="workflow">

  <enforcement>
    <![CDATA[
    PATH RESOLUTION:
    - Read the `src`, `ref`, or `target` attribute from the document XML to locate referenced files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory

    REFERENCE-BASED CREATION:
    - ALWAYS read AXEL-Brainstorm.md for structure, implementation steps, and validation
    - DO NOT duplicate content from reference documents
    - Reference documents are already loaded - use them as source of truth

    BRAINSTORM CREATION RULES:
    - MUST let user select inquiry workflow (Discovery, Elicitation, Socratic, Deep Inquiry)
    - MUST run selected inquiry workflow first for context gathering
    - MUST detect brainstorm type (5 types: feature, project, research, code-review, migration)
    - NEVER skip context gathering phase
    - Each type has different element requirements from AXEL-Brainstorm.md
    - Linear execution flow - stages run sequentially, no goto statements
    ]]>
  </enforcement>

  <objective>
    Create AXEL brainstorm documents through structured inquiry using reference-based approach.
    All specifications, type structures, and patterns are read from AXEL-Brainstorm.md.
    User selects inquiry workflow (Discovery, Elicitation, Socratic, Deep Inquiry) for context gathering.
    Optional output configuration allows saving brainstorm execution results to type-specific folders.
    Flow: select_inquiry → brainstorm → detect → collect → validate → generate → save → output_config
  </objective>

  <variables>
    <var name="topic" from="param.topic"/>
    <var name="context" from="param.context" default=""/>
    <var name="inquiry_mode" default="discovery"/>
  </variables>

  <documents load="always" mode="context">
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/references/AXEL-Brainstorm.md"/>
    <understanding>
      <![CDATA[
      !! MANDATORY: READ -> UNDERSTAND -> APPLY !!

      Bootstrap: Already loaded via skill-axel-core

      AXEL-Brainstorm.md provides:
      - <axel-tag-structure>: Element order and document hierarchy
      - <implementation name="creating-brainstorm">: Step-by-step creation process (Step 1-8)
      - <checklist name="brainstorm-validation">: Complete validation checklist
      - <frontmatter>: Specification format
      - <principle>: brainstorm-first, core-principles
      - <pattern>: context-gathering, scope-definition, suggested-documents
      - <decision name="brainstorm-type-structure">: 5 type structures
      - <decision name="output-to-todo">: Output mapping

      Brainstorms apply AXEL Methodology to discovery phase:
      Understanding Before Action - Gather context, ask questions, document assumptions.

      This workflow orchestrates the process - all content comes from reference.
      ]]>
    </understanding>
  </documents>

  <workflows name="inquiry" load="on-trigger">
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/workflows/brainstorm/refs/AXEL-Discovery-Workflow.md" trigger="discovery"/>
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/workflows/brainstorm/refs/AXEL-Elicitation-Workflow.md" trigger="elicitation"/>
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/workflows/brainstorm/refs/AXEL-Socratic-Workflow.md" trigger="socratic"/>
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/workflows/brainstorm/refs/AXEL-Deep-Inquiry-Workflow.md" trigger="deep"/>
    <understanding>
      !! MANDATORY: READ → UNDERSTAND → APPLY !!
      Inquiry workflow registry. User selects which inquiry approach to use for brainstorming.
    </understanding>
  </workflows>

  <execution flow="linear">
    <![CDATA[
    BRAINSTORM CREATOR WORKFLOW (9 Steps):

    Step 1 - Receive Parameters:
    - topic: ${param.topic} (required)
    - context: ${param.context} (optional)

    Step 2 - Select Inquiry Workflow:
    - Display inquiry workflow options to user:
      1. Discovery - Explore new topics, gather broad context (What?)
      2. Elicitation - Extract details, clarify ambiguities (How?)
      3. Socratic - Challenge assumptions, validate decisions (Why?)
      4. Deep Inquiry - Analyze risks, explore scenarios (What if?)
    - Ask user which inquiry approach (1-4 or name)
    - Map selection to workflow trigger (1→discovery, 2→elicitation, 3→socratic, 4→deep)
    - Resolve workflow path from inquiry workflows registry

    Step 3 - Run Inquiry Workflow:
    - Execute selected inquiry workflow with topic and context parameters
    - Gather brainstorm findings:
      - context_findings: discoveries from docs/codebase/external
      - key_questions: questions to ask user
      - recommendations: suggested next steps

    Step 4 - Detect Brainstorm Type:
    - Display brainstorm type options to user:
      1. Feature - New feature brainstorming
      2. Project - New project discovery
      3. Research - Topic investigation
      4. Code-Review - Code review preparation
      5. Migration - System migration planning
    - Ask user which brainstorm type (1-5 or name)
    - Map selection to brainstorm type (1→feature, 2→project, 3→research, 4→code-review, 5→migration)

    Step 5 - Collect Requirements:
    - Generate type-specific questions based on detected brainstorm type:
      - Feature: questions_to_answer, affected_components, integration_points
      - Project: tech_stack, architectural_decisions
      - Research: questions_to_answer, sources_to_check
      - Code-Review: review_criteria, files_to_review
      - Migration: current_state, target_state, risks
      - All types: context_findings, suggested_documents, open_questions, assumptions, next_steps
    - Display questions to user
    - Ask user to provide/confirm requirements
    - Parse user input into structured format:
      - Common elements: name, description, brainstorm_type, user_request, interpretation, scope
      - Type-specific elements based on detected type
      - Context elements: context_findings, suggested_documents, open_questions, assumptions, next_steps

    Step 6 - Validate:
    - Validate collected requirements against AXEL-Brainstorm.md checklist:
      - Frontmatter: name (kebab-case), type: brainstorm
      - Common: user_request, interpretation, scope, suggested_documents, open_questions, assumptions, next_steps
      - Type-specific: validate based on brainstorm_type
    - If validation fails:
      - Display validation errors
      - Stop with error (linear flow cannot loop back)
      - User must restart workflow with corrected information
    - If validation passes: continue to generation

    Step 7 - Generate Document:
    - Create brainstorm document following AXEL-Brainstorm.md structure:
      - Frontmatter with name (kebab-case), description, type: brainstorm
      - Element order per axel-tag-structure
      - Type-specific elements from brainstorm-type-structure decision
      - Apply patterns: context-gathering, scope-definition, suggested-documents
    - Determine save path and filename:
      - Reference: AXEL-Brainstorm.md <implementation name="file-locations">
      - Path format: .claude/brainstorms/{name}.md

    Step 8 - Save Brainstorm:
    - Display document preview to user:
      - Name, Type, Path
      - Full document content
    - Write brainstorm document to file: .claude/brainstorms/{name}.md
    - Display success message with created document path

    Step 9 - Output Configuration (Optional):
    - Ask user: "Would you like to configure output path for this brainstorm's results?"
    - If user says yes:
      - Determine default output path based on brainstorm_type:
        - feature → .claude/outputs/features/
        - project → .claude/outputs/projects/
        - research → .claude/outputs/research/
        - code-review → .claude/outputs/reviews/
        - migration → .claude/outputs/migrations/
      - Ask user to confirm or customize output path
      - Add <output> element to brainstorm document with configured path
      - Update saved brainstorm document with output configuration
    - If user says no:
      - Skip output configuration
      - Brainstorm can be executed without saving output to file
    - Display final message with:
      - Reference to AXEL-Brainstorm.md output-to-todo decision
      - Recommendation: Use this brainstorm output for Todo creation
    ]]>
  </execution>

  <output format="json">
    {
      "content": "generated brainstorm document",
      "name": "brainstorm name",
      "brainstorm_type": "feature|project|research|code-review|migration",
      "path": "save path"
    }
  </output>

  <understanding/>

</document>
```
