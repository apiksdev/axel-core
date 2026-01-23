---
name: claude-document
description: CLAUDE.md template - project configuration file
type: template
---

# AXEL Template: Claude

```xml
<document type="project">

  <enforcement>
    <![CDATA[
    ⛔ LOCALE COMPLIANCE - CHAT LANGUAGE ONLY
    - MUST read CLAUDE.md <locale> section for chat responses
    - Use "communication" field language for conversation/chat messages ONLY
    - Documents, code, and generated files follow their respective locale settings (code, docs)

    ⛔ CONTENT DUPLICATION RULES
    - ❌ NEVER copy content from referenced documents into new documents
    - Referenced documents are already loaded via context or on-demand loading
    - New documents should only contain unique, non-duplicated information
    - Reference existing content via <read src=".."/> in <documents> block
    - If content exists elsewhere → reference it, do not duplicate it

    ⛔ XML COMMENT FORMAT RULES
    - ❌ NEVER use multi-line decorative comments
    - ❌ NEVER use box-style comments with separator lines (====, ----, ****)
    - ❌ NEVER use comments like: <!-- ========== SECTION ========== -->
    - ✅ ALWAYS use single-line format: <!-- stage_id: Description -->
    - Comment must be placed directly before the element it describes

    ⛔ DOCUMENT LOADING RULES
    - ✅ AXEL-Bootstrap.md MUST be loaded FIRST if defined in <documents>
    - Bootstrap provides core DSL rules that govern all document processing

    ⛔ INVOKE EXECUTION RULES
    - ✅ <invoke name="X"/> → Execute using Claude Code tool named "X"
    - ✅ <param> elements map directly to tool parameters
    - Example: <invoke name="Skill"> → calls Skill tool
    - Example: <invoke name="Task"> → calls Task tool
    ]]>
  </enforcement>

  <project name="${project_name}" version="1.0.0">
    <description>
	  ${project_desc}
    </description>
    <stack>
      ${tech_stack}
    </stack>
  </project>

  <locale default="${locale}">
    - code: en
    - docs: ${locale}
    - communication: auto
    - commits: en
  </locale>

  <configurations>
    <var name="AXEL_CORE_PLUGIN_ROOT" value="${CLAUDE_PLUGIN_ROOT}"/>
    <var name="COMMIT_MESSAGE_FORMAT" value="${commit_format}"/>
  </configurations>

  <memories name="memories" load="always" mode="context">
    <memory name="session" src=".claude/MEMORIES.md"/>
    <memory name="learned" src=".claude/LEARNED.md"/>
    <understanding>
      !! MANDATORY: READ -> UNDERSTAND -> APPLY !!
      Session memory tracks conversation context.
      Learned memory stores lessons from past work.
    </understanding>
  </memories>

  <understanding/>

</document>
```
