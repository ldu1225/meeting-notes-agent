from google.adk.agents import Agent
from meeting_notes_agent.tools.transcription import transcribe_audio
from meeting_notes_agent.tools.notes_generator import generate_meeting_notes
from meeting_notes_agent.tools.file_saver import save_notes_to_file

class MeetingNotesAgent(Agent):
    def __init__(self):
        super().__init__(
            name='MeetingNotesAgent',
            model='gemini-2.5-pro',
            tools=[
                transcribe_audio,
                generate_meeting_notes,
                save_notes_to_file,
            ]
        )

    def process_meeting_audio(self, audio_file_path: str) -> str:
        transcribed_text = transcribe_audio(audio_file_path)
        meeting_notes_markdown = generate_meeting_notes(transcribed_text)
        file_path = save_notes_to_file(meeting_notes_markdown)
        return f"Meeting notes saved to {file_path}"

root_agent = MeetingNotesAgent()