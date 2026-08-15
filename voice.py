import sounddevice as sd
import speech_recognition as sr
import pyttsx3
import numpy as np


# ==========================================
# SETTINGS
# ==========================================

MICROPHONE_INDEX = 1
SAMPLE_RATE = 16000

CHANNELS = 1

# How loud something needs to be to count as speech
ENERGY_THRESHOLD = 0.015

# How long silence must last before we stop recording
SILENCE_DURATION = 1.2

# Maximum recording time
MAX_RECORDING_TIME = 8


# ==========================================
# TEXT TO SPEECH
# ==========================================

engine = pyttsx3.init()

engine.setProperty("rate", 165)
engine.setProperty("volume", 1.0)


def setup_voice():

    voices = engine.getProperty("voices")

    preferred = [
        "zira",
        "female",
        "woman",
        "hazel",
        "samantha"
    ]

    for voice in voices:

        name = voice.name.lower()

        if any(keyword in name for keyword in preferred):

            engine.setProperty("voice", voice.id)

            print(f"Voice selected: {voice.name}")

            return

    print("No feminine voice found. Using default voice.")


setup_voice()


def speak(text):

    print(f"JARVIS: {text}")

    engine.say(text)
    engine.runAndWait()


# ==========================================
# MICROPHONE
# ==========================================

def record_audio():

    print("🎙️ Waiting for speech...")

    block_duration = 0.1

    block_size = int(SAMPLE_RATE * block_duration)

    recorded_audio = []

    speaking = False

    silence_time = 0

    total_time = 0

    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="float32",
        device=MICROPHONE_INDEX
    ) as stream:

        while total_time < MAX_RECORDING_TIME:

            data, overflowed = stream.read(block_size)

            audio = data[:, 0]

            volume = np.sqrt(np.mean(audio ** 2))

            # ------------------------------
            # Speech detected
            # ------------------------------

            if volume > ENERGY_THRESHOLD:

                if not speaking:

                    print("🎙️ Speech detected...")

                speaking = True

                silence_time = 0

                recorded_audio.append(audio.copy())

            # ------------------------------
            # Silence
            # ------------------------------

            elif speaking:

                recorded_audio.append(audio.copy())

                silence_time += block_duration

                if silence_time >= SILENCE_DURATION:

                    break

            total_time += block_duration

    if not recorded_audio:

        return None

    audio_data = np.concatenate(recorded_audio)

    # Convert float32 → int16
    audio_data = np.int16(audio_data * 32767)

    return audio_data


# ==========================================
# SPEECH RECOGNITION
# ==========================================

def listen():

    audio_data = record_audio()

    if audio_data is None:

        return ""

    recognizer = sr.Recognizer()

    audio = sr.AudioData(
        audio_data.tobytes(),
        SAMPLE_RATE,
        2
    )

    try:

        text = recognizer.recognize_google(audio)

        text = text.lower().strip()

        print(f"You: {text}")

        return text

    except sr.UnknownValueError:

        print("JARVIS: I didn't understand that.")

        return ""

    except sr.RequestError:

        speak(
            "I'm having trouble connecting "
            "to the speech recognition service."
        )

        return ""

    except Exception as error:

        print(f"Recognition error: {error}")

        return ""


# ==========================================
# WAKE WORD
# ==========================================

def wait_for_wake_word():

    while True:

        command = listen()

        if not command:

            continue

        # Shutdown commands

        if any(word in command for word in [
            "exit",
            "goodbye",
            "shutdown",
            "quit"
        ]):

            speak("Shutting down, sir.")

            return False

        # Wake word

        if "jarvis" in command:

            speak("Yes, sir.")

            return True