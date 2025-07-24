import pytest
from meeting_notes_agent.agent import MeetingNotesAgent

def test_process_meeting_audio(mocker):
    # Mock the tools
    mock_transcribe = mocker.patch(
        'meeting_notes_agent.agent.transcribe_audio',
        return_value='This is a test transcription.'
    )
    mock_generate_notes = mocker.patch(
        'meeting_notes_agent.agent.generate_meeting_notes',
        return_value='# Meeting Notes'
    )
    mock_save_notes = mocker.patch(
        'meeting_notes_agent.agent.save_notes_to_file',
        return_value='meeting_20250724_120000.md'
    )

    agent = MeetingNotesAgent()
    result = agent.process_meeting_audio('fake_audio.mp3')

    mock_transcribe.assert_called_once_with('fake_audio.mp3')
    mock_generate_notes.assert_called_once_with('This is a test transcription.')
    mock_save_notes.assert_called_once_with('# Meeting Notes')
    assert result == "Meeting notes saved to meeting_20250724_120000.md"
