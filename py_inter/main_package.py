from sys import path

import package
from package.modulo import soma_modulo
from package.modulo import *

print(package.double(2)) #colocando o __init__.py dentro do package engana o python e faz o pack se comportar como modulo

print(*path, sep='\n')

print(soma_modulo(5, 5))
print(package.modulo.soma_modulo(10, 10))
print()

print(variavel) #é possivel criar uma lista de obj que pode ser acionado quando chamar o *