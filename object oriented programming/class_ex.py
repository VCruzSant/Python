# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Car:
    def __init__(self, name_car):
        self.name_car = name_car
        self._motor = None
        self._manufacture = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, value):
        self._motor = value


    @property
    def manufacture(self):
        return self._manufacture
    
    @manufacture.setter
    def manufacture(self, value):
        self._manufacture = value



class Motor:
    def __init__(self, name_motor):
        self.name_motor = name_motor


class Manufacturer:
    def __init__(self, name_manufacturer):
        self.name_manufacturer = name_manufacturer

lancer = Car('Lancer')
motor_2_0 = Motor('2.0')
mitsubishi = Manufacturer('Mitsubishi')

lancer.motor = motor_2_0
lancer.manufacture = mitsubishi

print(lancer.manufacture.name_manufacturer, lancer.name_car,  lancer.motor.name_motor)

lancer_evo = Car('Lancer Evo')
lancer_evo.motor = motor_2_0
lancer_evo.manufacture = mitsubishi
 
print(lancer_evo.manufacture.name_manufacturer, lancer_evo.name_car,  lancer.motor.name_motor)
