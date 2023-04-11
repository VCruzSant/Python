'''
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador

'''
text = 'anything'
iterator = iter(text)

while True:
    try: 
        letra = next(iterator)
        print(letra)

    except StopIteration:
        break


'''
Tudo isso:

for letra in text:
    print letra
'''