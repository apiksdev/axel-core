---
name: skill-template-bootstrap
description: Skill template bootstrap - selects between linear and staged execution patterns
type: template
---

# AXEL Template: Skill

```xml
<document type="template">

  <enforcement>
    <![CDATA[
    - Read `src` attribute from <read/> elements to locate sub-templates
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
    - load="on-demand" means template loads when user request matches ask keywords
    - Select appropriate sub-template based on skill pattern needed
    ]]>
  </enforcement>

  <objective>
    Navigation template for skill pattern selection.
    Two patterns: Linear (guidance-only) and Staged (with stages, branching, triggers).
  </objective>

  <templates load="on-demand">
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/skill/refs/AXEL-Skill-Linear-Tpl.md"
          ask="[simple, linear, basic, guidance, no stages]"/>
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/skill/refs/AXEL-Skill-Staged-Tpl.md"
          ask="[staged, complex, branching, triggers, invoke, workflow, orchestration]"/>
  </templates>

  <understanding/>

</document>
```
