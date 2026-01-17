---
name: agent-template-bootstrap
description: Agent template bootstrap - selects between linear and staged execution patterns
type: template
---

# AXEL Template: Agent

```xml
<document type="reference">

  <enforcement>
    <![CDATA[
    - Read `src` attribute from <read/> elements to locate sub-templates
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
    - load="on-demand" means template loads when user request matches ask keywords
    - Select appropriate sub-template based on execution pattern needed
    ]]>
  </enforcement>

  <objective>
    Navigation template for agent execution pattern selection.
    Two patterns: Linear (no stages) and Staged (with stages, branching, parallel, loop).
  </objective>

  <templates load="on-demand">
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/agents/refs/AXEL-Agent-Linear-Tpl.md"
          ask="[simple, linear, basic, straightforward, no stages]"/>
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/agents/refs/AXEL-Agent-Staged-Tpl.md"
          ask="[staged, complex, branching, parallel, loop, retry, orchestration]"/>
    <understanding>
      Linear template: Simple agents without stages, text-based execution.
      Staged template: Complex agents with stages, branching, parallel, loops.
    </understanding>
  </templates>

  <understanding/>

</document>
```
