import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's command
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said: " + command)
            return command
        except sr.UnknownValueError:
            return "Could not understand your command."
        except sr.RequestError:
            return "Could not request results; check your network connection."

# Main loop
while True:
    command = listen()
    if "hello" in command:
        speak("Hello! How can I assist you?")
    elif "what is your name" in command:
        speak("I am your Python voice assistant.")
    elif "goodbye" in command:
        speak("Goodbye!")
        break
    else:
        speak("I didn't understand your command. Please try again.")
