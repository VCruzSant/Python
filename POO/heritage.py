# Herança simples - Relações entre classes
# Associação - usa 
# Agregação - tem
# Composição - É dono de, 
# Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class People:
    cpf = 'cpf geral: 7654321'
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def print_name_class(self):
        print(self.name, self.surname, '->', self.__class__.__name__)

# herança sendo estabelecida
class Customer(People):
    ...

class Student(People):
    cpf = 'cpf do aluno: 1234567'

c1 = Customer('vini', 'Sant')
s1 = Student('Da', 'Cruz')

c1.print_name_class()
s1.print_name_class()
# method resolution order: busca primeira na classe em que é chamdo
print(s1.cpf)
print(c1.cpf)