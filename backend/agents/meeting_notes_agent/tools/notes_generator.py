import google.generativeai as genai

def generate_meeting_notes(transcription: str) -> str:
    """Generates meeting notes from a transcription."""
    if not transcription:
        return 'No transcription provided to generate notes.'

    model = genai.GenerativeModel('gemini-2.5-pro')
    prompt = f"""
Please generate meeting notes from the following transcription.
The notes should be in markdown format and include the following sections:
- A brief summary of the meeting.
- A list of action items.
- A list of key decisions made.

Transcription:
{transcription}
"""
    response = model.generate_content(prompt)
    return response.text
