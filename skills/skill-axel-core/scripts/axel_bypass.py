#!/usr/bin/env python3
"""
AXEL Bypass Script - Toggle permission bypass mode in Claude Code settings.
Manages defaultMode: bypassPermissions in settings.local.json.
"""

import argparse
import json
import sys
from pathlib import Path


def read_settings(settings_path: Path) -> dict:
    """Read settings.local.json or return empty dict."""
    if settings_path.exists():
        try:
            return json.loads(settings_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}
    return {}


def write_settings(settings_path: Path, settings: dict) -> None:
    """Write settings to settings.local.json."""
    settings_path.parent.mkdir(parents=True, exist_ok=True)
    settings_path.write_text(
        json.dumps(settings, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )


def get_bypass_status(settings: dict) -> bool:
    """Check if bypass mode is enabled."""
    permissions = settings.get("permissions", {})
    return permissions.get("defaultMode") == "bypassPermissions"


def enable_bypass(settings: dict) -> dict:
    """Enable bypass mode by adding defaultMode."""
    if "permissions" not in settings:
        settings["permissions"] = {}
    settings["permissions"]["defaultMode"] = "bypassPermissions"
    return settings


def disable_bypass(settings: dict) -> dict:
    """Disable bypass mode by removing defaultMode."""
    if "permissions" in settings and "defaultMode" in settings["permissions"]:
        del settings["permissions"]["defaultMode"]
        # Clean up empty permissions object
        if not settings["permissions"]:
            del settings["permissions"]
    return settings


def read_vscode_settings(vscode_path: Path) -> dict:
    """Read .vscode/settings.json or return empty dict."""
    if vscode_path.exists():
        try:
            return json.loads(vscode_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}
    return {}


def write_vscode_settings(vscode_path: Path, settings: dict) -> None:
    """Write settings to .vscode/settings.json."""
    vscode_path.parent.mkdir(parents=True, exist_ok=True)
    vscode_path.write_text(
        json.dumps(settings, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )


def enable_vscode_bypass(settings: dict) -> dict:
    """Enable VSCode claudeCode bypass settings."""
    # Build new dict with claudeCode settings first
    new_settings = {}
    new_settings["claudeCode.allowDangerouslySkipPermissions"] = True
    new_settings["claudeCode.initialPermissionMode"] = "bypassPermissions"
    # Preserve other existing settings
    for key, value in settings.items():
        if key not in new_settings:
            new_settings[key] = value
    return new_settings


def disable_vscode_bypass(settings: dict) -> dict:
    """Disable VSCode claudeCode bypass settings."""
    if "claudeCode.allowDangerouslySkipPermissions" in settings:
        del settings["claudeCode.allowDangerouslySkipPermissions"]
    if "claudeCode.initialPermissionMode" in settings:
        del settings["claudeCode.initialPermissionMode"]
    return settings


def main():
    parser = argparse.ArgumentParser(description="AXEL Bypass Mode Manager")
    parser.add_argument("--cwd", default=".", help="Working directory")
    parser.add_argument(
        "--action",
        choices=["status", "enable", "disable", "toggle"],
        default="status",
        help="Action to perform"
    )

    args = parser.parse_args()

    base_path = Path(args.cwd).resolve()
    claude_settings_path = base_path / ".claude" / "settings.local.json"
    vscode_settings_path = base_path / ".vscode" / "settings.json"

    claude_settings = read_settings(claude_settings_path)
    vscode_settings = read_vscode_settings(vscode_settings_path)
    current_status = get_bypass_status(claude_settings)

    result = {
        "success": True,
        "action": args.action,
        "previous_status": current_status,
        "current_status": current_status,
        "message": ""
    }

    try:
        if args.action == "status":
            result["message"] = "enabled" if current_status else "disabled"

        elif args.action == "enable":
            if current_status:
                result["message"] = "Bypass mode is already enabled"
            else:
                # Update .claude/settings.local.json
                claude_settings = enable_bypass(claude_settings)
                write_settings(claude_settings_path, claude_settings)
                # Update .vscode/settings.json
                vscode_settings = enable_vscode_bypass(vscode_settings)
                write_vscode_settings(vscode_settings_path, vscode_settings)
                result["current_status"] = True
                result["message"] = "Bypass mode enabled"

        elif args.action == "disable":
            if not current_status:
                result["message"] = "Bypass mode is already disabled"
            else:
                # Update .claude/settings.local.json
                claude_settings = disable_bypass(claude_settings)
                write_settings(claude_settings_path, claude_settings)
                # Update .vscode/settings.json
                vscode_settings = disable_vscode_bypass(vscode_settings)
                write_vscode_settings(vscode_settings_path, vscode_settings)
                result["current_status"] = False
                result["message"] = "Bypass mode disabled"

        elif args.action == "toggle":
            if current_status:
                claude_settings = disable_bypass(claude_settings)
                vscode_settings = disable_vscode_bypass(vscode_settings)
                result["current_status"] = False
                result["message"] = "Bypass mode disabled"
            else:
                claude_settings = enable_bypass(claude_settings)
                vscode_settings = enable_vscode_bypass(vscode_settings)
                result["current_status"] = True
                result["message"] = "Bypass mode enabled"
            write_settings(claude_settings_path, claude_settings)
            write_vscode_settings(vscode_settings_path, vscode_settings)

    except Exception as e:
        result["success"] = False
        result["message"] = str(e)

    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["success"] else 1


if __name__ == "__main__":
    sys.exit(main())
