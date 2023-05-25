# __dict__ e vars para atributos de instância 

class People:
    attribute = 'value'
    YEAR_CURRENT = 2023

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_years_birth(self):
        print(self.name)
        return People.YEAR_CURRENT - self.age
    
p1 = People('vinicius', 20)
# print(p1.get_years_birth())

# p1.name = 'Santiago'
# del p1.name
# print(People.name)

print(p1.__dict__) #dicionario que contém os valores do seu objeto | pode ser utilizado vars(p1)