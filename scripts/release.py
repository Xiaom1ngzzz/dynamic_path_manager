#!/usr/bin/env python3
"""
Release script for Dynamic Path Manager.
"""

import os
import sys
import subprocess
import re
from pathlib import Path


def run_command(cmd, check=True):
    """Run a command and return the result."""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"Error: {result.stderr}")
        sys.exit(1)
    return result


def get_current_version():
    """Get the current version from __init__.py."""
    init_file = Path("src/dynamic_path_manager/__init__.py")
    with open(init_file) as f:
        content = f.read()
    match = re.search(r'__version__ = ["\']([^"\']+)["\']', content)
    if match:
        return match.group(1)
    raise ValueError("Could not find version in __init__.py")


def update_version(new_version):
    """Update version in __init__.py and pyproject.toml."""
    # Update __init__.py
    init_file = Path("src/dynamic_path_manager/__init__.py")
    with open(init_file) as f:
        content = f.read()
    content = re.sub(
        r'__version__ = ["\'][^"\']+["\']',
        f'__version__ = "{new_version}"',
        content
    )
    with open(init_file, 'w') as f:
        f.write(content)

    # Update pyproject.toml
    pyproject_file = Path("pyproject.toml")
    with open(pyproject_file) as f:
        content = f.read()
    content = re.sub(
        r'version = "[^"]+"',
        f'version = "{new_version}"',
        content
    )
    with open(pyproject_file, 'w') as f:
        f.write(content)

    print(f"Updated version to {new_version}")


def main():
    """Main release process."""
    if len(sys.argv) != 2:
        print("Usage: python scripts/release.py <new_version>")
        print("Example: python scripts/release.py 1.1.0")
        sys.exit(1)

    new_version = sys.argv[1]
    current_version = get_current_version()

    print(f"Current version: {current_version}")
    print(f"New version: {new_version}")

    # Confirm
    response = input("Continue with release? (y/N): ")
    if response.lower() != 'y':
        print("Release cancelled")
        sys.exit(0)

    # Update version
    update_version(new_version)

    # Run tests
    print("Running tests...")
    run_command("python3 -m pytest")

    # Build package
    print("Building package...")
    run_command("python3 -m build")

    # Check package
    print("Checking package...")
    run_command("twine check dist/*")

    # Commit changes
    print("Committing changes...")
    run_command(f"git add .")
    run_command(f"git commit -m 'Release version {new_version}'")
    run_command(f"git tag v{new_version}")

    print(f"Release {new_version} ready!")
    print("Next steps:")
    print("1. Push to GitHub: git push origin main --tags")
    print("2. Upload to PyPI: twine upload dist/*")
    print("3. Create GitHub release with release notes")


if __name__ == "__main__":
    main()
