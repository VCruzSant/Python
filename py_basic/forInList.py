"""
for in with list
"""

lista = ["vinicius", "cruz", "santiago"]
indic = range(len(lista))

for nome in lista:  # itera sobre os valores da lista
    print(nome)

print("-" * 10)

for letra in lista[1]:  # itera sobre um valor especificado dentro de uma lista
    print(letra)

print("-" * 10)

for indice in indic:
    print(indice, lista[indice])
