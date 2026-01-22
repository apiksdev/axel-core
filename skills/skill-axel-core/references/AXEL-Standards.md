---
name: axel-standards
description: AXEL element reference - structured documentation for all XML elements
type: reference
---

# AXEL Standards

```xml
<document type="reference">

  <enforcement>
    - Read `src`, `ref`, or `target` attributes from document references to locate files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
    - Elements listed in document structure order (axel-tag-structure)
  </enforcement>

  <objective>
    AXEL (AI XML Execution Language) element reference.
    Structured documentation for all XML elements with depth, document types, and usage.
  </objective>

  <elements>

    <element name="document" depth="0" document_types="all">
    <![CDATA[
    Purpose: Root container for all AXEL documents

    Example:
    <document type="project|skill|agent|workflow|command|memory|reference" entry="cmd:main">
      <enforcement>...</enforcement>
      <objective>...</objective>
      <execution>...</execution>
    </document>

    Notes:
    - type (required): Document type
    - entry: Entry point for commands only
    ]]>
    </element>

    <element name="enforcement" depth="1" document_types="all" parent="document">
    <![CDATA[
    Purpose: Define mandatory rules that AI MUST follow. Violation = task failure.
    Format: Bullet list inside tag

    Content:
    - Lines with `-` → mandatory rules
    - Lines with `X` → strict prohibitions

    Example:
    <enforcement>
      - Read src attribute from references
      - ${CLAUDE_PLUGIN_ROOT} resolves to plugin directory
      X Never skip validation
      X Never guess file paths
    </enforcement>
    ]]>
    </element>

    <element name="project" depth="1" document_types="project" parent="document">
    <![CDATA[
    Purpose: Project metadata and configuration

    Example:
    <project name="{required}" version="{optional}">
      <description>Full-stack web application</description>
      <stack>
        - language: TypeScript, C#
        - frontend: React 18
        - backend: .NET 8
      </stack>
    </project>

    Children: description, stack
    ]]>
    </element>

    <element name="locale" depth="1" document_types="project" parent="document">
    <![CDATA[
    Purpose: Language and localization settings

    Example:
    <locale default="en|tr|...">
      - code: en
      - docs: en
      - communication: auto
      - commits: en
    </locale>
    ]]>
    </element>

    <element name="documents" depth="1" document_types="project,skill,agent,workflow,command,reference" parent="document">
    <![CDATA[
    Purpose: Document registry - references to load

    Example:
    <documents name="{required}" load="always|on-demand|on-trigger" mode="context|data|map">
      <read src="${CLAUDE_PLUGIN_ROOT}/AXEL-Bootstrap.md"/>
      <read src=".claude/references/standards.md"/>
    </documents>
    ]]>
    </element>

    <element name="memories" depth="1" document_types="project" parent="document">
    <![CDATA[
    Purpose: Memory registry - memory file references

    Example:
    <memories load="always|on-demand">
      <memory name="{id}" src="{path}" auto-save="true|false" what="summary|full" template="{template-path}"/>
    </memories>
    ]]>
    </element>

    <element name="templates" depth="1" document_types="project,skill,agent,workflow,command,reference" parent="document">
    <![CDATA[
    Purpose: Template registry - templates for output generation

    Example:
    <templates load="always|on-demand|on-trigger" mode="context|template">
      <read src=".claude/templates/dto.md" ask="dto, request"/>
    </templates>
    ]]>
    </element>

    <element name="examples" depth="1" document_types="project,skill,agent,reference" parent="document">
    <![CDATA[
    Purpose: Container for code examples

    Example:
    <examples>
      <example name="signal" language="xml">...</example>
    </examples>
    ]]>
    </element>

    <element name="skills" depth="1" document_types="project" parent="document" optional="true">
    <![CDATA[
    Purpose: Skill registry (optional)

    Example:
    <skills load="always|on-demand">
      <ref src="${CLAUDE_PLUGIN_ROOT}/skills/skill-frontend/SKILL.md"/>
    </skills>

    Notes:
    - Optional registry - only add when project has custom skills
    ]]>
    </element>

    <element name="agents" depth="1" document_types="project" parent="document" optional="true">
    <![CDATA[
    Purpose: Agent registry (optional)

    Example:
    <agents load="always|on-demand">
      <ref src="${CLAUDE_PLUGIN_ROOT}/agents/agent-review/AGENT.md"/>
    </agents>

    Notes:
    - Optional registry - only add when project has custom agents
    ]]>
    </element>

    <element name="commands" depth="1" document_types="project" parent="document" optional="true">
    <![CDATA[
    Purpose: Command index/quick reference (CLAUDE.md only, optional)
    Format: Container with <ref> children (name attribute + content)

    Example:
    <commands>
      <ref name="/axel-project">
        - create - Create new project
        - list - List projects
      </ref>
    </commands>

    Notes:
    - Optional registry - only add when project has custom commands
    - Contains <ref> elements with name attribute (slash command path)
    - Content: Bullet list of sub-commands with descriptions
    - No src attribute needed - purely documentation/index
    ]]>
    </element>

    <element name="role" depth="1" document_types="skill" parent="document">
    <![CDATA[
    Purpose: AI persona and expertise definition
    Format: Text description

    Example:
    <role>
      Senior Frontend Developer with 10+ years experience.
      Expert in React, TypeScript, and modern CSS.
    </role>
    ]]>
    </element>

    <element name="capabilities" depth="1" document_types="skill" parent="document">
    <![CDATA[
    Purpose: What the skill can do
    Format: Bullet list

    Example:
    <capabilities>
      - Create React components with TypeScript
      - Write unit tests with Jest
    </capabilities>
    ]]>
    </element>

    <element name="workflows" depth="1" document_types="skill" parent="document">
    <![CDATA[
    Purpose: Workflow registry

    Example:
    <workflows load="always|on-demand|on-trigger">
      <read src=".claude/workflows/build.md" triggers="[build, deploy]"/>
    </workflows>
    ]]>
    </element>

    <element name="archetype" depth="1" document_types="agent" parent="document">
    <![CDATA[
    Purpose: Agent archetype definition

    Example:
    <archetype type="analysis|generation|validation|orchestration">
      Code quality assessment and security review
    </archetype>
    ]]>
    </element>

    <element name="system-prompt" depth="1" document_types="agent" parent="document">
    <![CDATA[
    Purpose: Agent identity and behavior definition
    Format: "You are..." text (300-2000 chars)

    Attributes:
    - voice (optional): Narrative voice for prompt
      - "second-person" (default): "You are..." format
      - "first-person": "I am..." format
      - "third-person": "The agent is..." format

    Content:
    - Role and specialization declaration
    - Core responsibilities (3-5 items)
    - Quality standards (critical/major/minor)
    - Edge case handling

    Example:
    <system-prompt voice="second-person">
      You are a Code Review specialist responsible for:
      - Identifying bugs and security issues
      - Ensuring code quality standards
      - Providing actionable feedback

      Quality Levels:
      - Critical: Security vulnerabilities, data loss risks
      - Major: Logic errors, performance issues
      - Minor: Style issues, naming conventions
    </system-prompt>
    ]]>
    </element>

    <element name="output" depth="1" document_types="agent" parent="document">
    <![CDATA[
    Purpose: Expected output format definition

    Example:
    <output format="markdown|json|yaml|text|xml" target="{optional-filename}">
      ## Review Summary
      - Total Issues: {count}
      - Critical: {critical_count}

      ## Findings
      {findings_list}
    </output>
    ]]>
    </element>

    <element name="objective" depth="1" document_types="skill,agent,workflow,command,reference" parent="document">
    <![CDATA[
    Purpose: Describe what the document does (1-3 sentences)
    Format: Short description text

    Example:
    <objective>
      Manage project workflow documents.
      Lists, creates, and edits workflow files.
    </objective>
    ]]>
    </element>

    <element name="variables" depth="1" document_types="command" parent="document">
    <![CDATA[
    Purpose: Variable definitions container
    Format: Container with <var> children

    Example:
    <variables>
      <var name="project" value="MyProject"/>
      <var name="target" from="args.0"/>
      <var name="name" ask="user"/>
    </variables>
    ]]>
    </element>

    <element name="command" depth="1" document_types="command" parent="document">
    <![CDATA[
    Purpose: Routing block - routes to stages based on arguments

    Example:
    <command id="cmd:main">
      <goto when="${action} = 'list'" to="list"/>
      <goto when="${action} = 'create'" to="create"/>
      <goto to="help"/>
    </command>

    Rules:
    - id="cmd:main" (required, always this value)
    - Contains ONLY <goto> tags
    - Last goto = default (no when condition)
    ]]>
    </element>

    <element name="execution" depth="1" document_types="command,agent,workflow,skill" parent="document">
    <![CDATA[
    Purpose: Container for execution flow

    Example:
    <execution flow="linear|staged">
      <stage id="init">...</stage>
      <stage id="process">...</stage>
    </execution>

    Notes:
    - linear: No stages, text-based instructions in CDATA
    - staged: Stage blocks with sequential/branching/loop patterns

    Children (staged only): stage, parallel, confirm
    ]]>
    </element>

    <element name="context" depth="1" document_types="reference" parent="document">
    <![CDATA[
    Purpose: Usage context and background information
    Format: Bullet list

    Example:
    <context>
      - Used for defining multi-step processes
      - Stage-based flow with implicit sequential execution
    </context>
    ]]>
    </element>

    <element name="requirements" depth="1" document_types="reference" parent="document">
    <![CDATA[
    Purpose: Document requirements specification
    Format: Bullet list

    Example:
    <requirements>
      - Frontmatter must have name, description, type
      - Document root must have type attribute
      - Every stage must end with stop or goto
    </requirements>
    ]]>
    </element>

    <element name="implementation" depth="1" document_types="reference" parent="document">
    <![CDATA[
    Purpose: Implementation steps or file locations

    Example:
    <implementation name="{optional-identifier}">
      .claude/agents/agent-{name}/
      - AGENT.md - Main agent file
    </implementation>
    ]]>
    </element>

    <element name="verification" depth="1" document_types="reference" parent="document">
    <![CDATA[
    Purpose: Verification rules and checks
    Format: Question list or bullet points

    Example:
    <verification>
      - Is document type valid?
      - Does objective explain the purpose?
      - Is understanding at document end?
    </verification>
    ]]>
    </element>

    <element name="checklist" depth="1" document_types="skill,reference,workflow,agent" parent="document">
    <![CDATA[
    Purpose: Validation checklist

    Example:
    <checklist name="{identifier}" src="{optional-external-file}">
      Frontmatter:
      - [ ] name format correct?
      - [ ] type set to "command"?

      Structure:
      - [ ] document type="command"?
      - [ ] single cmd:main block?
    </checklist>
    ]]>
    </element>

    <element name="pattern" depth="1" document_types="reference" parent="document">
    <![CDATA[
    Purpose: Document a design pattern

    Example:
    <pattern name="{required}">
      When: Basic list/create/edit commands
      Structure: cmd:main routes to stages
      Flow: routing → stage → stop
    </pattern>
    ]]>
    </element>

    <element name="principle" depth="1" document_types="reference" parent="document">
    <![CDATA[
    Purpose: Document a guiding principle

    Example:
    <principle name="{required}">
      - Every execution path must end with stop
      - stop kind="end" for success
    </principle>
    ]]>
    </element>

    <element name="decision" depth="1" document_types="reference" parent="document">
    <![CDATA[
    Purpose: Document an architectural decision

    Example:
    <decision name="{required}">
      When: Using goto for flow control
      Pattern: Use to="stage-id" for all jumps
      Reason: Consistent flow control
    </decision>
    ]]>
    </element>

    <element name="memory" depth="0" document_types="memory">
    <![CDATA[
    Purpose: Memory entry container

    Example:
    <memory type="session|learned|todo|backlog" priority="critical|high|normal|low" tags="keyword1,keyword2">
      <timestamp format="YYYY-MM-DD HH:mm"/>
      <subject>Short description (5-10 words)</subject>
      <context>Bullet list of context</context>
      <files>- path/to/file.cs</files>
      <solution>Solution text (learned, todo, backlog)</solution>
      <lesson>Lesson text (learned only)</lesson>
      <remaining>Remaining tasks (session only)</remaining>
      <alternative>Alternative approach (todo, backlog)</alternative>
    </memory>
    ]]>
    </element>

    <element name="timestamp" depth="1" document_types="memory" parent="memory">
    <![CDATA[
    Purpose: Entry timestamp

    Example:
    <timestamp format="YYYY-MM-DD HH:mm"/>
    ]]>
    </element>

    <element name="subject" depth="1" document_types="memory" parent="memory">
    <![CDATA[
    Purpose: Memory subject (5-10 words)

    Example:
    <subject>Database Query Optimization Issue</subject>
    ]]>
    </element>

    <element name="files" depth="1" document_types="memory" parent="memory">
    <![CDATA[
    Purpose: Related files (bullet list or empty)

    Example:
    <files>- src/Services/UserService.cs</files>
    <files/>
    ]]>
    </element>

    <element name="remaining" depth="1" document_types="memory" parent="memory" memory_type="session">
    <![CDATA[
    Purpose: Remaining tasks (session only)

    Example:
    <remaining>- Complete unit tests</remaining>
    ]]>
    </element>

    <element name="solution" depth="1" document_types="memory" parent="memory" memory_type="learned,todo,backlog">
    <![CDATA[
    Purpose: Solution description

    Example:
    <solution>Used Include() for eager loading</solution>
    ]]>
    </element>

    <element name="lesson" depth="1" document_types="memory" parent="memory" memory_type="learned">
    <![CDATA[
    Purpose: Learned lesson

    Example:
    <lesson>Always check for N+1 queries</lesson>
    ]]>
    </element>

    <element name="alternative" depth="1" document_types="memory" parent="memory" memory_type="todo,backlog">
    <![CDATA[
    Purpose: Alternative approach

    Example:
    <alternative>Could also use projection queries</alternative>
    ]]>
    </element>

    <element name="understanding" depth="1|2" document_types="all" parent="document,documents">
    <![CDATA[
    Purpose: Request interpretation rules / document end marker
    Format: Self-closing or with content

    Usage:
    - <understanding/> at document end = "I understand, I will apply"
    - <understanding>...</understanding> = interpretation rules
    - Inside <documents>: explains loaded files

    Example (document end):
    <understanding/>

    Example (inside documents):
    <documents load="always" mode="context">
      <read src=".claude/BOOTSTRAP.md"/>
      <understanding>
        Bootstrap provides core AXEL rules.
      </understanding>
    </documents>
    ]]>
    </element>

    <element name="read" depth="2" document_types="all" parent="documents,templates,workflows,stage">
    <![CDATA[
    Purpose: Include external file content

    Example:
    <read src="{required}" mode="context|data|template" triggers="[keyword1, keyword2]" ask="keyword1, keyword2"/>
    ]]>
    </element>

    <element name="ref" depth="2" document_types="all" parent="skills,agents,workflows,commands">
    <![CDATA[
    Purpose: Reference component with optional project config

    Example (simple):
    <ref src=".claude/agents/agent-review/AGENT.md" ask="review, code review"/>

    Example (with project config - extends skill/agent behavior):
    <ref name="{required}" src="{required}" ask="keyword1, keyword2">
      <prompt>Additional instructions for this project</prompt>
      <documents>
        <read src=".claude/checklists/impl.md" ask="checklist"/>
      </documents>
      <templates>
        <read src=".claude/templates/dto.md" ask="dto"/>
      </templates>
    </ref>

    Notes:
    - ask: Keywords that trigger on-demand loading (comma-separated)
    - Project config allows extending plugin skill/agent behavior
      with project-specific instructions, documents, and templates.
    ]]>
    </element>

    <element name="var" depth="2" document_types="command,workflow" parent="variables">
    <![CDATA[
    Purpose: Variable definition (access: ${varname})

    Example:
    <var name="{required}" value="{static}"/>
    <var name="{required}" from="args.0|args.*|env:VAR_NAME"/>
    <var name="{required}" ask="Prompt text for user"/>
    ]]>
    </element>

    <element name="set" depth="2" document_types="command,workflow,agent,skill" parent="stage">
    <![CDATA[
    Purpose: Variable assignment (inside stages)

    Example:
    <set var="{required}" value="{static}"/>
    <set var="{required}" from="task.output|bash.exit_code|validate.result"/>
    ]]>
    </element>

    <element name="stage" depth="2" document_types="command,workflow,agent,skill" parent="execution">
    <![CDATA[
    Purpose: Execution stage - single step in flow (implicit sequential order)

    Example:
    <stage id="{required-unique}">
      <print>Starting process...</print>
      <ask>
        - name: "Enter name:" default="project"
      </ask>
    </stage>

    Children: print, tasks, bash, workflow, call, invoke, ask, goto, stop, set
    ]]>
    </element>

    <element name="parallel" depth="2" document_types="command,workflow,agent,skill" parent="execution">
    <![CDATA[
    Purpose: Parallel execution of multiple stages

    Example:
    <parallel id="{required}">
      <stage id="build-frontend">
        <bash run="npm run build:frontend"/>
      </stage>
      <stage id="build-backend">
        <bash run="npm run build:backend"/>
      </stage>
    </parallel>
    ]]>
    </element>

    <element name="confirm" depth="2" document_types="command,workflow,agent,skill" parent="execution">
    <![CDATA[
    Purpose: User confirmation stage

    Example:
    <confirm id="{required}">
      <print>
        ## Installation Plan
        **Project:** ${project_name}
        Proceed?
      </print>
      <ask var="confirm" prompt="Continue? (y/n):" default="y">
        <goto when="${confirm} = 'no'" to="cancelled"/>
        <goto when="${confirm} = 'yes'" to="execute"/>
      </ask>
    </confirm>

    Children: print, ask, stop
    ]]>
    </element>

    <element name="example" depth="2" document_types="reference,skill,agent" parent="examples">
    <![CDATA[
    Purpose: Single code example

    Example:
    <example name="{required}" language="xml|bash|csharp|typescript">
      Code content here
    </example>
    ]]>
    </element>

    <element name="print" depth="3" document_types="command,workflow,agent,skill" parent="stage,confirm">
    <![CDATA[
    Purpose: Display message to user

    Example:
    <print>
      ## Project Setup Complete
      **Name:** ${project_name}
      **Path:** ${project_path}
    </print>
    ]]>
    </element>

    <element name="tasks" depth="3" document_types="workflow,agent,skill" parent="stage">
    <![CDATA[
    Purpose: Batch declarative operations OR AI tasks with output

    Example:
    <tasks output="{variable-name}">
      Step 1 - Parse Input:
      - Extract mode from prompt
      - Extract target path

      Step 2 - Process:
      - Apply rules
      - Generate output
    </tasks>

    Notes:
    - output: Optional attribute, captures task result
    - Format: Step N - Name: followed by bullet list
    - Batch Syntax: (details), <- template, -> destination
    ]]>
    </element>

    <element name="bash" depth="3" document_types="command,workflow,agent,skill" parent="stage">
    <![CDATA[
    Purpose: Execute shell command

    Example:
    <bash run="{single-command}"/>
    <bash run="python --version" output="python_check"/>
    <bash output="build_result">
      npm install
      npm run build
    </bash>

    Attributes:
    - run: Single command (optional, use content for multi-line)
    - output: Variable name to capture command output (optional)
    ]]>
    </element>

    <element name="workflow" depth="3" document_types="command,agent,skill" parent="stage">
    <![CDATA[
    Purpose: Trigger a workflow

    Example:
    <workflow src=".claude/workflows/deploy.md" output="deploy_result">
      <param name="environment" value="production"/>
    </workflow>
    ]]>
    </element>

    <element name="call" depth="3" document_types="command,workflow,agent,skill" parent="stage">
    <![CDATA[
    Purpose: Call another slash command

    Example:
    <call command="{required-/slash-command}" args="{optional}"/>
    <call command="/axel:session-save" auto-save-check="session"/>

    auto-save-check: Execute only if memory auto-save="true" in CLAUDE.md
    ]]>
    </element>

    <element name="invoke" depth="3" document_types="command,workflow,agent,skill" parent="stage">
    <![CDATA[
    Purpose: Direct agent/skill invocation via Claude Code tools

    Example (agent with output):
    <invoke name="Task" output="analyzer">
      <param name="subagent_type">axel:agent-analyzer</param>
      <param name="prompt">
        - mode: analyze
        - target: ${target}
      </param>
    </invoke>

    Example (skill):
    <invoke name="Skill">
      <param name="skill">skill-name</param>
    </invoke>

    Example (resume agent):
    <invoke name="Task">
      <param name="resume">${analyzer.agent_id}</param>
      <param name="prompt">Continue analysis with new context</param>
    </invoke>

    Notes:
    - output: Namespace for result access (${name.output}, ${name.agent_id})
    - resume: Agent ID to continue previous execution
    ]]>
    </element>

    <element name="ask" depth="3" document_types="command,workflow,agent,skill" parent="stage,confirm">
    <![CDATA[
    Purpose: Request user input

    Example (multiple variables):
    <ask>
      - project_name: "Enter name:" default="${cwd.basename}"
      - project_desc: "Description:"
    </ask>

    Example (confirmation with branching):
    <ask var="{name}" prompt="{text}" default="{value}">
      <goto when="${confirm} = 'no'" to="cancelled"/>
      <goto when="${confirm} = 'yes'" to="execute"/>
    </ask>
    ]]>
    </element>

    <element name="wait" depth="3" document_types="command,workflow,agent,skill" parent="stage">
    <![CDATA[
    Purpose: Wait for user

    Example:
    <wait for="user|input|confirmation"/>
    ]]>
    </element>

    <element name="goto" depth="3" document_types="command,workflow,agent,skill" parent="stage,command,ask">
    <![CDATA[
    Purpose: Flow control - jump to stage

    Example:
    <goto when="${condition}" to="{required-stage-id}"/>
    <goto to="{default-stage}"/>

    Operators: = != > < >= <= AND OR '' (empty)
    ]]>
    </element>

    <element name="stop" depth="3" document_types="command,workflow,agent,skill" parent="stage,confirm">
    <![CDATA[
    Purpose: Terminate execution

    Example:
    <stop kind="end|error"/>
    <stop when="${condition}" kind="error"/>
    ]]>
    </element>

    <element name="write" depth="3" document_types="command,workflow,agent,skill" parent="stage">
    <![CDATA[
    Purpose: Write content to file

    Attributes:
    - src (required): Target file path
    - mode (required): Write mode - create|append|prepend|merge
    - content (optional): Variable reference for content

    Example:
    <write src=".claude/MEMORIES.md" mode="append"/>
    <write src="${file.path}" content="${validated.content}" mode="create"/>
    ]]>
    </element>

    <element name="term" depth="1" document_types="reference" parent="document">
    <![CDATA[
    Purpose: Terminology definition for glossary documents

    Example:
    <term name="workflow">
      - Definition: Multi-step process document with staged or linear execution
      - Usage: Use to define complex operations with multiple stages
    </term>

    Notes:
    - name (required): Term identifier in kebab-case
    - Content: Definition and Usage bullet points
    ]]>
    </element>

    <element name="axel-tag-structure" depth="2" document_types="reference" parent="templates">
    <![CDATA[
    Purpose: Document structure visualization in tree format
    Format: ASCII tree inside CDATA block

    Example:
    <axel-tag-structure>
      Component Document Structure
      +-- Frontmatter (name, description, type)
      +-- <document type="reference">
      |   +-- <enforcement>
      |   +-- <objective>
      |   +-- <context>
      +-- </document>
    </axel-tag-structure>

    Notes:
    - Used in Component and Checklist patterns
    - Shows hierarchical document structure
    - Placed inside templates section
    - Content wrapped in CDATA to preserve special characters
    ]]>
    </element>

    <element name="note" depth="1" document_types="reference" parent="document">
    <![CDATA[
    Purpose: Additional information or cross-reference note

    Example:
    <note name="detailed-reference">
      For detailed information:
      - Element specifications → AXEL-Standards.md
      - Usage examples → AXEL-Standards.md
    </note>

    Notes:
    - name (required): Note identifier
    - Used for supplementary information
    ]]>
    </element>

    <element name="example" depth="1" document_types="reference" parent="document">
    <![CDATA[
    Purpose: Standalone code example (without examples wrapper)
    Format: Code content inside CDATA block

    Example:
    <example name="success-response" language="json"><![CDATA[
    {
      "success": true,
      "data": { "id": "usr_123" }
    }
    ]]></example>

    Notes:
    - name (required): Example identifier
    - language (required): Code language (json, xml, csharp, typescript)
    - Used in Standards pattern for code samples
    - Different from depth=2 example inside <examples> container
    ]]>
    </element>

  </elements>

  <understanding/>

</document>
```
