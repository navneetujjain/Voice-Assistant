import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.say("Hello Main Hoo Desi James")
print("engine said")
engine.say("Please Tell Me What Can I Do For You")
engine.runAndWait()
with sr.Microphone() as source:
    print("James is Listening To You")
    voice = listener.listen(source)
    command = listener.recognize_google(voice)
    command = command.lower()
    if "james" in command:
        command = command.replace("james", "")
        if "play" in command:
            command = command.replace("play", "")
            engine.say(f"You asked me to play {command} , Wait a moment I'm just going to play the song")
            engine.runAndWait()
            pywhatkit.playonyt(command)
        elif "time" in command:
            command = datetime.datetime.now().strftime("%I:%M %p")
            engine.say(f"The Time Is {command}")
            engine.runAndWait()
        elif "wikipedia" in command or "search" in command or "who is" in command:
            if "wikipedia" in command:
                search = command.replace("wikipedia", "")
                info = wikipedia.summary(search, 2)

            elif "search" in command:
                search = command.replace("search", "")
                info = wikipedia.summary(search, 2)
            elif "who is" in command:
                search = command.replace("who is", "")
                info = wikipedia.summary(search, 2)

    else:
        engine.say("You didn't called James, Please Rerun The Program And Try Again!!")
        engine.runAndWait()
