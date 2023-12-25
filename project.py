import smtplib
import speech_recognition  as sr
from email.message import EmailMessage
import pyttsx3

listener = sr.Recognizer()
tts = pyttsx3.Engine()

def talking_tom(text):
    tts.say(text)
    tts.runAndWait()


def mic():
    with sr.Microphone() as source:
        print("Talk")
        voice = listener.listen(source)
        data = listener.recognize_google(voice)
        print(data)
        return data.lower()

dict = {"test":"rajmayank79799@gmail.com"}

def send_mail(receiver , subject , body):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("project96619@gmail.com","dxghikiuidbtgzws")
    email = EmailMessage()
    email["from"] = "project96619@gmail.com"
    email["to"]= receiver
    email["subject"] = subject
    email.set_content(body)
    server.send_message(email)

def main_poc():
    talking_tom("whom do you want to send this email ?")
    name = mic()
    receiver = dict[name]
    talking_tom("what's the subject of the email")
    subject = mic()
    talking_tom("speak the body of the email")
    body = mic()
    send_mail(receiver , subject , body)
    print("email sent successfully")
main_poc()