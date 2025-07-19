import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2 as cv
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import pyautogui
import time
import openai
import requests
import json
import smtplib
import sys
import torch
import pyjokes
import joblib
from notepad import open_notepad, close_notepad, write_on_notepad
from instagram import instagram
from pdf import pdfreader
from hide_files import hide

# Load saved model and vectorizer
model = joblib.load("JARVIS/jarvis_model.pkl")
vectorizer = joblib.load("JARVIS/jarvis_vectorizer.pkl")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)

engine.setProperty('voices',voices[0].id)

contacts = {
    "ansh":"+919815594491",
    "kushagr":"+919116682263"
}

#text to speach
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def predict_intent(text):
    text_vec = vectorizer.transform([text])
    pred = model.predict(text_vec)
    return pred[0]

#voice to text 
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1  # Wait for 1 second of silence before stopping recording

        r.energy_threshold = 200  # Minimum loudness needed to detect speech

        r.dynamic_energy_threshold = True  # Automatically adjust loudness sensitivity based on background noise

        r.adjust_for_ambient_noise(source, duration=1)  # Listen for 1 second to background noise to calibrate

        audio = r.listen(source,timeout=5,phrase_time_limit=8)
        
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}")
    
    except Exception as e:
        speak("Speak that again please...")
        return "none"
    
    return query
        
#to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    
    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour >12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am jarvis , How may I help you!")

#send email
def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('aloc1345@gmail.com','gqmx tzzu bmkv ryir')
    server.sendmail('aloc1345@gmail.com',to,content)
    server.close()

def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=5e32c849b61e426abfc90f7d55451d25'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is {head[i]}")
        
if __name__ == "__main__":
    wish()
    while True:
    # if 1:
        query = takecommand().lower()
        
        #logic building for task
        intent = predict_intent(query)
        
        if intent == "open_notepad":
            open_notepad()
            speak("Notepad is open. What would you like me to write?")
            while(True):
                text_to_write = takecommand().lower()
                intent = predict_intent(text_to_write)
                if text_to_write:
                    write_on_notepad(text_to_write)
                
                if intent == "close_notepad":
                    close_notepad(speak)
                    break
                
        elif "open cmd" in query:
            os.system("start cmd")
            
        elif "open camera" in query:
            cap = cv.VideoCapture(0)
            while True:
                ret, img = cap.read()
                if not ret:
                    print("Failed to capture image")
                    break;
                cv.imshow("webcam",img)
                k = cv.waitKey(50)
                if k == 27:
                    break; 
            cap.release()
            cv.destroyAllWindows()
            
        elif "play music" in query:
            musicdir = "C:\\Users\\Jatin bagga\\Desktop\\ML\\music"
            songs = os.listdir(musicdir)
            rd = random.choice(songs)
            os.startfile(os.path.join(musicdir,rd))
            
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip adress is {ip}")
            
        elif "wikipedia" in query:
            speak("searching wikipedia... " )
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("according to wikipedia")
            speak(results)
            # print(results)
            
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
            
        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")
            
        elif "open google" in query:
            speak("Sir, what should I search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
            
        elif "send message" in query:
            speak("Whom do you want to send the message")
            name = takecommand().lower().replace(" ", "")
        
            speak("what is the message")
            msg = takecommand()
              
            webbrowser.open("https://web.whatsapp.com")
            time.sleep(10)  # Wait for WhatsApp Web to fully open

            pyautogui.click(x=304, y=220)  # Click on search bar (adjust x, y as per your screen)
            pyautogui.write(name)
            pyautogui.press('enter')
            time.sleep(2)

            pyautogui.write(msg)
            pyautogui.press('enter') 
                 
        elif "where am i" in query or "my location" in query:
            try:
                ip_info = requests.get('https://ipinfo.io').json()
                city = ip_info.get('city')
                region = ip_info.get('region')
                country = ip_info.get('country')
                speak(f"You are in {city}, {region}, {country}")
            except Exception as e:
                speak("Sorry, I couldn't fetch your location.")

        elif "play songs on youtube" in query:
            speak("what song you want to listen")
            task = takecommand().lower()
            kit.playonyt(task)
            
        elif "take screenshot" in query:
            speak("Taking screenshot...")
            img = pyautogui.screenshot()
            img.save("screenshot.png")
            speak("Screenshot saved as screenshot.png")

        elif "send email"in query:
            
            speak("what do you want to say")
            content = takecommand().lower()
            to = "jbagga_be22@thapar.edu"
            sendEmail(to,content)
                  
        # elif intent == "close_notepad":
        #     close_notepad(speak)
        
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke();
            speak(joke)
            
        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            
        elif "tell news" in query:
            speak("please wait sir, telling the news")
            news()
            
        elif "instagram profile" in query:
            instagram(speak, query,takecommand)
            
        elif "read pdf " in query:
            pdfreader(speak)
            
        elif "hide folder" in query:
            hide(takecommand, speak)
            
        elif "you can sleep now" in query:
            speak("Thanks for using me")
            sys.exit()
        

        