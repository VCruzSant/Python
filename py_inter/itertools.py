# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')

people = ['Joana', 'Kleide', 'Maria', 'Igor']
tshirt = [
    ['black', 'white'],
    ['p', 'm'],
    ['masc', 'femin'],
    ]

print_iter(combinations(people, 2))
print_iter(permutations(people, 2))
print_iter(product(*tshirt))