"""
Basic tests for Python components
"""

import sys
sys.path.insert(0, 'python')

from main import __version__


def test_version():
    """Test that version is defined."""
    assert __version__ == "0.1.0"
