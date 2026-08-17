import os
import subprocess

from voice import speak


# ==========================================
# FOLDERS
# ==========================================

def open_downloads():

    speak("Opening Downloads, sir.")

    downloads_path = os.path.join(
        os.path.expanduser("~"),
        "Downloads"
    )

    if os.path.exists(downloads_path):
        os.startfile(downloads_path)
        return

    speak("I couldn't find your Downloads folder, sir.")


def open_desktop():

    speak("Opening Desktop, sir.")

    desktop_path = os.path.join(
        os.path.expanduser("~"),
        "Desktop"
    )

    if os.path.exists(desktop_path):
        os.startfile(desktop_path)
        return

    one_drive_desktop = os.path.join(
        os.path.expanduser("~"),
        "OneDrive",
        "Desktop"
    )

    if os.path.exists(one_drive_desktop):
        os.startfile(one_drive_desktop)
        return

    speak("I couldn't find your Desktop folder, sir.")


def open_file_explorer():

    speak("Opening File Explorer, sir.")

    try:
        subprocess.Popen("explorer")

    except FileNotFoundError:
        speak("I couldn't open File Explorer, sir.")