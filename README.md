# JARVIS

### Modular Desktop Voice Assistant for Windows

JARVIS is a Python-based desktop voice assistant designed to interact with a Windows computer through natural voice commands.

Version 1.1 focuses on modular command architecture, reliable command routing, web search capabilities, and real-time system intelligence.
 
---

## Features

### Voice Interaction  

- Wake-word detection
- Speech recognition
- Text-to-speech responses
- Intent-based command routing
- Empty-command handling
- Unknown-command handling

### Application Control

JARVIS can launch:

- Mozilla Firefox
- Spotify
- Visual Studio Code

### File & Windows Navigation

JARVIS can open:

- Desktop
- Downloads
- File Explorer

### Web Search

JARVIS supports:

- Google searches
- YouTube searches
- Natural search-query extraction

Example commands:

- Search Google for Python tutorials
- Google how to learn Python
- Search YouTube for coding music
- YouTube coding music

### System Intelligence

JARVIS can provide real-time information about the computer:

- Current time
- Current date
- CPU usage
- RAM usage
- Battery level
- Charging status
- Operating system information

Example commands:

- What is my CPU usage?
- How much RAM am I using?
- What is my battery level?
- Am I charging?
- What system am I running?

---

## Architecture

JARVIS follows a modular command-processing architecture.

                    JARVIS
                       |
                       v
                 Voice Input
                       |
                       v
                    main.py
                       |
                       v
                 Command Router
                       |
                       v
                  Intent Detection
                       |
          +------------+------------+
          |            |            |
          v            v            v
       Commands       Files        Web
          |            |            |
          v            v            v
       Apps/System   Windows    Google/YouTube
                       |
                       v
                    Response
                       |
                       v
                 Voice Output

The project separates command detection from command execution, making the system easier to maintain and extend.

---

## Project Structure

```text
PROJECT JARVIS/
│
├── commands/
│   ├── __init__.py
│   ├── apps.py
│   ├── files.py
│   ├── system.py
│   └── web.py
│
├── core/
│   ├── __init__.py
│   └── router.py
│
├── utils/
│   ├── __init__.py
│   └── query.py
│
├── main.py
├── voice.py
│
├── test_router.py
├── test_query.py
├── test_commands.py
│
├── requirements.txt
├── README.md
└── .gitignore
```
---

## How It Works

JARVIS processes commands through several stages:

### 1. Voice Input

The microphone captures the user's speech.

Example:

"What is my CPU usage?"

### 2. Speech Recognition

The speech is converted into text.

what is my cpu usage

### 3. Intent Detection

The router identifies the user's intention.

cpu

### 4. Command Execution

The appropriate command module is called.

system.tell_cpu_usage()

### 5. System Data

JARVIS retrieves the requested information using the appropriate system module.

### 6. Voice Response

JARVIS responds using text-to-speech.

"Current CPU usage is 24 percent, sir."

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| SpeechRecognition | Speech-to-text |
| pyttsx3 | Text-to-speech |
| sounddevice | Audio input |
| NumPy | Audio processing |
| psutil | System monitoring |
| PyAudioWPatch | Windows audio support |
| Webbrowser | Web search integration |

---

## Installation

### 1. Download the Repository

Download the project and open a terminal inside the project directory.

    cd "PROJECT JARVIS"

### 2. Create a Virtual Environment

    python -m venv venv

Activate it:

    .\venv\Scripts\Activate.ps1

### 3. Install Dependencies

    python -m pip install -r requirements.txt

---

## Running JARVIS

Start the assistant with:

    python main.py

JARVIS will start with:

    JARVIS online and ready.

The assistant will then wait for the configured wake word.

---

## Example Commands

### General

    Hello
    Hi
    How are you?
    What time is it?
    What is today's date?

### Applications

    Open Firefox
    Launch Firefox
    Open Spotify
    Launch Spotify
    Open VS Code

### Files

    Open Desktop
    Open Downloads
    Open File Explorer

### Google

    Search Google for Python tutorials
    Google how to learn Python
    Search Google Python projects

### YouTube

    Search YouTube for coding music
    YouTube coding music
    Find on YouTube Python tutorials

### System

    What is my CPU usage?
    How much RAM am I using?
    What is my battery level?
    Am I charging?
    What system am I running?

### Exit

    Goodbye
    Exit
    Shutdown
    Quit

---

## Testing

JARVIS includes separate test files for different parts of the application.

### Router Testing

Tests command-to-intent detection.

    python test_router.py

### Query Testing

Tests Google and YouTube query extraction.

    python test_query.py

### Command Testing

Tests the actual command modules.

    python test_commands.py

Note: test_commands.py executes real actions such as opening applications, folders, and web browsers.

---

## V1.1 Improvements

Version 1.1 introduced a major architectural improvement over the original implementation.

### Original Architecture

    main.py
       |
       v
    commands.py

### V1.1 Architecture

    main.py
       |
       v
    core/router.py
       |
       +-- commands/apps.py
       |
       +-- commands/files.py
       |
       +-- commands/system.py
       |
       +-- commands/web.py

This modular structure makes the project easier to maintain, test, and extend.

---

## Current Limitations

- Windows-focused functionality
- Application paths may vary between systems
- Voice recognition depends on microphone quality and configuration
- Visual Studio Code detection may require additional configuration
- Some commands require specific Windows applications to be installed
- Internet connection may be required for certain speech-recognition and web-search features

---

## Roadmap

### V1.2

Planned improvements:

- Windows system actions
- Open Task Manager
- Open Windows Settings
- Lock computer
- Restart with confirmation
- Shutdown with confirmation
- Improved command matching
- Better error handling

### Future Versions

Potential long-term features:

- AI-powered conversational responses
- Custom application launching
- Music controls
- System automation
- File searching
- Advanced natural-language understanding
- Custom wake-word detection
- Personalized assistant settings
- GUI dashboard

---

## Version

**Current Version: 1.1**

JARVIS V1.1 focuses on modular architecture, reliable command routing, desktop interaction, web search, and real-time system intelligence.

---

## Privacy

JARVIS is designed as a local desktop assistant and does not intentionally collect or store personal user data.

### Microphone

JARVIS requires microphone access to detect the wake word and process voice commands.

Audio is processed for the purpose of recognizing commands. JARVIS does not intentionally record or permanently store conversations or microphone recordings.

### System Information

JARVIS can access basic system information such as:

- CPU usage
- RAM usage
- Battery level
- Charging status
- Operating system information

This information is used only to provide the requested response and is not intentionally uploaded or stored by JARVIS.

### Web Searches

When a user requests a Google or YouTube search, JARVIS opens the corresponding website in the user's browser.

Search queries are sent to the respective website by the browser.

JARVIS does not maintain a separate database of search history.

### Third-Party Services

JARVIS may interact with third-party services such as:

- Google
- YouTube
- Speech recognition services

These services may have their own privacy policies and data-handling practices.

Users should review the privacy policies of third-party services they use with JARVIS.

### Local Processing

Whenever possible, JARVIS performs operations locally on the user's Windows machine.

No personal information is intentionally collected, sold, or shared by this project.

---

## License

This project is developed for educational and personal use.
---

## Author

**Omar Osama**

Computer Science Student & Software Engineer
