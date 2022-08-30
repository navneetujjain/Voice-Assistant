import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


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
                engine.say(info)
                engine.runAndWait()
            elif "search" in command:
                search = command.replace("search", "")
                info = wikipedia.summary(search, 2)
                engine.say(info)
                engine.runAndWait()
            elif "who is" in command:
                search = command.replace("who is", "")
                info = wikipedia.summary(search, 2)
                engine.say(info)
                engine.runAndWait()
        elif "jokes" in command or "joke" in command:
            engine.say(pyjokes.get_joke())
            engine.say("Wasn't That Funny? Yes Na. Then Laugh Ha ha ha ha ha hi hi hi hu hu hu")
            engine.runAndWait()
        elif "are you in a relatioship" in command:
            engine.say("Yes, I am in a relationship with wifi")
            engine.runAndWait()
        elif "will you marry me" in command:
            engine.say("It's better to marry a girl than marrying a virtual assistant")
            engine.say("I will suggest you to install bumble and start looking for girls")
            engine.runAndWait()    
        else:
            engine.say("I am Still Learning Things And I'm Sorry To Inform You That I Don't Know What You Asked")
            engine.say("Maybe Next Time, Till Then Rerun The Program And Ask Me Something That I Know")
            engine.runAndWait()

    else:
        engine.say("You didn't called James, Please Rerun The Program And Try Again!!")
        engine.runAndWait()
