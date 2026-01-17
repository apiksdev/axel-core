---
name: axel-checklist
description: AXEL document validation rules
type: reference
---

# AXEL Checklist

```xml
<document type="reference">

  <enforcement><![CDATA[
    RULE APPLICATION:
    - checklist when="" defines scope for all child rules
    - rule when="" can override/narrow checklist scope
    - No when = applies to all documents in scope

    SCOPE CONDITIONS:
    - type=X: Document type match
    - flow=X: Flow type match
    - has=X: Document has specific elements
    - has-dir=X: Directory exists in project root (e.g., ".claude-plugin")
    - has-file=X: File exists in project root (e.g., "plugin.json")
    - path-contains=X: File path contains substring (e.g., "axel-plugins")
    - locale=X: Locale match

    RULE PHASES (by prefix):
    - Phase 1 frontmatter: fm-* rules
    - Phase 2 structure: struct-*, order-* rules
    - Phase 3 format: fmt-*, reg-*, path-* rules
    - Phase 4 execution: exec-*, var-*, mem-*, tr-* rules
  ]]></enforcement>

  <objective>
    AXEL document validation rules in machine-readable format.
  </objective>

  <!-- All document types -->
  <checklist name="default">
    <rule id="fm-required" severity="critical" auto-fix="true">
      <check>Has YAML frontmatter with name, description, type</check>
      <fix>Generate frontmatter from filename and document type</fix>
    </rule>
    <rule id="fm-name-kebab" severity="warning" auto-fix="true">
      <check>Frontmatter name is kebab-case</check>
      <fix>Convert to kebab-case</fix>
    </rule>
    <rule id="fm-type-match" severity="critical" auto-fix="true">
      <check>Frontmatter type matches document type attribute</check>
      <fix>Sync types</fix>
    </rule>
    <rule id="fmt-indent" severity="warning" auto-fix="true">
      <check>Consistent 2-space indentation</check>
      <fix>Normalize to 2 spaces</fix>
    </rule>
    <rule id="var-format" severity="warning" auto-fix="true">
      <check>Variables use ${var} format</check>
      <fix>Convert to ${} format</fix>
    </rule>
    <rule id="path-no-absolute" severity="warning" auto-fix="true" when="has-dir=.claude-plugin">
      <check>No hardcoded absolute paths in src</check>
      <fix>Use ${CLAUDE_PLUGIN_ROOT}</fix>
    </rule>
    <rule id="path-exists" severity="critical" auto-fix="false">
      <check>Referenced files exist</check>
      <fix>Fix path or create file</fix>
    </rule>
  </checklist>

  <!-- All except memory -->
  <checklist name="standard" when="type!=memory">
    <rule id="struct-objective" severity="critical" auto-fix="true" when="type!=project">
      <check>Has objective element</check>
      <fix>Add empty objective element</fix>
    </rule>
    <rule id="struct-understanding" severity="warning" auto-fix="true">
      <check>understanding/ is last element before /document</check>
      <fix>Move to end</fix>
    </rule>
    <rule id="order-base" severity="warning" auto-fix="true">
      <check>Element order: enforcement → objective → documents → understanding</check>
      <fix>Reorder elements</fix>
    </rule>
  </checklist>

  <!-- Code format (critical) -->
  <checklist name="code-format">
    <rule id="fmt-fence-count" severity="critical" auto-fix="true">
      <check><![CDATA[File has exactly 2 occurrences of ``` (opening and closing)]]></check>
      <fix>Keep only outer fence, convert inner to {{{lang}}}</fix>
    </rule>
    <rule id="fmt-fence-placeholder" severity="critical" auto-fix="true">
      <check><![CDATA[Nested code fences use {{{lang}}} placeholder syntax]]></check>
      <fix><![CDATA[Replace ``` with {{{lang}}}]]></fix>
    </rule>
    <rule id="fmt-cdata" severity="critical" auto-fix="true">
      <check><![CDATA[Content with < > & | && wrapped in CDATA]]></check>
      <fix>Wrap in CDATA</fix>
    </rule>
    <rule id="fmt-no-escape" severity="critical" auto-fix="true">
      <check><![CDATA[No &lt; &gt; &amp; escape sequences (use CDATA)]]></check>
      <fix>Replace with CDATA</fix>
    </rule>
  </checklist>

  <!-- Registry blocks -->
  <checklist name="registry" when="has=documents,templates,memories">
    <rule id="reg-understanding" severity="warning" auto-fix="true">
      <check>Registry blocks have understanding as last child</check>
      <fix>Add understanding with !! MANDATORY: READ → UNDERSTAND → APPLY !!</fix>
    </rule>
    <rule id="path-resolution" severity="warning" auto-fix="true">
      <check>Enforcement has path resolution rule</check>
      <fix>Add standard path resolution text</fix>
    </rule>
  </checklist>

  <!-- Staged flow only -->
  <checklist name="staged" when="flow=staged">
    <rule id="exec-staged-unique-ids" severity="critical" auto-fix="true">
      <check>Stage ids are unique</check>
      <fix>Append numeric suffix to duplicate ids</fix>
    </rule>
    <rule id="exec-staged-tasks" severity="warning" auto-fix="true">
      <check>Every stage has tasks element</check>
      <fix>Add empty tasks element</fix>
    </rule>
    <rule id="exec-stage-comment" severity="warning" auto-fix="true">
      <check><![CDATA[Stage comments single-line: <!-- id: Desc -->]]></check>
      <fix>Convert to single-line</fix>
    </rule>
    <rule id="exec-goto-match" severity="critical" auto-fix="true">
      <check><![CDATA[Every <goto to="X"> has matching <stage id="X">]]></check>
      <fix>Create empty stage with matching id</fix>
    </rule>
    <rule id="exec-bash-cdata" severity="critical" auto-fix="true">
      <check><![CDATA[<bash> element uses CDATA, not run attribute with &quot; entities]]></check>
      <fix><![CDATA[Convert <bash run="..."> to <bash><![CDATA[...]]]]><![CDATA[></bash>]]></fix>
    </rule>
    <rule id="exec-python-encoding" severity="warning" auto-fix="true">
      <check>Python commands start with PYTHONIOENCODING=utf-8</check>
      <fix>Add PYTHONIOENCODING=utf-8 prefix to python commands</fix>
    </rule>
    <rule id="var-defined" severity="warning" auto-fix="true">
      <check><![CDATA[Every ${var} has matching <set var> or <var name>]]></check>
      <fix><![CDATA[Add <var name="X" description=""/> to variables block]]></fix>
    </rule>
    <rule id="var-used" severity="info" auto-fix="false">
      <check>Every defined variable is used somewhere</check>
      <fix>Remove or use variable</fix>
    </rule>
  </checklist>

  <!-- Skill -->
  <checklist name="skill" when="type=skill">
    <rule id="fm-name-prefix-skill" severity="warning" auto-fix="true">
      <check>Name starts with skill-</check>
      <fix>Add skill- prefix</fix>
    </rule>
    <rule id="fm-allowed-tools" severity="warning" auto-fix="true">
      <check>Has allowed-tools list</check>
      <fix>Add empty allowed-tools list</fix>
    </rule>
  </checklist>

  <!-- Agent -->
  <checklist name="agent" when="type=agent">
    <rule id="fm-name-prefix-agent" severity="warning" auto-fix="true">
      <check>Name starts with agent-</check>
      <fix>Add agent- prefix</fix>
    </rule>
    <rule id="struct-archetype" severity="critical" auto-fix="true">
      <check>Has archetype element after objective</check>
      <fix>Add archetype with default: analysis</fix>
    </rule>
    <rule id="agent-archetype-valid" severity="critical" auto-fix="false">
      <check>Archetype is analysis|generation|validation|orchestration</check>
      <fix>Use valid archetype</fix>
    </rule>
    <rule id="agent-system-prompt" severity="critical" auto-fix="false">
      <check>Has system-prompt element</check>
      <fix>Add system-prompt</fix>
    </rule>
    <rule id="agent-prompt-format" severity="warning" auto-fix="false">
      <check>system-prompt 300-2000 chars, starts with You are...</check>
      <fix>Adjust prompt</fix>
    </rule>
  </checklist>

  <!-- Workflow -->
  <checklist name="workflow" when="type=workflow">
    <rule id="fm-triggers" severity="warning" auto-fix="true">
      <check>Frontmatter has triggers defined</check>
      <fix>Add empty triggers list</fix>
    </rule>
    <rule id="exec-workflow-stages" severity="warning" auto-fix="true">
      <check>Has init and complete stages</check>
      <fix>Add empty init/complete stages</fix>
    </rule>
    <rule id="exec-last-stop" severity="warning" auto-fix="true">
      <check>Last stage ends with stop</check>
      <fix>Add stop element</fix>
    </rule>
  </checklist>

  <!-- Command -->
  <checklist name="command" when="type=command">
    <rule id="struct-entry" severity="critical" auto-fix="true" when="flow=staged">
      <check>Document has entry=cmd:main attribute</check>
      <fix>Add entry="cmd:main" attribute</fix>
    </rule>
  </checklist>

  <!-- Memory -->
  <checklist name="memory" when="type=memory">
    <rule id="mem-type-attr" severity="critical" auto-fix="false">
      <check>Has type=session|learned</check>
      <fix>Add type attribute</fix>
    </rule>
    <rule id="mem-subject" severity="warning" auto-fix="false">
      <check>Entry has subject (5-10 words)</check>
      <fix>Add subject</fix>
    </rule>
  </checklist>

  <!-- Turkish locale -->
  <checklist name="turkish" when="locale=tr">
    <rule id="tr-chars" severity="warning" auto-fix="true">
      <check>Correct Turkish chars: ı ş ç ğ ö ü İ Ş Ç Ğ Ö Ü</check>
      <fix>Replace ASCII equivalents</fix>
    </rule>
  </checklist>

  <understanding/>

</document>
```
