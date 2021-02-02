from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import wolframalpha
import wikipedia
import webbrowser
import random
from string import Template

#import speech_recognition as sr
#import pyttsx3

# Create your views here.

# Create your views here.
def home(request):
    template_name = 'APP/home.html'

    return render(request, template_name)

def chat(request):
    return render(request, 'APP/chat_view.html')


def bot_search(request):
    query = request.GET.get('query')
    # firstly we'll convert the inputed text into lower form
    text = query.lower()
    #Jarvis Greetings
    jarvis_greetings=['hi this is jarvis....how can i help u..?', 'hi jarvis there','hey ...how jarvis can help u...', 'hello', 'hi', 'hi there', 'hola', 'howdy', 'hey', 'hey there....', 'holaaa...']
    #user Greetings
    user_greetings = ['hello', 'hi', 'hi there', 'holaa...', 'howdy', 'hey', 'hey there', 'hellooooo', 'hiiiii']
    #exit chat
    exit_chat = ['bye','exit']

    for words in text.split():
        if words in user_greetings:
            return render(request, 'Myapp/chat_view.html', {'ans': random.choice(jarvis_greetings), 'query': query})
        elif words in exit_chat:
            return redirect('home') 
 

    try:
        client = wolframalpha.Client("LR923L-9T34JW6H9Q")
        res = client.query(query)
        ans = next(res.results).text
        return render(request, 'Myapp/chat_view.html', {'ans': ans, 'query': query})

            
    except Exception:
        try:
            ans = wikipedia.summary(query, sentences=5)
            return render(request, 'Myapp/chat_view.html', {'ans': ans, 'query': query})


        except Exception:
            ans = "FOUND NOTHING"
            return render(request, 'Myapp/chat_view.html', {'ans': ans, 'query': query})

def mail(request):
    return render(request, 'Myapp/send_mail.html')

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def send_mail(request):
    # Send email to visitor as well as owner
    # creates SMTP session
    email = request.GET.get('email')
    name = request.GET.get('name')
    message = request.GET.get('message')

    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("Your Mail ID", "Your Pass Key")

    msg = MIMEMultipart()
    message_template = read_template('Myapp/message.txt')
    message = message_template.substitute(PERSON_NAME=name,MESSAGE=message)
    msg['From'] = 'Your Mail ID'
    msg['To'] = email
    msg['Subject'] = "CONFORMATION MAIL"
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    try :
        s.send_message(msg)
        s.quit()
        ans = "Message Sent"
        return render(request, 'Myapp/send_mail.html', {'ans': ans})
    except Exception as e:
        s.quit()
        ans = "Message Not Sent"
        return render(request, 'Myapp/send_mail.html', {'ans': ans})
    # terminating the session
    
<<<<<<< HEAD

=======
>>>>>>> bd6b110c4cd35d74a9491721fe2a7604fb395549
