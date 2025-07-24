import os
import pytest
from meeting_notes_agent.tools.file_saver import save_notes_to_file

def test_save_notes_to_file_success():
    notes = """# Meeting Notes

## Summary
This is a test summary."""
    file_path = save_notes_to_file(notes)
    assert os.path.exists(file_path)
    with open(file_path, 'r') as f:
        content = f.read()
        assert content == notes
    os.remove(file_path)

def test_save_notes_to_file_creation_and_content():
    notes = "Test content"
    file_path = save_notes_to_file(notes)
    assert os.path.isfile(file_path)
    with open(file_path, 'r') as f:
        assert f.read() == "Test content"
    os.remove(file_path)
