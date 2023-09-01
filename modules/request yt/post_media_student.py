import requests
from pprint import pprint
from get_token import token
from requests_toolbelt import MultipartEncoder
from mimetypes import MimeTypes

_print = print
print = pprint

# caminho do arquivo de foto:
midia_path = 'C:\\codando 1\\Python\\modules\\request yt\\python_logo.png'

# identificando tipo de arquivo:
mimetypes = MimeTypes()
mime_file = mimetypes.guess_type(midia_path)[0]

# open necessário para enviar os bites do arquivo | rb -> bites
multipart = MultipartEncoder(fields={
    'aluno_id': '1',
    'foto': (midia_path, open(midia_path, 'rb'), mime_file)
})


URL = 'http://localhost:3001/fotos'

headers = {
    'Authorization': token,
    'Content-Type': multipart.content_type
}


response = requests.post(URL, headers=headers, data=multipart)

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
