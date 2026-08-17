from core.router import route_command


test_commands = [

    # ==========================================
    # FIREFOX
    # ==========================================

    "open firefox",
    "launch firefox",
    "start firefox",
    "please open firefox",
    "can you launch firefox",

    # ==========================================
    # VS CODE
    # ==========================================

    "open vscode",
    "open vs code",
    "launch visual studio code",
    "please start vscode",

    # ==========================================
    # SPOTIFY
    # ==========================================

    "open spotify",
    "launch spotify",
    "start spotify",

    # ==========================================
    # FOLDERS
    # ==========================================

    "open downloads",
    "launch downloads",
    "open desktop",
    "start desktop",
    "open file explorer",
    "launch explorer",

    # ==========================================
    # TIME
    # ==========================================

    "what time is it",
    "tell me the time",
    "what's the time",

    # ==========================================
    # DATE
    # ==========================================

    "what date is it",
    "tell me the date",
    "what's today's date",

    # ==========================================
    # GREETINGS
    # ==========================================

    "hello",
    "hi",
    "hey",
    "hello jarvis",

    # ==========================================
    # GOOGLE
    # ==========================================

    "search google for python tutorials",
    "google python tutorials",
    "google how to learn python",
    "search google python tutorials",

    # ==========================================
    # YOUTUBE
    # ==========================================

    "search youtube for coding music",
    "search youtube coding music",
    "find on youtube coding music",
    "youtube coding music",

    # ==========================================
    # CPU
    # ==========================================

    "what is my cpu usage",
    "what's my cpu usage",
    "how much cpu am i using",

    # ==========================================
    # RAM
    # ==========================================

    "what is my ram usage",
    "how much ram am i using",
    "what's my memory usage",

    # ==========================================
    # BATTERY
    # ==========================================

    "what is my battery level",
    "what percentage is my battery",
    "am i charging",

    # ==========================================
    # SYSTEM
    # ==========================================

    "what operating system am i using",
    "what system am i running",
    "system information",

    # ==========================================
    # UNKNOWN
    # ==========================================

    "something random"
]


for command in test_commands:

    result = route_command(command)

    print(f"{command:<45} -> {result}")