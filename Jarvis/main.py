import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclib


def speak(text):
    print("speaking... "+ text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait() 
    engine.stop()

def processcommand(command):
    command = command.lower().strip()

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
    elif command.startswith("play"):
        song = command.splits(" ")[1]       
        link = musiclib.music(song)
        webbrowser.open(link)

if __name__ == "__main__":
    speak("INITIALIZING IRSHARD BHAI.....")
    while True:
        recognizer = sr.Recognizer() 
        print("Recognizing")    
        try :
            with sr.Microphone() as mic:
                print("Listening")
                audio = recognizer.listen(mic,timeout=4,phrase_time_limit=1)
            word = recognizer.recognize_google(audio)
            print(word)
            if word.lower() == "jarvis":
                speak("meet the sweet sound")
                with sr.Microphone() as mic:
                    print("Jarvis is active")
                    audio = recognizer.listen(mic)
                command = recognizer.recognize_google(audio)

                processcommand(command)
        except sr.UnknownValueError :
            print("Unknown value error")
        except Exception as e :
            print("Google recorgnizer error or other" + e)           

