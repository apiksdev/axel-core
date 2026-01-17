---
name: axel:learned-save
description: Save learned lesson to LEARNED.md
type: command
allowed-tools:
  - Read
  - Write
  - Edit
---

# AXEL Command: /axel:learned-save

```xml
<document type="command" entry="cmd:main">

  <enforcement>
    <![CDATA[
    - Read the `src`, `ref`, or `target` attribute from the document XML to locate referenced files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
    - .claude/LEARNED.md contains type="learned" memory entries
    - mode="append" for adding new entries without overwriting
    - Notation: {{{xml}}} = ```xml code fence, {{{/xml}}} = ``` close fence
    ]]>
  </enforcement>

  <objective>
    Save learned lesson to LEARNED.md file.
    Single-purpose command with linear execution.
  </objective>

  <documents name="core" load="always" mode="context">
    <read src="${CLAUDE_PLUGIN_ROOT}/references/AXEL-Core.md"/>
    <understanding>
      !! MANDATORY: READ → UNDERSTAND → APPLY !!
      Syntax reference provides AXEL DSL rules for memory entry format.
    </understanding>
  </documents>

  <execution flow="linear">
    <![CDATA[
    Step 1 - Problem Analysis:
    - Identify the problem that was solved
    - Analyze the root cause of the problem
    - Document the solution steps taken
    - Extract the key lesson learned

    Step 2 - Create Memory Entry:
    - Create a new learned memory entry
    - Append to .claude/LEARNED.md file

    Format:
    ## {YYYY-MM-DD HH:mm:ss} - {problem title 5-10 words}

    {{{xml}}}
    <memory type="learned" priority="high" tags="{relevant,tags}">
        <timestamp format="YYYY-MM-DD HH:mm" />
        <subject>{problem title 5-10 words}</subject>

        <context>
          - {problem description}
          - {root cause}
        </context>

        <files>
          - {related file 1}
          - {related file 2}
        </files>

        <solution>
          - {solution step 1}
          - {solution step 2}
        </solution>

        <lesson>
          - {key takeaway}
        </lesson>
    </memory>
    {{{/xml}}}

    ---

    Step 3 - Complete:
    - Each learned entry separated by --- divider
    - IMPORTANT: Append to file, do not overwrite existing entries
    - Signal to user: "Learned lesson saved to .claude/LEARNED.md"
    ]]>
  </execution>

  <understanding/>

</document>
```
