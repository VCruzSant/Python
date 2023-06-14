class Cars:
    def __init__(self, car1, car2):
        self.car1 = car1
        self.car2 = car2

    def ultrapassing(self):
        print(f'{self.car1} ultrapassou {self.car2}')

cs1 = Cars('bmw', '220i')

cs2 = Cars('Palio', 'Celta')

cs1.ultrapassing()
cs2.ultrapassing()
