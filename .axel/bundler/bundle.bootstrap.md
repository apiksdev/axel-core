---
name: axel-bundle-config
description: Bundle configuration - defines source files and output content for bundled documents
type: config
---

# AXEL Bundle Configuration

```xml
<document type="bundle">

  <objective>
    Bundle generation configuration.
    Defines source files and output content for bundled documents.
  </objective>

  <bundles>
    <bundle target="AXEL-Bootstrap.md">
      <enforcement>
        <![CDATA[
        PATH RESOLUTION:
        - Read the `src`, `ref`, or `target` attribute from the document XML to locate referenced files
        - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory

        MANDATORY READING:
        - All content in this bootstrap MUST be read and understood
        - Each <axel-*> section contains rules from its source file
        - Rules are cumulative - all sections apply

        COMPLIANCE:
        - Every rule MUST be applied
        - Skipping a rule = TASK FAILURE
        - If uncertain → ASK the user
        ]]>
      </enforcement>

      <objective>
        AXEL Bootstrap - Core syntax, enforcement rules, and understanding guidelines.
        Single document containing all essential AXEL references.
      </objective>

      <understanding>
        Self-closing understanding element will be added at document end.
      </understanding>

      <sources>
        <!-- Inline: Content merged directly into bundle output with wrapper element -->
        <source load="inline">
          <file src="references/AXEL-Enforcement.md"/>
          <file src="references/AXEL-Core.md"/>
          <file src="references/AXEL-Understanding.md"/>
        </source>

        <!-- On-demand: Loaded when user mentions keywords -->
        <source load="on-demand">
          <file src="references/AXEL-Standards.md" ask="standard, pattern, example"/>
          <file src="references/AXEL-Conventions.md" ask="convention, style, format"/>
          <understanding>
            !! MANDATORY: READ → UNDERSTAND → APPLY !!
            Standards and conventions loaded when specific topics arise.
          </understanding>
        </source>

        <!-- On-trigger: Loaded on specific events/commands -->
        <source load="on-trigger">
          <file src="references/AXEL-Checklist.md" trigger="validate, pre-commit"/>
          <understanding>
            !! MANDATORY: READ → UNDERSTAND → APPLY !!
            Validation checklist loaded on validate or pre-commit commands.
          </understanding>
        </source>
      </sources>
    </bundle>
  </bundles>

  <understanding/>

</document>
```
