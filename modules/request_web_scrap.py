# + Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - pip install requests types-requests bs4
import requests
from bs4 import BeautifulSoup

# definindo url
URL = 'http://localhost:3001/'
# mandando requisição get na url:
response = requests.get(URL)
# definindo html do site que eu mandei a requisição:
raw_html = response.text
# html convertido:
parse_html = BeautifulSoup(raw_html, 'html.parser')
# Pegando tudo:
# print(parse_html)

# Apenas o titulo:
print(parse_html.title)

# apenas o texto do titulo sem a tag html:
# coloquei o if pq a tipagem diz que pode retornar 2 coisas:
if parse_html.title is not None:
    print(parse_html.title.text)
