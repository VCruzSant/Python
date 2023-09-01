import requests
from pprint import pprint
from get_token import token

_print = print
print = pprint

URL = 'http://localhost:3001/alunos/1'

headers = {
    'Authorization': token
}

student_data = {
    "nome": "Enzo",
    "sobrenome": "JuniorFilho",
    "email": "enzo@email.com",
    "idade": "16",
    "peso": "60",
    "altura": "1.68"
}

response = requests.put(URL, json=student_data, headers=headers)

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
