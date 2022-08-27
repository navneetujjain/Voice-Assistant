import speech_recognition as sr
import pyttsx3
import pywhatkit



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
            engine.say(f"You asked me to play {command} , Wait a minute I'm just going to play the song")
            engine.runAndWait()
            pywhatkit.playonyt(command)
    else:
        engine.say("You didn't called James, Please Rerun The Program And Try Again!!")
        engine.runAndWait()
