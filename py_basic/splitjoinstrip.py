"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = 'algo, aleatorio e interessante'
list_palavras = frase.split() #se não for passado nenhum argumento, ele divide entre espaços
print(list_palavras)


list_formated = []
list_virgula = frase.split(',')#passei a virgula como argumento, então ele vai separar antes e depois da virgula
print(list_virgula)


for i, corte in enumerate(list_virgula):
    list_formated.append(list_virgula[i].lstrip()) #strip tira espaço
print(list_formated)

print('-' * 10)

test_join = '-'.join('abc') #.join separa o que está sendo passado como argumento com o que foi salvo na variavel, somente iteráveis
print(test_join)

frases_unidas = '-'.join(list_formated)
print(frases_unidas)