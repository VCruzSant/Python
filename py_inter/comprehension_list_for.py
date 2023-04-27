lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))

print(lista)

name = [
    [letra for letra in 'vini']
    for x in range(3)
]
print(name)