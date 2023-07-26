# enviando E-mails com SMTP python
import smtplib
import os
from pathlib import Path
from string import Template
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

# caminho do html
PATH_FILE_HTML = Path(__file__).parent / 'send_email_file.html'

# Dados remetente e destinatário -> get no .env
sender = os.getenv('FROM_EMAIL', '')
addresser = sender

# Configurações SMTP
smtp_server = os.getenv("SMTP_SERVER", '')
smtp_user = os.getenv("FROM_EMAIL", '')
smtp_pass = os.getenv("EMAIL_PASS", '')
smtp_port = os.getenv("SMTP_PORT")

# mensagem de texto
with open(PATH_FILE_HTML, 'r', encoding='utf8') as file:
    reader = file.read()
    template = Template(reader)
    txt_email = template.substitute(name='Vini')

# transformar a mensagem em MIMEMultipart

mime_multipart = MIMEMultipart()
mime_multipart['from'] = sender
mime_multipart['to'] = addresser
mime_multipart['subject'] = 'Assunto do E-mail: blabla'

email_body = MIMEText(txt_email, 'html', 'utf-8')
mime_multipart.attach(email_body)

# Envia e-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_user, smtp_pass)
    server.send_message(mime_multipart)
    print('e-mail enviado com sucesso')
