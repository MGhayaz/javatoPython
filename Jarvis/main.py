import speech_recognition as sr
import webbrowser
import requests
import pyttsx3
# local music library
import musiclib
# importing function from gemini service script to render and collect ai related interaction
from gemini_service import ask_ai

# api key leke aaye from config jo env se key utayi. param use kare for clear formating
from config import NEWS_API_KEY
if not NEWS_API_KEY:
    raise ValueError("NEWS_API_KEY not found")
url = "https://newsapi.org/v2/top-headlines"
params = {
    "country": "in",
    "apiKey": NEWS_API_KEY
}

def speak(text):
    engine = pyttsx3.init()
    print("speaking..."+ text)
    engine.say(text)
    engine.runAndWait() 
    engine.stop()

def processcommand(command):
    command = command.lower()

    if "youtube" in command:
        webbrowser.open("https://www.youtube.com")

    elif "chatgpt" in command or "open ai" in command:
        webbrowser.open("https://chatgpt.com")

    elif "linkedin" in command:
        webbrowser.open("https://www.linkedin.com")

    elif "gemini" in command:
        webbrowser.open("https://gemini.google.com")

    elif "github" in command:
        webbrowser.open("https://github.com")

    elif "leetcode" in command:
        webbrowser.open("https://leetcode.com")

    elif "claude" in command:
        webbrowser.open("https://claude.ai")

        #LOCAL MUSIC DICT SE GANE CHALARA BY MATCHING KEY LIKE SKYFALL   
    elif command.startswith("play"):
        song = command.replace("play","",1).strip()       
        link = musiclib.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Song not found")

        # news lane ka code block through api called NewsAPI
    elif "latest" in command.lower():
        r = requests.get(url, params=params)
        if(r.status_code ==200):
            data = r.json()   
            articles = data.get('articles',[]) 
            for article in articles :
                speak(article["title"])   
        else :
            print("failed to retrieve") 
    elif command != "": 
        answer = ask_ai(command)
        speak(answer)
                       

if __name__ == "__main__":
    speak("INITIALIZING IRSHARD BHAI.....")
    recognizer = sr.Recognizer() 
    while True:  
        print("Recognizing")    
        try :
            with sr.Microphone() as mic:
                print("Listening")
                audio = recognizer.listen(mic,timeout=3,phrase_time_limit=2)
            word = recognizer.recognize_google(audio)
            print(word)
            if word.lower() == "jarvis":
                speak("Yeayy")
                with sr.Microphone() as mic:
                    print("Jarvis is active")
                    audio = recognizer.listen(mic)
                command = recognizer.recognize_google(audio)

                processcommand(command)
        except sr.UnknownValueError :
            print("Unknown value error")
        except Exception as e :
            print("Google recorgnizer error or other" , e)           

