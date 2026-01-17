---
name: axel:commit
description: Smart git commit with AI-generated messages from CLAUDE.md configuration
type: command
allowed-tools:
  - Read
  - Bash
  - AskUserQuestion
---

# AXEL Command: /axel:commit

```xml
<document type="command" entry="cmd:main">

  <enforcement>
    <![CDATA[
    COMMIT RULES:
    - MUST find git repository root using: git rev-parse --show-toplevel
    - MUST change to git root directory before commit operations
    - MUST read CLAUDE.md for COMMIT_MESSAGE_FORMAT configuration
    - MUST get user approval before committing (NEVER auto-commit)
    - Default to "single-line" format if configuration not found
    - Handle unstaged changes by offering stage-all option
    ]]>
  </enforcement>

  <objective>
    Smart git commit command that:
    1. Finds repository root directory
    2. Reads commit format from CLAUDE.md configurations
    3. Analyzes staged changes
    4. Generates AI commit message based on format
    5. Gets user approval before committing
    6. Commits in correct directory (git root)
  </objective>

  <variables>
    <var name="action" from="args.0" default=""/>
  </variables>

  <command id="cmd:main">
    <goto to="route"/>
  </command>

  <execution flow="linear">
    <![CDATA[
    SMART GIT COMMIT - Linear execution flow

    Step 1 - Route Action:
    - If action = "help":
      * Show usage information:
        ## Commit Command

        Usage: /axel:commit [action]

        Actions:
        - (default) : Analyze changes and commit with AI-generated message
        - help      : Show this help message

        Configuration (CLAUDE.md):
        - COMMIT_MESSAGE_FORMAT: "single-line" (default), "conventional", or "detailed"

        Flow:
        1. Find git repository root
        2. Read commit format from CLAUDE.md
        3. Analyze staged/unstaged changes
        4. Generate AI commit message
        5. Show message and get approval
        6. Commit changes
      * Exit command
    - Otherwise: Continue to Step 2

    Step 2 - Find Git Repository Root:
    - Run bash: git rev-parse --show-toplevel
    - If error (contains "fatal"):
      * Show error: "Not a git repository. Please run this command from within a git repository."
      * Exit with error
    - Store result in git_root variable
    - Show: "Repository root: ${git_root}"

    Step 3 - Read Commit Message Format:
    - Read CLAUDE.md file in git root directory
    - Look for configurations block
    - Extract COMMIT_MESSAGE_FORMAT value
    - Valid values: "single-line", "conventional", "detailed"
    - Default to "single-line" if not found or invalid
    - Store in commit_format variable
    - Show: "Commit format: ${commit_format}"

    Step 4 - Analyze Repository Changes:
    - Change to git root directory: cd "${git_root}"
    - Run bash: git status --porcelain
    - If empty (no changes):
      * Show: "No changes to commit. Working tree is clean."
      * Exit command
    - Run bash: git diff --cached --name-only (get staged files)
    - Run bash: git diff --name-only (get unstaged files)
    - If only unstaged files exist (no staged files):
      * Show: "Unstaged Changes Detected"
      * Show: "You have unstaged changes but nothing is staged for commit."
      * Show: "Files with changes:" + unstaged files list
      * Ask: "Stage all files for commit? (1=Yes, 2=No)"
      * If 1 → Run bash: git add -A, then re-run Step 4
      * If 2 → Show "Commit cancelled by user.", exit command
    - If no staged files and no unstaged files:
      * Show: "No changes to commit. Working tree is clean."
      * Exit command
    - Continue to Step 5

    Step 5 - Get Diff of Staged Changes:
    - Run bash: cd "${git_root}" && git diff --cached
    - Store full diff in diff_result variable
    - Run bash: cd "${git_root}" && git diff --cached --stat
    - Store summary in diff_stat variable

    Step 6 - Generate Commit Message:
    - Analyze diff_result and staged files
    - Generate message based on commit_format:

      IF commit_format = "single-line":
        - Format: "type: description"
        - Max 72 characters
        - Types: feat, fix, docs, refactor, test, chore, style, perf, build, ci
        - Focus on WHAT changed and WHY
        - Example: "feat: add user authentication with JWT tokens"

      IF commit_format = "conventional":
        - Format: "type(scope): description"
        - Max 72 characters for title
        - Optional body after blank line
        - Types: feat, fix, docs, refactor, test, chore, style, perf, build, ci
        - Example:
          feat(auth): add JWT authentication

          Implemented JWT-based authentication for API endpoints

      IF commit_format = "detailed":
        - Title line (max 72 chars)
        - Blank line
        - Body wrapped at 72 chars with bullet points
        - Describe what changed and why
        - Example:
          feat: add user authentication system

          - Implemented JWT token generation and validation
          - Added login and logout endpoints
          - Created middleware for protected routes
          - Updated user model with password hashing

    - Quality check:
      * Clear and concise
      * Describes "what" and "why" (not just "how")
      * Follows conventional commits style
      * Appropriate type based on changes
    - Store in commit_message variable

    Step 7 - Approval Loop:
    - Show:
      ## Proposed Commit Message

      ```
      ${commit_message}
      ```

      ---
      **Files to be committed:**
      ${staged_files}

      **Changes summary:**
      ${diff_stat}
    - Ask: "Choose action: (1=Commit, 2=Cancel, 3=Edit message)"
    - If 1 → Continue to Step 8
    - If 2 → Show "Commit cancelled by user.", exit command
    - If 3 → Ask "Enter new commit message:", update commit_message, return to Step 7 (repeat approval loop)

    Step 8 - Execute Commit:
    - Run bash: cd "${git_root}" && git commit -m "${commit_message}"
    - If result contains "error" or "fatal":
      * Show: "Commit Failed"
      * Show error output
      * Show possible reasons:
        - Pre-commit hooks failing
        - No changes staged
        - Git configuration issues
      * Show: "Please resolve the issue and try again."
      * Exit with error
    - If success:
      * Show: "Commit Successful"
      * Show commit result output
      * Show: "Committed in: ${git_root}"
      * Exit command
    ]]>
  </execution>

  <understanding/>

</document>
```
