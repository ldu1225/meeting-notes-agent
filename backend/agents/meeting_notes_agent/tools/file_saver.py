import datetime

def save_notes_to_file(notes: str) -> str:
    """Saves notes to a timestamped markdown file."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"meeting_{timestamp}.md"
    with open(file_path, "w") as f:
        f.write(notes)
    return file_path
