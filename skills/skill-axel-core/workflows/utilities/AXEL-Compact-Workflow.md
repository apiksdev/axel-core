---
name: axel-compact-workflow
description: Compact memories (session/learned) to archive using Python script
type: workflow
triggers:
  - compact
allowed-tools:
  - Bash
---

# AXEL Workflow: Compact Memories

```xml
<document type="workflow">

  <enforcement>
    <![CDATA[
    PATH RESOLUTION:
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
    - Script at: ${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/scripts/axel_compact.py
    - Source files: ${PROJECT_ROOT}/.claude/MEMORIES.md, ${PROJECT_ROOT}/.claude/LEARNED.md
    - Archive dirs: ${PROJECT_ROOT}/.claude/memories/sessions, ${PROJECT_ROOT}/.claude/memories/learned

    SCRIPT OUTPUT:
    - Script outputs JSON with success/error info
    - Parse JSON and report results to user
    ]]>
  </enforcement>

  <objective>
    Compact memories (session or learned) to archive.
    Uses axel_compact.py script for fast file operations.
  </objective>

  <variables>
    <var name="script_path" value="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/scripts/axel_compact.py"/>
    <var name="action" from="param.action"/>
    <var name="type" from="param.type"/>
  </variables>

  <execution flow="staged">

    <!-- validate: Check parameters -->
    <stage id="validate">
      <goto when="action != 'memories'" to="invalid_action"/>
      <goto when="type = 'session'" to="compact_session"/>
      <goto when="type = 'learned'" to="compact_learned"/>
      <goto to="invalid_type"/>
    </stage>

    <!-- compact_session: Archive session memories -->
    <stage id="compact_session">
      <bash><![CDATA[
        PYTHONIOENCODING=utf-8 python "${script_path}" --action memories-session --source-file ".claude/MEMORIES.md" --target-dir ".claude/memories/sessions" --target-pattern "session-{YYYY-MM-DD-HHmm}.md" --filter "priority=normal,priority=low" --element-tag "memory" --cwd "${PROJECT_ROOT}"
      ]]></bash>
      <goto to="report"/>
    </stage>

    <!-- compact_learned: Archive learned memories -->
    <stage id="compact_learned">
      <bash><![CDATA[
        PYTHONIOENCODING=utf-8 python "${script_path}" --action memories-learned --source-file ".claude/LEARNED.md" --target-dir ".claude/memories/learned" --target-pattern "learned-{YYYY-MM-DD-HHmm}.md" --filter "priority=normal,priority=low" --element-tag "memory" --cwd "${PROJECT_ROOT}"
      ]]></bash>
      <goto to="report"/>
    </stage>

    <!-- report: Show results -->
    <stage id="report">
      <print>
        Parse the JSON output from the script and report:
        - Number of items compacted
        - List of moved items
        - Source and target file paths
        - Any errors encountered
      </print>
      <stop kind="end"/>
    </stage>

    <!-- invalid_action: Error for wrong action -->
    <stage id="invalid_action">
      <print>
        ## Error
        Invalid action. Use: /axel:compact memories {type}
      </print>
      <stop kind="error"/>
    </stage>

    <!-- invalid_type: Error for wrong type -->
    <stage id="invalid_type">
      <print>
        ## Error
        Invalid type: ${type}

        **Valid types:**
        - session - Archive session memories
        - learned - Archive learned memories
      </print>
      <stop kind="error"/>
    </stage>

  </execution>

  <understanding/>

</document>
```
