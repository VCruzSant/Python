'''
retorno de valores dentro de uma função (return)
'''

def soma(x, y):
    return x + y #sem o return, a função retorna nonetype

um_mais_um = soma(1, 1)
print(um_mais_um)
print(type(um_mais_um))

'''
*args - empacotamento e desempacotamento 
'''

def numbers(*args):
    total = 0
    print(args, type(args))
    for numbs in args:
        total += numbs
        print(numbs, total)

calc = numbers(1,2,3,4)
print(calc)