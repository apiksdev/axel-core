# AXEL - AI XML Execution Language

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Marketplace](https://img.shields.io/badge/Marketplace-AXEL-orange)](https://github.com/apiksdev/axel-marketplace)
[![Support](https://img.shields.io/badge/Support-Development-3fb950)](FUNDING.md)

AXEL is an XML-based DSL (Domain-Specific Language) plugin for Claude Code. It is used to configure AI systems, manage multi-step processes, and persistently store session information.

## Table of Contents

- [The Problem We Solved](#the-problem-we-solved)
- [Why AXEL?](#why-axel)
- [Get Started](#get-started)
- [Commands](#commands)
- [Core Concepts](#core-concepts)
- [Document Load Modes](#document-load-modes)
- [Project](#project)
- [Skill](#skill)
- [Agent](#agent)
- [Workflow](#workflow)
- [Command](#command)
- [Memory](#memory)
- [Project Structure](#project-structure)
- [Scripts](#scripts)
- [Best Practices](#best-practices)
- [Support](#support)
- [License](#license)

---

## The Problem We Solved

AI coding assistants are powerful tools, but they come with a fundamental challenge: **inconsistent behavior**. After months of working with Claude Code on complex projects, we encountered recurring issues that made collaboration frustrating and unpredictable.

### The Issues We Faced

**1. Assumption-Based Behavior**

Instead of reading files thoroughly, Claude Code often made assumptions about content. When given a spec file, it would skim through and miss critical details. We'd define specific coding standards in our requirements, only to receive code that ignored half of them.

**2. Context Amnesia**

In longer conversations, previously established rules would fade away. We'd spend time defining coding standards at the start of a session, only to watch them be completely ignored 10 messages later. The AI would "forget" that we agreed on specific patterns.

**3. Selective Reading**

When presented with documentation or specification files, Claude Code exhibited selective attention—reading some sections while skipping others entirely. A 50-line config file might get only its first 10 lines processed. Complex multi-part instructions would have entire sections overlooked.

**4. Spec Drift**

Even when rules were clearly stated and initially followed, behavior would drift over time. What started as compliant code would gradually deviate from specifications as the conversation progressed.

**5. Inconsistent Execution**

The same prompt, given in different sessions, would produce wildly different results. There was no reliable way to ensure reproducible behavior across conversations.

### Real Examples From Our Experience

These aren't hypothetical—they happened repeatedly:

**"I know, but..."**

We'd define a rule clearly. The AI would acknowledge it. Then immediately violate it, saying "I know the rule says X, but I think Y is better." Our preferences weren't being respected—they were being overridden by the AI's own judgment.

**Command vs Skill Confusion**

When we created a command like `/axel:todos`, the AI would sometimes interpret it as a skill to embody rather than a command to execute. Instead of running the defined workflow, it would start "acting as a todo manager" and improvise.

**Workflow Skipping**

A command designed to create a todo file would suddenly start implementing the todo's content directly. The AI would skip the entire creation workflow and jump straight to execution—ignoring the staged process we carefully designed.

**Path Hallucination**

When referencing plugin paths like `${CLAUDE_PLUGIN_ROOT}/workflows/...`, the AI would guess paths, invent usernames, or use paths from completely different systems. Instead of resolving the variable properly, it would hallucinate plausible-looking but wrong paths.

**"I Read It" Without Reading**

The AI would claim to have read a spec file, then produce output that violated half its rules. Loading a file into context didn't mean understanding or applying it—the content was tokenized but not internalized.

**Context Fade**

Rules established at the start of a conversation would weaken over time. By message 15, the AI would "forget" patterns agreed upon in message 3. Each new task felt like starting over.

**Mechanical Checking**

When asked to validate a document, the AI would run through checklists mechanically—marking items as "passed" without actually verifying them against file content. Validation theater, not real validation.

**"You Could Also..." Syndrome**

Instead of giving one clear answer, the AI would offer multiple alternatives. "You could use A, or alternatively B, or maybe C..." Decision fatigue. We wanted guidance, not a menu of options.

**Over-Engineering Simple Tasks**

A request to "add a button" would result in a full component library, abstraction layers, and utility functions. The AI couldn't resist "improving" beyond what was asked.

**"I'll Fix It Later"**

When caught making a mistake, the AI would acknowledge it but continue with the flawed approach, promising to fix it later. Later never came—or when it did, new issues appeared.

**Proposing Without Reading**

The AI would suggest code changes before reading the existing codebase. Recommendations would conflict with established patterns, use wrong abstractions, or duplicate existing functionality.

**Content Duplication**

When creating new documents, the AI would copy-paste content from referenced files instead of linking to them. The same information would exist in multiple places, inevitably drifting out of sync.

**Inconsistent Naming**

Variable names, file names, and patterns would vary randomly between sessions. What was `userService` yesterday became `UserManager` today and `user_handler` tomorrow.

### The Mental Toll

Working around these issues was exhausting. We found ourselves:

- Repeating instructions multiple times per conversation
- Breaking down simple tasks into micro-steps
- Manually checking every output against our specs
- Losing trust in the AI's ability to follow directions
- Spending more time correcting than creating

### The XML Approach

We realized that natural language instructions, no matter how carefully written, left too much room for interpretation—and misinterpretation. The AI needed something it couldn't skip, couldn't misread, and couldn't "creatively reinterpret."

**XML emerged as the solution because:**

- **Explicit Structure**: Tags clearly delineate sections—no ambiguity about where rules start and end
- **Mandatory Elements**: Required tags like `<enforcement>`, `<documents load="..">`, and `<understanding>` force the AI to acknowledge rules
- **Parseable Format**: The AI processes XML differently than prose—it's harder to skip elements
- **Self-Documenting**: The structure itself communicates intent
- **Validation Points**: `<understanding/>` tags create checkpoints where the AI must confirm comprehension

### What AXEL Solves

AXEL isn't just a syntax—it's a behavioral contract. By encoding instructions in structured XML documents, we create:

1. **Enforceable Rules**: `<enforcement>` blocks that must be processed before execution
2. **Staged Execution**: Step-by-step workflows that prevent the AI from jumping ahead
3. **Persistent Memory**: Session and learned memories that survive across conversations
4. **Explicit Dependencies**: Todo systems with clear prerequisite chains
5. **Reproducible Behavior**: The same AXEL document produces consistent results

The result is an AI that actually reads, actually understands, and actually follows the rules—because the rules are baked into a format it can't ignore.

### What AXEL Doesn't Solve

We believe in transparency. AXEL improves consistency, but it's not magic:

- **Token Cost**: AXEL documents consume context tokens. We mitigate this with `load="on-demand"` and `load="on-trigger"` to avoid loading unnecessary documents, but large workflows with many references can still strain token limits.
- **Advanced Customization**: While commands handle most tasks automatically, creating custom workflows or advanced documents requires understanding the XML syntax.
- **Maintenance Overhead**: AXEL documents need updates when code changes. Specs must stay in sync with implementation.
- **Fundamental AI Limitations**: AI can still make mistakes. AXEL improves consistency but doesn't guarantee perfection.
- **Complex Edge Cases**: In highly ambiguous scenarios, AI behavior may still be unpredictable.
- **Creativity vs Rules**: Overly strict rules can sometimes limit the AI's ability to suggest creative solutions.

AXEL is a tool, not a cure-all. It works best when you understand both its strengths and its limits.

**THE HONEST TRUTH: WE HAVEN'T SOLVED THESE PROBLEMS 100%. BUT WE'VE REDUCED THEM TO A LEVEL WHERE THEY'RE MANAGEABLE—IRRITATING WHEN THEY HAPPEN, BUT NO LONGER BLOCKING OUR WORK.**

---

## Why AXEL?

AXEL transforms how AI assistants understand and execute your project requirements. Instead of repeating context in every conversation, AXEL creates a **living knowledge base** that grows with your project.

### Smart Document Loading

Stop wasting tokens on redundant context. AXEL's intelligent loading system delivers the right information at the right time:

- **Always-on references** for core rules and standards
- **On-demand loading** triggered by conversation keywords
- **Conditional triggers** for domain-specific guides

### Declarative XML Syntax

Human-readable, machine-executable documents that define exactly how AI should behave:

- **Self-documenting structure** with enforced conventions
- **Staged execution flows** for complex multi-step processes
- **Built-in validation** catches errors before runtime

### Reusable Workflows

Define once, execute anywhere. Create standardized processes that your team can rely on:

- **Templated workflows** for common operations (deployment, code review, migrations)
- **Parameterized execution** adapts workflows to different contexts
- **Stage-based flow control** with conditional branching and parallel execution
- **Shareable across projects** through the plugin system

### Persistent Memory

Session and learned memories that survive across conversations:

- **Session memories** track progress and decisions
- **Learned lessons** capture solutions to problems
- **Automatic archiving** keeps context manageable

---

## Get Started

### Prerequisites

- **Python 3.8+**: Required for utility scripts
- **Claude Code**: CLI and VS Code extension for Claude

### Install Plugin

```bash
# Add marketplace (if not added)
claude plugin marketplace add apiksdev/axel-marketplace

# Install axel-core plugin
claude plugin install axel-core@axel-marketplace
```

> See: [axel-marketplace](https://github.com/apiksdev/axel-marketplace)

### Initialize AXEL in Your Project

After installing the plugin, initialize the AXEL structure in your project:

```
/axel:install
```

This command will prompt you for:
- **Project name**: Your project's name
- **Project description**: Short description
- **Tech stack**: Technologies you use
- **Locale**: Language preference (en/tr)

After installation, the following structure is created:

```
your-project/
├── CLAUDE.md                    # Project configuration
└── .claude/
    ├── commands/                # Custom slash commands
    ├── skills/                  # AI capabilities
    ├── agents/                  # Autonomous task executors
    ├── workflows/               # Multi-step processes
    ├── templates/               # Document templates
    ├── references/              # Technical references
    ├── workspaces/
    │   └── default/
    │       ├── pending/
    │       ├── in-progress/
    │       └── completed/
    ├── BOOTSTRAP.md             # Bootstrap loader (auto-loaded)
    ├── MEMORIES.md              # Session records
    └── LEARNED.md               # Learned lessons
```

---

## Commands

| Command                    | Description                                                                                                  |
| -------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `/axel:install`            | Initialize AXEL structure with folders and configuration files                                               |
| `/axel:create`             | Create AXEL documents (agent, workflow, skill, command, bootstrap)                                           |
| `/axel:fix`                | Validate AXEL document against Bootstrap rules, show numbered inconsistencies, and apply user-selected fixes |
| `/axel:run`                | Execute a single AXEL workflow file                                                                          |
| `/axel:memories`           | Memory management - load memory files                                                                        |
| `/axel:session-save`       | Save current session context to MEMORIES.md                                                                  |
| `/axel:learned-save`       | Save learned lesson to LEARNED.md                                                                            |
| `/axel:compact`            | Compact memories (session/learned) to archive                                                                |
| `/axel:changelog`          | Manage CHANGELOG.md with automatic version bumping and git change analysis                                   |
| `/axel:versions`           | Check plugin versions against marketplace and GitHub                                                         |
| `/axel:commit`             | Smart git commit with AI-generated messages from CLAUDE.md configuration                                     |
| `/axel:research`           | Start AXEL research session - comprehensive research with Pure Markdown output                               |
| `/axel:bypass-permissions` | Toggle Claude Code permission bypass mode on/off                                                             |
| `/axel:yo`                 | Hey, let me confirm I understand what you want before I do anything                                          |
| `/axel:core`               | Execute skill-axel-core with trigger-based workflow dispatch                                                 |

### Command Details

#### `/axel:install`
Initialize AXEL structure in your project. Creates folders and configuration files.

#### `/axel:create`
Create AXEL documents with type-specific templates.

```bash
/axel:create {type} [topic]

# Available types:
# - agent     : Autonomous task executor
# - workflow  : Multi-step process
# - skill     : Expert role definition
# - command   : Slash command definition
# - bootstrap : Project bootstrap file

# Examples:
/axel:create agent code-reviewer
/axel:create agent pr-analyzer
/axel:create workflow database-migration
/axel:create workflow deploy-production
/axel:create skill react-developer
/axel:create skill api-designer
/axel:create command generate-tests
/axel:create command sync-translations
/axel:create bootstrap
```

#### `/axel:fix`
Validate and fix AXEL document against Bootstrap rules.

```bash
/axel:fix {path}

# Example:
/axel:fix skills/my-skill/SKILL.md
```

#### `/axel:run`
Execute a single AXEL workflow file (stateless).

```bash
/axel:run {workflow.md}

# Examples:
/axel:run .claude/workflows/my-workflow.md
/axel:run .claude/workflows/build-deploy.md
```

#### `/axel:memories`
Load memory files (session/learned).

```bash
/axel:memories session   # Load session memories
/axel:memories learned   # Load learned lessons
/axel:memories all       # Load all
```

#### `/axel:session-save`
Save current session context and decisions to `.claude/MEMORIES.md`.

#### `/axel:learned-save`
Save learned lesson to `.claude/LEARNED.md`.

#### `/axel:compact`
Archive memory files.

```bash
/axel:compact memories session   # Archive session memories
/axel:compact memories learned   # Archive learned memories
```

#### `/axel:changelog`
Manage CHANGELOG.md with automatic version bumping and git change analysis.

Features:
- Semantic versioning (MAJOR.MINOR.PATCH)
- Git change analysis (excludes whitespace-only changes)
- Multi-project type support (Claude Plugin, Node.js, Python, Rust, PHP, .NET)
- Optional version file sync
- CURRENT version option for iterative development
- Optional commit integration with `/axel:commit`

```bash
/axel:changelog
```

#### `/axel:versions`
Check plugin versions against marketplace and GitHub.

Features:
- Compare local vs remote versions
- Marketplace integration
- Semantic version comparison
- Status indicators (up-to-date, update available, ahead)

```bash
/axel:versions
```

#### `/axel:commit`
Smart git commit with AI-generated messages from CLAUDE.md configuration.

#### `/axel:research`
Start comprehensive research session with Pure Markdown output.

```bash
/axel:research {topic}

# Example:
/axel:research React Server Components
```

#### `/axel:bypass-permissions`
Toggle Claude Code permission bypass mode on/off.

#### `/axel:yo`
Confirm AI understanding before taking action. Shows goal, plan, scope, and assumptions before execution.

```bash
/axel:yo {what you want me to do}

# Examples:
/axel:yo Add dark mode to settings
/axel:yo Fix the login bug
```

#### `/axel:core`
Direct access to skill-axel-core with trigger-based workflow dispatch.

---

## Core Concepts

### Document Structure

Every AXEL document consists of three parts:

**1. YAML Frontmatter**
```yaml
---
name: document-name
description: Short description
type: workflow
---
```

**2. Markdown Title**
```markdown
# Document Name
```

**3. XML Content in Code Fence**
```xml
<document type="workflow">
  <enforcement>Mandatory rules</enforcement>
  <objective>Purpose</objective>
  <documents name="bootstrap" load="always" mode="context">
    <read src=".claude/BOOTSTRAP.md"/>
  </documents>
  <execution flow="staged">
    <stage id="init">...</stage>
  </execution>
  <understanding/>
</document>
```

### Document Types

| Type                    | Description              | Use Case                           |
| ----------------------- | ------------------------ | ---------------------------------- |
| [project](#project)     | Central configuration    | CLAUDE.md file                     |
| [skill](#skill)         | Expert role definition   | Specializing AI in a specific area |
| [agent](#agent)         | Autonomous task executor | Independent AI tasks               |
| [workflow](#workflow)   | Multi-step process       | Stage-based flow management        |
| [command](#command)     | Slash command definition | `/command` triggered operations    |
| [memory](#memory)       | Memory record            | Session and learned records        |
| [research](#research)   | Research documentation   | Investigation and analysis output  |


---

## Document Load Modes

AXEL's smart loading system optimizes context usage by loading documents only when needed.

| Mode                | When to Use                                    | Example Use Case                          |
| ------------------- | ---------------------------------------------- | ----------------------------------------- |
| `load="always"`     | Core rules, standards that apply to every task | Bootstrap, coding conventions             |
| `load="on-demand"`  | Reference docs needed only for specific topics | Auth docs when discussing JWT             |
| `load="on-trigger"` | Specialized guides for specific domains        | A11y guide when accessibility mentioned   |

### Always Load (Bootstrap)

Perfect for project-wide rules that AI must follow in every interaction.

```xml
<documents name="bootstrap" load="always" mode="context">
  <read src=".claude/BOOTSTRAP.md"/>
  <understanding>
    !! MANDATORY: READ → UNDERSTAND → APPLY !!
    Bootstrap provides project rules, standards, and conventions.
  </understanding>
</documents>
```

### On-Demand Load

Ideal for topic-specific references. Documents load when keywords appear in conversation, saving context tokens.

```xml
<documents name="refs" load="on-demand" mode="context">
  <read src="./auth.md" ask="auth, login, jwt"/>
  <read src="./database.md" ask="database, db, schema"/>
  <understanding>
    Reference documents loaded when related keywords appear in conversation.
  </understanding>
</documents>
```

### On-Trigger Load

Best for specialized domain guides that apply to specific scenarios.

```xml
<documents name="guides" load="on-trigger" mode="context">
  <read src="./accessibility-guide.md" trigger="a11y, accessibility"/>
  <read src="./animation-patterns.md" trigger="animation, motion"/>
  <understanding>
    Domain-specific guides loaded when trigger keywords detected in conversation.
  </understanding>
</documents>
```

### Registry Query Syntax

Dynamic lookup for registered documents, templates, agents, workflows, skills.

```
Format: ${registry:name[filter].property}
```


---

## Project

Central configuration file for AXEL-powered projects.

**File Location**: `CLAUDE.md` (project root)

```xml
<document type="project">
  <enforcement>Project rules</enforcement>
  <project name="my-app" version="1.0.0">
    <description>Project description</description>
    <stack>typescript, react, nodejs</stack>
  </project>
  <locale default="en">
    - code: en
    - docs: en
    - communication: tr
  </locale>
  <configurations>
    <var name="DEFAULT_WORKSPACE" value="default"/>
  </configurations>
  <documents name="bootstrap" load="always" mode="context">
    <read src=".claude/BOOTSTRAP.md"/>
  </documents>
  <understanding/>
</document>
```

---

## Skill

Specializes AI in a specific area with defined capabilities and execution patterns.

**File Location**: `.claude/skills/skill-{name}/SKILL.md`

```xml
<document type="skill">
  <role>Senior Frontend Developer</role>
  <capabilities>
    - React component development
    - TypeScript type safety
    - State management
  </capabilities>
  <execution flow="linear">
    Step 1: Analyze requirements
    Step 2: Design component
    Step 3: Implement
  </execution>
  <understanding/>
</document>
```

---

## Agent

Used for autonomous tasks. Works independently to achieve a specific goal.

**File Location**: `.claude/agents/agent-{name}/AGENT.md`

**Archetypes**:
- `analysis` - Code, PR, or data analysis
- `generation` - Content, code, documentation creation
- `validation` - Standards compliance check
- `orchestration` - Multi-step workflow coordination

```xml
<document type="agent">
  <archetype type="analysis"/>
  <system-prompt>
    You are a code reviewer that analyzes code quality...
  </system-prompt>
  <execution flow="staged">
    <stage id="analyze">...</stage>
    <stage id="report">...</stage>
  </execution>
  <understanding/>
</document>
```

---

## Workflow

Manages multi-step processes. Provides stage-based flow control.

**File Location**: `.claude/workflows/{workflow-name}.md`

**Stage Flow**: `INIT → DISCOVER → ANALYZE → EXECUTE → VERIFY → COMPLETE`

```xml
<document type="workflow">
  <execution flow="staged">
    <stage id="init">
      <print>Starting workflow...</print>
      <ask var="name" prompt="Project name?"/>
    </stage>
    <stage id="execute">
      <tasks>
        Create folders:
          - .claude/
          - .claude/references/
      </tasks>
      <goto when="tasks.done" to="complete"/>
    </stage>
    <stage id="complete">
      <print>Done!</print>
      <stop kind="end"/>
    </stage>
  </execution>
  <understanding/>
</document>
```

---

## Command

Defines slash commands that users can invoke.

**File Location**: `.claude/commands/{command-name}.md`

```xml
<document type="command" entry="cmd:main">
  <variables>
    <var name="action" from="args.0"/>
  </variables>
  <command id="cmd:main">
    <goto when="action == 'list'" to="list"/>
    <goto when="action == 'create'" to="create"/>
    <goto when="else" to="help"/>
  </command>
  <execution flow="staged">
    <stage id="help">...</stage>
    <stage id="list">...</stage>
    <stage id="create">...</stage>
  </execution>
  <understanding/>
</document>
```

---

## Memory

Stores session information and learned lessons.

**File Locations**:
- `.claude/MEMORIES.md` - Session records
- `.claude/LEARNED.md` - Learned lessons

**Memory Types**:
- `session` - Session progress, decisions, remaining work
- `learned` - Problems encountered, solutions, lessons

**Priority Levels**:
- `critical` - Never archived
- `high` - Kept for long time
- `normal` - Standard (default)
- `low` - Short-lived

```xml
<memory type="session" priority="high" tags="auth, backend">
  <timestamp format="2025-01-05 14:30"/>
  <subject>Auth service implementation</subject>
  <context>
    - JWT token system set up
    - Refresh token mechanism added
  </context>
  <files>
    - src/services/auth.ts
    - src/middleware/jwt.ts
  </files>
  <remaining>
    - Write unit tests
  </remaining>
</memory>
```

---

## Research

Comprehensive research and analysis documentation with Pure Markdown output.

**Generated by**: `/axel:research` command

**Output Format**: Pure Markdown (no AXEL XML structure)

Research documents provide:
- Topic exploration and analysis
- Structured findings and insights
- References and sources
- Key takeaways and recommendations

**Example Structure**:
```markdown
# Research: [Topic Name]

## Overview
Brief introduction to the research topic

## Key Findings
- Finding 1
- Finding 2
- Finding 3

## Analysis
Detailed analysis and insights

## Recommendations
Actionable recommendations based on research

## References
- Source 1
- Source 2
```

---

## Project Structure

```
axel-core/
├── .claude-plugin/
│   └── plugin.json              # Plugin metadata
├── AXEL-Bootstrap.md            # Core AXEL rules and syntax
├── CLAUDE.md                    # Project configuration
├── README.md                    # This file
├── commands/                    # Slash command definitions
│   ├── axel-bypass-permissions.md
│   ├── axel-changelog.md
│   ├── axel-versions.md
│   ├── axel-commit.md
│   ├── axel-compact.md
│   ├── axel-core.md
│   ├── axel-create.md
│   ├── axel-fix.md
│   ├── axel-install.md
│   ├── axel-learned-save.md
│   ├── axel-memories.md
│   ├── axel-research.md
│   ├── axel-run.md
│   ├── axel-session-save.md
│   └── axel-yo.md
├── agents/
│   └── agent-axel-runner/
│       └── AGENT.md             # AXEL runner agent
├── skills/
│   └── skill-axel-core/
│       ├── SKILL.md             # Main skill definition
│       ├── references/          # Reference documentation
│       │   ├── AXEL-Agent.md
│       │   ├── AXEL-Claude.md
│       │   ├── AXEL-Command.md
│       │   ├── AXEL-Conventions.md
│       │   ├── AXEL-Memory.md
│       │   ├── AXEL-Research.md
│       │   ├── AXEL-Skill.md
│       │   ├── AXEL-Standards.md
│       │   └── AXEL-Workflow.md
│       ├── scripts/             # Python utility scripts
│       ├── templates/           # Document templates
│       │   └── research/        # Research templates
│       └── workflows/           # Workflow definitions
│           ├── creators/        # Document creator workflows
│           ├── research/        # Research workflows
│           └── utilities/       # Utility workflows
└── references/                  # Core references
    ├── AXEL-Checklist.md
    ├── AXEL-Core.md
    ├── AXEL-Enforcement.md
    └── AXEL-Understanding.md
```

---

## Scripts

Python scripts for fast execution of common operations:

| Script | Purpose | Used By |
|--------|---------|---------|
| `axel_install.py` | Project initialization and folder structure creation | `/axel:install` |
| `axel_compact.py` | Memory archiving and cleanup | `/axel:compact` |
| `axel_bypass.py` | Permission bypass toggle in settings | `/axel:bypass-permissions` |

**Note**: Python 3.8+ is required for these scripts to function properly.

---

## Best Practices

1. **Understanding Required**: Every document must end with `<understanding/>`
2. **Enforcement First**: Define rules at the beginning of the document
3. **Smart Document Loading**: Use `load="always"` for core rules, `load="on-demand"` for topic-specific references
4. **Session Save**: Run `/axel:session-save` when finishing work
5. **Learned Save**: Run `/axel:learned-save` when you learn something important

---

## Support

[Support AXEL development](FUNDING.md)

---

## License

AXEL is licensed under the **Apache License 2.0**.

See [LICENSE](LICENSE) for full details.

## Author

Apiks

