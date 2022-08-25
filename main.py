import getpass
import pyttsx3                      #pip install pyttsx3
import speech_recognition as sr     #pip install speechrecognition 
import datetime
import wikipedia                    #pip install wikipedia
import webbrowser
import os
import smtplib
import random

print("Initializing Jarvis")
master = "Sir"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Speak function will pronounce the string which will pass through it
def speak(text):
    engine.say(text)
    engine.runAndWait()

# This function will greet you as per the given time
def Wishme():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour <12):
        speak("Good Morning"+master)
    elif(hour>12 and hour < 18):
        speak("Good Afternoon"+master)
    else:
        speak("Good Evening"+master)
    speak("I am jarvis. How may I help you ?")

# This function will take command
def takecommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1.5
        audio = r.listen(source)
    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")
    except Exception as ep :
        print("Say that again please...")
        speak("Say that again please...")
        return"none" 
    return query
# Main function start here :-
speak("Initializing Jarvis...")
speak("kindly tell the passcode")
passcode = getpass.getpass()
passc =str("b\'"+passcode+"'")
k=open(r"C:\Users\Shubham\Desktop\Program\Python38-32\Jarvis\password.binary","rb")
a=str(k.read())
k.close()
if( passc == a):
    Wishme()
    speak("At your service sir")
    while True:
        query=takecommand().lower()
        no=0
        #logic for your task
        if('wikipedia' in query):
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "are you up " in query:
            speak("For you sir, always")
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif "open google" in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'play music' in query:
            speak("playing music")
            music_dir = r"D:\music"
            songs=os.listdir(music_dir)
            no = random.randint(1,len(songs))
            print(songs[no])
            speak(f"playing {songs[no]}\n")
            os.startfile(os.path.join(music_dir,songs[no]))
        elif "thank you" in query:
            speak("It's my pleasure sir")
        elif 'the time' in query:
            timing = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is {timing}")
        elif 'open code' in query:
            speak("opening visual studio code ")
            codepath =r"C:\Microsoft VS Code\Code.exe"
            os.startfile(codepath)
        elif 'open need for speed' in query:
            speak("opening need for speed folder ")
            codepath1=r"D:\Need For Speed"
            os.startfile(codepath1)
        elif 'open gta' in query:
            speak("opening gta san andreas folder ")
            codepath1=r"D:\GTA San Andreas"
            os.startfile(codepath1)
        elif 'play movies' in query:
            speak("playing movies")
            movie_dir = r"D:\movies"
            movie=os.listdir(movie_dir)
            no = random.randint(1,len(movie))
            print(movie[no])
            speak(f"playing {movie[no]}\n")
            os.startfile(os.path.join(movie_dir,movie[no]))
        elif 'play web series' in query:
            speak("playing webseries")
            web_dir = r"D:\web series"
            web=os.listdir(web_dir)
            no = random.randint(1,len(web))
            print(web[no])
            speak(f"playing {web[no]}\n")
            os.startfile(os.path.join(web_dir,web[no]))
        elif 'play videos' in query:
            speak("playing short and funny videos")
            vid_dir = r"D:\shortvideos"
            vid=os.listdir(vid_dir)
            no = random.randint(1,len(vid))
            print(vid[no])
            speak(f"playing {vid[no]}\n")
            os.startfile(os.path.join(vid_dir,vid[no]))
        elif 'think about me' in query:
            speak("As always sir, a great pleasure watching you work")
            speak("What was I thinking? You're usually so discrete.")
else:
    speak("You are not authorized to access this area...")    