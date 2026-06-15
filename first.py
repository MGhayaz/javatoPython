# import pyjokes
# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Hello, I am your assistant. How can I help you?")
# engine.runAndWait()
# jokes = pyjokes.get_joke()
# print(jokes)
# print("""Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.
# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.
# Then the trav'ller in the dark,
# Thanks you for your tiny spark,
# He could not see which way to go,
# If you did not twinkle so.
# In the dark blue sky you keep,
# And often thro' my curtains peep,
# For you never shut your eye,
# Till the sun is in the sky.
# 'Tis your bright and tiny spark,
# Lights the trav'ller in the dark:
# Tho' I know not what you are,
# Twinkle, twinkle, little star.""")
import os

# specify the directory path you want to list
directory = "c:/Users/moham/Downloads/Development"

try:
    # os.listdir() returns a list of all entries in the directory
    contents = os.listdir(directory)

    print(f"Contents of '{directory}':")
    for entry in contents:
        print(entry)

except FileNotFoundError:
    print("Error: The specified directory does not exist.")
except PermissionError:
    print("Error: Permission denied to access this directory.")