import pyttsx3
import speech_recognition as sr
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio , language= 'es-pe')
        print(f"You Said : {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query


def game_play():
    speak("Vamos a jugar piedra papel o tijera !!")
    speak("Son 3 partidas")
    i = 0
    Me_score = 0
    Com_score = 0
    while (i < 3):
        choose = ("piedra", "papel", "tijera")  # Tuple
        com_choose = random.choice(choose)
        query = takeCommand().lower()
        if (query == "piedra"):
            if (com_choose == "piedra"):
                speak("piedra")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "papel"):
                speak("papel")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("tijera")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "papel"):
            if (com_choose == "piedra"):
                speak("piedra")
                Me_score += 1
                print(f"Score:- ME :- {Me_score + 1} : COM :- {Com_score}")

            elif (com_choose == "papel"):
                speak("papel")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("tijera")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "tijera" or query == "tijeras"):
            if (com_choose == "piedra"):
                speak("piedra")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "papel"):
                speak("papel")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("tijera")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
        i += 1

    if Me_score < Com_score:
        speak("Yo gane")
    else :
        speak("tu ganaste")
    print(f"Resultado :- Tu :- {Me_score} : IA :- {Com_score}")
