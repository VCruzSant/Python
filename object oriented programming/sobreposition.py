# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class


# class MyString(str):
#     def upper(self):
#         print('ABC')
#         retorn = super().upper()
#         print('código depois normal sem sobreposição')
#         return retorn

# myname = MyString('vini')

# print(myname.upper())

class A():
    atribut_a = 'value a'

    def __init__(self, atribute):
        self.atribute = 'atributo A'

    def metod(self):
        print('A')

class B(A):
    atribut_b = 'value b'


    def __init__(self, atribute, atri_b):
        super().__init__(atribute)
        self.atri_b = atri_b

    def metod(self):
        print('B')

class C(B):
    atribut_c = 'value c'

    def __init__(self, *args, **kwarg):
        super().__init__(*args, **kwarg)

    def metod(self): 
        super(B, self).metod()
        super(C, self).metod() # -> mesma coisa que super().metod() de mandeira explicita
        print('C')

c = C()
# print(c.atribut_a)
# print(c.atribut_b)
# print(c.atribut_c)
c.metod()

print(C.mro())