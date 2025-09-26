import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
# from dotenv import load_dotenv
import os


# load_dotenv()

def registration_email(user):
    
    html_template_path = Path('users') / 'templates' / 'users' / 'registration_email.html'
    html_content = html_template_path.read_text()
    html = Template(html_content)
    
    email = EmailMessage()
    email['from'] = 'Homework Team'
    email['to'] = user.email
    email['subject'] = 'Welcome to Homework!'
    
    email.set_content(html.substitute(username= user.username), 'html')
    
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('contact.homeworkapp@gmail.com', os.environ.get('EMAIL_REGISTRATION_PASSWORD'))
        smtp.send_message(email)