from ast import If
from audioop import add
from email.mime import audio
from pyexpat import features
from re import M, S
from pip import main
import pyaudio
import speech_recognition as sr
import pyttsx3
import datetime
from sympy import solve_undetermined_coeffs
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
# print(voices[1])

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Greeting at start
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


# Youtube Functions
def youtube():
    url = "https://www.youtube.com/"
    webbrowser.open(url)

# Google Funtions
def google(query):
    speak("Opening on Google...")
    query = query.replace("google","")
    webbrowser.open("https://www.google.com/search?q="+query)

# Main Function
if __name__ == "__main__":
    wishMe()
    flag = True
    while flag:
        query = takeCommand().lower()
        # Search in wikipedia
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            #  Please use "according to wikipedia" for commands
            speak("According to Wikipedia")
            speak(results)
        # Open Youtube
        elif 'open youtube' in query:
            youtube()
            
        elif 'google' in query:
            google(query)

        # Tells the Time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Now time is {strTime}")
        
        # Open VS code
        elif 'open code' in query:
            codePath = "C:\\Users\\pallavi.meshram\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'exit' in query:
            speak("Happy to help you!, Have a good day ahead")
            flag = False




