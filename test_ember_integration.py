#!/usr/bin/env python3
"""
Ember integration test for strategy-game repo.

This test validates that Ember can:
- Access the repository
- Execute commands
- Create and modify files
- Work with git operations
"""

import os
import sys


def test_repo_exists():
    """Verify the repository exists and is accessible."""
    assert os.path.exists('.git'), "Repository must be a git repo"
    assert os.path.exists('README.md'), "README.md should exist"


def test_ember_can_write():
    """Verify Ember can write to the repository."""
    test_file = '.ember_test_marker'
    try:
        with open(test_file, 'w') as f:
            f.write("Ember was here\n")
        assert os.path.exists(test_file), "Test file should exist"
        with open(test_file, 'r') as f:
            content = f.read()
        assert "Ember was here" in content, "Content should match"
        print("✓ Ember can write files")
    finally:
        if os.path.exists(test_file):
            os.remove(test_file)


def test_repo_structure():
    """Verify expected repo structure."""
    assert os.path.exists('design'), "Design directory should exist"
    print("✓ Repository structure is valid")


if __name__ == '__main__':
    try:
        test_repo_exists()
        print("✓ Repository accessibility verified")
        
        test_ember_can_write()
        
        test_repo_structure()
        
        print("\n✓ All Ember validation tests passed!")
        sys.exit(0)
    except AssertionError as e:
        print(f"✗ Test failed: {e}")
        sys.exit(1)
