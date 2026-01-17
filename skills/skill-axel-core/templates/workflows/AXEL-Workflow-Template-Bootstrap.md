---
name: workflow-template-bootstrap
description: Workflow template bootstrap - selects between linear and staged execution patterns
type: template
---

# AXEL Template: Workflow

```xml
<document type="template">

  <enforcement>
    <![CDATA[
    - Read `src` attribute from <read/> elements to locate sub-templates
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
    - load="on-demand" means template loads when user request matches ask keywords
    - Select appropriate sub-template based on workflow pattern needed
    ]]>
  </enforcement>

  <objective>
    Navigation template for workflow pattern selection.
    Two patterns: Linear (no stages) and Staged (with stages, branching, parallel, loop).
  </objective>

  <templates load="on-demand">
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/workflows/refs/AXEL-Workflow-Linear-Tpl.md"
          ask="[simple, linear, basic, sequential, no stages]"/>
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/workflows/refs/AXEL-Workflow-Staged-Tpl.md"
          ask="[staged, complex, branching, parallel, loop, approval, user interaction]"/>
  </templates>

  <understanding/>

</document>
```
