from fileinput import filename
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(tex):
    tts = gTTS(text=tex, lang="en")
    filename = "voice.mp3"
    tts.save(filename)


    playsound.playsound(filename)


speak("hello")