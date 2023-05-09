# count -> contador sem fim | módulo -> itertools
from itertools import count

c1 = count(8, 8)
r1 = range(8, 80, 8)

print('count')
for c in c1:
    if c > 80:
        break
    print(c)
print()


print('range')
for r in r1:
    print(r) 


