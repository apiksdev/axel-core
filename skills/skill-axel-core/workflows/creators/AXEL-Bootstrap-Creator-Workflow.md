---
name: bootstrap-creator-workflow
description: Bootstrap document creator - creates project bootstrap files with configurable document references
type: workflow
---

# AXEL Workflow: Bootstrap Creator

```xml
<document type="workflow">

  <enforcement>
    <![CDATA[
    PATH RESOLUTION:
    - Read the `src`, `ref`, or `target` attribute from the document XML to locate referenced files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory
    - ${AXEL_CORE_PLUGIN_ROOT} resolves to AXEL core plugin installation directory

    REFERENCE-BASED CREATION:
    - Use AXEL-Bootstrap-Tpl.md format for output structure
    - DO NOT duplicate content from reference documents
    - Bootstrap files reference documents, not duplicate them

    NO ASSUMPTIONS:
    - If uncertain about files or paths → ASK user
    - If no files found → offer to create empty bootstrap or ask for manual input
    - If output path unclear → detect from prompt or ASK user
    ]]>
  </enforcement>

  <objective>
    Create project bootstrap files through structured inquiry.
    Scans for relevant documents, allows user to select and configure load modes,
    generates bootstrap file in reference document format.
  </objective>

  <variables>
    <var name="prompt" from="param.prompt" default=""/>
    <var name="topic" from="param.topic" default=""/>
  </variables>

  <templates load="always" mode="context">
    <read src="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/templates/claude/AXEL-Bootstrap-Tpl.md"/>
    <understanding>
      !! MANDATORY: READ → UNDERSTAND → APPLY !!
      Template provides output format: document type="reference" with documents registries.
    </understanding>
  </templates>

  <execution flow="linear">
    <![CDATA[
    LINEAR EXECUTION - Bootstrap document creation:

    ⚠️ DETERMINISTIC EXECUTION RULES:
    - Follow steps in EXACT order (1 → 2 → 3 → ...)
    - Use EXACT AskUserQuestion format specified for each question
    - NO skipping steps, NO reordering
    - Each AskUserQuestion MUST use the exact header, question, and options defined

    ============================================================
    Step 1 - Parse Input:
    ============================================================
    - Extract from ${prompt} and ${topic}:
      * subject: Bootstrap purpose (e.g., "frontend", "api", "axel")
      * scan_path: Directory to scan (if mentioned)
      * output_path: Where to save (if mentioned)
      * bootstrap_name: Name if explicitly provided (if mentioned)
    - Print: "## Bootstrap Creator\n\nAnalyzing request..."

    ============================================================
    Step 2 - Ask Subject (CONDITIONAL):
    ============================================================
    - IF subject is empty (not identifiable from prompt/topic):
      → AskUserQuestion:
          header: "Subject"
          question: "What is this bootstrap for?"
          multiSelect: false
          options:
            - label: "AXEL Plugin", description: "Bootstrap for AXEL documents"
            - label: "Code Project", description: "Code files like src/, lib/"
            - label: "Documentation", description: "Documentation like docs/, guides/"
      → Set subject from answer
    - ELSE: Continue with extracted subject

    ============================================================
    Step 3 - Ask Scan Path (CONDITIONAL):
    ============================================================
    - IF scan_path is empty:
      → First, scan project for directories (especially under .claude/)
      → Build dynamic options from found directories
      → AskUserQuestion:
          header: "Directory"
          question: "Which directory to scan?"
          multiSelect: false
          options: (dynamic, max 3 from scan + Other always available)
            - Found directories prioritized: .claude/references, .claude/, ./
            - Example: ".claude/references/", ".claude/", "./"
      → Set scan_path from answer (or custom input via Other)
    - ELSE: Continue with extracted scan_path

    ============================================================
    Step 4 - Scan Files:
    ============================================================
    - Use Glob: ${scan_path}/**/*.md
    - Collect files into list
    - Print: "Scanned: ${scan_path}\nFound: {count} files"
    - IF count == 0:
      → AskUserQuestion:
          header: "No Files"
          question: "No files found, what to do?"
          multiSelect: false
          options:
            - label: "Create empty", description: "Create empty bootstrap, add later"
            - label: "Different dir", description: "Try another directory"
      → IF "Create empty": Set files = [], go to Step 7
      → IF "Different dir": Return to Step 3

    ============================================================
    Step 5 - Select Files:
    ============================================================
    - Print numbered file list
    - AskUserQuestion:
        header: "Files"
        question: "Which files to include?"
        multiSelect: false
        options:
          - label: "All (Recommended)", description: "Include all found files"
          - label: "Select specific", description: "Choose files individually"
    - IF "All": selected_files = all files, go to Step 6
    - IF "Select specific":
      → Use batch selection (4 files per AskUserQuestion, multiSelect: true)
      → FOR EACH batch of 4 files:
        → AskUserQuestion:
            header: "Batch {n}/{total}"
            question: "Select files to include"
            multiSelect: true
            options: (dynamic, file names from batch)
        → Add selected files to selected_files list

    ============================================================
    Step 6 - Configure Load Modes:
    ============================================================
    - IF selected_files is empty: Skip to Step 7
    - AskUserQuestion:
        header: "Load Mode"
        question: "Load mode for files?"
        multiSelect: false
        options:
          - label: "always (Recommended)", description: "All files always loaded"
          - label: "on-demand", description: "All files loaded via keywords"
          - label: "on-trigger", description: "All files loaded via triggers"
          - label: "Mixed", description: "Select load mode per file"

    - IF "always": Set all files load_mode = always

    - IF "on-demand":
      → Auto-generate keywords from filenames:
        * "AXEL-Standards.md" → ask="standard, standards, rules"
        * "AXEL-Agent.md" → ask="agent"
        * Pattern: filename without extension, lowercase, related terms
      → Set ask keywords for all files

    - IF "on-trigger":
      → Auto-generate trigger from filenames:
        * "AXEL-Standards.md" → trigger="standards"
        * Pattern: filename without AXEL- prefix and .md extension, lowercase
      → Set trigger for all files

    - IF "Mixed":
      → PHASE 1: Collect load modes in BATCHES (4 files per AskUserQuestion)
        → FOR EACH batch of 4 files in selected_files:
          → AskUserQuestion with multiple questions (one per file):
              questions: [
                { header: "{short_name1}", question: "Load mode?", multiSelect: false, options: [...] },
                { header: "{short_name2}", question: "Load mode?", multiSelect: false, options: [...] },
                { header: "{short_name3}", question: "Load mode?", multiSelect: false, options: [...] },
                { header: "{short_name4}", question: "Load mode?", multiSelect: false, options: [...] }
              ]
              header format: filename without ".md" extension (max 25 chars)
                * "AXEL-Standards.md" → "AXEL-Standards"
                * "AXEL-Bootstrap-Creator-Workflow.md" → "AXEL-Bootstrap-Creator-W"
              options (same for all):
                - label: "always", description: "Always load"
                - label: "on-demand", description: "Load via keyword"
                - label: "on-trigger", description: "Load via trigger"
                - label: "ignored", description: "Skip this file"
          → Store answers: file_configs[filename] = {src, load_mode}
          → IF load_mode == "ignored": Remove from selected_files

      → PHASE 2: Auto-generate keywords/triggers (NO user questions)
        → FOR EACH file in file_configs (where load_mode != ignored):
          → IF load_mode == "on-demand":
            → Auto-generate: ask = derive_keywords(filename)
            → Pattern: "AXEL-Standards.md" → "standard, standards"
          → IF load_mode == "on-trigger":
            → Auto-generate: trigger = derive_trigger(filename)
            → Pattern: "AXEL-Standards.md" → "standards"

    ============================================================
    Step 7 - Output Path:
    ============================================================
    - IF output_path is empty:
      → AskUserQuestion:
          header: "Save"
          question: "Where to save bootstrap?"
          multiSelect: false
          options:
            - label: "AXEL-Bootstrap.md", description: "Project root directory"
            - label: ".claude/BOOTSTRAP.md", description: ".claude folder"
            - label: "AI suggest", description: "Suggest path based on project structure"
    - IF "AI suggest": Analyze project and suggest appropriate path
    - Set output_path from answer (or custom input via Other)

    ============================================================
    Step 8 - Metadata (AUTO):
    ============================================================
    - IF bootstrap_name is empty:
      → Auto-generate from subject (kebab-case + "-bootstrap")
    - Set bootstrap_objective = "Project bootstrap for ${subject}"
    - Print: "Name: ${bootstrap_name}"

    ============================================================
    Step 9 - Generate Document:
    ============================================================
    - Reference: AXEL-Bootstrap-Tpl.md
    - ⚠️ MANDATORY BUILD STRUCTURE (all rules below are required):
      * Frontmatter: name=${bootstrap_name}, description=${bootstrap_objective}, type=reference
      * Title: # AXEL Bootstrap: ${bootstrap_name}
      * Enforcement: Standard PATH RESOLUTION + MANDATORY READING
      * Objective: ${bootstrap_objective}
      * ONE documents block per load mode, multiple read elements inside
      * Each documents block MUST have understanding as last child
      * Understanding: self-closing at document end
    - Group files by load_mode → each group = one documents block

    ============================================================
    Step 10 - Validate:
    ============================================================
    - Check: frontmatter, document type, paths, load attributes, understanding
    - Auto-fix any issues

    ============================================================
    Step 11 - Save:
    ============================================================
    - Write to ${output_path}
    - Print:
      "## Bootstrap Created

      **File:** ${output_path}
      **Documents:** {count} references

      Load modes:
      - always: {count}
      - on-demand: {count}
      - on-trigger: {count}"
    ]]>
  </execution>

  <output format="json">
    {
      "content": "generated bootstrap document",
      "name": "bootstrap name",
      "path": "file save path"
    }
  </output>

  <understanding/>

</document>
```
