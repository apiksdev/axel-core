---
name: axel-understanding
description: AI context reading, request interpretation and thinking rules
type: reference
---

# AXEL Understanding

```xml
<document type="reference">

  <understanding>
  ⛔ **CONTEXT READING - SKIP = TASK FAILED**

  **Required Files (required load="always"):**
  - MUST load and UNDERSTAND the content
  - Saying "I loaded it" means nothing → active checking and application is REQUIRED
  - Do not perform actions without reading the file = TASK FAILED
  - If it exists in context and hasn't changed → "ℹ️ {file} in context"
  - If not in context or has changed → load it, "✅ {file} loaded"
  - If file not found → "⚠️ {file} not found" and ask the user

  **Optional Files (optional load="on-demand"):**
  - Load if relevant operation will be performed
  - Skipping references = incomplete and low-quality work
  - Load when needed, do not load unnecessarily

  ⛔ **REQUEST INTERPRETATION - MAKING ASSUMPTIONS = ERROR**

  - Before taking action, examine existing similar files and references
  - NEVER add your own preferences → only apply documented rules
  - Apply PROJECT STANDARDS, not your own habits
  - If there is uncertainty → ASK the user
  - Making assumptions = INCORRECT WORK, assumption = failed task
  - Writing code without examining examples and understanding files = WORK WILL BE REJECTED

  ⛔ **APPLICATION - READING IS NOT ENOUGH**

  - Saying "I read it" means nothing
  - Actively CHECK the rules and APPLY them at every step
  - NEVER choose Speed > Quality → do it right the first time
  - "I'll fix it later" is NOT ACCEPTABLE

  ⛔ **WORKFLOW COMPLIANCE**

  - If workflow is defined → MUST follow it
  - No step can be skipped
  - Order cannot be changed
  - "Not necessary" or "we can skip" is NOT ACCEPTABLE
  - Workflow rule > all other rules

  🧠 **THINKING PROCESS - SKIPPING = LOW QUALITY WORK**

  ⛔ **UNDERSTANDING CONTEXT IS REQUIRED - BEFORE STARTING WORK**

  🚨 STARTING WORK WITHOUT READING LOADED CONTEXT = FORBIDDEN 🚨

  - CLAUDE.md → Project rules, standards, constraints
  - Memory files → Previous session context, decisions
  - Reference files → Technical standards, templates

  ⛔ **CONTEXT CHECKLIST (BEFORE EVERY TASK)**

  - [ ] Was CLAUDE.md read? → Are project standards understood?
  - [ ] Is there a memory/checkpoint? → Was previous context loaded?
  - [ ] Was existing code/structure reviewed? → Are patterns understood?

  🚫 **WORK DONE WITHOUT READING CONTEXT = INVALID**

  - Writing code without reading context → FORBIDDEN
  - Making changes without knowing standards → FORBIDDEN
  - Designing without seeing patterns → FORBIDDEN
  - Continuing without knowing previous decisions → FORBIDDEN

  </understanding>

</document>
```
