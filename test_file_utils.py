import pytest
import os
from data_processing_common import sanitize_filename

def test_sanitize_filename():
    """Test filename sanitization."""
    # Test basic sanitization
    result = sanitize_filename("Test File Name.txt", max_length=50, max_words=5)
    assert result == "test_file_name"
    
    # Test with special characters
    result = sanitize_filename("My-File@Name#123!", max_length=50, max_words=5)
    assert "my" in result
    assert "@" not in result
    assert "#" not in result

def test_sanitize_filename_max_words():
    """Test word limit in filename sanitization."""
    result = sanitize_filename("one two three four five six seven", max_words=3)
    words = result.split('_')
    assert len(words) <= 3

def test_sanitize_filename_max_length():
    """Test length limit in filename sanitization."""
    long_name = "a" * 100
    result = sanitize_filename(long_name, max_length=50, max_words=5)
    assert len(result) <= 50

def test_sanitize_filename_empty():
    """Test empty filename returns 'untitled'."""
    result = sanitize_filename("", max_length=50, max_words=5)
    assert result == "untitled"

def test_sanitize_filename_removes_unwanted_words():
    """Test that common unwanted words are removed."""
    result = sanitize_filename("image photo the document text", max_length=50, max_words=5)
    # All words should be filtered out, resulting in 'untitled'
    assert result == "untitled"
