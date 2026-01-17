#!/usr/bin/env python3
"""
AXEL Compact Script - Fast compact operations for memories.
Moves matching items from source file to target archive file.
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path


def read_file(file_path: Path) -> str:
    """Read file content."""
    if file_path.exists():
        return file_path.read_text(encoding="utf-8")
    return ""


def write_file(file_path: Path, content: str) -> bool:
    """Write content to file, creating parent directories if needed."""
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding="utf-8")
        return True
    except Exception:
        return False


def parse_filter(filter_str: str) -> list[tuple[str, str]]:
    """Parse filter string into list of (attr, value) tuples.

    Examples:
        "priority=normal,priority=low" -> [("priority", "normal"), ("priority", "low")]
        "status=completed" -> [("status", "completed")]
    """
    if not filter_str:
        return []

    filters = []
    for item in filter_str.split(","):
        if "=" in item:
            attr, value = item.split("=", 1)
            filters.append((attr.strip(), value.strip()))
    return filters


def extract_elements(content: str, tag: str) -> list[dict]:
    """Extract XML elements from markdown content.

    Returns list of dicts with:
        - full_match: Complete element string including tags
        - attrs: Dict of attributes
        - inner: Inner content
        - title: Extracted title if available
    """
    # Pattern to match <tag ...>...</tag> including nested content
    pattern = rf'<{tag}\s+([^>]*)>(.*?)</{tag}>'
    matches = re.findall(pattern, content, re.DOTALL)

    elements = []
    for attrs_str, inner in matches:
        # Parse attributes
        attrs = {}
        attr_pattern = r'(\w+)=["\']([^"\']*)["\']'
        for attr_match in re.finditer(attr_pattern, attrs_str):
            attrs[attr_match.group(1)] = attr_match.group(2)

        # Extract title/subject
        title = ""
        title_match = re.search(r'<title>([^<]+)</title>', inner)
        if title_match:
            title = title_match.group(1).strip()
        else:
            subject_match = re.search(r'<subject>([^<]+)</subject>', inner)
            if subject_match:
                title = subject_match.group(1).strip()

        # Reconstruct full match
        full_match = f'<{tag} {attrs_str}>{inner}</{tag}>'

        elements.append({
            "full_match": full_match,
            "attrs": attrs,
            "inner": inner,
            "title": title
        })

    return elements


def filter_elements(elements: list[dict], filters: list[tuple[str, str]]) -> list[dict]:
    """Filter elements by attribute values.

    OR logic: element matches if ANY filter condition is true.
    """
    if not filters:
        return elements

    matched = []
    for elem in elements:
        for attr, value in filters:
            if elem["attrs"].get(attr) == value:
                matched.append(elem)
                break  # OR logic - match any filter

    return matched


def remove_elements_from_content(content: str, elements: list[dict]) -> str:
    """Remove matched elements from content."""
    for elem in elements:
        # Remove the element and any surrounding whitespace/newlines
        pattern = re.escape(elem["full_match"])
        content = re.sub(rf'\n*{pattern}\n*', '\n', content)

    # Clean up multiple consecutive newlines
    content = re.sub(r'\n{3,}', '\n\n', content)
    return content.strip() + '\n'


def add_timestamp_attr(element: str, tag: str, attr_name: str, timestamp: str) -> str:
    """Add timestamp attribute to element."""
    # Add attribute to opening tag
    return re.sub(
        rf'<{tag}\s+',
        f'<{tag} {attr_name}="{timestamp}" ',
        element,
        count=1
    )


def compact_to_archive(
    source_file: Path,
    target_dir: Path,
    target_pattern: str,
    filter_str: str,
    element_tag: str
) -> dict:
    """Compact elements to timestamped archive file."""
    result = {
        "success": True,
        "mode": "archive",
        "source_file": str(source_file),
        "target_file": "",
        "items_found": 0,
        "items_moved": 0,
        "moved_items": [],
        "errors": []
    }

    # Read source
    content = read_file(source_file)
    if not content:
        result["errors"].append(f"Source file not found or empty: {source_file}")
        return result

    # Extract and filter elements
    elements = extract_elements(content, element_tag)
    result["items_found"] = len(elements)

    filters = parse_filter(filter_str)
    matched = filter_elements(elements, filters)

    if not matched:
        result["errors"].append("No items match the filter criteria")
        return result

    # Generate target filename
    now = datetime.now()
    target_filename = target_pattern.replace(
        "{YYYY-MM-DD-HHmm}",
        now.strftime("%Y-%m-%d-%H%M")
    )
    target_file = target_dir / target_filename
    result["target_file"] = str(target_file)

    # Prepare archive content
    timestamp = now.strftime("%Y-%m-%d %H:%M")
    archive_content = f"# Archived {element_tag}s - {timestamp}\n\n"

    for elem in matched:
        archived_elem = elem["full_match"]

        # Add archived timestamp to element
        archived_elem = add_timestamp_attr(
            archived_elem,
            element_tag,
            "archived",
            timestamp
        )
        archive_content += f"```xml\n{archived_elem}\n```\n\n"
        result["moved_items"].append({
            "title": elem["title"],
            **elem["attrs"]
        })

    # Write archive
    if not write_file(target_file, archive_content):
        result["success"] = False
        result["errors"].append(f"Failed to write archive: {target_file}")
        return result

    # Update source - remove matched elements
    updated_content = remove_elements_from_content(content, matched)
    if not write_file(source_file, updated_content):
        result["success"] = False
        result["errors"].append(f"Failed to update source: {source_file}")
        return result

    result["items_moved"] = len(matched)
    return result


def compact_to_index(
    source_file: Path,
    target_file: Path,
    filter_str: str,
    element_tag: str
) -> dict:
    """Compact elements to index file (append mode)."""
    result = {
        "success": True,
        "mode": "index",
        "source_file": str(source_file),
        "target_file": str(target_file),
        "items_found": 0,
        "items_moved": 0,
        "moved_items": [],
        "errors": []
    }

    # Read source
    content = read_file(source_file)
    if not content:
        result["errors"].append(f"Source file not found or empty: {source_file}")
        return result

    # Extract and filter elements
    elements = extract_elements(content, element_tag)
    result["items_found"] = len(elements)

    filters = parse_filter(filter_str)
    matched = filter_elements(elements, filters)

    if not matched:
        result["errors"].append("No items match the filter criteria")
        return result

    # Read existing target or create structure
    target_content = read_file(target_file)
    if not target_content:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        target_content = f"# Completed {element_tag}s\n\nLast updated: {timestamp}\n\n"

    # Append matched elements
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    for elem in matched:
        # Add compacted timestamp to element
        compacted_elem = add_timestamp_attr(
            elem["full_match"],
            element_tag,
            "compacted",
            timestamp
        )
        target_content += f"\n```xml\n{compacted_elem}\n```\n"
        result["moved_items"].append({
            "title": elem["title"],
            **elem["attrs"]
        })

    # Write target
    if not write_file(target_file, target_content):
        result["success"] = False
        result["errors"].append(f"Failed to write target: {target_file}")
        return result

    # Update source - remove matched elements
    updated_content = remove_elements_from_content(content, matched)
    if not write_file(source_file, updated_content):
        result["success"] = False
        result["errors"].append(f"Failed to update source: {source_file}")
        return result

    result["items_moved"] = len(matched)
    return result


def main():
    parser = argparse.ArgumentParser(description="AXEL Compact Script")
    parser.add_argument(
        "--action",
        required=True,
        choices=["memories-session", "memories-learned"],
        help="Compact action type"
    )
    parser.add_argument("--source-file", required=True, help="Source file path")
    parser.add_argument("--target-file", help="Target file path (index mode)")
    parser.add_argument("--target-dir", help="Target directory (archive mode)")
    parser.add_argument("--target-pattern", help="Target filename pattern (archive mode)")
    parser.add_argument("--filter", default="", help="Filter criteria (e.g., priority=normal,priority=low)")
    parser.add_argument("--element-tag", required=True, help="XML element tag (memory)")
    parser.add_argument("--cwd", default=".", help="Working directory")

    args = parser.parse_args()

    base_path = Path(args.cwd).resolve()
    source_file = base_path / args.source_file

    # Determine mode and execute
    if args.target_dir:
        # Archive mode (for memories)
        target_dir = base_path / args.target_dir
        result = compact_to_archive(
            source_file=source_file,
            target_dir=target_dir,
            target_pattern=args.target_pattern or f"{args.element_tag}-{{YYYY-MM-DD-HHmm}}.md",
            filter_str=args.filter,
            element_tag=args.element_tag
        )
    elif args.target_file:
        # Index mode
        target_file = base_path / args.target_file
        result = compact_to_index(
            source_file=source_file,
            target_file=target_file,
            filter_str=args.filter,
            element_tag=args.element_tag
        )
    else:
        result = {
            "success": False,
            "errors": ["Either --target-file or --target-dir must be specified"]
        }

    # Add action to result
    result["action"] = args.action

    # Output JSON
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["success"] else 1


if __name__ == "__main__":
    sys.exit(main())
