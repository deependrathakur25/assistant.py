from email.mime import audio
from time import strftime
from debugpy import listen
import pyaudio
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme(datetime):
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Deepu")
    elif hour>12 and hour<18:
        speak("Good Afternoon Deepu")
    else:
        speak("good evening deepu")
    
    speak("raam raam deepu how can i help u?")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold= 1
        audio=r.listen(source,timeout=1,phrase_time_limit=10)
    try:
        print("recognizing....")
        query=r.recognize_google(audio,language="en-in")
        print("user said:",query)
    except Exception as e:
        print(e)
        speak("say that again please....")
        return "none"
    return query

if __name__=='__main__':
    #speak deepu is the biggest sexiext boy
    wishme(datetime)
    #while true:
    if 1:
        query= takecommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia....please wait for a while")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            #speak results
        elif 'open youtube' in query:
            webbrowser.open("Youtube.com")
        elif 'open google' in query:
            webbrowser.open("Google.com")
        elif 'open notepad' in query:
            npath='C:\\Windows\\notepad.exe'
            os.startfile(npath)
        elif 'open cmd' in query:
            os.startfile("start cmd")
        elif 'time' in query:
            strTime=datetime.datetime.now(),strftime("%h:%m:%s")
            speak(f"deepu sir the time is{strTime}")
        elif 'no thanks' in query:
            speak("its okay deepu sir,give me chance to help later")

sys.exit()














