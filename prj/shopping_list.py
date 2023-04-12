import os

lista = []

while True:
    selecionar = input('Selecione uma opção: [l]istar | [i]nserir | [a]pagar ')
    num_valid = None
    numbs = '123456789'


    if selecionar in numbs:
        print('Digite apenas as letras indicadas')
        continue

    if len(selecionar) > 1:
        print('Apenas uma letra é permitida')


    elif selecionar == 'l':
        os.system('cls')
        for indice, iten in enumerate(lista):
            print(indice, iten)
            continue

        if lista == []:
            print('não há itens na sua lista')
            


    elif selecionar == 'i':
        os.system('cls')
        add_iten = input('Adicionar: ')
        if add_iten == '':
            print('Digite algum item')
            continue
        lista.append(add_iten)
        print(f'{add_iten} adicionado a lista de compras')



    elif selecionar == 'a':
        os.system('cls')
        enumerated_list = list(enumerate(lista))

        if lista == []:
            print('não há itens na sua lista para apagar')
            continue
        
        del_iten = input(f'Selecione o indice que deseja apagar: {enumerated_list} ')
        try:
            indice_del = int(del_iten)
            num_valid = True
            print(f'{lista[indice_del]} foi apagado da lista de compras')
            lista.pop(indice_del)


        except ValueError:
            print('Digite um indice')

        except IndexError:
            print('Ese indice não está na lista')

        except Exception as error:
            num_valid = None  
            print(error)

    else:
        print('Digite apenas as letras indicadas')
