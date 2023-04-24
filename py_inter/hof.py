'''
Higher Of Function
funções de primeria classe
'''

def saldation(msg, name): #First-Class Functions
    return f'{msg}, {name}!'

def exec(funt, *args): #Higher Order Functions
    return funt(*args)# foi criado uma função com os argumentos passados

print(
    exec(saldation, 'bom dia', 'vini')
)

