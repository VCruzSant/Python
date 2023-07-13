import json
import os

FILE_NAME = 'my_j.json'
# abspath pega o caminho absoluto do diretório como um todo, desde a raiz até
# o local
# dirname(__file__) -> meu dir atual -> modules
# depois o join junta meu diretório atual com o nome do arquivo
# gerando -> c:\codando 1\Python\modules\my_j.json
PATH_ABSOLUTE = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        FILE_NAME
    )
)
# print(PATH_ABSOLUTE)
# print(os.path.abspath(os.path.dirname(__file__)))

movie = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',
    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}


with open(PATH_ABSOLUTE, 'w', encoding='utf8') as file:
    json.dump(movie, file, ensure_ascii=False, indent=2)

with open(PATH_ABSOLUTE, 'r', encoding='utf8') as file:
    json_movie = json.load(file)
    print(json_movie)
