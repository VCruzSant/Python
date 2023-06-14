class Car:
    MOTOR_FORGED = 200

    def __init__(self, name, cv):
        self.name = name
        self.cv = cv

    def horse_power(self):
        return (f'{Car.MOTOR_FORGED + self.cv} cv')
    
c1 = Car('bmw', 200)
print(c1.horse_power())
