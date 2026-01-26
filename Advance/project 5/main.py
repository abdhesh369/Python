import pyttsx3
import speech_recognition as sr
import sounddevice as sd
import soundfile as sf
import numpy as np
import webbrowser
import os
import time
import pyautogui
import pywhatkit
import wikipedia
import pyjokes

def speak():
    recognizer = sr.Recognizer()
    print("Listening....")
    duration = 5  
    samplerate = 16000
    try:
        audio_data = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype=np.int16)
        sd.wait()
        print("Recognizing...")
        audio = sr.AudioData(audio_data.tobytes(), samplerate, 2)
        data = recognizer.recognize_google(audio)
        print(f"You said: {data}")
    except sr.UnknownValueError:
        print("Could not understand audio. Try again..")
    except sr.RequestError as e:
        print(f"Error with speech recognition service: {e}")
    except Exception as e:
        print(f"Error: {e}")

speak()