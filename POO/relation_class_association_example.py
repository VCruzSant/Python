class Driver:
    def __init__(self, name):
        self.name_driver = name
        self._brand = None

    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand_name):
        self._brand = brand_name

class BrandName:
    def __init__(self, brand_name):
        self.brand_name = brand_name

    def action(self):
        return f'{self.brand_name} está acelerando.....'
    

d1 = Driver('vini')
d2 = Driver('Sant')
b1 = BrandName('BMW')
d1.brand = 'bmw'
print(d1.brand)

d1.brand = b1
d2.brand = b1

print(d1.brand.action())
print(d2.brand.action())
