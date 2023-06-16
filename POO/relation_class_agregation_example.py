class SellCar:
    def __init__(self, name):
        self.name = name
        # BASE DE DADOS
        self._car_name = []

    def insert_car(self, *cars):
        # INSERIR CARROS NA MINHA BASE DE DADO
        # for c in _car_name:
        #   self._car_name.append(c)
        # self._car_name += cars
        self._car_name.extend(cars)

    def total_price(self):
        # SOMAR VALORES DA MINHA BASE DE DADOS
        sumed = sum([p.price for p in self._car_name])
        return print(sumed)
    
    def list_cars(self):
        # LISTAR VALORES DA MINHA BASE DE DADOS
        print(f'modelos disponíveis dentro da {self.name}:')
        for c in self._car_name:
            print(c.name,'custa',c.price,'R$')
        print()

class Car:
    def __init__(self, name_car, price_car):
        self.name = name_car
        self.price = price_car

s1 = SellCar("auto Sant's")
c1, c2, c3 = Car('220i', 100.000), Car('118i', 80.000), Car('meca GLA', 150.000)

s1.insert_car(c1, c2, c3)
s1.list_cars()
s1.total_price()