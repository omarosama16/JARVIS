from voice import speak, listen, wait_for_wake_word
import commands


def handle_command(command):

    print(f"\n[COMMAND RECEIVED] {command}")

    if not command:
        speak("I didn't hear a command, sir.")
        return True

    # EXIT
    if any(word in command for word in [
        "exit",
        "goodbye",
        "shutdown",
        "quit"
    ]):
        speak("Goodbye, sir.")
        return False

    # GREETINGS
    if "hello" in command or "hi" in command:
        speak("Hello, sir.")

    # HOW ARE YOU
    elif "how are you" in command:
        speak("I'm functioning perfectly, sir.")

    # TIME
    elif "what time" in command or "current time" in command:
        commands.tell_time()

    # DATE
    elif (
        "what date" in command
        or "today's date" in command
        or "what day is it" in command
    ):
        commands.tell_date()

    # FIREFOX
    elif (
        "open firefox" in command
        or "launch firefox" in command
    ):
        commands.open_firefox()

    # VS CODE
    elif (
        "open vscode" in command
        or "open vs code" in command
        or "open visual studio code" in command
    ):
        commands.open_vscode()

    # SPOTIFY
    elif "open spotify" in command:
        commands.open_spotify()

    # DOWNLOADS
    elif "open downloads" in command:
        commands.open_downloads()

    # DESKTOP
    elif "open desktop" in command:
        commands.open_desktop()

    # FILE EXPLORER
    elif (
        "open file explorer" in command
        or "open explorer" in command
    ):
        commands.open_file_explorer()

    # GOOGLE
    elif "search google for" in command:

        query = command.split("search google for", 1)[1].strip()

        if query:
            commands.google_search(query)
        else:
            speak("What should I search for, sir?")

    # YOUTUBE
    elif "search youtube for" in command:

        query = command.split("search youtube for", 1)[1].strip()

        if query:
            commands.youtube_search(query)
        else:
            speak("What should I search for, sir?")

    # UNKNOWN
    else:
        speak(
            f"I heard {command}, but I don't know that command yet, sir."
        )

    return True


# ==========================================
# START
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