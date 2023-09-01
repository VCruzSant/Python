# Requisições HTTP

import requests

# http -> porta 80
# https -> porta 443

url = 'http://localhost:3000/'
response = requests.get(url)

# resposta geral do servidor
print(response)

# código que o servidor respondeu
print(response.status_code)

# cabeçalho que o servidor respondeu
print(response.headers)

# conteudo em bites que o servidor respondeu
# print(response.content)

# conteudo em texto html que o servidor respondeu
print(response.text)
