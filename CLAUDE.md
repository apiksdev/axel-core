---
name: axel-plugin
description: AXEL - AI XML Execution Language plugin for Claude Code
type: project
version: 1.0.0
---

# AXEL Plugin

```xml
<document type="project">

  <enforcement>
    <![CDATA[
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
    ]]>
  </enforcement>

  <project name="axel-plugin" version="1.0.0">
    <description>
       AXEL (AI XML Execution Language) development environment for creating and testing
      structured AI behavior components. AXEL is an XML-based DSL plugin for Claude Code
      that addresses inconsistent AI behavior through enforceable instructions that persist
      across sessions. This project serves as the development workspace for building AXEL
      components including Skills (specialized AI expertise), Agents (autonomous task executors),
      Workflows (multi-step processes), Commands (slash command definitions), Todos (task management),
      and Memory systems (cross-session context persistence).
    </description>
    <stack>
      - language: XML, Markdown, YAML
      - platform: Claude Code
      - type: DSL (Domain-Specific Language)
    </stack>
  </project>
  
  <locale default="en">
    - code: en
    - docs: en
    - communication: tr
    - commits: en
    - todos: tr
  </locale>
  
  <understanding/>
  
</document>
```
