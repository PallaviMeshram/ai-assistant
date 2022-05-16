from ast import If
from email.mime import audio
from pip import main
import pyaudio
import speech_recognition as sr
import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
# print(voices[1])

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour < 12):
        speak("Good Morning!")
    elif (hour >= 12 and hour < 18):
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am your Real virtual assistant, How may I help You?")


# Taking input from the Microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again Please!...")
        return "None"
    return query

# Main Function
if __name__ == "__main__":
    wishMe()
    takeCommand()
