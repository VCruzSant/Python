lista = ['vin', 'da', 'cruz']
lista.append('sant')

print(lista)

#lista_enumerated = enumerate(lista) --->enumera os números, mas não é possivel dar o print porque é apenas um iterator -> type: tuple
lista_enumerated = list(enumerate(lista)) #dessa forma é possivel salvar o enumerated numa variavel e imprimi-lá
print(lista_enumerated)

for indice, iten in enumerate(lista): #iterando para ver o valor enumerado 
    print(indice, iten)