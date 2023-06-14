class People():
    # método
    def __init__(self, name, surname): 
        # atributo / instancia 
        self.name = name
        self.surname = surname

p1 = People('vini', 'sant')
# p1.name = 'vini'
# p1.surname = 'sant'

print(p1.name, p1.surname)