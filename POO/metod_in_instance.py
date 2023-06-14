# Métodos em instancias de classe

class Car:
    def __init__(self, name):
        self.name = name

    def acelerate(self):
        print(f'{self.name} está acelerando')

bmw = Car('220i')
print(bmw.name)
# métodos devem ser chamados com '()'
bmw.acelerate()

meca = Car('GLA')
print(meca.name)
bmw.acelerate()
