'''
interpolação basica de string
s - str
d e i-int
f - float
x e X - hexadecimal (ABCDEF0123456789)
'''
name = 'vinicius'
value = 200.000
vari = '%s vai comprar ?' % name # usar o % e definir o tipo de dado, depois chamar a variavel 
total = '%s o valor é: %f' % (name, value)
resum = '%s arredondando fica %2.fR$' % (name, value)#colocar 2.f arrendonda para 2 casas
print(vari, total)
print(resum)
print('o hexadecimal de %i é %03x' % (5, 5)) #como não é comum ter apenas um algarismo no hexadecimal, pode completar com 0 -> 0(número de algarismos para aparecer)