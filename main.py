from voice import speak, listen, wait_for_wake_word

from core.router import route_command
from utils.query import extract_search_query

from commands import apps, files, web, system


# ==========================================
# COMMAND HANDLER
# ==========================================

def handle_command(command):

    print(f"\n[COMMAND RECEIVED] {command}")

    intent = route_command(command)

    print(f"[INTENT DETECTED] {intent}")

    # ==========================================
    # EMPTY
    # ==========================================

    if intent == "empty":
        speak("I didn't hear a command, sir.")
        return True

    # ==========================================
    # EXIT
    # ==========================================

    if intent == "exit":
        speak("Goodbye, sir.")
        return False

    # ==========================================
    # GREETING
    # ==========================================

    if intent == "greeting":
        speak("Hello, sir.")

    # ==========================================
    # STATUS
    # ==========================================

    elif intent == "status":
        speak("I'm functioning perfectly, sir.")

    # ==========================================
    # TIME
    # ==========================================

    elif intent == "time":
        system.tell_time()

    # ==========================================
    # DATE
    # ==========================================

    elif intent == "date":
        system.tell_date()

    # ==========================================
    # CPU
    # ==========================================

    elif intent == "cpu":
        system.tell_cpu_usage()

    # ==========================================
    # RAM
    # ==========================================

    elif intent == "ram":
        system.tell_ram_usage()

    # ==========================================
    # BATTERY
    # ==========================================

    elif intent == "battery":
        system.tell_battery()

    # ==========================================
    # SYSTEM INFORMATION
    # ==========================================

    elif intent == "system_info":
        system.tell_system_info()

    # ==========================================
    # FIREFOX
    # ==========================================

    elif intent == "firefox":
        apps.open_firefox()

    # ==========================================
    # VS CODE
    # ==========================================

    elif intent == "vscode":
        apps.open_vscode()

    # ==========================================
    # SPOTIFY
    # ==========================================

    elif intent == "spotify":
        apps.open_spotify()

    # ==========================================
    # DOWNLOADS
    # ==========================================

    elif intent == "downloads":
        files.open_downloads()

    # ==========================================
    # DESKTOP
    # ==========================================

    elif intent == "desktop":
        files.open_desktop()

    # ==========================================
    # FILE EXPLORER
    # ==========================================

    elif intent == "file_explorer":
        files.open_file_explorer()

    # ==========================================
    # GOOGLE SEARCH
    # ==========================================

    elif intent == "google_search":

        query = extract_search_query(command, "google")

        if query:
            web.google_search(query)

        else:
            speak("What should I search for, sir?")

    # ==========================================
    # YOUTUBE SEARCH
    # ==========================================

    elif intent == "youtube_search":

        query = extract_search_query(command, "youtube")

        if query:
            web.youtube_search(query)

        else:
            speak("What should I search for, sir?")

    # ==========================================
    # UNKNOWN
    # ==========================================

    else:
        speak(
            f"I heard {command}, but I don't know that command yet, sir."
        )

    return True


# ==========================================
# START JARVIS
# ==========================================

speak("JARVIS online and ready.")


while True:

    print("\n==============================")
    print("        JARVIS WAITING")
    print("==============================")

    awakened = wait_for_wake_word()

    print(f"[WAKE RESULT] {awakened}")

    if not awakened:
        break

    print("[JARVIS AWAKE] Listening for command...")

    command = listen()

    print(f"[FINAL COMMAND] {command}")

    if not handle_command(command):
        break