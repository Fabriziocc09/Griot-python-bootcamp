import pyttsx3
import datetime

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice" , voices[0].id)
engine.setProperty("velocity", 190)



def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >0 and hour <=12:
        speak("Buenos dias Fabrizio , en que te puedo ayudar?")
    elif hour>12 and hour<=18:
        speak("Buenos tardes Fabrizio , en que te puedo ayudar?")
    else :
        speak("Buenas noches Fabrizio , en que te puedo ayudar?")





