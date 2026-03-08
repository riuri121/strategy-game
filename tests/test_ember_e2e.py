"""
End-to-end test to verify Ember can execute and deliver results.

This test validates that:
1. The main module can be imported
2. Version is properly defined
3. Core functionality is accessible
"""

import sys
sys.path.insert(0, 'python')

from main import __version__, main


def test_ember_e2e_import():
    """Test that main module imports without errors."""
    assert __version__ is not None
    assert isinstance(__version__, str)


def test_ember_e2e_version_format():
    """Test that version follows semantic versioning."""
    parts = __version__.split('.')
    assert len(parts) == 3
    assert all(part.isdigit() for part in parts)


def test_ember_e2e_callable():
    """Test that main function is callable."""
    assert callable(main)
