# Mantendo Estados na classe

class Drive:
    def __init__(self, car, clutched=False):
        self.car = car
        self.clutched = clutched

    def acelerate(self):
        if self.clutched:
            print(f'{self.car} não pode acelerar enquanto está na embreagem')
            return
        print(f'{self.car} está acelerando')
    
    def exchange(self):
        if not self.clutched:
            print('precisa pisar na embreagem para mudar a marcha')
            return
        print(f'{self.car} está passando a marcha')

    def clutch(self):
        if self.clutched:
            print('já está na embreagem pisada')
            return
        print(f'{self.car} pisando na embreagem')
        self.clutched = True

    def stop_clutch(self):
        if not self.clutched:
            print('a embreagem ja está solta')
            return
        print('soltando embreagem')
        self.clutched = False

c1 = Drive('bmw')

c1.acelerate()
c1.exchange()
c1.clutch()
c1.clutch()
c1.acelerate()
c1.exchange()
c1.acelerate()
c1.stop_clutch()
c1.acelerate()