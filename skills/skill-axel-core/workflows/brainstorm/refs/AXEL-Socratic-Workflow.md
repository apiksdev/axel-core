---
name: inquiry-socratic
description: Socratic workflow - challenge assumptions, validate decisions, explore alternatives
type: workflow
triggers:
  - socratic
  - challenge
  - validate
  - why
---

# AXEL Workflow: Socratic

```xml
<document type="workflow">

  <enforcement>
    <![CDATA[
    PATH RESOLUTION:
    - Read the `src`, `ref`, or `target` attribute from the document XML to locate referenced files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory

    - Focus on QUESTIONING and VALIDATION
    - Ask "Why?" and "What if not?" questions
    - Challenge assumptions, don't accept at face value
    - Explore alternatives before committing
    - Use Devil's Advocate approach
    - NEVER agree blindly - always question
    - Output structured findings for bootstrap consumption
    ]]>
  </enforcement>

  <objective>
    Socratic workflow for challenging assumptions and validating decisions.
    Answers: Why this approach? What are the alternatives? Is this assumption valid?
    Uses: Devil's Advocate, Assumption Testing, Reversal techniques.
  </objective>

  <variables>
    <var name="topic" from="params.topic" />
    <var name="context" from="params.context" default="" />
  </variables>

  <execution flow="staged">

    <!-- STAGE: INIT -->
    <stage id="init">
      <print>
        ## Socratic Phase

        Questioning: **${topic}**
      </print>
    </stage>

    <!-- STAGE: QUESTION - Core Socratic questioning -->
    <stage id="question">
      <thinking focus="socratic-analysis">
        <![CDATA[
        Apply Socratic techniques to challenge and validate:

        DEVIL'S ADVOCATE:
        - What's wrong with this approach?
        - What would a critic say?
        - What's the strongest counter-argument?

        ASSUMPTION TESTING:
        - What assumptions are being made?
        - Are these assumptions valid?
        - What if an assumption is wrong?

        REVERSAL THINKING:
        - What if we did the opposite?
        - What would happen if we didn't do this?
        - What's the worst approach? (then avoid it)

        ALTERNATIVE EXPLORATION:
        - What other approaches exist?
        - Why weren't they chosen?
        - What would make them better?

        VALIDATION QUESTIONS:
        - How can we verify this is right?
        - What evidence supports this?
        - What would prove this wrong?
        ]]>
      </thinking>
      <tasks output="socratic_result">
        <![CDATA[
        Generate Socratic questions and findings:

        QUESTIONS TO ASK (select most relevant 3-5):
        1. "Why did you choose this approach? Did you consider alternatives?"

        2. "Is this assumption correct? How do you know?"

        3. "Let's think reverse - what if we did the opposite?"

        4. "What's the weakest point of this approach?"

        5. "How can you test this? How would you validate?"

        6. "What would a critic say? What's the strongest counter-argument?"

        7. "What other ways exist? Why didn't you choose them?"

        8. "What happens if this turns out to be wrong?"

        ANALYZE INPUT:
        - topic: ${topic}
        - existing context: ${context}

        Identify implicit assumptions and challenge them.

        OUTPUT:
        - validated: Points that passed scrutiny
        - challenged: Assumptions that need reconsideration
        - alternatives: Other approaches to consider
        - decisions: Decisions that need to be made
        - tests: Ways to validate the approach
        - key_questions: Most important questions to ask user
        ]]>
      </tasks>
    </stage>

    <!-- STAGE: COMPLETE -->
    <stage id="complete">
      <print>
        ## Socratic Findings

        **Validated Points:**
        ${socratic_result.validated}

        **Challenged Assumptions:**
        ${socratic_result.challenged}

        **Alternatives to Consider:**
        ${socratic_result.alternatives}

        **Decisions Needed:**
        ${socratic_result.decisions}

        **Validation Tests:**
        ${socratic_result.tests}

        **Key Questions:**
        ${socratic_result.key_questions}
      </print>
      <stop kind="end" output="${socratic_result}"/>
    </stage>

  </execution>

  <understanding/>

</document>
```
