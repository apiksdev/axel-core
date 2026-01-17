---
name: axel:session-save
description: Save current session context to MEMORIES.md
type: command
allowed-tools:
  - Read
  - Write
  - Edit
---

# AXEL Command: /axel:session-save

```xml
<document type="command" entry="cmd:main">

  <enforcement>
    <![CDATA[
    - Read the `src`, `ref`, or `target` attribute from the document XML to locate referenced files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
    - .claude/MEMORIES.md contains type="session" memory entries
    - mode="context" for loading reference files
    - mode="data" for reading existing memories
    - mode="template" for applying output format
    - Append new entries, do not overwrite existing content
    - Notation: {{{xml}}} = ```xml code fence, {{{/xml}}} = ``` close fence
    ]]>
  </enforcement>

  <objective>
    Save current session context and decisions to .claude/MEMORIES.md
    for future reference. Creates structured memory entries with
    timestamp, context, files, and remaining tasks.
  </objective>

  <documents load="always" mode="context">
    <read src="${CLAUDE_PLUGIN_ROOT}/references/AXEL-Core.md"/>
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/memory/refs/AXEL-Memory-Session-Tpl.md"/>
    <understanding>
      !! MANDATORY: READ → UNDERSTAND → APPLY !!
      Syntax provides AXEL formatting rules.
      Template provides memory entry structure.
    </understanding>
  </documents>

  <execution flow="linear">
    <![CDATA[
    LINEAR COMMAND (session memory save):

    Step 1 - Read Current State:
    - Read .claude/MEMORIES.md (mode="data") for existing entries
    - Analyze current session conversation

    Step 2 - Analyze Session:
    - Identify completed work and decisions made
    - List related files that were modified or discussed
    - Note remaining tasks to complete

    Step 3 - Create Memory Entry:
    Format as memory XML entry:

    ## {YYYY-MM-DD HH:mm:ss} - {5-10 word summary}

    {{{xml}}}
    <memory type="session" priority="normal" tags="{relevant,tags}">
        <timestamp format="YYYY-MM-DD HH:mm" />
        <subject>{5-10 word summary}</subject>

        <context>
          - {completed work item 1}
          - {completed work item 2}
          - {decision made}
        </context>

        <files>
          - {modified file 1}
          - {discussed file 2}
        </files>

        <remaining>
          - {task left to do}
        </remaining>
    </memory>
    {{{/xml}}}

    ---

    Step 4 - Append to File:
    - Append new entry to .claude/MEMORIES.md
    - Each session entry separated by --- divider
    - IMPORTANT: Append to file, do not overwrite existing entries

    Step 5 - Confirm:
    - Display "Session memory saved to .claude/MEMORIES.md" to user
    ]]>
  </execution>

  <understanding/>

</document>
```
