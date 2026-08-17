def route_command(command):
    """
    Determines which type of command was given.
    Returns the detected intent.
    """

    command = command.lower().strip()

    if not command:
        return "empty"

    # ==========================================
    # EXIT
    # ==========================================

    if any(word in command for word in [
        "exit",
        "goodbye",
        "shutdown",
        "quit"
    ]):
        return "exit"

    # ==========================================
    # GREETINGS
    # ==========================================

    if command in [
        "hello",
        "hi",
        "hey",
        "hello jarvis",
        "hi jarvis",
        "hey jarvis"
    ]:
        return "greeting"

    # ==========================================
    # HOW ARE YOU
    # ==========================================

    if "how are you" in command:
        return "status"

    # ==========================================
    # TIME
    # ==========================================

    if (
        "what time" in command
        or "current time" in command
        or "tell me the time" in command
        or "what's the time" in command
    ):
        return "time"

    # ==========================================
    # DATE
    # ==========================================

    if (
        "what date" in command
        or "today's date" in command
        or "what day is it" in command
        or "tell me the date" in command
        or "what's today's date" in command
    ):
        return "date"
    # ==========================================
    # CPU
    # ==========================================

    if "cpu" in command:
        return "cpu"

    # ==========================================
    # RAM
    # ==========================================

    if any(word in command for word in [
        "ram",
        "memory"
    ]):
        return "ram"


    # ==========================================
    # BATTERY
    # ==========================================

    if (
        "battery" in command
        or "charging" in command
    ):
        return "battery"

    # ==========================================
    # SYSTEM INFORMATION
    # ==========================================

    if any(phrase in command for phrase in [
        "operating system",
        "system information",
        "system info",
        "what system am i running"
    ]):
        return "system_info"

    # ==========================================
    # FIREFOX
    # ==========================================

    if (
        "firefox" in command
        and any(action in command for action in [
            "open",
            "launch",
            "start"
        ])
    ):
        return "firefox"

    # ==========================================
    # VS CODE
    # ==========================================

    if (
        any(name in command for name in [
            "vscode",
            "vs code",
            "visual studio code"
        ])
        and any(action in command for action in [
            "open",
            "launch",
            "start"
        ])
    ):
        return "vscode"

    # ==========================================
    # SPOTIFY
    # ==========================================

    if (
        "spotify" in command
        and any(action in command for action in [
            "open",
            "launch",
            "start"
        ])
    ):
        return "spotify"

    # ==========================================
    # DOWNLOADS
    # ==========================================

    if (
        "downloads" in command
        and any(action in command for action in [
            "open",
            "launch",
            "start"
        ])
    ):
        return "downloads"

    # ==========================================
    # DESKTOP
    # ==========================================

    if (
        "desktop" in command
        and any(action in command for action in [
            "open",
            "launch",
            "start"
        ])
    ):
        return "desktop"

    # ==========================================
    # FILE EXPLORER
    # ==========================================

    if (
        any(name in command for name in [
            "file explorer",
            "explorer"
        ])
        and any(action in command for action in [
            "open",
            "launch",
            "start"
        ])
    ):
        return "file_explorer"

    # ==========================================
    # GOOGLE SEARCH
    # ==========================================

    if (
        "google" in command
        and any(action in command for action in [
            "search",
            "google"
        ])
    ):
        return "google_search"

    # ==========================================
    # YOUTUBE SEARCH
    # ==========================================
    if (
        "youtube" in command
        and any(action in command for action in [
            "search",
            "find",
            "youtube"
        ])
    ):
        return "youtube_search"
    # ==========================================
    # UNKNOWN
    # ==========================================

    return "unknown"
