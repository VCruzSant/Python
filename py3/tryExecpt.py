'''
try -> tente executar o código
except -> ocorreu algum erro ao executar o código
'''

numstr = input('Digite um número: ')

if numstr.isdigit():
    numflo = float(numstr)
    print(f'o dobro de {numstr} é: {numflo} * 2')

else: 
    print('não é um número valido')