# when I Dockerize the containter pip install SpeechRecognition

import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Function that converts the text to speech


def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


# test to see if it works
SpeakText(input("Enter What you would want to hear here: "))

# this uses the microphone as a source for your sound input
# with sr.Microphone() as source2:
