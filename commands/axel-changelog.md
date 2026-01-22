---
name: axel:changelog
description: Manage CHANGELOG.md with automatic version bumping and git change analysis
type: command
---

# AXEL Command: /axel:changelog

```xml
<document type="command">

  <enforcement>
    <![CDATA[
    ⛔ VERSION CONTROL RULES
    - MUST find git repository root using: git rev-parse --show-toplevel
    - MUST operate in git root directory for all git commands
    - MUST be in a git repository
    - MUST use semantic versioning (MAJOR.MINOR.PATCH)
    - MUST exclude whitespace-only changes from analysis
    - MUST get user approval for version bump type
    - MUST work across different project types
    - MUST analyze uncommitted/staged changes (working tree)
    - MUST stop if no changes detected in working tree

    ⛔ PROJECT TYPE DETECTION & SYNCHRONIZATION
    Detect project type and sync version accordingly:
    - Claude Plugin: .claude-plugin/plugin.json → "version" field
    - Node.js/npm: package.json → "version" field
    - Python: pyproject.toml → [project] version or [tool.poetry] version
    - Rust: Cargo.toml → [package] version
    - PHP: composer.json → "version" field
    - .NET: *.csproj or Directory.Build.props → <Version> tag
    - Generic: CHANGELOG.md only (no sync needed)

    Priority order (first match wins):
    1. .claude-plugin/plugin.json
    2. package.json
    3. pyproject.toml
    4. Cargo.toml
    5. composer.json
    6. *.csproj or Directory.Build.props
    7. None (CHANGELOG.md only)

    ⛔ CHANGELOG FORMAT
    - Use bullet list format (not grouped sections)
    - Format: `## [X.Y.Z] - YYYY-MM-DD`
    - Prepend new version above previous versions
    - Use action prefixes: "Added", "Updated", "Removed", "Fixed"
    ]]>
  </enforcement>

  <objective>
    Automate CHANGELOG.md management with version control.
    Analyzes git changes, prompts for semantic version bump,
    and synchronizes CHANGELOG.md with plugin.json.
  </objective>

  <variables>
    <var name="arguments" from="args.*"/>
  </variables>

  <execution flow="linear"><![CDATA[
    Step 1 - Find Git Repository Root:
    - Run: `git rev-parse --show-toplevel`
    - IF error (contains "fatal"):
      → Print: "❌ Error: Not a git repository. CHANGELOG management requires git."
      → STOP
    - Store result in git_root variable
    - Print: "📂 Repository root: ${git_root}"

    Step 2 - Get Current Date:
    - Run cross-platform command:
      → Linux/macOS: `date +%Y-%m-%d`
      → Windows: `powershell -Command "Get-Date -Format 'yyyy-MM-dd'"`
      → Try: `date +%Y-%m-%d 2>/dev/null || powershell -Command "Get-Date -Format 'yyyy-MM-dd'"`
    - Store as: current_date
    - Example: "2026-01-22"

    Step 3 - Check CHANGELOG.md:
    - Change to git root: `cd "${git_root}"`
    - Run: `test -f CHANGELOG.md && echo "exists" || echo "missing"`
    - IF missing:
      → Create new CHANGELOG.md in git root:
        ```markdown
        # Changelog

        ## [0.1.0] - ${current_date}

        - Initial release
        ```
      → Set current_version = "0.1.0"
      → Print: "✅ Created CHANGELOG.md with version 0.1.0"
    - IF exists:
      → Read CHANGELOG.md
      → Extract version from first `## [X.Y.Z]` pattern
      → Store as: current_version
      → Print: "📋 Current version: ${current_version}"

    Step 4 - Detect Project Type & Version File:
    - In git root directory, check files in priority order:
      1. `.claude-plugin/plugin.json` → Claude Plugin
      2. `package.json` → Node.js/npm
      3. `pyproject.toml` → Python
      4. `Cargo.toml` → Rust
      5. `composer.json` → PHP
      6. `*.csproj` or `Directory.Build.props` → .NET
      7. None → Generic project (CHANGELOG only)

    - For first match found:
      → Read version file
      → Store project_type (e.g., "Claude Plugin", "Node.js", "Python", ".NET", etc.)
      → Store version_file (e.g., ".claude-plugin/plugin.json", "MyProject.csproj")
      → Store version_field (e.g., "version" for JSON, "[package] version" for TOML, "<Version>" for XML)
      → Print: "🔍 Detected: ${project_type} project (${version_file})"

    - IF no version file found:
      → Store project_type = "Generic"
      → Store version_file = null
      → Print: "📋 Generic project (CHANGELOG.md only)"

    Step 5 - Check for Uncommitted Changes:
    - Run in git root: `cd "${git_root}" && git status --short`
    - Count non-empty lines
    - Store as: change_count

    - IF change_count == 0:
      → Print: "⚠️ No changes detected in working tree"
      → Print: "💡 Make changes to your project, then run this command"
      → STOP

    - IF change_count > 0:
      → Print: "📝 Found ${change_count} file(s) with changes"
      → Continue

    Step 6 - Analyze Uncommitted Changes (Exclude Whitespace):
    - Get all changed files:
      → Run in git root: `cd "${git_root}" && git status --short`
      → Parse: `??` (untracked), `M` (modified), `D` (deleted), `A` (added)

    - For EACH modified file, check if it has non-whitespace changes:
      → Run in git root: `cd "${git_root}" && git diff --ignore-all-space --quiet -- <file>`
      → Exit code 0 = whitespace-only (SKIP this file)
      → Exit code 1 = real changes (INCLUDE this file)

    - Build final list:
      → Untracked files: Always include (`??`)
      → Modified files: Only if non-whitespace changes (`M`)
      → Deleted files: Always include (`D`)
      → Added files: Always include (`A`)

    - Categorize files:
      → Added: `??`, `A` status
      → Updated: `M` status (only non-whitespace)
      → Removed: `D` status

    - Store change summary
    - Print changes overview with file count

    Step 7 - Prompt Version Bump:
    - Use AskUserQuestion with 4 options:
      1. CURRENT (${current_version} - keep)
         Description: "Update current version entry (for iterative development)"
      2. PATCH (${current_version} → patch)
         Description: "Bug fixes, minor changes (backward compatible)"
      3. MINOR (${current_version} → minor)
         Description: "New features (backward compatible)"
      4. MAJOR (${current_version} → major)
         Description: "Breaking changes (not backward compatible)"
    - Get user selection
    - Store as: bump_type

    Step 8 - Calculate New Version:
    - Parse current_version: split by "." into [major, minor, patch]
    - Calculate new version:
      → IF CURRENT: new_version = "${current_version}" (keep same)
      → IF PATCH: new_version = "${major}.${minor}.${patch + 1}"
      → IF MINOR: new_version = "${major}.${minor + 1}.0"
      → IF MAJOR: new_version = "${major + 1}.0.0"

    - IF CURRENT selected:
      → Print: "🔄 Updating current version: ${current_version}"
    - ELSE:
      → Print: "🔢 New version: ${current_version} → ${new_version}"

    Step 9 - Format Changes for CHANGELOG:
    - Build bullet list from git changes:
      → For each added file: "- Added `filename`"
      → For each modified file: "- Updated `filename`"
      → For each deleted file: "- Removed `filename`"
    - Group intelligently (commands, references, workflows, etc.)
    - Store as: change_bullets

    Step 10 - Update CHANGELOG.md:
    - IF bump_type == "CURRENT":
      → Check if current version entry exists in CHANGELOG
      → Read CHANGELOG content
      → Search for `## [${current_version}]` pattern

      IF FOUND (version entry exists):
        → Extract existing bullets from current version
        → Merge with new change_bullets (avoid duplicates)
        → Use Edit tool to replace:
          OLD: `## [${current_version}] - <old_date>\n<old_bullets>`
          NEW: `## [${current_version}] - ${current_date}\n<merged_bullets>`
        → Print: "✅ Updated existing version ${current_version} in CHANGELOG.md"

      IF NOT FOUND (version entry doesn't exist):
        → Prepend new version entry (same as bump case)
        → Print: "✅ Created version ${current_version} entry in CHANGELOG.md"

    - ELSE (PATCH/MINOR/MAJOR):
      → Use Edit tool to prepend new version:
        OLD:
        ```
        # Changelog

        ## [${current_version}]
        ```
        NEW:
        ```
        # Changelog

        ## [${new_version}] - ${current_date}

        ${change_bullets}

        ## [${current_version}]
        ```
      → Print: "✅ Updated CHANGELOG.md"

    Step 11 - Update Version File (Conditional):
    - IF bump_type == "CURRENT":
      → Skip version file update (version hasn't changed)
      → Print: "⏭️ Skipped version file (version unchanged)"
      → Store version_file_updated = false

    - ELSE IF version_file != null:
      → Ask user for confirmation using AskUserQuestion:
        Question: "Update version in ${version_file}?"
        Header: "Sync Version"
        Options:
          1. "Yes, update ${version_file}"
             Description: "Sync version number to ${new_version} in ${version_file}"
          2. "No, skip version file"
             Description: "Only update CHANGELOG.md, leave ${version_file} unchanged"

      → IF user selected "Yes":
        → Determine file format and update accordingly:

          JSON files (.claude-plugin/plugin.json, package.json, composer.json):
          → Use Edit tool:
            OLD: `"version": "${current_version}"`
            NEW: `"version": "${new_version}"`

          TOML files (pyproject.toml, Cargo.toml):
          → Use Edit tool:
            OLD: `version = "${current_version}"`
            NEW: `version = "${new_version}"`

          XML files (*.csproj, Directory.Build.props):
          → Use Edit tool:
            OLD: `<Version>${current_version}</Version>`
            NEW: `<Version>${new_version}</Version>`

        → Store version_file_updated = true
        → Print: "✅ Updated ${version_file}"

      → IF user selected "No":
        → Store version_file_updated = false
        → Print: "⏭️ Skipped ${version_file} update"

    - ELSE:
      → Store version_file_updated = false
      → Skip (Generic project, CHANGELOG only)

    Step 12 - Summary:
    - Print final summary:
      ```
      ✅ Changelog updated successfully!

      Project Type: ${project_type}
      Version: ${current_version} → ${new_version}
      Date: ${current_date}
      Bump Type: ${bump_type}

      Files updated:
      - CHANGELOG.md
      ${version_file_updated ? "- " + version_file : ""}

      Changes logged:
      ${change_bullets}
      ```

    Step 13 - Commit Changes (Optional):
    - Ask user for confirmation using AskUserQuestion:
      Question: "Commit all changes now?"
      Header: "Git Commit"
      Options:
        1. "Yes, commit with axel:commit"
           Description: "Stage and commit all changes using axel:commit command"
        2. "No, I'll commit manually later"
           Description: "Skip commit step, you can commit manually when ready"

    - IF user selected "Yes":
      → Stage all changes in git root: `cd "${git_root}" && git add .`
      → Run axel:commit command
      → Print: "✅ Changes committed successfully"

    - IF user selected "No":
      → Print: "⏭️ Skipped commit. Run 'git add . && /axel:commit' when ready"
      → STOP
  ]]></execution>

  <understanding/>

</document>
```
