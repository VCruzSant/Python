# métodos de class
# Ao invés de receber "self" será "cls", ou seja, invez de ser instancia, vai ser a própria classe

class People:
    YEAR = 2023

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def metod_class(cls):
        print('hey')

    # factory metod
    @classmethod
    def age_50(cls, name):
        return cls(name, 50)
    
    @classmethod
    def without_name(cls, age):
        return cls('Anonimous', age)

p1 = People('vini', 19)
print(People.YEAR)
People.metod_class()

p2 = People.age_50('Sant')
print(p2.name, p2.age)

p3 = People.without_name(19)
print(p3.name, p3.age)