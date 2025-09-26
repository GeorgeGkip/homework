import smtplib
from email.message import EmailMessage
from django.template.loader import render_to_string
import os
# from string import Template
# from pathlib import Path
# from dotenv import load_dotenv

# load_dotenv()

def registration_email(user):
    
    html_content = render_to_string('users/registration_email.html', {'username': user.username})

    
    email = EmailMessage()
    email['from'] = 'Homework Team'
    email['to'] = user.email
    email['subject'] = 'Welcome to Homework!'
    
    email.set_content(html_content, 'html')
    
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('contact.homeworkapp@gmail.com', os.environ.get('EMAIL_REGISTRATION_PASSWORD'))
        smtp.send_message(email)