# Atributos de classe


class People:
    attribute = 'value'
    YEAR_CURRENT = 2023

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_years_birth(self):
        return People.YEAR_CURRENT - self.age
    
people = People('vinicius', 20)
print(people.get_years_birth())