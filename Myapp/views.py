from django.shortcuts import render

# Create your views here.
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

# Function for sending mail ////////////////////////////////////////////////////////////////////////////////////////////

def send_mail(name, email, message):
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("mitchellanthony1999august@gmail.com", "uqrrvfnreoetqhqq")

    msg = MIMEMultipart()
    message_template = read_template('APP/message.txt')
    message = message_template.substitute(PERSON_NAME=name,MESSAGE=message)
    msg['From'] = 'mitchellanthony1999august@gmail.com'
    msg['To'] = email
    msg['Subject'] = "CONFORMATION MAIL"
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    try :
        s.send_message(msg)
        s.quit()
        ans = "Message Sent"
        return render(request, 'APP/send_mail.html', {'ans': ans})
    except Exception as e:
        s.quit()
        ans = "Message Not Sent"
        return render(request, 'APP/send_mail.html', {'ans': ans})
    # terminating the session
    