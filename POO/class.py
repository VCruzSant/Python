# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.

string = 'vini' # str
print(string.upper())
print(isinstance(string, str)) #vari string é uma instancia da classe str

class People:
    ...

p1 = People()
p1.name = 'vini'
p1.surname = 'sant'

p2 = People()
p2.name = 'da'
p2.surname = 'cruz'

print(p1, p1.name, p1.surname)
print(p2, p2.name, p2.surname)