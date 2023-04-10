'''
Repetições
While --> Enquanto 
faça uma ação, ENQUANTO isso for verdadeiro 
'''
condicao = True
while condicao:
    name = input("Qual seu nome:")
    print(f'seu nome é: {name}')
    #enquanto minha condição for true, vai ser executado o while até a condicao ser false, vai ficar perguntando meu nome até eu mudar a condicao
    if name == 'sair': #se o user digitar sair:
        break # pare
print('saiu do laço')

print('-'*10)

contador = 0
while contador < 10: #enquanto o valor da minha variavel for menor do que 10, faça:
    contador = contador + 1 #pegue o valor e some + 1, quando o laço for repetido, ele volta para o while com o valor na mamoria e assim prossegue.
    print(contador) #depois que for somado, imprima

print('Acabou')
'''
Operadores de atribuição
--> = | += | -= | *= | = | //= | **= | %=
'''
cont = 0
cont += 1 # --> cont = cont + 1| é a mesma coisa
print(cont)

print(103-62)