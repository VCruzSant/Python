# os.path.getsize e os.stat para dados de arquivos
import os
from itertools import count
import math


def file_format(byte_size: int, base: int = 1024) -> str:
    """Formata bytes em tamanho apropriado"""

    # Original:
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python

    if byte_size <= 0:
        return '0B'

    sizes = 'B', 'KB', 'MB', 'GB', 'TB', 'PB'
    # math.log -> retorna logaritimo do byte_size
    # abreviando 1 000 para bater com a abreviação dos sizes
    indic_size_abreviated = int(math.log(byte_size, base))

    # por quanto o tamanho vai ser divido
    power = base ** indic_size_abreviated
    size_final = round(byte_size / power, 2)

    # abreviação desejada
    size_abreviation = sizes[indic_size_abreviated]

    return f'{size_final} {size_abreviation}'


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
        complete_path = os.path.join(root, file_)
        size_file = os.path.getsize(complete_path)
        print('      ', the_counter, complete_path, '', file_format(size_file))
