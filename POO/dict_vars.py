# __dict__ e vars para atributos de instancias 

class People:
    YEAR_ACTUAL = 2023

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_birthday(self):
        return People.YEAR_ACTUAL - self.age
    
p1 = People('vini', 20)
print(p1.get_birthday())

#alterando instancias da classe pelo dict
p1.__dict__['name'] = 'mudei pelo dict'

print(p1.__dict__)
# mesma coisa que p1.__dict__
print(vars(p1)) 