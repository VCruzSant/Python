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
        self._name = name_car
        self._motor = None
        self._fabric = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, value):
        self._motor = value
        return self._motor
    
    @property
    def fabric(self):
        return self._fabric
    
    @fabric.setter
    def fabric(self, value):
        self._fabric = value
        return self._fabric

class Motor:
    def __init__(self, name_car):
        self.name = name_car


class Fabric:
    def __init__(self, name_car):
        self.name = name_car

gla = Car('GLA')
motor_20 = Motor('2.0, 4 cilindros')
meca = Fabric('Meca')

gla.motor = motor_20
gla.fabric = meca

bm_car = Car('220i')
bmw = Fabric('BMW')

bm_car.motor = motor_20
bm_car.fabric = bmw


print(gla.motor.name)
print(gla.fabric.name)
print(bm_car.motor.name)
print(bm_car.fabric.name)