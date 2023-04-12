string = 'a b'
i = 0

while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
    
else: #se eu der break, o else não é executado
    print('não tem espaço na string')

print('fora do while')