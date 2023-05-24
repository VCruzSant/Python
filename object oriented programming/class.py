# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos (dados dentro da classe) e métodos (funções que estão dentro de uma classe).
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

class People:
    def __init__(self, n, s):
        self.name = n
        self.surname = s

p1 = People('vini', 'sant')
# p1.name = 'vini'
# p1.surname = 'sant'
print(p1)
# print(p1.name)
# print(p1.surname)
print(p1.name)
print(p1.surname)