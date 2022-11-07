from fileinput import filename
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(txt):
    tts = gTTS(text=txt, lang="hi",)
    filename = "voice.mp3"
    tts.save(filename)


    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said


#speak("hello there, i am AI Ohto")

text = get_audio()

def my_name_detector_function(text):
    if ("" in text or "" in text):
        return True
    return False


if my_name_detector_function(text):
    speak('')


#speak(text)
