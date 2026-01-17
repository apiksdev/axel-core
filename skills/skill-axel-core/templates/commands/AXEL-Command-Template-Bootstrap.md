---
name: command-document
description: Slash command definition template bootstrap
type: template
---

# AXEL Template: Command

```xml
<document type="template">

  <enforcement>
    <![CDATA[
    - Read `src` attribute from <read/> elements to locate sub-templates
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
    - Select appropriate template based on command complexity:
      - Linear: Single purpose, no stages, no subcommands
      - Staged: Subcommands, full staged execution (sequential, branching, loop)
    ]]>
  </enforcement>

  <objective>
    Routing template for slash command type selection.
    Linear (single action) or Staged (complex flow).
  </objective>

  <templates load="always" mode="context">
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/commands/refs/AXEL-Command-Linear-Tpl.md" ask="[linear command, single purpose, no stages, no subcommands, simple action, text instructions]"/>
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/commands/refs/AXEL-Command-Staged-Tpl.md" ask="[staged command, subcommands, sequential stages, branching, loop retry, invoke agent, mode routing, complex flow]"/>
    <understanding>
      Template selection for command complexity:
      - Linear: Single purpose commands without stages
      - Staged: Commands with routing, stages, and complex flow patterns
    </understanding>
  </templates>

  <understanding/>

</document>
```
