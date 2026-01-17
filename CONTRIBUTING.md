# Contributing to AXEL Core

Thank you for your interest in contributing to AXEL Core! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Contribution Guidelines](#contribution-guidelines)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)
- [Code Style](#code-style)
- [Reporting Issues](#reporting-issues)

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a new branch for your feature or fix
4. Make your changes
5. Submit a pull request

## Development Setup

AXEL Core is an XML-based DSL plugin for Claude Code. To set up your development environment:

1. Ensure you have Claude Code installed
2. Clone the repository:
   ```bash
   git clone https://github.com/apiksdev/axel-core.git
   cd axel-core
   ```
3. Review the project structure for existing documents

## Project Structure

```
axel-core/
├── AXEL-Bootstrap.md       # Main bootstrap (routes to references/)
├── CLAUDE.md               # Project instructions
├── README.md               # Project documentation
├── CODE_OF_CONDUCT.md      # Community guidelines
├── CONTRIBUTING.md         # This file
├── agents/                 # Autonomous task executors
├── commands/               # Slash command definitions
├── references/             # Root-level reference documents
└── skills/                 # Specialized AI expertise
```

## Contribution Guidelines

### AXEL Documents

When creating or modifying AXEL documents, follow these rules:

1. **Document Format**: AXEL documents use Markdown files with embedded XML:
   ````markdown
   ---
   name: document-name
   description: Brief description of the document
   type: workflow|skill|agent|command|config
   ---

   # Document Title

   ```xml
   <document type="...">
     <!-- XML content here -->
   </document>
   ```
   ````

2. **No Content Duplication**: Never copy content from referenced documents into new documents. Use `<read src=".."/>` references instead.

3. **XML Comment Format**:
   - Use single-line format: `<!-- stage_id: Description -->`
   - Never use multi-line decorative comments or box-style separators

4. **Document Types**: Follow the appropriate schema for each type:
   - Skills: Specialized AI expertise definitions
   - Agents: Autonomous task executor configurations
   - Workflows: Multi-step process definitions
   - Commands: Slash command definitions

### Code Quality

- Ensure XML is well-formed and valid
- Follow existing naming conventions
- Keep components focused and single-purpose
- Document complex logic with appropriate comments

## Commit Messages

We follow conventional commit format:

```
type(scope): description

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting changes
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```
feat(workflows): add new deployment workflow
fix(agents): resolve task executor timeout issue
docs(readme): update installation instructions
```

## Pull Request Process

1. **Create a descriptive PR title** following commit message conventions
2. **Fill out the PR template** with:
   - Description of changes
   - Related issue numbers
   - Testing performed
3. **Ensure all checks pass**
4. **Request review** from maintainers
5. **Address feedback** promptly
6. **Squash commits** if requested before merge

### PR Checklist

- [ ] Code follows project style guidelines
- [ ] XML documents are well-formed
- [ ] No duplicate content (use references)
- [ ] Comments follow single-line format
- [ ] Documentation updated if needed
- [ ] Commit messages follow conventions

## Code Style

### XML Guidelines

```xml
<!-- Good: Single-line comment -->
<workflow id="example-workflow">
  <stage id="init">
    <!-- init: Initialize the process -->
    <action type="setup"/>
  </stage>
</workflow>

<!-- Bad: Decorative multi-line comments -->
<!-- ========================================
     DO NOT USE THIS STYLE
     ======================================== -->
```

### Naming Conventions

**Plugin Root:**
- Main bootstrap: `AXEL-Bootstrap.md` (routes to `references/`)
- Project instructions: `CLAUDE.md`
- Root references: `references/AXEL-{Name}.md` (e.g., `AXEL-Core.md`, `AXEL-Enforcement.md`)

**Agents:**
- Directory: `agents/agent-axel-{name}/` (e.g., `agent-axel-runner/`)
- Definition file: `AGENT.md`

**Commands:**
- Directory: `commands/`
- Command files: `axel-{name}.md` (e.g., `axel-commit.md`, `axel-run.md`)

**Skills:**
- Directory: `skills/skill-axel-{name}/` (e.g., `skill-axel-core/`)
- Definition file: `SKILL.md`
- Skill references: `references/AXEL-{Name}.md`

**Templates (inside skills):**
- Directory: `templates/{category}/` (e.g., `templates/agents/`, `templates/commands/`)
- Bootstrap file: `AXEL-{Name}-Template-Bootstrap.md` (routes to `refs/`)
- Template files: `refs/AXEL-{Name}-Tpl.md` (e.g., `AXEL-Agent-Linear-Tpl.md`)

**Workflows (inside skills):**
- Directory: `workflows/{category}/` (e.g., `workflows/creators/`, `workflows/utilities/`)
- Bootstrap file: `AXEL-{Name}-Bootstrap.md` (routes to `refs/`, optional)
- Standalone workflow: `AXEL-{Name}-Workflow.md` (e.g., `AXEL-Commit-Workflow.md`)
- Referenced workflows: `refs/AXEL-{Name}-Workflow.md`

**Bootstrap Pattern:**
- Bootstrap files route to multiple files in `refs/` subdirectory
- Used in templates and workflows for organizing related documents

**IDs and Attributes:**
- IDs: `kebab-case` (e.g., `id="my-agent"`)
- Types: `PascalCase` for type names

## Reporting Issues

When reporting issues, please include:

1. **Clear title** describing the problem
2. **Environment details** (Claude Code version, OS)
3. **Steps to reproduce**
4. **Expected behavior**
5. **Actual behavior**
6. **Relevant logs or error messages**

Use the issue templates when available.

## Questions?

If you have questions about contributing:

- Check existing issues and discussions
- Review the documentation in `CLAUDE.md`
- Contact the team at support@apiks.com.tr.

Thank you for contributing to AXEL !
