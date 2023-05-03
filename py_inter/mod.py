# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes

import sys

platforma = 'A MINHA'
print(sys.platform)
print(platforma)
print()

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo

from sys import exit, platform
print(platform)
# exit() #antes -> sys.exit() | como foi importado a parte, n precisa chamar o sys. 
print()

# alias 1 - import nome_modulo as apelido
import sys as s
#s é apelido do sys
sys = 'algo no código'
print(sys)
print(s.platform)
print()

# alias 2 - from nome_modulo import objeto as apelido
from sys import platform as pf, exit as ex

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo

from sys import *

print(platform)
exit()
