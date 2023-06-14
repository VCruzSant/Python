# Mantendo Estados na classe

class Cam:
    def __init__(self, name, pict=False):
        self.name = name
        self.pict = pict


    def picting(self):
        if self.pict:
            print(f'{self.name} já está filmando')
            print()
            return
        
        print(f'{self.name} está filmando...')
        print()
        self.pict = True


    def stop_pict(self):
        if not self.pict:
            print(self.name, 'já está sem filmar')
            print()
            return
        
        print('parou de filmar....')
        print()
        self.pict = False


    def picture(self):
        if self.pict:
            print(f'{self.name} não pode tirar foto enquanto grava')
            print()
            return
        print(f'{self.name} tirou uma foto')
        print()

c1 = Cam('Canon')
c2 = Cam('Sony')

c1.picting()
c1.picture()
c1.stop_pict()
c1.picture()
