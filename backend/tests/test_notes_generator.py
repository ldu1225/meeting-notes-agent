import pytest
from meeting_notes_agent.tools.notes_generator import generate_meeting_notes

def test_generate_meeting_notes_success(mocker):
    # Mock the generative AI API call
    mock_generative_model = mocker.MagicMock()
    mock_generative_model.generate_content.return_value.text = """# Meeting Notes

## Summary
This is a test summary.

## Action Items
- Test action item 1
- Test action item 2

## Decisions
- Test decision 1"""
    mocker.patch(
        'meeting_notes_agent.tools.notes_generator.genai.GenerativeModel',
        return_value=mock_generative_model
    )

    notes = generate_meeting_notes('This is a test transcription.')
    assert '# Meeting Notes' in notes
    assert '## Summary' in notes
    assert '## Action Items' in notes
    assert '## Decisions' in notes

def test_generate_meeting_notes_empty_input():
    notes = generate_meeting_notes('')
    assert notes == 'No transcription provided to generate notes.'
