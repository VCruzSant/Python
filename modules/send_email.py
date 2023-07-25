# enviando E-mails com SMTP python
import os
from dotenv import load_dotenv

load_dotenv()

# Dados remetente e destinatário -> get no .env
sender = os.getenv('FROM_EMAIL', '')
addresser = sender

# Configurações SMTP
