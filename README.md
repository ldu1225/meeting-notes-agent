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

### 2. Authenticate with Google Cloud

Open a new terminal and run the following commands.

```bash
# 1. Authenticate with Google Cloud
# This will open a browser window for you to log in.
gcloud auth application-default login

# 2. Set your Project ID
# Replace "your-gcp-project-id" with your actual Google Cloud Project ID.
gcloud config set project your-gcp-project-id
```

### 3. Configure Projects

Set up both the backend and frontend.

```bash
# 1. Navigate to the project root
cd /path/to/your/meeting-notes-agent

# 2. Set up Backend Environment File
cd backend
cp .env.example .env
# Now, open the newly created '.env' file and add your Google Cloud Project ID.
cd ..

# 3. Install Backend Dependencies
cd backend
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
cd ..

# 4. Install Frontend Dependencies
cd frontend/adk-web
npm install
cd ../..
```

### 4. Run the Application

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

## 💡 4. How to Use

1.  From the "Tool to select" dropdown, choose `meeting_notes_agent`.
2.  **For general chat:** Type any text message and press enter.
3.  **To analyze an audio file:** Type the **full, absolute path** to your audio file (e.g., `/Users/yourname/Desktop/mymeeting.m4a`) and press enter.

---

## 🧑‍💻 5. Development with Gemini CLI

This project was bootstrapped and primarily developed using the **Gemini CLI**. It is the recommended tool for making modifications, adding features, or fixing bugs, as it understands the project's structure and conventions.

### Core Workflow

The agent follows a Test-Driven Development (TDD) methodology. When requesting a new feature, it's best practice to frame your request in a way that encourages writing tests first.

### Example Prompts

Here are some example prompts you can use with the Gemini CLI from the project's root directory:

**1. Running All Backend Tests:**
> Run all tests for the backend.

*(This will trigger the command: `./.venv/bin/pytest backend/`)*

**2. Adding a New Feature (Tool):**
> Create a new ADK tool in `backend/agents/meeting_notes_agent/tools/` named `summarizer.py`. It should have a function `summarize(text: str) -> str` that returns a one-sentence summary of the input text. Please follow TDD by creating `backend/tests/test_summarizer.py` first.

**3. Refactoring Existing Code:**
> Refactor the `file_saver.py` tool to handle `PermissionError` exceptions specifically and return a user-friendly error message. Also, add a test case for this scenario.

**4. Understanding the Code:**
> Explain the logic inside the `transcribe_audio` function in `backend/agents/meeting_notes_agent/tools/transcription.py`.
