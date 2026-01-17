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
    - MUST show understanding before any action
    - MUST wait for user approval
    - NO skill delegation - direct execution
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
      Step 1 - Analyze:
      - Read task: ${task}
      - Identify: goal, approach, scope, assumptions

      Step 2 - Present:
      - Print in this format:

        ## Yo! Here's what I understood:

        **Task:** ${task}

        **Goal:** [what to achieve]
        **Plan:** [how I'll do it]
        **Scope:** [files/areas affected]
        **Assumptions:** [what I'm assuming]

      Step 3 - Confirm:
      - Ask: "Is this what you meant?"
      - Options:
        - "Yes, do it" → proceed with task
        - "Nope, let me clarify" → get correction, re-present
        - "Cancel" → stop

      Step 4 - Execute or Stop:
      - If approved → do the task as understood
      - If cancelled → stop, no action taken
  ]]></execution>

  <understanding/>

</document>
```
