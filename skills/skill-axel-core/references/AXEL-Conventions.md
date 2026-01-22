---
name: axel-conventions
description: AXEL DSL style guide - how to write consistent AXEL documents
type: reference
---

# AXEL Conventions

```xml
<document type="reference">

  <enforcement>
    - Read the `src`, `ref`, or `target` attribute from the document XML to locate referenced files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
    - Conventions are style guidelines, not validation rules
    - Apply conventions for consistency, not correctness
  </enforcement>

  <objective>
    AXEL DSL style guide for writing consistent documents.
    Answers: "How should it be written?" (not "Is it correct?")
    Syntax = Vocabulary | Standards = Grammar | Checklist = Exam | Conventions = Writing Style
  </objective>

  <convention name="element-ordering"><![CDATA[
    Element Order (top to bottom):

    1. enforcement
    2. objective
    3. documents (load="always" first, then on-demand, then on-trigger)
    4. templates
    5. workflows
    6. skills
    7. agents
    8. variables
    9. type-specific elements (context, scope, requirements, etc.)
    10. execution
    11. output
    12. verification
    13. checklist
    14. understanding/

    Registry blocks order (within documents/templates/etc.):
    - read/ref elements first
    - understanding element LAST (inside the block)
  ]]></convention>

  <convention name="naming"><![CDATA[
    Naming Conventions:

    File names:
    - AXEL-{Name}-{Suffix}.md (PascalCase with hyphens)
    - Suffixes: Tpl (template), Workflow, Skill, Agent, etc.
    - Examples: AXEL-Todo-Linear-Tpl.md, AXEL-Discovery-Workflow.md

    Frontmatter name:
    - kebab-case always
    - skill prefix: skill-{name}
    - agent prefix: agent-{name}
    - Examples: skill-axel-expert, agent-code-reviewer

    Stage IDs:
    - Simple kebab-case: init, parse-input, validate-result, complete
    - NO prefixes like stage-, step-
    - Semantic names: what it does, not what number it is

    Variable names:
    - snake_case or camelCase (be consistent within document)
    - Descriptive: user_input, selectedWorkflow, base_path
    - NO single letters except loop iterators

    Registry names:
    - Lowercase: core, refs, templates, components
    - Descriptive of content group
  ]]></convention>

  <convention name="indentation"><![CDATA[
    Indentation:

    - 2 spaces (NOT tabs)
    - Consistent depth for child elements
    - CDATA content: align with element or use consistent internal indent
  ]]></convention>

  <convention name="attribute-ordering"><![CDATA[
    Attribute Order:

    General pattern: identity → source → behavior → metadata

    <read> element:
    1. src (required, first)
    2. ask (for on-demand)
    3. trigger (for on-trigger)
    4. mode (if not default)

    <documents/templates> element:
    1. name
    2. load
    3. mode

    <var> element:
    1. name
    2. from OR value
    3. default

    <stage> element:
    1. id (required, first)

    <invoke> element:
    1. name
    2. output
    3. resumable
  ]]></convention>

  <convention name="cdata-usage"><![CDATA[
    When to use CDATA:

    ALWAYS use CDATA for:
    - enforcement content
    - execution content (linear flow)
    - understanding content (inside registry blocks)
    - Content with special chars: < > & | && || ${}
    - Code examples
    - Multi-line structured content

    NO CDATA needed for:
    - Simple single-line text
    - objective (usually short)
    - Element content without special chars
  ]]></convention>

  <convention name="comments"><![CDATA[
    XML Comments:

    Format: <!-- stage_id: Short description -->

    Rules:
    - Single line ONLY
    - Placed directly BEFORE the element it describes
    - stage_id or element_id followed by colon
    - Brief description (5-10 words max)
  ]]></convention>

  <convention name="content-format"><![CDATA[
    Content Format:

    Bullet lists:
    - Use - for list items (not * or numbers)
    - Consistent indentation for nested items
    - One concept per line

    Headings inside CDATA:
    - Use text with colon: "Section Name:"
    - Or caps: "SECTION NAME"
    - NOT markdown # headings

    Variables in text:
    - Always ${varname} format
    - Descriptive names
    - Document what each variable contains

    Special markers:
    - !! MANDATORY: ... !! for critical instructions
    - Required: for enforcement rules
    - Optional: for optional elements
  ]]></convention>

  <convention name="understanding-format"><![CDATA[
    Understanding Element:

    Document-level (at end):
    - Self-closing: <understanding/>
    - NO content needed
    - MUST be last element before </document>

    Registry-level (inside documents/templates/etc.):
    - MUST have content
    - MUST start with: !! MANDATORY: READ -> UNDERSTAND -> APPLY !!
    - Brief description of what resources provide
    - 2-5 lines max
  ]]></convention>

  <convention name="enforcement-format"><![CDATA[
    Enforcement Format:

    Structure:
    1. PATH RESOLUTION (if document has file references)
    2. Context-specific rules
    3. Prohibitions (if any)

    Markers:
    - Regular rules: lines starting with -
    - Prohibitions: lines starting with X or using FORBIDDEN/NEVER
    - Critical sections: Use symbols like WARNING or FORBIDDEN
  ]]></convention>

  <convention name="execution-format"><![CDATA[
    Execution Format:

    Linear flow:
    - Use CDATA
    - Step N - Title: format
    - Bullet list under each step
    - Clear action verbs

    Staged flow:
    - Each stage has id
    - Comment before stage
    - tasks element with bullet list
    - goto or stop at end
  ]]></convention>

  <convention name="spacing"><![CDATA[
    Whitespace:

    Between major sections:
    - One blank line between top-level elements
    - No blank line between registry items (read, ref)
    - One blank line before understanding/ at document end

    Inside CDATA:
    - One blank line between logical sections
    - No trailing whitespace
    - Consistent indentation
  ]]></convention>

  <understanding/>

</document>
```
