# copy, sorted, produtos.sort
# Exercícios
import copy

from data import products


# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
new_products = [{**p, 'preco': round(p['preco'] * 1.1, 2)} for p in copy.deepcopy(products)]
print(*new_products, sep='\n')
print()


## Ordene os produtos por nome decrescente (do maior para menor)
## Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
products_ordened_name = sorted(
    copy.deepcopy(products),
    key=lambda p: p['nome'],
    reverse=True
)

print(*products_ordened_name, sep='\n')
print()


# # Ordene os produtos por preco crescente (do menor para maior)
# # Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

products_ordened_preco = sorted(
    copy.deepcopy(products),
    key=lambda p: p['preco'],
    reverse=True
)

print(*products_ordened_preco, sep='\n')