---
name: axel-syntax
description: AXEL syntax reference - document types, tag categories, minimal syntax
type: reference
---

# AXEL Syntax

```xml
<document type="reference">

  <enforcement>
    - Read the `src`, `ref`, or `target` attribute from the document XML to locate referenced files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
    - Syntax reference loaded in every AXEL context
    - For detailed patterns and examples, load AXEL-Standards.md on-demand
    - MUST use AskUserQuestion tool for <ask> element execution
    - MUST use AskUserQuestion tool for <confirm> element execution
    - User interaction tags (ask, confirm, wait) REQUIRE AskUserQuestion tool
  - Documents with invoke resumable="true" are RESUMABLE:
    - On re-invoke, continue from last incomplete stage
    - Run to completion - only user cancellation interrupts flow

    ⛔ **XML COMMENT FORMAT (MANDATORY)**
    - ❌ NEVER use multi-line decorative comments
    - ❌ NEVER use box-style separators (====, ----, ****)
    - ✅ ALWAYS use single-line: <!-- stage_id: Description -->
    - Comment directly before target element
  </enforcement>

  <objective>
    AXEL (AI XML Execution Language) syntax reference.
    Minimal reference for document types, tag categories, and basic syntax.
    For detailed patterns, examples, and best practices → AXEL-Standards.md
  </objective>

  <principle name="document-types">
    Nine Core Document Types:
    - `project` → Central configuration (CLAUDE.md)
    - `skill` → Expert role definition
    - `agent` → Autonomous task executor
    - `workflow` → Multi-step process (staged & linear execution)
    - `command` → Slash command definition
    - `memory` → Memory record (session, learned, todo, backlog)
    - `todo` → Task plan (coding, analysis, research, migration)
    - `reference` → Technical documentation (patterns: howto, knowledge, glossary, enforcement, standards, checklist, component)
  </principle>

  <principle name="tag-categories">
    Tag Categories:
    - Structure: document, objective, context, command
    - Loading: read, ref, documents, templates, workflows, workflow, skills, agents, commands, memories
    - Rules: enforcement, understanding, checklist, verification
    - Processing: execution (flow="linear|staged")
    - Actions: invoke, call, tasks, print, bash, workflow, thinking
    - Variables: variables, var, set, append (all optional)
    - Flow: stage, parallel, foreach, confirm, goto, stop
    - User Interaction: ask, confirm, wait (→ AskUserQuestion tool)
    - Content: prompt, param, parameter, examples, example
    - Knowledge: pattern, principle, decision, requirements, implementation, output, verification, todos, configurations
  </principle>

  <principle name="document-structure">
    Document Structure:
    - Frontmatter (YAML): name, description, type
    - Markdown heading: # Document Name
    - XML code fence: ```xml ... ```
    - Document element: `document type="..."`
    - Understanding at end: `understanding/`
  </principle>

  <pattern name="essential-tags">
    Essential Tags (Quick Reference):

    `read` - Load external file:
    - `read src="path"` → Load file
    - `mode`: context (default), data, template

    `enforcement` - Mandatory rules:
    - Lines with `-` → rules
    - Lines with `X` → prohibitions

    `call` - Invoke slash command:
    - `call command="/cmd" args="..."`

    `invoke` - Direct tool invocation:
    - `invoke name="Task|Skill"`
    - `invoke resumable="true"` → Agent supports resume on re-invoke
    - IF resumable="true" THEN enforcement MUST include RESUMABLE rules

    `variables` - Define variables:
    - `var name="x" value="..."`
    - `var name="x" from="args.0"`

    `goto` - Flow control:
    - `goto when="condition" to="stage"`
    - `goto command="cmd:name"`

    `stop` - Terminate:
    - `stop kind="end|error"`

    `ask` - User input (→ AskUserQuestion tool):
    - `ask var="name" prompt="Question?"` → Single question
    - `ask` with YAML list → Multiple questions
    - MUST use AskUserQuestion tool for execution

    `confirm` - User confirmation (→ AskUserQuestion tool):
    - `confirm id="..."` → Approval checkpoint
    - Contains: print (info), ask (confirmation)
    - MUST use AskUserQuestion tool for execution

    `bash` - Execute shell command:
    - `bash run="command"` → Single command
    - `bash run="cmd" output="result"` → Capture output to variable
    - `bash output="result">multi-line</bash>` → Multi-line with output

    `understanding` - Context explanation (REQUIRED):
    - See pattern "understanding-element" for details and examples

    `configurations` - Project-level key-value settings:
    - `configurations` → Container for project settings
    - `var name="key" value="value"` → Single configuration entry
    - Single instance per CLAUDE.md
  </pattern>

  <pattern name="foreach-element">
    `foreach` - Iterate over collection:
    - `foreach var="x" in="${list}" mode="sequential"` → One by one (default)
    - `foreach var="x" in="${list}" mode="parallel"` → All at once
  </pattern>

  <pattern name="append-element">
    `append` - Add value to array variable:
    - `append var="results" value="${item}"` → Push to array
  </pattern>

  <pattern name="variable-syntax">
    Variable Syntax:
    - Definition: `var name="..." value="..."`
    - Access: `${varname}`
    - From args: `from="args.0"`, `from="args.1"`
    - From env: `from="env:VAR_NAME"`
    - From prompt: `from="prompt.PARAM_NAME"` (agent receives from skill)
  </pattern>

  <pattern name="registry-query-syntax"><![CDATA[
    Registry Query Syntax:
    Dynamic lookup for documents, templates, agents, workflows, skills registries.

    Format: ${registry:name[filter].property}

    Registries: documents, templates, agents, workflows, skills, commands, memories

    Basic Queries:
    - ${documents:components[ask=command].src}  → Single value (exact match)
    - ${documents:components[].src}             → All src values (array)

    Filters (ask attribute only):
    - [ask=x]              → Exact match
    - [ask=x|y]            → OR (x or y)
    - [ask=x&y]            → AND (x and y)
    - [ask.starts(x|y)]    → Starts with OR
    - [ask.ends(x|y)]      → Ends with OR
    - [ask.contains(x|y)]  → Contains OR

    Results: .src (first match), .src[] (all matches)

    Example:
    <documents name="components" load="on-demand">
      <read src=".../AXEL-Command.md" ask="command, cmd"/>
      <read src=".../AXEL-Agent.md" ask="agent"/>
    </documents>

    ${documents:components[ask=command].src}         → ".../AXEL-Command.md"
    ${documents:components[ask=command|agent].src[]} → [both paths] (OR)
    ${documents:components[].src}                    → [all src values]
  ]]></pattern>

  <principle name="plugin-root-scope"><![CDATA[
    ${CLAUDE_PLUGIN_ROOT} Variable Scope:

    Context Rules:
    - Plugin internal documents: ${CLAUDE_PLUGIN_ROOT} automatically resolved
    - User documents: NEVER use this variable (not user's concern)
    - Plugin developer documents: AI MUST add automatically

    Why This Matters:
    - Claude Code cannot isolate plugin context from user context
    - Claude Code searches for files in user's project directory
    - Plugin files need explicit path prefix to be found

    Usage:
    - Inside plugin: <read src="${CLAUDE_PLUGIN_ROOT}/path/to/file.md"/>
    - User project: <read src="./local/path.md"/> (no plugin variable)
  ]]></principle>

  <pattern name="conditions"><![CDATA[
    Condition Operators:
    - `=` equals, `!=` not equal
    - `>`, `<`, `>=`, `<=` comparison
    - `AND`, `OR` logical
    - `''` empty check
  ]]></pattern>

  <pattern name="load-modes">
    Load Attributes:
    - `load="always"` → Always load
    - `load="on-demand"` → Load when requested
    - `load="on-trigger"` → Load on specific trigger
    - `mode="context"` → As context
    - `mode="data"` → As raw data
    - `mode="map"` → As key-value map
    - `mode="template"` → As output template (templates only)
  </pattern>

  <pattern name="understanding-element"><![CDATA[
    `understanding` Element (REQUIRED)

    Two Contexts:
    1. Document-level: <understanding/> at document end (self-closing)
    2. Registry-level: <understanding>...</understanding> inside documents/templates/memories

    Registry-Level Rules:
    - MUST start with: !! MANDATORY: READ → UNDERSTAND → APPLY !!
    - Describe what resources provide
    - See principle "bootstrap-default-reference" for example

    Validation:
    - Every registry block MUST have understanding
    - Document MUST end with understanding/
  ]]></pattern>

  <pattern name="content-format"><![CDATA[
    Content Format Rules:
    - Tag contents in bullet list format
    - CDATA for special characters (<, >, &, &&, |)
    - Code examples within CDATA blocks
    - Variables: `${var}` syntax
  ]]></pattern>

  <pattern name="code-fence-placeholder">
    `{{{...}}}` - Code Fence Placeholder

    Purpose: Writing code fences inside XML code fence (nested code blocks)

    Pattern:
    - `{{{xml}}}` → triple backtick + xml (opening)
    - `{{{/xml}}}` → triple backtick (closing)
    - Other: `{{{csharp}}}`, `{{{typescript}}}`, `{{{json}}}`, etc.

    Behavior:
    - AI MUST replace placeholders when writing to file
    - `{{{lang}}}` becomes opening code fence
    - `{{{/lang}}}` becomes closing code fence
  </pattern>

  <principle name="bootstrap-default-reference"><![CDATA[
    Bootstrap Reference (Optional):

    AXEL documents can optionally include AXEL-Bootstrap.md for core rules:

    <documents name="bootstrap" load="always" mode="context">
      <read src="${CLAUDE_PLUGIN_ROOT}/AXEL-Bootstrap.md"/>
      <understanding>
        !! MANDATORY: READ → UNDERSTAND → APPLY !!
        Bootstrap provides AXEL syntax, enforcement rules, and understanding guidelines.
      </understanding>
    </documents>

    When to use:
    - skill, agent, workflow, command documents using advanced AXEL features
    - Projects wanting centralized rule management

    When NOT needed:
    - Simple CLAUDE.md project configurations
    - memory documents (simple data format)
  ]]></principle>

  <understanding/>

</document>
```
