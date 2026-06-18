import pyttsx3

engine = pyttsx3.init()

engine.say("one")
engine.say("two")
engine.say("three")

engine.runAndWait()