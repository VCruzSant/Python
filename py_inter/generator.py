import sys

iterable = {'y', 'have', '__iter__' }
iterator = iter(iterable) #-> __iter__ & __next__

#Genetator -> pause

lista = [l for l in range(100)]
generator = (g for g in range(100))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))