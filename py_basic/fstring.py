'''
f-string
(caracter)(><^)(quantidade)
> esquerda 
< direita
^ centro
= força o número a aparecer antes
Sinal - + ou -
ex: 0>-100,.2f
Conversion flags - !r !s !a
'''

vari = 'sant'
print(f".{vari: >10}.") #coloque 10 caracteres a esquerda do valor da minha variavel 
print(f".{vari: ^10}.") #coloque 10 caracteres para manter o valor da minha variavel no centro
print(f".{vari:$^10}.") #coloque 10 caracteres para manter o valor da minha variavel no centro e preencha o espaço com $
print(f".{874325273654387:0=+10,.1f}.") 
