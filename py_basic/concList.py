list_a = [1, 2, 3]
list_b = [4, 5, 6]

list_ab = list_a + list_b #-> concatenção de listas, + faz polimorfismo
print(list_ab)


print('-' * 18)


list_a.extend(list_b) #-> .extend() "junta" com outra lista, mas não entrega nenhum valor em si.
print(list_a)

