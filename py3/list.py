"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Lista vazia -> falsy
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
#         0      1    2     3
lista = ['Vini', 123, True, []] #list()
print(lista[0].upper())# .upper() -> converte para letras maiúsculas
lista[-3] = 321
print(lista, lista[1])