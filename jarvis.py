import datetime
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice
#print(voices[1].id)

engine.setProperty('voice', voices[0].id)

def speak(audio):

    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')

speak('Iam Jarvis, how may i help you?')

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query

if __name__=="__main__" :
    wishme()
    takeCommand()