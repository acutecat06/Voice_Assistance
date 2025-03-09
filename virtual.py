import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec

print("Loading your AI personal assistant - Madmax, made by Adyasha")

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Ensure correct voice selection

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello, Good Morning")
        print("Hello, Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello, Good Afternoon")
        print("Hello, Good Afternoon")
    else:
        speak("Hello, Good Evening")
        print("Hello, Good Evening")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"User--> {statement}\n")
            return statement.lower()
        except Exception as e:
            speak("Pardon me, please say that again.")
            return "None"

speak("Loading your AI personal assistant - Madmax, made by Adyasha")
wishMe()

if __name__ == '__main__':
    while True:
        speak("Tell me, how can I help you now?")
        statement = takeCommand()

        if statement == "none":
            continue

        if "goodbye" in statement or "ok bye" in statement or "stop" in statement or "bye" in statement:
            speak("Your personal assistant Madmax is shutting down. Goodbye!")
            print("Your personal assistant Madmax is shutting down. Goodbye!")
            break

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("YouTube is open now.")
            time.sleep(3)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google Chrome is open now.")
            time.sleep(3)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://mail.google.com")
            speak("Google Mail is open now.")
            time.sleep(3)

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            print("Time is", strTime)

        elif 'who are you' in statement or 'what can you do' in statement:
            speak("I am Madmax version 1.0, your personal assistant. "
                  "I can open YouTube, Google, Gmail, Stack Overflow, predict time, take a photo, "
                  "and fetch top news headlines from Times of India.")

        elif "made" in statement or "created" in statement:
            speak("I was built by Adyasha in 2024 ")
            print("I was built by Adyasha in 2024 ")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com")
            speak("Here is Stack Overflow.")

        elif 'news' in statement:
            webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak("Here are some headlines from the Times of India. Happy reading!")
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            print("Taking a photo. Please wait 5 seconds.")
            speak("Taking a photo. Please wait 5 seconds.")
            ec.capture(0, "Robo Camera", "img.jpg")

        elif 'search' in statement:
            statement = statement.replace("search", "").strip()
            webbrowser.open_new_tab(f"https://www.google.com/search?q={statement}")
            speak(f"Searching for {statement}")
            time.sleep(5)

        elif "open presentation" in statement or "open ppt" in statement:
            speak("Opening your presentation.")
            path = r"#"  # Replace with actual file path
            subprocess.Popen([path], shell=True)
            time.sleep(5)

        elif "off" in statement or "shutdown" in statement:
            print("Shutting down your PC.")
            speak("Ok, your PC will shut down in 10 seconds. Make sure you exit all applications.")
            time.sleep(6)
            subprocess.call(["shutdown", "/s", "/t", "10"])

        elif "relax" in statement or "favorite song" in statement:
            print("Playing your favorite song to relax.")
            speak("Playing your favorite song to relax.")
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=Z1ijuWA9Sfs&list=RDZ1ijuWA9Sfs&start_radio=1")

        elif "resume" in statement:
            print("Opening your resume. Please wait a moment.")
            speak("Opening your resume. Please wait a moment.")
            resume_path = r"#"
            subprocess.Popen([resume_path], shell=True)

        elif "linkedin" in statement:
            print("Opening your LinkedIn profile.")
            speak("Opening your LinkedIn profile.")
            webbrowser.open_new_tab("#")

        elif "github" in statement:
            print("Opening your GitHub account.")
            speak("Opening your GitHub account.")
            webbrowser.open_new_tab("#")

time.sleep(5)
