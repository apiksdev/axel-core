---
name: research-template-bootstrap
description: Research template bootstrap - routes to appropriate research type template
type: template
---

# AXEL Template: Research

```xml
<document type="template">

  <enforcement>
    <![CDATA[
    - Read `src` attribute from <read/> elements to locate sub-templates
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
    - load="on-demand" means template loads when user request matches ask keywords
    - Select appropriate sub-template based on research type needed
    - Output is Pure Markdown, no XML in generated research reports
    ]]>
  </enforcement>

  <objective>
    Routing template for research type selection.
    Four types: Technical, Codebase, Web, Best Practices.
    All produce Pure Markdown output in .claude/research/ directory.
  </objective>

  <templates load="on-demand">
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/research/refs/AXEL-Research-Tech-Stack-Tpl.md"
          ask="[tech, technology, library, framework, comparison, evaluation, performance]"/>
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/research/refs/AXEL-Research-Architecture-Tpl.md"
          ask="[architecture, design, pattern, structure, codebase, code analysis, dependency]"/>
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/research/refs/AXEL-Research-Best-Practices-Tpl.md"
          ask="[best practice, standard, convention, guideline, security, optimization]"/>
    <understanding>
      Template selection for research type:
      - Tech-Stack: Technology/library comparison and evaluation
      - Architecture: Codebase analysis and design patterns
      - Best-Practices: Industry standards and conventions
      For web research, use Tech-Stack or Best-Practices based on topic.
    </understanding>
  </templates>

  <understanding/>

</document>
```
