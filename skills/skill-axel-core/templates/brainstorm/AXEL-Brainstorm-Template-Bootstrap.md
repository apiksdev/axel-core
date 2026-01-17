---
name: brainstorm-template
description: Routing template for AXEL brainstorm types - feature, project, research, code-review, migration
type: template
---

# AXEL Template: Brainstorm

```xml
<document type="brainstorm">

  <enforcement>
    <![CDATA[
    - Read `src` attribute from <read/> elements to locate sub-templates
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
    - load="always" means templates section loads with document
    - ask="[keywords]" triggers template load when user request matches
    - Select appropriate sub-template based on brainstorm type needed
    ]]>
  </enforcement>

  <objective>
    Routing template for brainstorm type selection.
    Routes to scenario-specific templates based on discovery purpose.
  </objective>

  <templates load="always">
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/brainstorm/refs/AXEL-Brainstorm-Feature-Tpl.md"
          ask="[feature, new feature, add feature, implement, create, build, develop, add functionality, endpoint, service, component, module]"/>
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/brainstorm/refs/AXEL-Brainstorm-Project-Tpl.md"
          ask="[project, new project, initialize, init, setup, bootstrap, scaffold, architecture, tech stack, greenfield]"/>
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/brainstorm/refs/AXEL-Brainstorm-Research-Tpl.md"
          ask="[research, investigate, explore, find, search, compare, discover, evaluate, analyze options, best practice, alternatives]"/>
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/brainstorm/refs/AXEL-Brainstorm-Code-Review-Tpl.md"
          ask="[review, code review, audit, inspect, check code, quality check, security review, performance review, refactor review]"/>
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/brainstorm/refs/AXEL-Brainstorm-Migration-Tpl.md"
          ask="[migrate, migration, upgrade, convert, port, transition, move, transfer, version upgrade, modernize]"/>
    <understanding>
      !! MANDATORY: READ -> UNDERSTAND -> APPLY !!
      - READ the template file first
      - UNDERSTAND the structure and patterns
      - APPLY the template structure EXACTLY
      Reference = HOW to think | Template = HOW to write
    </understanding>
  </templates>

  <understanding/>

</document>
```
