import requests
from pathlib import Path
from pprint import pprint

# configurado pprint
_print = print
print = pprint

# endpoint da API
URL = 'http://localhost:3001/tokens'

TOKEN_PATH = Path(__file__).parent / 'token.txt'

# credenciais usuario que eu vou logar
user_data = {
    "password": "654321",
    "email": "vinisant@email.com"
}

# fazendo a request e pegando a resposta:
response = requests.post(URL, json=user_data)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucessos
    print(f'Status code: {response.status_code}')
    # mensagem do status code:
    print(f'Reason: {response.reason}')
    print(f'JSON: {response.json()}')

    # atribuindo o retorno da request a uma variavel:
    response_data = response.json()
    # atribuindo o token(JSON = dict, facil de manipular) a uma variavel:
    token = response_data['token']

    # Criando um arquivo e escrevendo o token que o request no endpoint da API
    #   me retornou:
    with open(TOKEN_PATH, 'w', encoding='utf8') as file:
        file.write(token)

else:
    # Erros
    print(f'Status code: {response.status_code}')
    # mensagem do status code:
    print(f'Reason: {response.reason}')
    print(f'Text: {response.text}')
