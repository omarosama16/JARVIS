import os
import subprocess
import webbrowser
from datetime import datetime

from voice import speak


# ==========================================
# OPEN APPLICATIONS
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
        subprocess.Popen("code")
    except FileNotFoundError:
        speak("I couldn't find Visual Studio Code, sir.")


def open_spotify():
    speak("Opening Spotify, sir.")

    try:
        subprocess.Popen("spotify")
    except FileNotFoundError:
        speak("I couldn't find Spotify, sir.")


# ==========================================
# OPEN FOLDERS
# ==========================================

def open_downloads():
    speak("Opening Downloads, sir.")

    downloads_path = os.path.join(
        os.path.expanduser("~"),
        "Downloads"
    )

    os.startfile(downloads_path)


def open_desktop():
    speak("Opening Desktop, sir.")

    desktop_path = os.path.join(
        os.path.expanduser("~"),
        "Desktop"
    )

    os.startfile(desktop_path)


def open_file_explorer():
    speak("Opening File Explorer, sir.")

    subprocess.Popen("explorer")


# ==========================================
# WEB SEARCH
# ==========================================

def google_search(query):
    speak(f"Searching Google for {query}, sir.")

    url = (
        "https://www.google.com/search?q="
        + query.replace(" ", "+")
    )

    webbrowser.open(url)


def youtube_search(query):
    speak(f"Searching YouTube for {query}, sir.")

    url = (
        "https://www.youtube.com/results?search_query="
        + query.replace(" ", "+")
    )

    webbrowser.open(url)


# ==========================================
# TIME
# ==========================================

def tell_time():
    current_time = datetime.now().strftime("%I:%M %p")

    speak(f"The time is {current_time}, sir.")


# ==========================================
# DATE
# ==========================================

def tell_date():
    current_date = datetime.now().strftime("%A, %B %d, %Y")

    speak(f"Today is {current_date}, sir.")