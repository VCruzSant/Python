class Car:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name

    @classmethod
    def bmw(cls, name):
        return cls('BMW', name)
    
    @classmethod
    def meca(cls, name):
        return cls('Mercedes', name)
    
c1 = Car.bmw('180i')
c2 = Car.meca('GLA')

print(c1.__dict__)
print(vars(c2))