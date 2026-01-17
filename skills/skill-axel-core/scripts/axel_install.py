#!/usr/bin/env python3
"""
AXEL Install Script - Fast installation of AXEL folder structure and files.
Reads templates from plugin directory and copies to target project.
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path


def create_folders(base_path: Path) -> list[str]:
    """Create AXEL folder structure."""
    folders = [
        ".claude/commands",
        ".claude/skills",
        ".claude/references",
        ".claude/memories",
        ".claude/research",
    ]

    created = []
    for folder in folders:
        folder_path = base_path / folder
        if not folder_path.exists():
            folder_path.mkdir(parents=True, exist_ok=True)
            created.append(folder)

    return created


def write_file_if_not_exists(file_path: Path, content: str) -> bool:
    """Write file only if it doesn't exist. Returns True if created."""
    if file_path.exists():
        return False
    file_path.write_text(content, encoding="utf-8")
    return True


def read_template(template_path: Path, variables: dict[str, str]) -> str:
    """Read template file, strip frontmatter, and replace variables."""
    content = template_path.read_text(encoding="utf-8")

    # Strip YAML frontmatter (--- ... ---)
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            content = parts[2].strip()

    # Strip template header (# AXEL Template: ...)
    lines = content.split("\n")
    if lines and lines[0].startswith("# AXEL Template:"):
        lines = lines[1:]
        content = "\n".join(lines).strip()

    # Replace ${variable} placeholders
    for key, value in variables.items():
        content = content.replace(f"${{{key}}}", value)

    return content


def main():
    parser = argparse.ArgumentParser(description="AXEL Install Script")
    parser.add_argument("--name", required=True, help="Project name")
    parser.add_argument("--desc", required=True, help="Project description")
    parser.add_argument("--stack", required=True, help="Tech stack")
    parser.add_argument("--locale", default="en", help="Default locale")
    parser.add_argument("--commit-format", default="conventional",
                        choices=["single-line", "conventional", "detailed"],
                        help="Git commit message format")
    parser.add_argument("--plugin-root", required=True, help="AXEL plugin root path")
    parser.add_argument("--cwd", default=".", help="Working directory")

    args = parser.parse_args()

    base_path = Path(args.cwd).resolve()
    plugin_root = Path(args.plugin_root)

    result = {
        "success": True,
        "project_name": args.name,
        "folders_created": [],
        "files_created": [],
        "files_skipped": [],
        "errors": []
    }

    try:
        # Create folders
        result["folders_created"] = create_folders(base_path)

        # No template copies needed - CLAUDE.md references plugin's AXEL-Bootstrap.md directly

        # Generate memory files with real install data
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        memories_content = generate_memories(args.name, timestamp, args.stack)
        memories_path = base_path / ".claude/MEMORIES.md"
        if write_file_if_not_exists(memories_path, memories_content):
            result["files_created"].append(".claude/MEMORIES.md")
        else:
            result["files_skipped"].append(".claude/MEMORIES.md")

        learned_content = generate_learned(args.name, timestamp)
        learned_path = base_path / ".claude/LEARNED.md"
        if write_file_if_not_exists(learned_path, learned_content):
            result["files_created"].append(".claude/LEARNED.md")
        else:
            result["files_skipped"].append(".claude/LEARNED.md")

        # Generate .claude/BOOTSTRAP.md (project-level bootstrap)
        bootstrap_content = generate_bootstrap(plugin_root)
        bootstrap_path = base_path / ".claude/BOOTSTRAP.md"
        if write_file_if_not_exists(bootstrap_path, bootstrap_content):
            result["files_created"].append(".claude/BOOTSTRAP.md")
        else:
            result["files_skipped"].append(".claude/BOOTSTRAP.md")

        # Generate CLAUDE.md with project info (references plugin's AXEL-Bootstrap.md)
        claude_content = generate_claude(args.name, args.desc, args.stack, args.locale, args.commit_format, plugin_root)
        claude_path = base_path / "CLAUDE.md"
        if write_file_if_not_exists(claude_path, claude_content):
            result["files_created"].append("CLAUDE.md")
        else:
            result["files_skipped"].append("CLAUDE.md")

    except Exception as e:
        result["success"] = False
        result["errors"].append(str(e))

    # Output JSON result
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["success"] else 1


def generate_memories(project_name: str, timestamp: str, stack: str) -> str:
    """Generate MEMORIES.md with install session record."""
    return f"""# {project_name} Session Memories

```table-of-contents
```

## {timestamp} - AXEL Installation

```xml
<memory type="session" priority="high" tags="install, setup, axel">
  <timestamp>{timestamp}</timestamp>
  <subject>AXEL project structure initialized</subject>

  <context>
    - Project: {project_name}
    - Stack: {stack}
    - AXEL folder structure created
    - Core reference files installed
    - Memory files initialized
  </context>

  <files>
    - CLAUDE.md
    - .claude/MEMORIES.md
    - .claude/LEARNED.md
  </files>

  <remaining>
    - Configure project-specific references in .claude/references/
    - Add project skills and agents as needed
    - Start development work
  </remaining>
</memory>
```
"""


def generate_learned(project_name: str, timestamp: str) -> str:
    """Generate LEARNED.md with install lesson."""
    return f"""# {project_name} Learned Lessons

```table-of-contents
```

## {timestamp} - AXEL Setup Best Practice

```xml
<memory type="learned" priority="normal" tags="setup, axel, best-practice">
  <timestamp>{timestamp}</timestamp>
  <subject>AXEL project initialization</subject>

  <files>
    - CLAUDE.md
  </files>

  <context>
    - New project initialized with AXEL structure
    - CLAUDE.md references plugin's AXEL-Bootstrap.md directly
    - Memory files created automatically
  </context>

  <solution>
    - Use /axel:install command for consistent project setup
    - Python script provides fast installation when available
  </solution>

  <lesson>
    - Always start new AXEL projects with /axel:install
    - Customize .claude/references/ files for project-specific rules
    - Keep MEMORIES.md updated with session context
  </lesson>
</memory>
```
"""


def generate_bootstrap(plugin_root: Path) -> str:
    """Generate .claude/BOOTSTRAP.md from template."""
    # Template path
    template_path = plugin_root / "skills/skill-axel-core/templates/claude/AXEL-Bootstrap-Tpl.md"

    # No variable replacement - keep ${AXEL_CORE_PLUGIN_ROOT} as-is in the output
    # Read and process template without variable substitution
    content = read_template(template_path, {})

    # Add frontmatter
    frontmatter = """---
name: project-bootstrap
description: Project-level bootstrap with AXEL core references
type: reference
---

# Project Bootstrap

"""

    return frontmatter + content


def generate_claude(project_name: str, project_desc: str, stack: str, locale: str, commit_format: str, plugin_root: Path) -> str:
    """Generate CLAUDE.md from template with variable substitution."""
    project_slug = project_name.lower().replace(" ", "-")

    # Template path
    template_path = plugin_root / "skills/skill-axel-core/templates/claude/AXEL-Claude-Tpl.md"

    # Variables to replace in template
    variables = {
        "project_name": project_name,
        "project_desc": project_desc,
        "tech_stack": stack,
        "locale": locale,
        "commit_format": commit_format,
        "CLAUDE_PLUGIN_ROOT": str(plugin_root.resolve()),
    }

    # Read and process template
    content = read_template(template_path, variables)

    # Add frontmatter
    frontmatter = f"""---
name: {project_slug}
description: {project_desc}
type: project
---

# {project_name}

"""

    return frontmatter + content


if __name__ == "__main__":
    sys.exit(main())
