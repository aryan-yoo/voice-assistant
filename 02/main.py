import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
from songs import songs
import songs
import smtplib


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def  get_audio():
    with sr.Microphone() as source:
        print("listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except  sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except  sr.UnknownValueError:
            print("Sorry, I could not understand what you said")


def processcommand(c):
    if c.startswith("open "):
        try:
            page = c.split()[1]
            url = f"https://www.{page}.com"
            webbrowser.open(url)
        except IndexError:
            print("Invalid input. Please use the format 'open <page>'")
    elif(c.startswith("play ") and c.endswith(" song")):
        try:
            song = c.split()[1]
            url = songs["die for you"]
            webbrowser.open(url)
            print("Playing " + song)
        except:
            print("The song you ask for is not in the playlist")
    elif("wikipedia" in c.lower()):
        try:
            search = c.replace("wikipedia","").split()
            result = wikipedia.summary(" ".join(search), sentences=2)
            print(result)
            speak(result)
        except:
            print("Invalid input. Please use the format 'wikipedia <search>'")
    elif(c.lower() == "send mail"):
        try:
            server = smtplib.SMTP('smtp-mail.outlook.com',587)
            username = "aryanchristian55@gmail.com"
            password = "9173649500Aryan"
            server.ehlo()
            server.starttls()
            server.login(username, password)
            speak("What is the subject of the email")
            subject = get_audio()
            print(subject)
            speak("What is the body of the email")
            body = get_audio()
            print(body)
            speak("What is the recipient's email")
            recipient = get_audio().replace(" ","")
            email_text = f"From: {username}\nTo: {recipient}\nSubject: {subject}\n\n{body}"
            server.sendmail(username,recipient,email_text)
            server.quit()
            speak("Email sent")
        except:
            print("Invalid input. Please use the format 'send email'")






if __name__ == "__main__":
    speak("initializing 0...")
    while True:
        r = sr.Recognizer()
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio = r.listen(source, timeout=2,phrase_time_limit=2)
            word = r.recognize_google(audio)
            print(word)
            if(word.lower() == "0" or word.lower() == "zero"):
                speak("yea")
                command = get_audio()
                processcommand(command)

                    
                   
        except sr.UnknownValueError:
            print("sorry, i could not understand the audio")
        except sr.RequestError as e:
            print("could not pass the request")
        except Exception as e:
            print("Error:{}".format(e))

