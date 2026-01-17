---
name: axel-fix-workflow
description: Validate AXEL document against Bootstrap rules and auto-fix predefined issues
type: workflow
triggers:
  - fix
  - axel fix
  - fix document
---

# AXEL Workflow: Fix

```xml
<document type="workflow">

  <enforcement>
    <![CDATA[
    EXECUTION MODES:
    - mode=auto: Apply all auto-fixes without confirmation (default)
    - mode=dry-run: Check only, report issues, no changes
    - mode=step: Interactive, ask for each fix [y/n/all/skip-phase]

    AUTO-FIX BEHAVIOR:
    - Rules with auto-fix="true" are applied based on mode
    - Rules with auto-fix="false" are always reported only
    - Critical issues block execution until fixed
    - Warning issues are fixed but noted in report

    RULE PHASES (execution order):
    1. frontmatter - fm-* rules (must exist before other checks)
    2. structure - struct-*, order-* rules (elements must exist)
    3. format - fmt-*, reg-* rules (content formatting)
    4. execution - exec-*, var-* rules (flow validation)

    SOURCE LOADING:
    - AXEL-Checklist.md provides all validation rules
    - Checklist groups scope rules by document type
    ]]>
  </enforcement>

  <objective>
    Auto-fix predefined AXEL document issues without user prompts.
    Read target → Apply rules → Fix automatically → Report results.
  </objective>

  <documents>
    <read src="${CLAUDE_PLUGIN_ROOT}/references/AXEL-Checklist.md"/>
    <understanding><![CDATA[
      !! MANDATORY: READ → UNDERSTAND → APPLY !!
      AXEL-Checklist.md provides all validation rules.
      Apply rules based on document type using checklist when conditions.
    ]]></understanding>
  </documents>

  <variables>
    <var name="target_path" description="Path to AXEL document to fix"/>
    <var name="mode" description="Execution mode: auto|dry-run|step (default: auto)"/>
    <var name="issues_found" description="List of detected issues"/>
    <var name="fixes_applied" description="List of applied fixes"/>
  </variables>

  <execution flow="linear"><![CDATA[
    Step 1 - Read Target:
    - Get target_path from prompt arguments
    - Get mode (default: auto)
    - Read file content
    - Parse frontmatter and XML structure

    Step 2 - Load Rules:
    - !! MANDATORY: Load AXEL-Checklist.md from documents !!
    - Filter checklists by document type (when conditions)
    - Group rules by phase: frontmatter → structure → format → execution

    Step 3 - Batch Check (read-only):
    - For each rule in phase order:
      - Print: [CHECK] rule_id: check description
      - Apply check condition to document
      - If check fails:
        - Print: [FAIL] rule_id - severity
        - Add to issues_found with rule details
      - If check passes:
        - Print: [PASS] rule_id

    Step 4 - Apply Fixes (mode-dependent):
    - IF mode=dry-run:
      - Print: "Dry-run mode - no changes applied"
      - Skip to Step 6

    - IF mode=step:
      - For each issue where auto-fix="true":
        - Print: [FIX?] rule_id: fix description
        - Ask user: Apply this fix? [y/n/all/skip-phase]
        - If yes: apply fix, add to fixes_applied
        - If all: switch to auto mode for remaining
        - If skip-phase: skip to next phase

    - IF mode=auto:
      - For each phase in order:
        - For each issue where auto-fix="true":
          - Print: [FIX] rule_id: applying fix
          - Apply the fix transformation
          - Add to fixes_applied

    Step 5 - Write Changes:
    - If fixes_applied is not empty:
      - Write updated content to target_path
      - Print: [WRITE] Saved to target_path

    Step 6 - Report Results:
    - Print summary table
  ]]></execution>

  <output format="markdown"><![CDATA[
    ## Fix Report: ${target_path}

    ### Auto-Fixed by Phase
    | Phase | Count | Rules |
    |-------|-------|-------|
    | frontmatter | X | fm-required, fm-name-kebab... |
    | structure | X | struct-enforcement... |
    | format | X | fmt-cdata... |
    | execution | X | exec-goto-match... |

    ### Manual Fixes Needed
    | Rule | Severity | Description | Location |
    |------|----------|-------------|----------|
    | ...  | ...      | ...         | Line X   |

    ### Summary
    - Total issues: X
    - Auto-fixed: Y
    - Manual needed: Z
  ]]></output>

  <understanding/>

</document>
```
