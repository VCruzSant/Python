# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa: #base class
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self._age = None

    def speak_name(self):
        print(self.name, self.surname, self.__class__.__name__)


    @property
    def get_age(self):
        return self._age
    
    @get_age.setter
    def get_age(self, value):
        print('definindo idade')
        self._age = value



class Cliente(Pessoa):
    ...

class Aluno(Pessoa):
    def speak_name(self):
        print('nem sai da classe Aluno'.upper())
        print(self.name, self.surname, self.__class__.__name__)

c1 = Cliente('Vini', 'Sant')
c2 = Cliente('imagine', 'people')
a1 = Aluno('Da', 'Cruz')

c1.speak_name()
c1.get_age = 11

a1.speak_name()


print(c1.get_age)




# method resolution order:
# Cliente
# Pessoa
# builtins.object