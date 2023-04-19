def myfunction(): #definir a função
    print('python')

myfunction()

def sum(a, b, c=None ):
    if c is not None:
        soma = a + b + c
        print(soma)
    else:
        print (a + b)

sum(1, 2) 
sum(b=3, a=4) #argumentos nomeados -> escolher a ordem 
sum(1, 2, 3)

