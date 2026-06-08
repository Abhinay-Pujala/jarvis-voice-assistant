#For Recognize Our Speech and convert it into text
from datetime import datetime
import threading
import speech_recognition as sr
import sys
#To Access Web Pages
import os as s
import webbrowser

#To convert Text into audio

import pyttsx3

import openai as OpenAI

#This is for songs(Created By me)
import musiclibrary

import loadenv as env

#Giving names to the recognizer and converter


# client = OpenAI(api_key=env.load_env_var(OPENAI_API_KEY))

engine = pyttsx3.init()


#Function for convert text to audio using ttsx

def speak(text):
    engine.say(text)
    engine.runAndWait()

# def openAIResponse(command):
#     """Get a response from OpenAI API"""
#     try:
#         # Make a request to OpenAI's API to generate a response for the command
#         response = client.chat.completions.create(
#                 model="gpt-4o-mini",
#                 messages=[
#                     {
#                         "role":"system",
#                         "content":"You are Jarvis, a helpful voice assistant. Give short and clear answers."
#                     },
#                     {
#                         "role":"user",
#                         "content":command
#                     }
#                 ]
#         )
#         return response.choices[0].message.content
#     except Exception as e:
#         return f"Error: {str(e)}"
    
def save_notes(note):
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open("notes.txt", "a", encoding='utf-8') as file:
        file.write(f"{current_time}: {note}\n")
    speak('Note Saved Successfully')

def open_app(app_name):
    if "chrome" in app_name.lower():
        s.system('start chrome')
    elif "settings" in app_name.lower():
        s.system('start ms-settings:')
    elif "edge" in app_name.lower():
        s.system("start msedge")
    elif "vs code" in app_name.lower():
        s.system('start code')
    elif "whatsapp" in app_name.lower():
        s.system("start whatsapp:")
    else:
        speak(f"I can't find app {app_name}")


def close_app(app):
    if "chrome" in app.lower():
        s.system("taskkill /F /IM chrome.exe")
    elif "settings" in app.lower():
        s.system("taskkill /F /IM SystemSettings.exe")
    elif "edge" in app.lower():
        s.system("taskkill /F /IM msedge.exe")
    elif "vs code" in app.lower():
        s.system("taskkill /F /IM Code.exe")
    elif "whatsapp" in app.lower():
        s.system("taskkill /F /IM WhatsApp.exe")
    else:
        speak(f"I can't find app {app}")

