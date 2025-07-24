import pytest
from meeting_notes_agent.tools.transcription import transcribe_audio

def test_transcribe_audio_success(mocker):
    # Mock the speech-to-text API call
    mocker.patch(
        'meeting_notes_agent.tools.transcription.speech.SpeechClient.recognize',
        return_value=mocker.MagicMock(
            results=[
                mocker.MagicMock(
                    alternatives=[
                        mocker.MagicMock(transcript='This is a test transcription.')
                    ]
                )
            ]
        )
    )
    mocker.patch('builtins.open', mocker.mock_open(read_data=b'fake audio data'))

    transcription = transcribe_audio('fake_audio.mp3')
    assert transcription == 'This is a test transcription.'

def test_transcribe_audio_file_not_found():
    with pytest.raises(FileNotFoundError):
        transcribe_audio('non_existent_file.mp3')
