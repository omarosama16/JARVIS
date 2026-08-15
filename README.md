# 🤖 PROJECT JARVIS

> A Python-based desktop voice assistant inspired by JARVIS from Iron Man.

PROJECT JARVIS is a Windows desktop voice assistant built with Python. It uses speech recognition and text-to-speech to listen for voice commands, respond naturally, and perform useful actions on the computer.

The project is being developed incrementally, with each version adding new capabilities and improving the assistant's intelligence and usability.

---

## ✨ Features

### 🎙️ Voice Interaction
- Voice command recognition
- Text-to-speech responses
- "Jarvis" wake word
- Automatic speech detection
- Silence detection
- Feminine voice selection when available

### 💻 Desktop Control
- Open Firefox
- Open Visual Studio Code
- Open Spotify
- Open File Explorer
- Open Desktop
- Open Downloads

### 🌐 Web
- Google search
- YouTube search

### 🕐 Information
- Current time
- Current date

### 🛑 Control
- Voice-controlled shutdown
- Exit commands such as:
  - "Exit"
  - "Goodbye"
  - "Shutdown"
  - "Quit"

---

## 🛠️ Technologies

- **Python 3**
- **SpeechRecognition**
- **SoundDevice**
- **NumPy**
- **pyttsx3**
- **Webbrowser**
- **Windows subprocess / OS APIs**

---

## 📁 Project Structure

```text
PROJECT-JARVIS/
│
├── main.py              # Main program and command handling
├── voice.py             # Speech recognition and text-to-speech
├── commands.py          # Desktop and web commands
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── .gitignore           # Ignored files

```
---

## ⚙️ Installation
### 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/PROJECT-JARVIS.git
### 2. Navigate to the project
cd PROJECT-JARVIS
### 3. Create a virtual environment
python -m venv venv
### 4. Activate the virtual environment

Windows PowerShell:

.\venv\Scripts\Activate.ps1

Windows Command Prompt:

venv\Scripts\activate
### 5. Install dependencies
pip install -r requirements.txt

---
## ▶️ Usage

Start JARVIS with:

python main.py

Once JARVIS starts, say:

"Jarvis"

JARVIS will respond:

"Yes, sir."

You can then give it a command.

### Example Commands
"Open Firefox"


"Open Visual Studio Code"


"Open Spotify"


"Open Downloads"


"Open File Explorer"


"What time is it?"


"What date is it?"


"Search Google for Python tutorials"


"Search YouTube for lo-fi music"


"Goodbye"

---
🧠 How It Works

JARVIS is divided into three main components:

voice.py

Responsible for:

Microphone input
Speech detection
Speech recognition
Text-to-speech
Wake-word detection
commands.py

Responsible for executing actions such as:

Launching applications
Opening folders
Performing web searches
Getting the current time
Getting the current date
main.py

Acts as the central controller.

It:

Waits for the wake word.
Activates JARVIS.
Listens for a command.
Processes the command.
Executes the appropriate action.
Returns to the waiting state.
             ┌───────────────┐
             │   Microphone  │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │    voice.py   │
             │ Speech → Text │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │    main.py    │
             │Command Handler│
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │  commands.py  │
             │ Execute Action│
             └───────┬───────┘
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       Firefox    Spotify    Web Search
🖥️ Platform

Currently designed for:

Windows

Some commands rely on Windows-specific applications, paths, and system behavior.

🚧 Roadmap

PROJECT JARVIS is being developed in multiple versions.

V1.0 — Voice Assistant
 Voice recognition
 Wake word
 Text-to-speech
 Open applications
 Open folders
 Google search
 YouTube search
 Time and date
 Voice shutdown
V1.1 — Smarter Commands
 Natural language commands
 More application support
 Better command recognition
 Improved error handling
 System information
 Battery status
 CPU and RAM monitoring
V1.2 — Automation
 Volume control
 Media controls
 Screenshot commands
 Window management
 File operations
 More Windows automation
V2.0 — AI Assistant
 AI integration
 Natural conversations
 Context awareness
 Memory
 More advanced automation
 GUI
 Custom personality
