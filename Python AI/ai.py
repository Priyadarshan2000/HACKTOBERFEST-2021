import pyttsx3
import datetime
import speech_recognition as sr

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
newvoicerate = 150
engine.setProperty('rate' , newvoicerate)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#speak("Hello! How Are You")
#speak("What is Your Name?")

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)
time()

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("The Current Date is")
    speak(date)
    speak(month)
    speak(year)
#date()

def wishme():
    speak("Welcome Back Sir!")
    time()
    date()
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        speak("Good Evening")
    elif hour>=18 and hour<=24:
        speak("Good Night")
    else:
        speak("Good Night")
    speak("Friday at your service . How can i help you ?")
#wishme()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        Print("Recongnizing.....")
        query = r.recognize_google(audio,"en=IN")
        print(query)
    
    except Exception as e:
        print(e)
        speak("Say that again please.....")
    
        return "None"
    
    return query

takecommand()
if __name__ == "__main__":

    wishme()

    while true:
        query = takecommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("Sesrching....")
            query=query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            speak(result)

