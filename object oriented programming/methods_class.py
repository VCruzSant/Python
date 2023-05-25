# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class People:
    year = 2023

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def method_class(cls): #cls é a porpria class -> People
        print('hey')

    @classmethod
    def people_50(cls, name): #cls é a porpria class -> People
        return cls(name, 50) #exemplo de dar 50 anos para todos os nomes recebidos
    
    @classmethod
    def people_age(cls, age): #cls é a porpria class -> People
        return cls('anonima', age) #exemplo de digitar somente a idade

p1 = People('sant', 20)
print(p1.year)

People.method_class()


p2 = People.people_50('vini')
print(p2.age)

p3 = People.people_age(25)
print(p3.name, p3.age)
