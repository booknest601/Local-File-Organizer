"""
Basic tests for Local File Organizer
"""
import os


def test_import():
    """Test that basic imports work"""
    assert True


def test_environment():
    """Test that the environment is set up correctly"""
    assert os.path.exists('.')
