---
name: memory-document
description: Memory management and session context definition template
type: template
---

# AXEL Template: Memory

```xml
<document type="memory">

  <enforcement>
    <![CDATA[
    - Read `src` attribute from <read/> elements to locate sub-templates
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
    - load="always" means templates section loads with document
    - ask="[keywords]" triggers template load when user request matches
    - Select appropriate sub-template based on memory type needed
    ]]>
  </enforcement>

  <objective>
    Guidance template for Memory type selection.
    Provides example templates for Session and Learned memory types.
  </objective>

  <templates load="always">
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/memory/refs/AXEL-Memory-Session-Tpl.md" ask="[save session context, store work progress, track completed and remaining tasks, save agent task state, store entity design progress, track implementation status]"/>
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/memory/refs/AXEL-Memory-Learned-Tpl.md" ask="[record learned lesson, document problem and solution, save debugging experience]"/>
  </templates>

  <understanding/>

</document>
```
