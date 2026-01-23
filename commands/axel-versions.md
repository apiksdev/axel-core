---
name: axel:versions
description: Check AXEL plugins (version, health, updates)
type: command
allowed-tools:
  - Bash
  - WebFetch
---

# AXEL Command: /axel:versions

```xml
<document type="command">

  <enforcement>
    <![CDATA[
    ⛔ VERSION CHECK RULES
    - Read marketplace.json from axel-marketplace plugin
    - Scan local plugins in parent directory
    - Compare local vs remote (GitHub) versions
    - Detect plugins not installed from marketplace
    - Semantic version comparison (x.y.z)
    - Handle fetch errors gracefully

    ⛔ MARKETPLACE INTEGRATION
    - Parse axel-marketplace/.claude-plugin/marketplace.json
    - Build complete plugin list from marketplace
    - Check each marketplace plugin against local installation
    - Show "Not installed" for missing plugins

    ⛔ PERFORMANCE OPTIMIZATION
    - CRITICAL: Make ALL WebFetch calls in PARALLEL
    - First collect all plugin info (local versions, repo URLs)
    - Then fetch ALL remote versions at once (single message, multiple tool calls)
    - Then process results and compare
    - This reduces total time from 4+ seconds to ~1 second

    ⛔ OUTPUT FORMAT
    - Table format with alignment
    - Status indicators:
      ✅ Up-to-date (local == remote)
      ⚠️ Update available (local < remote)
      🔄 Ahead (local > remote, dev version)
      📦 Not installed (in marketplace, not local)
      💡 Local only (local only, not in marketplace)
      ❌ Fetch failed (network error)
    ]]>
  </enforcement>

  <objective>
    Check AXEL ecosystem plugin versions against marketplace and GitHub.
    Compare local installations with marketplace catalog and remote versions.
  </objective>

  <execution flow="linear"><![CDATA[
    Step 1 - Print Header:
    - Print: "📦 AXEL Plugin Version Check"
    - Print: ""

    Step 2 - Read Marketplace Catalog:
    - Read: ../axel-marketplace/.claude-plugin/marketplace.json
    - IF file not found:
      → Print: "⚠️ Warning: axel-marketplace not found, checking local plugins only"
      → Set marketplace_available = false
    - ELSE:
      → Parse JSON to get plugins array
      → Store marketplace plugin names and repos
      → Set marketplace_available = true
      → Print: "🌐 Marketplace catalog loaded"

    Step 3 - Scan Local Plugins:
    - Run: cd .. && find . -maxdepth 2 -name "plugin.json" -path "*/.claude-plugin/*" ! -path "*/axel-marketplace/*" 2>/dev/null | sort
    - Store local plugin paths
    - Build local plugin list with names

    Step 4 - Build Combined Plugin List:
    - Merge marketplace plugins + local plugins
    - Remove duplicates
    - For each plugin, store:
      * name
      * in_marketplace (true/false)
      * in_local (true/false)
      * local_path (if installed)
      * repo_url (from marketplace or local)

    Step 5 - Collect All Plugin Info (Phase 1):
    FOR EACH plugin in combined list:
      A) Get Local Version:
      - IF plugin in_local:
        → Read: ${local_path}/plugin.json
        → Parse: name, version, repository
        → Store in array: plugins[i] = {name, local_version, repo_url, in_local, in_marketplace}
      - ELSE:
        → Get repo_url from marketplace
        → Store in array: plugins[i] = {name, local_version="N/A", repo_url, in_local=false, in_marketplace=true}

      B) Convert repo URL to GitHub raw:
        → https://github.com/USER/REPO → https://raw.githubusercontent.com/USER/REPO/master/.claude-plugin/plugin.json
        → Store: raw_url in plugins[i]

    Step 6 - Fetch ALL Remote Versions in PARALLEL (Phase 2):
    CRITICAL: Make ALL WebFetch calls in a SINGLE message
    - For plugin 1: WebFetch(url=raw_url_1, prompt="Extract version")
    - For plugin 2: WebFetch(url=raw_url_2, prompt="Extract version")
    - For plugin 3: WebFetch(url=raw_url_3, prompt="Extract version")
    - For plugin N: WebFetch(url=raw_url_N, prompt="Extract version")
    - All calls execute simultaneously (~1 second total instead of N seconds)
    - Store results: remote_versions array

    Step 7 - Print Table Header:
    - Print: "Plugin              Local    Remote   Status"
    - Print: "─────────────────────────────────────────────────────"

    Step 8 - Compare and Display Results (Phase 3):
    FOR EACH plugin with index i:

      A) Get versions:
      - local_version = plugins[i].local_version
      - remote_version = remote_versions[i]
      - IF remote_version fetch failed or empty:
        → Set remote_version = "N/A"

      B) Determine Status:
      - IF NOT in_local AND in_marketplace:
        → status = "📦 Not installed"
      - ELSE IF in_local AND NOT in_marketplace:
        → status = "💡 Local only"
      - ELSE IF remote_version = "N/A":
        → status = "❌ Fetch failed"
      - ELSE compare versions using bash:
        ```bash
        local_ver="${local_version}"
        remote_ver="${remote_version}"

        # Parse semantic versions
        IFS='.' read -r l_major l_minor l_patch <<< "$local_ver"
        IFS='.' read -r r_major r_minor r_patch <<< "$remote_ver"

        # Compare
        if [ "$l_major" -gt "$r_major" ] || \
           ([ "$l_major" -eq "$r_major" ] && [ "$l_minor" -gt "$r_minor" ]) || \
           ([ "$l_major" -eq "$r_major" ] && [ "$l_minor" -eq "$r_minor" ] && [ "$l_patch" -gt "$r_patch" ]); then
          echo "🔄 Ahead (dev)"
        elif [ "$l_major" -lt "$r_major" ] || \
             ([ "$l_major" -eq "$r_major" ] && [ "$l_minor" -lt "$r_minor" ]) || \
             ([ "$l_major" -eq "$r_major" ] && [ "$l_minor" -eq "$r_minor" ] && [ "$l_patch" -lt "$r_patch" ]); then
          echo "⚠️ Update available"
        else
          echo "✅ Up-to-date"
        fi
        ```

      C) Format and Print Row:
      - Use printf: "%-20s %-8s %-8s %s\n" "${plugin_name}" "${local_version}" "${remote_version}" "${status}"
      - Print formatted row

    Step 9 - Print Footer:
    - Print: ""
    - Print: "💡 Tip: Enable marketplace auto-update to keep plugins in sync"
    - IF any plugin has "📦 Not installed" status:
      → Print: "📦 Install missing plugins from marketplace"
  ]]></execution>

  <understanding>
    ✅ CORRECT PARALLEL EXECUTION:

    After collecting all plugin info (Step 5):
    plugins = [
      {name: "axel-core", local: "1.1.0", raw_url: "https://raw.githubusercontent.com/..."},
      {name: "axel-bundler", local: "1.0.1", raw_url: "https://raw.githubusercontent.com/..."},
      {name: "axel-todos", local: "1.0.1", raw_url: "https://raw.githubusercontent.com/..."},
      {name: "axel-documenter", local: "1.0.0", raw_url: "https://raw.githubusercontent.com/..."}
    ]

    Step 6 - Make ALL WebFetch calls in ONE message:
    - WebFetch(url=plugins[0].raw_url, prompt="Extract version")
    - WebFetch(url=plugins[1].raw_url, prompt="Extract version")
    - WebFetch(url=plugins[2].raw_url, prompt="Extract version")
    - WebFetch(url=plugins[3].raw_url, prompt="Extract version")

    This executes all 4 fetches simultaneously in ~1 second total.

    ❌ WRONG (SEQUENTIAL):
    - Fetch plugin 1 → wait → result
    - Fetch plugin 2 → wait → result
    - Fetch plugin 3 → wait → result
    - Fetch plugin 4 → wait → result
    This takes ~4+ seconds total.

    Performance Improvement:
    - Sequential: N plugins × 1 second = N seconds
    - Parallel: All plugins at once = ~1 second
    - For 4 plugins: 4x faster
    - For 10 plugins: 10x faster
  </understanding>

</document>
```
