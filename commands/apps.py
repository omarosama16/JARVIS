import os
import subprocess

from voice import speak


# ==========================================
# APPLICATIONS
# ==========================================

def open_firefox():

    speak("Opening Firefox, sir.")

    firefox_paths = [
        r"C:\Program Files\Mozilla Firefox\firefox.exe",
        r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
    ]

    for path in firefox_paths:

        if os.path.exists(path):
            subprocess.Popen(path)
            return

    try:
        subprocess.Popen("firefox")

    except FileNotFoundError:
        speak("I couldn't find Firefox, sir.")


def open_vscode():

    speak("Opening Visual Studio Code, sir.")

    try:
        result = subprocess.run(
            ["where", "code"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            code_path = result.stdout.strip().splitlines()[0]
            subprocess.Popen(code_path)
            return

    except Exception:
        pass

    vscode_paths = [
        os.path.expandvars(
            r"%LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe"
        ),
        os.path.expandvars(
            r"%LOCALAPPDATA%\Programs\Microsoft VS Code\bin\code.cmd"
        ),
        r"C:\Program Files\Microsoft VS Code\Code.exe",
        r"C:\Program Files (x86)\Microsoft VS Code\Code.exe"
    ]

    for path in vscode_paths:

        if os.path.exists(path):
            subprocess.Popen(path)
            return

    speak("I couldn't find Visual Studio Code, sir.")


def open_spotify():

    speak("Opening Spotify, sir.")

    try:
        subprocess.Popen("spotify")

    except FileNotFoundError:
        speak("I couldn't find Spotify, sir.")