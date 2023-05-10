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

def filt_preco(prdt):
    return prdt['preco'] > 20

# new_products = [
#     p for p in products 
#     if p['preco'] > 20]

new_products = filter(
    # lambda x: x['preco'] > 25,
    filt_preco,
    products
)


print_iter(new_products)