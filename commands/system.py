from datetime import datetime
import psutil
from voice import speak


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

# ==========================================
# CPU
# ==========================================

def tell_cpu_usage():

    cpu_usage = psutil.cpu_percent(interval=1)

    speak(
        f"Current CPU usage is {cpu_usage} percent, sir."
    )


# ==========================================
# RAM
# ==========================================

def tell_ram_usage():

    memory = psutil.virtual_memory()

    ram_usage = memory.percent

    speak(
        f"Current memory usage is {ram_usage} percent, sir."
    )


# ==========================================
# BATTERY
# ==========================================

def tell_battery():

    battery = psutil.sensors_battery()

    if battery is None:
        speak("I couldn't detect a battery, sir.")
        return

    percentage = battery.percent

    if battery.power_plugged:
        speak(
            f"Battery is at {percentage} percent and charging, sir."
        )

    else:
        speak(
            f"Battery is at {percentage} percent, sir."
        )


# ==========================================
# OPERATING SYSTEM
# ==========================================

def tell_system_info():

    import platform

    system = platform.system()
    release = platform.release()

    speak(
        f"You are running {system} {release}, sir."
    )    