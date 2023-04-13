"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

import decimal

numb1 = decimal.Decimal('0.5')
numb2 = decimal.Decimal('0.3')
numb3 = numb1 + numb2
print(f'{numb3:.2f}') #str

print(round(numb3, 1)) #float

#para contornar o problema da imprecisão, importe o decimal e passe um argumento tipo str ou use round