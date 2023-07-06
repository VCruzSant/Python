# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count

path = os.path.abspath('.')
print(path)

counter = count()

for root, dirs, files in os.walk(path):
    the_counter = next(counter)
    print(the_counter, 'Pasta:', root)

    for dir_ in dirs:
        print('     ', the_counter, 'sub-directory(dir):', dir_)

        for file_ in files:
            # pegando caminho completo:
            print('         ', the_counter, os.path.join(root, file_))
            # Para apagar tudo:
            # os.unlink(root, dirs)
