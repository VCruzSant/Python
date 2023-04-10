'''Calculator with While'''
while True:
    num_1 = input('Digite um número: ') 
    num_2 = input('Digite outro número: ')
    operator = input('Qual operação( + | - | / | * ): ')

    num_valid = None #flag


    float_num_1 = 0 #declarando variavel fora de bloco para não gerar algum bug
    float_num_2 = 0
    


    try:
        float_num_1 = float(num_1)
        float_num_2 = float(num_2)
        num_valid = True #verificando se foi convertido
    
    except Exception as error:
        num_valid = None #se não for convertido, de erro
        print(error)

    if num_valid is None: #se não for convertido, imprima e continue novamente
        print('Um ou ambos os números não são validos, digite outros')
        continue



    operator_perm = '+-/*'

    if operator not in operator_perm: #se o operador selecionado não está entre os permitidos, imprima e continue novamente
        print('operação invalida')
        continue


    if len(operator) > 1: #verifica a quantidade de operadores
        print('Digite apenas um operador')
        continue


    print('Resultado:')

    if operator == '+':
        calc = float_num_1 + float_num_2
        print(f'{float_num_1} + {float_num_2} = {calc}')

    if operator == '-':
        calcsub = float_num_1 - float_num_2
        print(f'{float_num_1} - {float_num_2} = {calcsub}')

    if operator == '/':
        calcdiv = float_num_1 / float_num_2
        print(f'{float_num_1} / {float_num_2} = {calcdiv}')

    if operator == '*':
        calcmult = float_num_1 * float_num_2
        print(f'{float_num_1} * {float_num_2} = {calcmult}')

    sair = input('Quer sair? [s]im: ').lower().startswith('s') #converte para minúsculo e verifica se começa com 's' -> bool

    if sair is True:
        print('você saiu')
        break #para o programa se for True