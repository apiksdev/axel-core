---
name: axel:yo
description: Hey, let me confirm I understand what you want before I do anything
type: command
---

# AXEL Command: /axel:yo

```xml
<document type="command">

  <enforcement>
    <![CDATA[
    ⛔ NO ASSUMPTIONS - ASSUMPTION = TASK FAILED

    - NEVER assume without investigating the codebase first
    - Making assumptions = INCORRECT WORK, assumption = failed task
    - "I think it might be..." = FORBIDDEN without evidence
    - "Probably..." or "Usually..." = FORBIDDEN without verification
    - If uncertain → SEARCH the codebase, then propose
    - Do not speculate about code you have not inspected

    ⛔ INVESTIGATION REQUIRED - NO INVESTIGATION = NO ACTION

    - ALWAYS read and understand relevant files before proposing
    - If user references a file/path → MUST open and inspect it first
    - Be rigorous and persistent in searching code for key facts
    - Review style, conventions, and patterns before proposing changes
    - Writing code without examining examples = WORK WILL BE REJECTED

    ⛔ WORKFLOW COMPLIANCE

    - MUST show understanding before any action
    - MUST wait for user approval
    - NO skill delegation - direct execution
    - Investigation step CANNOT be skipped
    ]]>
  </enforcement>

  <objective>
    Confirm AI understanding of task before execution.
    "Yo, this is what I'm gonna do - cool?"
  </objective>

  <variables>
    <var name="task" from="args.*"/>
  </variables>

  <execution flow="linear"><![CDATA[
    IF task is empty:
      Print help:
        ## /axel:yo

        **Usage:** /axel:yo {what you want me to do}

        **Example:**
          /axel:yo Add dark mode to settings
          /axel:yo Fix the login bug

      STOP

    ELSE:
      Step 1 - Investigate (MANDATORY):
      - Read task: ${task}
      - BEFORE analyzing, search the codebase:
        * Find related files (Glob/Grep)
        * Read existing code that will be affected
        * Check for existing patterns/conventions
        * Look for similar implementations
      - Print investigation findings:
        "🔍 **Investigation:**"
        - Files found: [list relevant files]
        - Patterns observed: [existing conventions]
        - Related code: [similar implementations]
      - IF no investigation done → STOP, cannot proceed without evidence

      Step 2 - Analyze (based on investigation):
      - Identify: goal, approach, scope
      - Base ALL conclusions on investigation findings
      - NO assumptions allowed - only facts from codebase

      Step 3 - Present:
      - Print in this format:

        ## Yo! Here's what I understood:

        **Task:** ${task}

        **Goal:**
        - [what to achieve - based on investigation]

        **Plan:**
        - [step 1 - following existing patterns]
        - [step 2]
        - [step N]

        **Scope:**
        - [file/area 1]
        - [file/area 2]

        **Evidence:**
        - [finding 1 that supports this plan]
        - [finding 2]

      Step 4 - Confirm:
      - Ask: "Is this what you meant?"
      - Options:
        - "Yes, do it" → proceed with task
        - "Nope, let me clarify" → get correction, re-investigate, re-present
        - "Cancel" → stop

      Step 5 - Execute or Stop:
      - If approved → do the task as understood
      - If cancelled → stop, no action taken
  ]]></execution>

  <understanding>
    ✅ CORRECT BEHAVIOR:

    User: "/axel:yo Add validation to user form"
    AI: "🔍 Investigation: Searched for form files, found src/components/UserForm.tsx.
         Read existing validation in src/utils/validators.ts. Pattern uses Zod schema.
         Found similar validation in LoginForm.tsx using zodResolver."
    → THEN presents plan based on findings

    User: "/axel:yo Fix the login bug"
    AI: "🔍 Investigation: Searched for login-related files. Found auth service in
         src/services/auth.ts. Checked recent changes. Found error handling pattern
         in similar endpoints."
    → THEN analyzes based on actual code

    ❌ WRONG BEHAVIOR (FORBIDDEN):

    User: "/axel:yo Add validation to user form"
    AI: "Goal: Add validation. Plan: I'll use React Hook Form with Yup..."
    → WRONG: Assumed tech stack without checking codebase

    User: "/axel:yo Fix the login bug"
    AI: "Goal: Fix login. Plan: The issue is probably in the auth middleware..."
    → WRONG: Used "probably" without investigating

    User: "/axel:yo Update the config"
    AI: "Plan: I'll update the config.json file..."
    → WRONG: Assumed file name/location without searching
  </understanding>

</document>
```
