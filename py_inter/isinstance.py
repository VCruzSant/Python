lista = [
    'a', 1, 2.3, True, [0, 1, 2], (3, 4), {5, 6}, {'name': 'vini'},
]

for iten in lista:
    if isinstance(iten, set):
        iten.add(3)
        print(iten)
        print()

    elif isinstance(iten, str):
        print('STRING')
        print(iten)
        print()

    elif isinstance(iten, bool):
        print(iten)
        print()

    else:
        print('OUTRO')
        print(iten)
        print()

    