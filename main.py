import webbrowser
from time import sleep
import os
import openai
import mouse
import pywhatkit
from dotenv import load_dotenv


import pyautogui
import pyttsx3
import datetime
import speech_recognition
import speedtest

import pyttsx3

def speak_logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} was called with arguments: {args}, {kwargs}")
        return result
    return wrapper

class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init("sapi5")
        self.voices = self.engine.getProperty("voices")
        self.engine.setProperty('voice', self.voices[0].id)
        self.engine.setProperty("rate", 180)

    @speak_logger
    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()



def askGPT(text):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = text,
        temperature = 0.6,
        max_tokens = 200,
    )
    return response["choices"][0]["text"]

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source,0,5)

    try:
        query  = r.recognize_google(audio,language='es-es')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query




class MainCode :
    if __name__ == "__main__" :

        while True:
            
            assistant = VoiceAssistant()
            query = takeCommand().lower()
            tasks = []
            from GreetMe import greetMe
            greetMe()


            while True:
                    query = takeCommand().lower()
                    if query.lower() == 'salir':
                        break

                  
                    elif "multiplica" in query:
                        query = query.replace("multiplica", "")
                        numbers = query.split()
                        if len(numbers) == 3:
                            x, y = float(numbers[0]), float(numbers[2])
                            multiplica = lambda x, y: x * y
                            assistant.speak("El resultado es: " + str(multiplica(x, y)))
                            print("El resultado es: " + str(multiplica(x, y)))
                        else:
                            assistant.speak("Lo siento, no pude procesar esta pregunta.")
                    
                    elif "divide" in query:
                        query = query.replace("divide", "")
                        numbers = query.split()
                        if len(numbers) == 3:
                            x, y = float(numbers[0]), float(numbers[2])
                            divide = lambda x, y: x / y
                            assistant.speak("El resultado es: " + str(divide(x, y)))
                            print("El resultado es: " + str(divide(x, y)))
                        else:
                            assistant.speak("Lo siento, no pude procesar esta pregunta.")

                    elif "área" in query:
                        print("entro")
                        query = query.replace("área", "")
                        numbers = query.split()

                        if len(numbers) == 3:
                            l , w = float(numbers[0]) , float(numbers[2])
                            calculate_area = lambda l, w: l * w
                            print("El area de este rectángulo es:" +  str(calculate_area(l,w)))
                            assistant.speak("El area de este rectángulo es:" +  str(calculate_area(l,w)))



                    elif "calculate" in query:
                        from Calculatenumbers import Calc
                        query = query.replace("calcula", "")
                        query = query.replace("jarvis", "")
                        Calc(query)




                    elif "google" in query:
                        from SearchNow import searchGoogle
                        searchGoogle(query)
            

                    elif "youtube" in query:
                        query = query.replace("youtube search", "")
                        query = query.replace("youtube", "")
                        query = query.replace("jarvis", "")
                        web = "https://www.youtube.com/results?search_query=" + query
                        webbrowser.open(web)


                    elif "new" in query:

                        web = "https://www.youtube.com/"
                        webbrowser.open(web)


                    elif "instagram" in query:
                        web = "https://www.instagram.com/"
                        webbrowser.open(web)


                    elif "wikipedia" in query:
                        from SearchNow import searchWikipedia

                        searchWikipedia(query)

                    elif "internet speed" in query:
                        assistant.speak("Calculando")
                        wifi = speedtest.Speedtest()
                        upload_net = round(wifi.upload()/1048576)
                        download_net = round(wifi.download()/1048576)
                        print("velocidad de subida" , upload_net)
                        print("velocidad de bajada" , download_net)
                        assistant.speak(f"velocidad de subida, {upload_net}")
                        assistant.speak(f"velocidad de bajada, {download_net}")


                    elif "pon " in query:
                        query = query.replace("pon", "")
                        query = query.replace("pon" , "")
                        song = query
                        webbrowser.open(f"https://open.spotify.com/search/{song}")
                        sleep(10)
                        pyautogui.click(800,310)
                        print(f"Reproduciendo la canción en Spotify: {song}")

                    elif "play" in query:
                        from game import game_play

                        game_play()

                    elif "open" in query:  # EASY METHOD
                        query = query.replace("abre", "")
                        query = query.replace("jarvis", "")
                        pyautogui.press("super")
                        pyautogui.typewrite(query)
                        pyautogui.sleep(2)
                        pyautogui.press("enter")

                    elif "una pestaña" in query or "1 tab" in query:
                        pyautogui.hotkey("ctrl", "w")
                        assistant.speak("All tabs closed")

                    elif "chat" in query:
                            query = query.replace("chat", "")
                            response = askGPT(query)
                            print(response)
                            assistant.speak(response)