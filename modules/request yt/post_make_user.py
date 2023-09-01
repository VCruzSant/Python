import requests
from pprint import pprint

_print = print
print = pprint

URL = 'http://localhost:3001/users'

user_data = {
    "nome": "vini sant",
    "password": "654321",
    "email": "vinisant@email.com"
}

response = requests.post(URL, json=user_data)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucessos
    print(f'Status code: {response.status_code}')
    # mensagem do status code:
    print(f'Reason: {response.reason}')
    print(f'JSON: {response.json()}')

else:
    # Erros
    print(f'Status code: {response.status_code}')
    # mensagem do status code:
    print(f'Reason: {response.reason}')
    print(f'Text: {response.text}')
