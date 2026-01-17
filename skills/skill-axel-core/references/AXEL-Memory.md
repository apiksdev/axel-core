---
name: axel-memory
description: Structure of memory management and session context definition files
type: reference
---

```xml
<document type="reference">

  <enforcement>
    - Read `src` attribute from template references to locate memory template files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
    - Memory files located in project's .claude/ directory
  </enforcement>

  <objective>
    Structure of memory definition files. AXEL Memory is an XML-based memory management format that permanently stores AI session information and learned lessons. It is designed for information transfer between sessions and context preservation.
  </objective>

  <frontmatter>
    <![CDATA[
---
name: memory-session              # Memory name (kebab-case)
description: Session memory       # Brief description, 80 characters
type: memory                      # Always "memory"
---
    ]]>
  </frontmatter>

  <templates load="always" mode="context">
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/memory/AXEL-Memory-Template-Bootstrap.md"/>
    <axel-tag-structure>
      <![CDATA[
      Memory Entry Structure (Cumulative)
      +-- ## YYYY-MM-DD HH:mm - Subject (markdown heading)
      +-- {{{xml}}}
      +-- <memory type="session|learned" priority="critical|high|normal|low" tags="...">
      |   +-- <timestamp format="YYYY-MM-DD HH:mm"/>
      |   +-- <subject>
      |   +-- <context>
      |   +-- <files/> (session: empty, learned: bullet list)
      |   +-- <remaining> [session only]
      |   +-- <solution> [learned only]
      |   +-- <lesson> [learned only]
      +-- </memory>
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
    - Used for permanent storage of AI session information
    - Enables information transfer between sessions
    - Supports two memory types: session, learned
    - Each entry is an independent memory record
    - Entries are kept in chronological order
    - Markdown heading defines entry title with timestamp
  </context>

  <principle name="memory-type-selection">
    - session: Work progress, completed tasks, decisions, remaining work
    - learned: Problems encountered, solutions, lessons learned
  </principle>

  <principle name="priority-system">
    - critical: Never archived, permanent information
    - high: Kept for long time, important decision/solution
    - normal: Standard, can be archived over time (default)
    - low: Short-lived, can be archived quickly
  </principle>

  <decision name="memory-structure-by-type" date="2024-12">
    When: Creating memory entries
    Action: Use type-specific structure
    - Session: context (completed work) → files → remaining
    - Learned: files → context (problem) → solution → lesson
    Reason: Each type has different information requirements
  </decision>

  <decision name="tagging-convention" date="2024-12">
    When: Categorizing memory entries
    Action: Use tags attribute with comma-separated keywords
    Example: tags="backend, auth, security"
    Reason: Enables filtering and searching across memory files
  </decision>

  <requirements>
    - Frontmatter must include name (kebab-case), description, type: memory
    - Memory entry must have type attribute (session/learned)
    - Memory entry must have priority attribute
    - Timestamp must include format attribute (YYYY-MM-DD HH:mm)
    - Subject must be 5-10 words
    - Context must use bullet list format
  </requirements>

  <implementation name="file-locations">
    .claude/
    - MEMORIES.md                  # Session memories
    - LEARNED.md                   # Learned lessons

    Archive locations:
    - .claude/memories/              # Archived session memories
    - .claude/learned/               # Archived learned entries
  </implementation>

  <implementation name="creating-memory">
    Step 1 - Select Memory Type:
    - session: Work progress, completed tasks, decisions, remaining work
    - learned: Problems encountered, solutions, lessons learned

    Step 2 - Set Priority:
    - critical: Never archived, permanent information
    - high: Kept for long time, important decision/solution
    - normal: Standard, can be archived over time (default)
    - low: Short-lived, can be archived quickly

    Step 3 - Define Content:
    - Subject: 5-10 words description
    - Context: Bullet list of relevant information
    - Tags: Comma-separated keywords

    Step 4 - Add Type-Specific Fields:
    - Session: files, remaining
    - Learned: files, solution, lesson

    Step 5 - Format Entry:
    - Markdown heading: ## YYYY-MM-DD HH:mm - Subject
    - Memory XML with type, priority, tags attributes

    Step 6 - AXEL Checklist:
    - MUST validate against AXEL-Checklist.md standards
    - Verify memory-validation checklist
  </implementation>

  <output format="markdown">
    File: MEMORIES.md | LEARNED.md
    Path: .claude/{file}
    Structure:
    - Markdown heading (## YYYY-MM-DD HH:mm - Subject)
    - AXEL XML in code fence (```xml ... ```)
    - Memory element with type, priority, tags attributes
  </output>

  <verification>
    - Is frontmatter correct? (name: kebab-case, type: memory)
    - Is memory type attribute defined?
    - Is priority attribute defined?
    - Is timestamp format attribute present?
    - Is subject 5-10 words?
    - Is context in bullet list format?
    - Are type-specific tags present?
  </verification>

  <checklist name="memory-validation">
    Common:
    - Is frontmatter correct? (name: kebab-case, type: memory)
    - Is description defined?
    - Is memory type attribute defined? (session/learned)
    - Is memory priority attribute defined?
    - Does memory tags attribute exist?
    - Does timestamp format attribute exist?
    - Is subject 5-10 words?
    - Is context in bullet list format?
    - Are entries in chronological order?

    Session:
    - Is files defined? (can be empty)
    - Is remaining defined?

    Learned:
    - Is files in bullet list format?
    - Is solution defined?
    - Is lesson defined?
  </checklist>

  <understanding/>

</document>
```
