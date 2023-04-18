#operadores in e not in
#String iteráveis 
# 0  1  2  3  4  5  6  7 
# S  a  n  t  i  a  g  o
#-8 -7 -6 -5 -4 -3 -2 -1 - pode ser negativo também 
name = 'Santiago' 
print(name[5])

print('S' in name ) #s está nas letras do valor da variavel "nome", -> case sensitive, retorna bool

print('-' * 10)

nome = input('Digite seu nome: ')
verif = input('O que deseja encontrar:')

if verif in nome:
    print(f'{verif} está em {nome}')
else: 
    print(f'{verif} não está em {nome}')