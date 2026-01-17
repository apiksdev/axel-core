---
name: axel-brainstorm
description: Brainstorm engineering - structured understanding of user requests before planning
type: reference
---

```xml
<document type="reference">

  <enforcement>
    - MUST gather context before interpreting user request
    - MUST identify ambiguities and ask clarifying questions
    - NEVER assume technical choices without user confirmation
    - NEVER skip context gathering phase
    - Read `src` attribute from template references to locate brainstorm template files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
  </enforcement>

  <objective>
    Structure of brainstorm definition files. AXEL Brainstorm is an XML-based configuration format for structured understanding of user requests before planning. It applies AXEL Methodology principles (question-driven understanding, no assumptions) to the discovery phase.
  </objective>

  <frontmatter>
    <![CDATA[
---
name: brainstorm-feature          # Brainstorm name (kebab-case)
description: Feature brainstorm   # Short description, max 200 characters
type: brainstorm                  # Always "brainstorm"
---
    ]]>
  </frontmatter>

  <templates load="always" mode="context">
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/brainstorm/AXEL-Brainstorm-Template-Bootstrap.md"/>
    <axel-tag-structure>
      <![CDATA[
      Brainstorm Document Structure (Unified)
      +-- Frontmatter (name, description, type: brainstorm)
      +-- # Brainstorm Title
      +-- ```xml
      +-- <document type="brainstorm">
      |   +-- <enforcement> [all]
      |   +-- <objective> [all]
      |   +-- <documents name="{required}" load="always|on-demand" mode="context"> [all, optional]
      |   |   +-- <read src="path/to/file.md" ask="[triggers]"/>
      |   +-- <user_request> [all]
      |   +-- <interpretation> [all]
      |   +-- <scope> [all]
      |   +-- <context_findings> [all]
      |   +-- <affected_components> [feature, code-review, migration]
      |   +-- <tech_stack> [project]
      |   +-- <review_criteria> [code-review]
      |   +-- <current_state> [migration]
      |   +-- <target_state> [migration]
      |   +-- <questions_to_answer> [all]
      |   +-- <sources_to_check> [research]
      |   +-- <suggested_documents> [all]
      |   +-- <open_questions> [all]
      |   +-- <assumptions> [all]
      |   +-- <next_steps> [all]
      |   +-- <understanding/> [all]
      +-- </document>
      +-- ```
      ]]>
    </axel-tag-structure>
    <understanding>
      !! MANDATORY: READ -> UNDERSTAND -> APPLY !!
      - READ the template file first
      - UNDERSTAND the structure and patterns
      - APPLY the template structure EXACTLY
      Reference = HOW to think | Template = HOW to write
    </understanding>
  </templates>

  <context>
    - Used for structured understanding before planning
    - Applies AXEL Methodology to discovery phase
    - Supports multiple brainstorm types: Feature, Project, Research, Code-Review, Migration
    - Ensures user requests are fully understood before implementation
    - Prevents unclear requirements from producing faulty plans
  </context>

  <principle name="brainstorm-first">
    Entry Point: Understanding Before Action
    - Every task MUST start with brainstorm phase
    - Gather context (docs, codebase, web) based on request
    - Interpret and summarize understanding
    - Identify uncertainties and ask questions
    - NEVER proceed to planning without clear understanding
  </principle>

  <principle name="core-principles">
    - Understanding First: Unclear request = unclear plan = faulty result
    - Ask Questions: Don't guess missing information, ask the user
    - Gather Context: Check docs, codebase, and external sources
    - Identify Scope: Define clear boundaries (include/exclude)
    - Document Assumptions: Make implicit assumptions explicit
  </principle>

  <decision name="brainstorm-type-structure" date="2024-12">
    When: Creating brainstorms for different scenarios
    Action: Use scenario-specific structure
    - Feature: user_request, interpretation, scope, context_findings, questions_to_answer, affected_components, suggested_documents, open_questions, assumptions, next_steps
    - Project: user_request, interpretation, tech_stack, scope, context_findings, suggested_documents, open_questions, assumptions, next_steps
    - Research: user_request, interpretation, scope, questions_to_answer, sources_to_check, context_findings, suggested_documents, open_questions, assumptions, next_steps
    - Code-Review: user_request, interpretation, scope, review_criteria, affected_components, context_findings, suggested_documents, open_questions, assumptions, next_steps
    - Migration: user_request, interpretation, current_state, target_state, scope, context_findings, suggested_documents, open_questions, assumptions, next_steps
    Reason: Each scenario has different discovery requirements
  </decision>

  <decision name="output-to-todo" date="2024-12">
    When: Brainstorm is complete
    Action: Output structured understanding for Todo creation
    - suggested_documents -> Todo's documents element
    - scope -> Todo's scope/context element
    - interpretation -> Todo's objective element
    - open_questions -> Must be resolved before Todo creation
    Reason: Brainstorm output feeds directly into Todo creation
  </decision>

  <pattern name="context-gathering">
    <![CDATA[
    Context Gathering Process:
    1. Project documents: Check CLAUDE.md, references, existing docs
    2. Codebase: Scan relevant files, identify patterns
    3. External sources: Web search for docs, best practices (if needed)
    4. Existing implementations: Find similar features as reference

    Output Format:
      <context_findings>
        Project Documents:
        - Document name: Key finding

        Codebase:
        - File/pattern: Finding

        External:
        - Source: Finding
      </context_findings>
    ]]>
  </pattern>

  <pattern name="scope-definition">
    <![CDATA[
    Scope Definition Format:
      <scope>
        Include:
        - What IS part of this brainstorm
        - Specific files, features, components

        Exclude:
        - What is NOT part of this brainstorm
        - Out-of-scope items to avoid confusion

        Boundaries:
        - Clear limits on what will be analyzed/designed
      </scope>
    ]]>
  </pattern>

  <pattern name="suggested-documents">
    <![CDATA[
    Suggested Documents Format:
      <suggested_documents>
        Reference Files:
        - references/path/to/file.md

        Codebase Files:
        - @src/path/to/file.cs
        - @src/path/to/another.cs

        External:
        - URL or documentation reference
      </suggested_documents>

    Note: Use @ prefix for codebase files to indicate they should be loaded as context
    ]]>
  </pattern>

  <requirements>
    - Frontmatter must include name (kebab-case), description, type: brainstorm
    - Document must have type="brainstorm" root element
    - Use correct template for brainstorm type (Feature/Project/Research/Code-Review/Migration)
    - user_request must capture original request verbatim or summarized
    - interpretation must summarize understanding clearly
    - scope must define include/exclude boundaries
    - suggested_documents must list files for Todo context
    - open_questions must be identified (can be empty if none)
  </requirements>

  <implementation name="file-locations">
    .claude/brainstorms/
    - {brainstorm-name}.md        # Brainstorm file (e.g.: feature-auth.md)
  </implementation>

  <implementation name="creating-brainstorm">
    Step 1 - Determine Brainstorm Type:
    - Feature: New feature understanding
    - Project: Project setup understanding
    - Research: Investigation/exploration
    - Code-Review: Code analysis preparation
    - Migration: System change understanding

    Step 2 - Capture User Request:
    - Record original request verbatim or summarized
    - Identify key goals and expectations

    Step 3 - Gather Context:
    - Check project documents (CLAUDE.md, references)
    - Scan relevant codebase files
    - Search external sources if needed

    Step 4 - Define Scope:
    - Include: What IS part of this brainstorm
    - Exclude: What is NOT part of this brainstorm
    - Boundaries: Clear limits on analysis

    Step 5 - Interpret and Analyze:
    - Summarize understanding clearly
    - Identify affected components (feature, code-review, migration)
    - Document context findings

    Step 6 - Identify Unknowns:
    - List open questions for user clarification
    - Document assumptions being made
    - Suggest documents for Todo context

    Step 7 - Define Next Steps:
    - What should happen after brainstorm
    - Typically: Todo creation with gathered information

    Step 8 - AXEL Checklist:
    - MUST validate against AXEL-Checklist.md standards
    - Verify brainstorm-validation checklist
  </implementation>

  <output format="markdown">
    File: {brainstorm-name}.md
    Path: .claude/brainstorms/{brainstorm-name}.md
    Structure:
    - YAML frontmatter (---)
    - Markdown title (# Brainstorm Name)
    - AXEL XML in code fence (```xml ... ```)
    - Document type="brainstorm" with user_request, interpretation, scope
  </output>

  <verification>
    - Is frontmatter correct? (name: kebab-case, type: brainstorm)
    - Is correct template used for brainstorm type?
    - Is user_request captured accurately?
    - Is interpretation clear and specific?
    - Is scope defined with include/exclude?
    - Are suggested_documents listed?
    - Are open_questions identified?
  </verification>

  <checklist name="brainstorm-validation">
    Pre-brainstorm:
    - Has brainstorm type been determined? (Feature/Project/Research/Code-Review/Migration)
    - Has context gathering been initiated?
    - Are there clarifying questions to ask?

    Post-brainstorm (All Types):
    - Is frontmatter correct? (name: kebab-case, type: brainstorm)
    - Is user_request captured?
    - Is interpretation clear?
    - Is scope defined? (include/exclude)
    - Are suggested_documents listed?
    - Are open_questions identified?
    - Are assumptions documented?
    - Are next_steps defined?

    Post-brainstorm (Feature):
    - Are questions_to_answer defined? (Functional, Technical, Design)
    - Are affected_components identified?
    - Are integration points documented?

    Post-brainstorm (Project):
    - Is tech_stack defined?
    - Are architectural decisions documented?

    Post-brainstorm (Research):
    - Are questions_to_answer listed?
    - Are sources_to_check identified?

    Post-brainstorm (Code-Review):
    - Are review_criteria defined?
    - Are files to review listed in affected_components?

    Post-brainstorm (Migration):
    - Is current_state documented?
    - Is target_state defined?
    - Are risks identified?
  </checklist>

  <understanding/>

</document>
```
