import pprint

def p(inf):
    pprint.pprint(inf,  sort_dicts=False, width=37)

#List Comprehesion -> forma rápida de criar listas
#print(list(range(10)))

lista = []
for numb in range(10):
    lista.append(numb)
# print(lista)

lista_1 = [1 for numb in range(10) ]
# print(lista_1)

lista = [numb for numb in range(10)]
# print(lista)

list_mult = [numb * 2 for numb in range(10)]
# print(list_mult)

#mapeamento de dados in list comprehension
products = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

new_products = [
    {**prdt, 'preco': prdt['preco'] * 1.1}
    if prdt['preco'] > 10 else {**prdt}
    for prdt in products
]

# print(*new_products, sep='\n')

# p(new_products)

lista = [iten for iten in range(11) if iten < 6]
print(lista)