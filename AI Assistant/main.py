
import pyttsx3  #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

# print(voices[0].id)------David Voice
# print(voices[1].id)------Zira Voice

engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am jarvis Sir. Please tell me how may I help U")

def takeCommand():
    # It take Input from user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 #-----second of Non Speaking audio before a phrase is considered complete------
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said :  {query}\n")
    except Exception as e:
        # print(e)
        print("Say that Again, Please...")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()

if __name__=="__main__":
    # speak("Hello Good Morning")
    wishMe()
    # while True:
    if 1:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'play music' in query:
            music_dir='C:\\Users\\gaura\\Desktop\\Python Projects\\AI Assistant\\music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'time now' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"the time is{strTime}")
        
        elif 'open code' in query:
            codePath="C:\\Users\\gaura\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to gaurav' in query:
            try:
                speak("What should i send")
                content=takeCommand()
                to="gauravsingh27012000@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent Successfully!")
            except Exception as e:
                print(e)
                speak("I am sorry! I cannot send this email at the Moment")