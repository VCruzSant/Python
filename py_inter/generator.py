import sys

iterable = {'y', 'have', '__iter__' }
iterator = iter(iterable) #-> __iter__ & __next__

#Genetator -> pause

lista = [l for l in range(100)] #está na memória
generator = (g for g in range(100))# generator espera pedir um valor para ele antes de colocar na memória

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))