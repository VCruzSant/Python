name = input('Digite seu nome: ')
yearsO = input('Digite sua idade: ')

inName = name[::-1]
nName = len(name)
firstL = name[0]
lastL = name[-1]

if name and yearsO:
    print(f'Seu nome é {name}')
    print(f'Seu nome invertido é {inName}')
    
    if ' ' in name:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não tem espaços')

    print(f'Seu nome tem {nName} letras')
    print(f'A primeira letra do seu nome é {firstL}')
    print(f'A ultima letra do seu nome é {lastL}')

else:
    print('Há campos vazios')
    

