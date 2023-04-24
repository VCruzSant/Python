# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

people = {
    'name': 'vini',
    'surname': 'sant',
}

print(len(people)) 

for chave in people.keys():
    print(chave)

for value in people.values():
    print(value)

for chave, value in people.items():
    print(chave,':', value)

people.setdefault('yearsold', 120)
print(people['yearsold'])