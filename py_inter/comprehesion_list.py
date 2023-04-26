#List Comprehesion -> forma rápida de criar listas
print(list(range(10)))

lista = []
for numb in range(10):
    lista.append(numb)
# print(lista)

lista_1 = [1 for numb in range(10) ]
print(lista_1)

lista = [numb for numb in range(10)]
print(lista)

list_mult = [numb * 2 for numb in range(10)]
print(list_mult)