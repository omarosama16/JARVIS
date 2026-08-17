from commands import apps, files, web, system


# ==========================================
# SYSTEM
# ==========================================

print("\n===== TESTING SYSTEM =====")

system.tell_time()
system.tell_date()


# ==========================================
# SYSTEM INFORMATION
# ==========================================

print("\n===== TESTING SYSTEM INFORMATION =====")

system.tell_cpu_usage()
system.tell_ram_usage()
system.tell_battery()
system.tell_system_info()


# ==========================================
# FILES
# ==========================================

print("\n===== TESTING FILES =====")

files.open_desktop()
files.open_downloads()
files.open_file_explorer()


# ==========================================
# APPS
# ==========================================

print("\n===== TESTING APPS =====")

apps.open_firefox()
apps.open_vscode()
apps.open_spotify()


# ==========================================
# WEB
# ==========================================

print("\n===== TESTING WEB =====")

web.google_search("python tutorials")
web.youtube_search("coding music")