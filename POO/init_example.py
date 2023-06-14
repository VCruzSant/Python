class Car():
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name

c1 = Car('dodge', 'charger')
c2 = Car('bmw', '320i')

print(c1.brand, c1.name)
print(c2.brand, c2.name)