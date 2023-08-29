# sys.arg -> executa arquivos com argumentos no sistema
# fonte -> Fira Code

import sys

argmnts = sys.argv
len_argmnts = len(argmnts)

if len_argmnts <= 1:
    print('Você não passou argumentos')
else:
    print(f'Você passo os argumentos: {argmnts}')
