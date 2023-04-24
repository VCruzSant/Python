# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list

people = {
    'name': 'vini',
    'surname': 'sant',
    'yearsold': '19',
    'adress':   [
        {'street': 'Lorem', 'numb': 24},
        {'otherstreet': 'anyLorem', 'numb': 87},
    ], #dict dentro de dict
}

#print(people, type(people))
print(people['name'])

for key in people:
    print(f'{key}: {people[key]}')
