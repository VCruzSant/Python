class Car:
    def __init__(self, brand):
        self._brand = brand
        self._name = None

    @property
    def brand(self):
        print('estou no getter, te mostro o valor')
        return self._brand
    
    @property
    def name(self):
        print('estou no getter, te mostro o valor')
        return self._name
    
    @brand.setter
    def brand(self, value):
        print('estou no setter, altero o valor')
        self._brand = value
        
    @name.setter
    def name(self, value):
        print('estou no setter, altero o valor')
        self._name = value

# ____________________
# código cliente:

c1 = Car('DMW')
print(c1.brand)
print(c1.name)
c1.name = '220i'
print(c1.name)