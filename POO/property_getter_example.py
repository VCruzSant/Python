class Car:
    def __init__(self, brand):
        self.brand_name = brand

    @property
    def brand(self):
        return self.brand_name

#____________________
# código cliente:
c1 = Car('BMW')
print(c1.brand)