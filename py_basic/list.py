"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
Lista vazia -> falsy
Dica: evite mover muita coisa na lista quando tiver vários indices para o programa não ficar lento
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
#         0      1    2     3
lista = ['Vini', 123, True, []] #list()
print(lista[0].upper())# .upper() -> converte para letras maiúsculas
lista[-3] = 321
print(lista, lista[1])
del lista[1] #exclui o indice selecionado
print(lista)
lista.pop() # -> remove o ultimo item da lista, até o momento seria o []
lista.append('novo indice')#.append -> adiciona item no final da list
lista.append('mais um ind')
print(lista)
exclui = lista.pop(2) #posso apontar um indice para o pop remover e ainda salva-lo numa variavel 
print(f"{lista} removido: {exclui}")
print(lista)
lista.insert(1, 'inserido') #-> requer dois argumentos, o indice que vai ser colocado e o valor
print(lista)