#Function for making actions according to the commands we give
def processCommand(c):
    print(c)
    if "bye" in c.lower():
        speak("ok bye sir! if you need any help,just call me.")
        sys.exit()
    if "google" in c.lower():
        speak("opening google")
        webbrowser.open("https://google.com")

    elif "help" in c.lower():
        speak(
        "You can ask me time, open apps, close apps, play music, and ask AI questions."
        )

    elif "the time" in c.lower():
        hour=datetime.now().strftime("%H")
        min=datetime.now().strftime("%M")
        sec=datetime.now().strftime("%S")
        speak(f"time is {hour} ,{min}minutes {sec}seconds")
    elif "chat gpt" in c.lower():
        speak("sure")
        webbrowser.open("chatgpt.com")
    elif "good job" in c.lower():
        speak("thank you")
    elif "who created you" in c.lower():
        speak("mister abhinay sir")
    elif "em chestunnav" in c.lower():
        speak("neekendhuku raa.")
    elif "youtube" in c.lower():
            speak("opening youtube")
            webbrowser.open("https://youtube.com")
    elif "linkedin" in c.lower():
        speak("opening linkedin")
        webbrowser.open("https://linkedin.com")
    elif "facebook" in c.lower():
        speak("opening facebook")
        webbrowser.open("https://facebook.com")
    elif "hotstar" in c.lower():
        speak("opening hotstar")
        webbrowser.open("https://www.hotstar.com")

    elif c.lower().startswith("note"):
        note_text = c[4:].strip()
        if note_text:
            save_notes(note_text)
        else:
            speak("Tell me what I need to nate for you, Sir.")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        if song in musiclibrary.music:
            webbrowser.open(musiclibrary.music[song])
        else:
            speak("Sorry, I couldn't find that song.")

    elif c.lower().startswith("calculate"):
        try:
            expression = c.lower().replace("calculate", "").strip()

            expression = expression.replace("plus", "+")
            expression = expression.replace("minus", "-")
            expression = expression.replace("times", "*")
            expression = expression.replace("multiplied by", "*")
            expression = expression.replace("x", "*")
            expression = expression.replace("into", "*")


            expression = expression.replace("divided by", "/")
            expression = expression.replace("by", "/")


            result = eval(expression)

            speak(f"The answer is {result}")
            print(f"The answer is {result}")
        except Exception:
            speak("Sorry, I couldn't calculate that.")


    elif "close everything" in c.lower():
        speak("Are you sure you want to close all running apps?")
        with sr.Microphone() as source:
            audio = r.listen(source)
        confirm = r.recognize_google(audio).lower()
        if "close" in confirm:
            speak("Okay, closing all apps.")
            s.system("taskkill /F /IM chrome.exe")
            s.system("taskkill /F /IM msedge.exe")
            s.system("taskkill /F /IM WhatsApp.exe")
            s.system("taskkill /F /IM Code.exe")
            s.system("taskkill /F /IM SystemSettings.exe")
        else:
            speak("Okay, I won't close anything.")
    elif "open" in c.lower():
        apps_string = c.lower().split("open", 1)[1]

        # Split using commas or 'and' or 'also'
        import re
        app_list = re.split(r",| and | also", apps_string)

        for app_name in app_list:
            app_name = app_name.strip()
            if app_name:
                speak(f"Opening {app_name}")
                threading.Thread(target=open_app, args=(app_name,)).start()
    elif "close" in c.lower():
        apps_string = c.lower().split("close", 1)[1]

        # Split using commas or 'and' or 'also'
        import re
        app_list = re.split(r",| and | also", apps_string)

        for app_name in app_list:
            app_name = app_name.strip()
            if app_name:
                speak(f"closing {app_name}")
                threading.Thread(target=close_app, args=(app_name,)).start()


'''Main Part'''



if __name__ == "__main__":
    #This is what it speaks at first
    
    speak("Hi, My name is jarvis. How can I help You?")
    #loop for continues listening
    r=sr.Recognizer()
    while True:
        try:
           
            #Activating Microphone to hear our commands
            with sr.Microphone() as source:
                print("Listening...")
                # For Listening
                audio = r.listen(source)
                r.adjust_for_ambient_noise(source,duration=1)
            # Using google recognizer for less errors.
            word = r.recognize_google(audio).lower()
            print("recognising..")
            print(f"you :{word}")
            #Function to print the command
            if "bye" in word.lower():
                speak("ok bye sir! if you need any help,just call me.")
                sys.exit()
            #Only do when we call it with name(jarvis)
            if "jarvis" in word.lower():
                speak("Yes?")
                while True:
                    try:
                    #again Taking command
                        with sr.Microphone() as source:
                            print("jarvis Activated...,listening for your command")
                            r.adjust_for_ambient_noise(source,duration=1)
                            audio = r.listen(source)
                        command = r.recognize_google(audio).lower()
                        print(f"you :{command}")
                        if "stop listening" in command.lower():
                            speak("oh! sure sir.")
                            break
                        # if "ask ai" in command.lower():
                        #     question = command.replace("ask ai", "").strip()
                        #     speak("Let me process this with OpenAI.")
                        #     response = openAIResponse(question)
                        #     speak(response)
                        #     continue
                        processCommand(command)
                        continue
                    except Exception as e:
                        print("I can't understand!")
                        speak("I can't understand")
        except Exception as e:
            print("I can't understand!")