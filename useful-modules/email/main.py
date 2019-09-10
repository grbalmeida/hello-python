from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

from config import email, password, sender, subject

path = 'useful-modules/email'

with open(f'{path}/template.html', 'r') as html:
  template = Template(html.read())
  current_date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
  page_body = template.substitute(name='Luiz Otavio', date=current_date)

message = MIMEMultipart()
message['from'] = sender
message['to'] = email
message['subject'] = subject

body = MIMEText(page_body, 'html')
message.attach(body)

with open(f'{path}/image.jpeg', 'rb') as image:
  image = MIMEImage(image.read())
  message.attach(image)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login(email, password)
  smtp.send_message(message)
  print('Email successfully sent')
