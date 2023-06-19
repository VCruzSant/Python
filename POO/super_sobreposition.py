class MyString(str):
    def upper(self):
        # após criar esse método, o upper normal não vai funcionar pq ele foi sobreposto
        ...
        # por isso, é usado essa tática:
        print('chamou upper')
        returned = super().upper()
        print('dps do upper')
        return returned

p1 = MyString('uma string')
print(p1.upper())

class A:
    atribute_A = 'value A'

    
    def __init__(self, value):
        self.value = value


    def method(self):
        print('A')

class B(A):
    atribute_B = 'value B'
    # se eu for executar algo no B, tenho que passsar os atributos requeridos em A, se não vai dar error
    def __init__(self, value, value_for_b):
        super().__init__(value) #value é inutil, só serve para n dar erro na herança
        self.value_for_b = value_for_b

    def method(self):
        print('B')

class C(B):
    atribute_C = 'value C'
    def method(self):
        # Quando executar method C, executar o que ele está herdando
        print('C')
        super(C, self).method() # super(C, self) = super(), de maneira explicita 
        super(B, self).method() # A partir de B. procure o method

c = C('v', 'ov')
print(c.atribute_A)
print(c.atribute_B)
print(c.atribute_C)
c.method()
print(C.mro())
print(B.mro())

b = B('valor', 'outro valor')