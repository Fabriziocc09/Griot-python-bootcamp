import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
wikipedia.set_lang('es')
import webbrowser
import asyncio

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty('rate', 170)



def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,2)
    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-gb')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

query = takeCommand().lower()
query2 = takeCommand()


def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("grillot","")
        query = query.replace("busca en google","")
        query = query.replace("google","")
        




def searchWikipedia(query):
    if "wikipedia" in query:
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        results = wikipedia.summary(query,sentences = 2)
        print(results)
        speak(results)