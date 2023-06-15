class Classe:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def func_in_class():
        print('to dentro da classe')

c1 = Classe('um belo nome')
c1.func_in_class()
Classe.func_in_class()