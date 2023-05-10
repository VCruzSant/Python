# map, partial, GeneratorType e esgotamento de Iterators
from functools import partial
from types import GeneratorType

products = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]



def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

def more_percent(value, percent):
    return round(value * percent, 2)


def alter_value(p):
    return {**p, 'preco':ten_percent(p['preco'])}

ten_percent = partial( #controla os argumentos e gera uma nova funcão
    more_percent, 
    percent=1.1
)

# new_products = [{**p, 'preco':ten_percent(p['preco'])} for p in products]
new_products = map( #list comprehesion com functoin e iterável 
    alter_value,
    products
)



print_iter(new_products)
print(isinstance(new_products, GeneratorType))
print()


fiz_map = list(map(
    lambda x: x *3, #o python ja passa o for 
    [1, 2, 3, 4]
))

print(fiz_map)