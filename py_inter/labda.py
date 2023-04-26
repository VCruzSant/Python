# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.


lista = [
    1,
    2,
    3,
    7,
    4,
    6,
    5,
]
lista.sort()  # ordena
# sorted(lista) -> shallow copy ordenada
# lista.sort(reverse=True) reverse

lista_name = [
    {"nome": "Luiz", "sobrenome": "miranda"},
    {"nome": "Maria", "sobrenome": "Oliveira"},
    {"nome": "Daniel", "sobrenome": "Silva"},
    {"nome": "Eduardo", "sobrenome": "Moreira"},
    {"nome": "Aline", "sobrenome": "Souza"},
]

# def ordened(item):
#     return item['nome'] -> ensinando o python a organizar

# lista_name.sort(key=ordened)-> pedindo pro python organizar

# lista_name.sort(key=lambda item:item['nome']) -> utilizando lambda para ensinar e organizar


def ordened(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista_name, key=lambda item: item["nome"])  # criando uma shallow copy
l2 = sorted(lista_name, key=lambda item: item["sobrenome"])  # criando uma shallow copy

ordened(l1)
ordened(l2)
