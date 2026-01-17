---
name: axel-install-workflow
description: Initialize AXEL structure with folders and configuration files
type: workflow
triggers:
  - install
  - init
allowed-tools:
  - Read
  - Bash
  - AskUserQuestion
---

# AXEL Workflow: Install

```xml
<document type="workflow">

  <enforcement>
    <![CDATA[
    PATH RESOLUTION:
    - Read the `src`, `ref`, or `target` attribute from the document XML to locate referenced files
    - ${CLAUDE_PLUGIN_ROOT} resolves to plugin installation directory

    INSTALL RULES:
    - Collect parameters from user first
    - Execute Python script for fast installation
    - Python is REQUIRED for this workflow
    ]]>
  </enforcement>

  <objective>
    Initialize AXEL with folder structure and configuration files.
    Collects parameters, then executes Python script for fast installation.
  </objective>

  <variables>
    <var name="plugin_root" value="${CLAUDE_PLUGIN_ROOT}"/>
    <var name="script_path" value="${CLAUDE_PLUGIN_ROOT}/skills/skill-axel-core/scripts/axel_install.py"/>
    <var name="project_name" from="param.project_name"/>
    <var name="project_desc" from="param.project_desc"/>
    <var name="tech_stack" from="param.tech_stack"/>
    <var name="locale" from="param.locale" default="en"/>
    <var name="commit_format" from="param.commit_format" default="conventional"/>
  </variables>

  <execution flow="staged">

    <!-- collect-info: Collect project information from user -->
    <stage id="collect-info">
      <print>Starting AXEL installation...</print>
      <ask>
        - var: project_name
          prompt: "Project name:"
          default: ${cwd.basename}
        - var: project_desc
          prompt: "Project description:"
        - var: tech_stack
          prompt: "Tech stack (e.g.: typescript, react, nodejs):"
        - var: locale
          prompt: "Default locale:"
          default: en
        - var: commit_format
          prompt: "Commit message format:"
          options: [single-line, conventional, detailed]
          default: conventional
      </ask>
      <goto to="execute"/>
    </stage>

    <!-- execute: Run Python installation script -->
    <stage id="execute">
      <print>Running installation...</print>
      <bash output="install_result"><![CDATA[
PYTHONIOENCODING=utf-8 python "${script_path}" --name "${project_name}" --desc "${project_desc}" --stack "${tech_stack}" --locale "${locale}" --commit-format "${commit_format}" --plugin-root "${plugin_root}" --cwd "${cwd}"
      ]]></bash>
      <goto to="complete"/>
    </stage>

    <!-- complete: Report result and complete -->
    <stage id="complete">
      <print>${install_result}</print>
      <goto to="done"/>
    </stage>

    <!-- done: Final completion -->
    <stage id="done">
      <print>
        ## Installation Complete

        AXEL kurulumu tamamlandi. Baslamak icin:
        - CLAUDE.md dosyasini inceleyin
        - Referans dosyalari olusturmak icin /axel:documenter komutunu calistirin
      </print>
      <stop kind="end"/>
    </stage>

  </execution>

  <understanding/>

</document>
```
