#!/usr/bin/env python3
"""
LIFTS Static Site Generator

Reads site data from assets/data/site-data.md (YAML front matter) and replaces
{{ key.path }} placeholders in HTML files. Also generates scripts/site-data.js
for JavaScript access to the data.

Usage:
    python build.py              # Build site (in-place replacement)
    python build.py --dry-run    # Preview changes without writing
    python build.py --verbose    # Show detailed replacement info
    python build.py --validate   # Only validate, don't write changes
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("Error: PyYAML is required. Install with: pip install pyyaml")
    sys.exit(1)


# =============================================================================
# Configuration
# =============================================================================

REPO_ROOT = Path(__file__).parent
DATA_FILE = REPO_ROOT / "assets" / "data" / "site-data.md"
JS_OUTPUT = REPO_ROOT / "scripts" / "site-data.js"

# HTML files to process (relative to repo root)
HTML_FILES = [
    "index.html",
    "ascent.html",
    "missions.html",
    "launches.html",
    "nexo.html",
    "cubesat.html",
    "about.html",
    "contact.html",
    "careers.html",
    "updates.html",
    "contributors.html",
    "privacy.html",
]

# Placeholder pattern: {{ key.path.to.value }}
PLACEHOLDER_PATTERN = re.compile(r"\{\{\s*([\w.]+)\s*\}\}")


# =============================================================================
# Data Loading
# =============================================================================

def load_site_data(data_file: Path) -> dict:
    """Load and parse YAML front matter from the data file."""
    if not data_file.exists():
        print(f"Error: Data file not found: {data_file}")
        sys.exit(1)

    content = data_file.read_text(encoding="utf-8")

    # Extract YAML front matter (between --- delimiters at start of line)
    if not content.startswith("---"):
        print(f"Error: Data file must start with YAML front matter (---)")
        sys.exit(1)

    # Find the closing --- that's at the start of a line (not in a comment)
    lines = content.split('\n')
    start_line = 1  # Skip the opening ---
    end_line = None
    
    for i, line in enumerate(lines[1:], start=1):
        # Match --- at start of line (possibly with trailing whitespace)
        if line.strip() == '---':
            end_line = i
            break
    
    if end_line is None:
        print(f"Error: No closing --- found for YAML front matter")
        sys.exit(1)

    yaml_content = '\n'.join(lines[start_line:end_line])

    try:
        data = yaml.safe_load(yaml_content)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        sys.exit(1)

    if not isinstance(data, dict):
        print(f"Error: YAML front matter must be a dictionary")
        sys.exit(1)

    return data


def get_nested_value(data: dict, key_path: str) -> Any:
    """
    Get a value from a nested dictionary using dot notation.
    Returns None if the key path doesn't exist.
    """
    keys = key_path.split(".")
    value = data

    for key in keys:
        if isinstance(value, dict) and key in value:
            value = value[key]
        else:
            return None

    return value


def flatten_dict(d: dict, parent_key: str = "", sep: str = ".") -> dict:
    """Flatten a nested dictionary into dot-notation keys."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def count_data_keys(data: dict) -> int:
    """Count total number of leaf keys in nested dict."""
    return len(flatten_dict(data))


# =============================================================================
# Validation
# =============================================================================

def find_placeholders(content: str) -> list[str]:
    """Find all {{ key.path }} placeholders in content."""
    return PLACEHOLDER_PATTERN.findall(content)


def validate_placeholders(
    html_files: list[Path],
    data: dict,
    verbose: bool = False
) -> tuple[dict[str, list[str]], set[str], set[str]]:
    """
    Validate all placeholders in HTML files against the data.

    Returns:
        - file_placeholders: dict mapping file path to list of placeholders
        - missing_keys: set of placeholder keys not found in data
        - used_keys: set of all keys used in placeholders
    """
    file_placeholders = {}
    missing_keys = set()
    used_keys = set()

    for html_file in html_files:
        if not html_file.exists():
            if verbose:
                print(f"  Skipping (not found): {html_file.name}")
            continue

        content = html_file.read_text(encoding="utf-8")
        placeholders = find_placeholders(content)

        if placeholders:
            file_placeholders[str(html_file)] = placeholders
            used_keys.update(placeholders)

            for key in placeholders:
                value = get_nested_value(data, key)
                if value is None:
                    missing_keys.add(key)

    return file_placeholders, missing_keys, used_keys


def find_unused_keys(data: dict, used_keys: set[str]) -> set[str]:
    """Find data keys that are defined but never used in placeholders."""
    all_keys = set(flatten_dict(data).keys())
    return all_keys - used_keys


# =============================================================================
# Processing
# =============================================================================

