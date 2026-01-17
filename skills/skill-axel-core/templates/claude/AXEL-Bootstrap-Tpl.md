---
name: bootstrap-document
description: Project-level BOOTSTRAP.md template
type: template
---

# AXEL Template: Bootstrap

```xml
<document type="reference">

  <enforcement>
    <![CDATA[
    PATH RESOLUTION:
    - Read the `src`, `ref`, or `target` attribute from the document XML to locate referenced files
    - ${AXEL_CORE_PLUGIN_ROOT} resolves to AXEL core plugin installation directory
    - ${CLAUDE_PLUGIN_ROOT} resolves to current plugin installation directory
    - All paths are resolved relative to appropriate root directories

    MANDATORY READING:
    - This bootstrap MUST be loaded before other project references
    - Core AXEL-Bootstrap.md loaded on-demand for DSL work
    - All enforcement rules are cumulative and must be applied

    COMPLIANCE:
    - Every rule MUST be applied
    - Skipping a rule = TASK FAILURE
    - If uncertain → ASK the user

    ⛔ PROJECT-SPECIFIC RULES
    - Add project-specific enforcement rules below
    - Keep rules focused and actionable
    - Override or extend core rules when necessary
    ]]>
  </enforcement>

  <objective>
    Project Bootstrap - Project-specific rules and references to core AXEL Bootstrap.
    Single entry point for all project-level enforcement and guidelines.
  </objective>

  <documents name="axel-bootstrap" load="on-demand" mode="context">
    <read src="${AXEL_CORE_PLUGIN_ROOT}/AXEL-Bootstrap.md" ask="axel, bootstrap, core"/>
    <understanding>
      !! MANDATORY: READ → UNDERSTAND → APPLY !!
      Core AXEL DSL rules and enforcement from plugin.
      Load on-demand when working with AXEL components.
    </understanding>
  </documents>

  <understanding/>

</document>
```
