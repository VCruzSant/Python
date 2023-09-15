# Deque - Trabalhando com LIFO e FIFO
# deque - Double-ended queue
#
# Lifo  e fifo
# pilha e fila

# LIFO (Last In First Out)
# Pilha (stack)
# Significa que o último item a entrar será o primeiro a sair (list)
# Artigo:
# https://www.otaviomiranda.com.br/2020/pilhas-em-python-com-listas-stack/
# Vídeo:
# https://youtu.be/svWVHEihyNI
# Para tirar itens do final: O(1) Tempo constante
# Para tirar itens do início: O(n) Tempo Linear

from collections import deque

list_ = [0, 1, 2, 3, 4, 5, ]

# ✅ Legal (LIFO com lista):
list_.append(6)
# [0, 1, 2, 3, 4, 5, 6, ]

list_.pop()
# [0, 1, 2, 3, 4, 5, ]

# 🚫 Ruim (FIFO com lista)
#         0  1  2  3  4  5
list_1 = [0, 1, 2, 3, 4, 5, ]

list_1.insert(0, 10)
#   0  1  2  3  4  5  6
# [10, 0, 1, 2, 3, 4, 5,

list_1.insert(0, 11)
#  0   1   2  3  4  5  6  7
# [11, 10, 0, 1, 2, 3, 4, 5,

# Ou seja, mexer na ponta direita da lista com LIFO -> OK ✅
# Ou seja, mexer na ponta esquerda da lista com FIFO -> RUIM 🚫


# FIFO (First In First Out)
# Filas (queue)
# Significa que o primeiro item a entrar será o primeiro a sair (deque)
# Artigo:
# https://www.otaviomiranda.com.br/2020/filas-em-python-com-deque-queue/
# Vídeo:
# https://youtu.be/RHb-8hXs3HE
# Para tirar itens do final: O(1) Tempo constante
# Para tirar itens do início: O(1) Tempo constante

# ✅ Legal -> FIFO com deque

correct_row: deque[int] = deque()

correct_row.append(3)  # adiciona no final
correct_row.append(4)  # adiciona no final
correct_row.append(5)  # adiciona no final

correct_row.appendleft(0)  # adiciona no começo
correct_row.appendleft(1)  # adiciona no começo
correct_row.appendleft(2)  # adiciona no começo

print(correct_row)
