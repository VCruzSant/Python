products = {
    'name': 'pen',
    'price': 1.4,
    'category': 'office',
}

dc = {
    chave: valor.upper() #colocar em caixa alta
    if isinstance(valor, str) else valor #se for tipo str, senão me retorna valor
    for chave, valor 
    in products.items()
}
# print(dc, sep='\n')

s3t = {i + 2 for i in range(11)}
print(s3t)