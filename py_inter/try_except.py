#try, excpet, else & finally.
#colocar o código fora do try para ver a classe do erro 

# x = 1
# y = 0
# a = x / y

#retorna ZeroDivisionError -> colocar no except

try:
    x = 1
    y = 0
    b = 1
    print(b[0])
    a = x / y

except ZeroDivisionError: #expecificando o except, assim outro erro pode ser apontado 
    print('Tentou divir por zero')

except NameError: #pode não ter uma variável definida, ai vai gerar o NameError no terminal e assim podemos tratarlo
    print('Sem variável definida')

except Exception as error: #classe de erros de é para erros gerais
    print('erro desconhecido:', error)

print('continue')
