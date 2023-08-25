import wolframalpha
import pyttsx3
import speech_recognition

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",120)



def WolfRamAlpha(query):
    apikey = "QG4GJ9-TPJVGAL953"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("no puedo")

def Calc(query):
    Term = str(query)
    Term = Term.replace("calcula", "")
    Term = Term.replace("mas", "+")
    Term = Term.replace("menos", "-")
    Term = Term.replace("por", "*")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        speak(result)

    except:
        speak("The value is not answerable")

    