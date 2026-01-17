---
name: axel:memories
description: Memory management - load memory files
type: command
allowed-tools:
  - Read
  - Task
  - AskUserQuestion
---

# AXEL Command: /axel:memories

```xml
<document type="command" entry="cmd:main">

  <enforcement>
    - Read the `src`, `ref`, or `target` attribute from the document XML to locate referenced files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
    - Memory files: .claude/MEMORIES.md, .claude/LEARNED.md
    - Archived to: .claude/memories/archived/
  </enforcement>

  <objective>
    Memory management - load memory files.
  </objective>

  <documents name="core" load="always" mode="context">
    <read src="${CLAUDE_PLUGIN_ROOT}/AXEL-Bootstrap.md"/>
    <understanding>
      !! MANDATORY: READ → UNDERSTAND → APPLY !!
      Bootstrap provides core AXEL rules.
    </understanding>
  </documents>

  <variables>
    <var name="action" from="args.0"/>
    <var name="type" from="args.1"/>
    <var name="plugin_root" value="${CLAUDE_PLUGIN_ROOT}"/>
  </variables>

  <command id="cmd:main">
    <goto when="action == ''" to="help"/>
    <goto when="action == 'session'" to="load-session"/>
    <goto when="action == 'learned'" to="load-learned"/>
    <goto when="action == 'all'" to="load-all"/>
    <goto to="help"/>
  </command>

  <execution flow="staged">

    <!-- help: Usage -->
    <stage id="help">
      <print>
        ## /axel:memories

        **Usage:**
          /axel:memories session    - Load session memories
          /axel:memories learned    - Load learned lessons
          /axel:memories all        - Load all
      </print>
      <stop kind="end"/>
    </stage>

    <!-- load-session: Load session memories -->
    <stage id="load-session">
      <read src=".claude/MEMORIES.md" output="content" mode="raw"/>
      <goto when="content == error" to="no-file"/>
      <tasks output="list">
        Parse MEMORIES.md, list memories:
        - [priority] subject
      </tasks>
      <print>${list}</print>
      <stop kind="end"/>
    </stage>

    <!-- load-learned: Load learned lessons -->
    <stage id="load-learned">
      <read src=".claude/LEARNED.md" output="content" mode="raw"/>
      <goto when="content == error" to="no-file"/>
      <tasks output="list">
        Parse LEARNED.md, list lessons:
        - [priority] subject
      </tasks>
      <print>${list}</print>
      <stop kind="end"/>
    </stage>

    <!-- load-all: Load all memories -->
    <stage id="load-all">
      <read src=".claude/MEMORIES.md" output="mem" mode="raw"/>
      <read src=".claude/LEARNED.md" output="learn" mode="raw"/>
      <tasks output="list">
        Parse both files, list all:
        **Session:** ...
        **Learned:** ...
      </tasks>
      <print>${list}</print>
      <stop kind="end"/>
    </stage>

    <!-- no-file: File not found -->
    <stage id="no-file">
      <print>Memory file not found. Run `/axel:axel-install` first.</print>
      <stop kind="end"/>
    </stage>

  </execution>

  <understanding/>

</document>
```
