import os
import soundfile as sf
from pydub import AudioSegment
from google.cloud import speech

def transcribe_audio(audio_file_path: str) -> str:
    """
    Transcribes an audio file using Google Cloud Speech-to-Text.
    - Handles WAV files directly and robustly.
    - Attempts to convert other formats (like M4A, MP3) using pydub,
      which requires ffmpeg to be installed on the system.
    """
    if not os.path.exists(audio_file_path):
        raise FileNotFoundError(f"File not found at path: {audio_file_path}")

    file_to_process = audio_file_path
    temp_wav_path = None
    is_temp_file = False

    # If not a WAV file, try to convert it
    if not audio_file_path.lower().endswith('.wav'):
        try:
            sound = AudioSegment.from_file(audio_file_path)
            if len(sound) == 0:
                return "The provided audio file appears to be empty."

            temp_wav_path = "temp_conversion.wav"
            sound.export(temp_wav_path, format="wav")
            file_to_process = temp_wav_path
            is_temp_file = True

        except Exception as e:
            error_message = (
                f"Failed to convert '{os.path.basename(audio_file_path)}'. "
                f"This usually means the required 'ffmpeg' library is not installed on your system. "
                f"Please install ffmpeg and try again. Original error: {e}"
            )
            return error_message

    # Now, process the WAV file (either original or temporary)
    try:
        info = sf.info(file_to_process)
        sample_rate = info.samplerate
        channels = info.channels

        with open(file_to_process, "rb") as audio_file:
            content = audio_file.read()
            if not content:
                return "The WAV file content is empty."

    except Exception as e:
        return f"Error reading WAV file '{os.path.basename(file_to_process)}': {e}. It might be corrupted."
    finally:
        # Clean up the temporary file if one was created
        if is_temp_file and temp_wav_path and os.path.exists(temp_wav_path):
            os.remove(temp_wav_path)

    # Proceed with Google Cloud Speech-to-Text
    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=sample_rate,
        language_code="en-US",
        audio_channel_count=channels,
    )

    try:
        response = client.recognize(config=config, audio=audio)
        if response.results:
            return "".join(result.alternatives[0].transcript for result in response.results)
        return "Could not transcribe the audio. The file might be silent or contain unsupported speech."
    except Exception as e:
        return f"Google Speech-to-Text API error: {e}"
