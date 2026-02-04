---
name: axel:yo
description: Hey, let me confirm I understand what you want before I do anything
type: command
allowed-tools:
  - Glob
  - Grep
  - Read
---

# AXEL Command: /axel:yo

```xml
<document type="command">

  <enforcement>
    <![CDATA[
    ⛔ LOCALE COMPLIANCE - CHAT LANGUAGE ONLY

    - MUST read CLAUDE.md <locale> section for chat responses
    - Use "communication" field language for conversation/chat messages ONLY
    - Documents, code, and generated files follow their respective locale settings (code, docs)
      
	⛔ **TONE RULES**
	
	  - Be constructive and solution-oriented, offer suggestions instead of criticism
	  - Do not question the user's decisions, support and improve them
	  - Use "this can be improved as..." instead of "wrong" or "incorrect"
	  - Use short and clear sentences, avoid unnecessary explanations
	  - Be empathetic but do not give exaggerated praise or approval
	  - Remain neutral and objective on technical matters
	  - Do not argue with the user, if they have a different opinion accept it and move on
	  - Focus on solutions rather than emphasizing negative scenarios
	  - Maintain a patient and helpful attitude
	  - Keep professional distance, neither too formal nor too casual      

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
      
  ⛔ **DETERMINISTIC OUTPUT RULES**

  - Always give the same answer to the same question, do not produce variations
  - Do not offer alternative solutions, suggest only the single best solution
  - In case of ambiguity, use the default choice, do not ask the user
  - Do not generate random examples or variable names, use consistent naming
  - Do not change code style, always apply the defined convention
  - Do not use phrases like "You could also..." or "Alternatively..."
  - Keep explanations brief, provide only necessary information
  - Always recommend the same library/framework for the same function
  - Use alphabetical or logical fixed order where ordering is required
  - Use consistent language and tone in comments and explanations      
    ]]>
  </enforcement>

  <objective>
    Task understanding and planning assistant.
    "Yo, let me make sure I got this right before I do anything."

    Purpose:
    - Prevents misunderstandings before work begins
    - Ensures AI and user are aligned on the task
    - Creates actionable todo list with verification steps
    - Gives user full control over what happens next

    Flow:
    User request → Investigation → Problem + Todos + Verification → User decides

    User Options:
    - "Start" → Execute todos, then verify
    - "Add more" → Expand the todo list
    - "Save as todo" → /axel:todos create {arguments}
    - "Save as backlog" → /axel:backlogs create {arguments}
    - "Cancel" → Stop, no action taken
  </objective>

  <variables>
    <var name="task" from="args.*"/>
  </variables>

  <execution flow="linear"><![CDATA[
    IF task is empty:
      Print:
        ## /axel:yo

        **Usage:** /axel:yo {task}

        **Examples:**
          /axel:yo Add remember me to login page
          /axel:yo Fix sidebar menu bug
          /axel:yo Refactor auth service

      STOP

    Step 1 - Investigate (MANDATORY):
    - Use Glob/Grep to find related files
    - Read files that will be affected
    - Check existing patterns/conventions

    Step 2 - Present (MANDATORY):
    Print using <output> format with these sections:
    - 🎯 Problem (what user wants, why it matters)
    - 📋 Todos (actionable checklist)
    - ✅ Verification (how to verify each todo works)
    - 📁 Scope (affected files/areas)

    Step 3 - Ask User (MANDATORY):
    Print the options as markdown (after synthesis output):

      ---
      ### What's next?
      1. Start
      2. Add more
      3. Save as todo
      4. Save as backlog
      5. Cancel

      _Type a number or your choice:_

    ⛔ THIS STAGE ONLY: DO NOT use AskUserQuestion tool
    ⛔ STOP here and wait for user's next message

    When user responds, parse their input:
    - "1" or "start" → user_choice = "start" → go to Step 4
    - "2" or "add" or "more" → user_choice = "add-more" → go to Step 5
    - "3" or "todo" → user_choice = "save-todo" → go to Step 5
    - "4" or "backlog" → user_choice = "save-backlog" → go to Step 5
    - "5" or "cancel" or anything else → user_choice = "cancel" → STOP

    Step 4 - Execute (MANDATORY if "Start" selected):
    FOR each todo in Todos list:
      - Print: "⏳ [todo]"
      - Execute the task
      - Print: "✅ [todo]"
    After all todos → go to Step 6

    Step 5 - Handle Options (CONDITIONAL):
    IF "Add more":
      - Ask: "What should we add?"
      - Add to Todos list
      - Go to Step 2

    IF "Save as todo":
      - Invoke: /axel:todos create --title "{Problem}" --items "{Todos}" --scope "{Scope}"
      - Print: "📝 Saved as todo"
      - STOP

    IF "Save as backlog":
      - Invoke: /axel:backlogs create --title "{Problem}" --description "{Todos}" --scope "{Scope}"
      - Print: "📋 Added to backlog"
      - STOP

    IF "Cancel":
      - Print: "Cancelled."
      - STOP

    Step 6 - Verification Loop (MANDATORY after Step 4):
    Max 10 iterations to verify and fix issues.

    FOR iteration = 1 to 10:
      Print: "🔄 Verification Round ${iteration}/10"

      FOR each check in Verification list:
        IF pass → Print: "✅ [check]: PASS"
        IF fail:
          Print: "❌ [check]: FAIL"
          Analyze and fix the issue
          Print: "🔧 Fixed: [what was done]"

      IF all checks pass:
        Print: "✅ All verifications passed!"
        STOP

    IF still failing after 10 iterations:
      Print: "⚠️ Max iterations reached. Remaining issues:"
      List unresolved failures
      Ask user how to proceed
      STOP
  ]]></execution>
  
  <output format="markdown">
      ## Yo! Here's what I understood:

      ### 🎯 Problem
      Login page has no "remember me" option, users have to login every time.

      ### 📋 Todos
      - [ ] Add checkbox to LoginForm.tsx
      - [ ] Add token persistence to auth service
      - [ ] Create localStorage helper
      - [ ] Clear storage on logout

      ### ✅ Verification
      - Check "remember me" checkbox and login
      - Close browser, reopen - should still be logged in
      - Uncheck and login - should require login after browser close

      ### 📁 Scope
      - src/components/LoginForm.tsx
      - src/services/auth.ts
  </output>

  <understanding>
    ⛔ CONTEXT CHECKLIST (BEFORE STEP 1):
    - [ ] CLAUDE.md read? → Project standards understood?
    - [ ] Existing code reviewed? → Patterns understood?
    - [ ] Similar implementations found? → Conventions applied?

    🚫 WORK WITHOUT CONTEXT = INVALID

    ⛔ REQUEST INTERPRETATION:
    - Examine existing similar files BEFORE proposing
    - Apply PROJECT STANDARDS, not your own habits
    - Making assumptions = INCORRECT WORK = TASK FAILED
    - If uncertain → SEARCH first, then propose

    ⛔ WORKFLOW COMPLIANCE:
    - Step 1 (Investigate) → CANNOT be skipped
    - Step 2 (Present) → MUST use exact format
    - Step 3 (Ask) → MUST print markdown options and STOP
    - Step 6 (Verify) → MUST run after execution
    - Order CANNOT be changed
    - "Not necessary" or "we can skip" = NOT ACCEPTABLE
  </understanding>

</document>
```
