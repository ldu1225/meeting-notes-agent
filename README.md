# Meeting Notes Agent Suite 🎙️📝

This repository contains the complete suite for the Meeting Notes Agent, including the Python-based ADK agent (`backend`) and the Angular-based web interface (`frontend`).

---

## 🏛️ Project Structure

```
/
├── backend/          # The Google ADK Agent project
│   ├── agents/
│   └── ...
└── frontend/         # The adk-web project (Angular UI)
    ├── src/
    └── ...
```

---

## ✨ Features

-   **Monorepo Structure:** Backend and frontend projects managed in a single, easy-to-navigate repository.
-   **Multi-format Audio Transcription:** Leverages Google's Speech-to-Text API to transcribe various audio formats.
-   **Intelligent Note Generation:** Uses a powerful LLM to summarize the transcribed text into key points, action items, and decisions.
-   **Interactive Web UI:** Provides a user-friendly web interface for interaction.
-   **Robust Error Handling:** Clearly communicates issues, such as missing dependencies (`ffmpeg`) or authentication problems.

---

## 🚀 A to Z Deployment Guide

Follow these steps to get the entire suite running from scratch on a new macOS system.

### 1. Install System Dependencies

Open a new terminal and run the following commands.

```bash
# 1. Install Homebrew (if you don't have it)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. Install FFmpeg for audio processing
brew install ffmpeg

# 3. Install the Google Cloud SDK
brew install --cask google-cloud-sdk

# 4. Authenticate with Google Cloud
# This will open a browser window for you to log in.
gcloud auth application-default login
```

### 2. Configure Projects

Set up both the backend and frontend.

```bash
# 1. Navigate to the project root
cd /path/to/your/meeting-notes-suite

# 2. Set up the Backend
cd backend
python3 -m venv .venv
./.venv/bin/pip install google-adk pydub soundfile
cd ..

# 3. Set up the Frontend
cd frontend
npm install
sudo npm install -g @angular/cli # Admin password required
cd ..
```

### 3. Run the Application

You will need **two separate terminal windows** to run the servers.

**Terminal 1: Start the Backend**

```bash
# Navigate to the backend directory
cd /path/to/your/meeting-notes-suite/backend

# Run the ADK API server
./.venv/bin/adk api_server agents --session_service_uri="sqlite:///sessions.db" --allow_origins=http://localhost:4200 --host=0.0.0.0
```

**Terminal 2: Start the Frontend**

```bash
# Navigate to the frontend directory
cd /path/to/your/meeting-notes-suite/frontend

# Start the web server
ng serve
```

### 4. Access the Agent

Once both servers are running, open your web browser and navigate to:

**[http://localhost:4200](http://localhost:4200)**

---

## 💡 How to Use

1.  From the "Tool to select" dropdown, choose `meeting_notes_agent`.
2.  **For general chat:** Type any text message and press enter.
3.  **To analyze an audio file:** Type the **full, absolute path** to your audio file (e.g., `/Users/yourname/Desktop/mymeeting.m4a`) and press enter.