def replace_placeholders(
    content: str,
    data: dict,
    verbose: bool = False,
    file_name: str = ""
) -> tuple[str, int]:
    """
    Replace all {{ key.path }} placeholders with values from data.

    Returns:
        - Modified content
        - Count of replacements made
    """
    count = 0

    def replacer(match):
        nonlocal count
        key_path = match.group(1)
        value = get_nested_value(data, key_path)

        if value is not None:
            count += 1
            str_value = str(value)
            if verbose:
                print(f"    {key_path} → {str_value[:50]}{'...' if len(str_value) > 50 else ''}")
            return str_value
        else:
            # Leave placeholder unchanged if key not found
            if verbose:
                print(f"    WARNING: {key_path} not found in data")
            return match.group(0)

    new_content = PLACEHOLDER_PATTERN.sub(replacer, content)
    return new_content, count


def generate_js_data(data: dict) -> str:
    """Generate JavaScript file with site data for client-side use."""
    js_content = """/**
 * LIFTS Site Data
 * Auto-generated by build.py - DO NOT EDIT DIRECTLY
 * Edit assets/data/site-data.md instead and run: python build.py
 */

window.SITE_DATA = %s;
""" % json.dumps(data, indent=2, ensure_ascii=False)

    return js_content


# =============================================================================
# Main
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="LIFTS Static Site Generator - Replace placeholders with site data"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without writing files"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show detailed replacement info"
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Only validate placeholders, don't make changes"
    )
    args = parser.parse_args()

    print("=" * 60)
    print("LIFTS Static Site Generator")
    print("=" * 60)

    # Load site data
    print(f"\n📂 Loading data from: {DATA_FILE.relative_to(REPO_ROOT)}")
    data = load_site_data(DATA_FILE)
    print(f"   ✓ Loaded {count_data_keys(data)} data keys")

    # Resolve HTML file paths
    html_paths = [REPO_ROOT / f for f in HTML_FILES]

    # Validate placeholders
    print(f"\n🔍 Validating placeholders in {len(HTML_FILES)} HTML files...")
    file_placeholders, missing_keys, used_keys = validate_placeholders(
        html_paths, data, verbose=args.verbose
    )

    # Report validation results
    total_placeholders = sum(len(p) for p in file_placeholders.values())
    print(f"   Found {total_placeholders} placeholders in {len(file_placeholders)} files")

    if missing_keys:
        print(f"\n❌ ERROR: {len(missing_keys)} placeholder key(s) not found in data:")
        for key in sorted(missing_keys):
            print(f"   • {key}")
        if not args.dry_run:
            print("\n   Fix the missing keys in site-data.md or remove invalid placeholders.")
            sys.exit(1)

    # Check for unused keys (informational)
    unused_keys = find_unused_keys(data, used_keys)
    if unused_keys and args.verbose:
        print(f"\n📋 Info: {len(unused_keys)} data key(s) defined but not used:")
        for key in sorted(unused_keys)[:10]:  # Show first 10
            print(f"   • {key}")
        if len(unused_keys) > 10:
            print(f"   ... and {len(unused_keys) - 10} more")

    if args.validate:
        print("\n✓ Validation complete (--validate mode, no changes made)")
        sys.exit(0 if not missing_keys else 1)

    # Process HTML files
    print(f"\n{'📝 Preview of changes:' if args.dry_run else '✏️  Updating HTML files:'}")

    total_replacements = 0
    files_modified = 0

    for html_file in html_paths:
        if not html_file.exists():
            continue

        content = html_file.read_text(encoding="utf-8")
        placeholders = find_placeholders(content)

        if not placeholders:
            continue

        if args.verbose:
            print(f"\n  {html_file.name}:")

        new_content, count = replace_placeholders(
            content, data, verbose=args.verbose, file_name=html_file.name
        )

        if count > 0:
            total_replacements += count
            files_modified += 1

            if not args.dry_run:
                html_file.write_text(new_content, encoding="utf-8")
                if not args.verbose:
                    print(f"   ✓ {html_file.name}: {count} replacement(s)")
            else:
                if not args.verbose:
                    print(f"   → {html_file.name}: {count} replacement(s)")

    # Generate JavaScript data file
    print(f"\n{'📝 Would generate:' if args.dry_run else '✏️  Generating:'} {JS_OUTPUT.relative_to(REPO_ROOT)}")

    js_content = generate_js_data(data)
    if not args.dry_run:
        JS_OUTPUT.write_text(js_content, encoding="utf-8")
        print(f"   ✓ Generated site-data.js ({len(js_content)} bytes)")
    else:
        print(f"   → Would generate site-data.js ({len(js_content)} bytes)")

    # Summary
    print("\n" + "=" * 60)
    if args.dry_run:
        print(f"DRY RUN COMPLETE")
        print(f"Would make {total_replacements} replacement(s) in {files_modified} file(s)")
    else:
        print(f"BUILD COMPLETE")
        print(f"Made {total_replacements} replacement(s) in {files_modified} file(s)")
    print("=" * 60)


if __name__ == "__main__":
    main()
