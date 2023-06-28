# Metaclasses são o tipo das classes
# EM PYTHON, TUDO É UM OBJETO (CLASSES TAMBÉM)
# Então, qual é o tipo de uma classe? (type)
# Seu objeto é uma instância da sua classe
# Sua classe é uma instância de type (type é uma metaclass)
# type('Name', (Bases,), __dict__)
#
# Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
# __new__ da metaclass é chamado e cria a nova classe
# __call__ da metaclass é chamado com os argumentos e chama:
#   __new__ da class com os argumentos (cria a instância)
#   __init__ da class com os argumentos
# __call__ da metaclass termina a execução
#
# Métodos importantes da metaclass
# __new__(mcs, name, bases, dct) (Cria a classe)
# __call__(cls, *args, **kwargs) (Cria e inicializa a instância)
#
# "Metaclasses são magias mais profundas do que 99% dos usuários
# deveriam se preocupar. Se você quer saber se precisa delas,
# não precisa (as pessoas que realmente precisam delas sabem
# com certeza que precisam delas e não precisam de uma explicação
# sobre o porquê)."
# — Tim Peters (CPython Core Developer)
def my_repr(self):
    return f'{type(self).__name__}({self.__dict__})'


class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('Metaclass New')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 1234
        cls.__repr__ = my_repr
        if 'speek' not in cls.__dict__ or not callable(cls.__dict__['speek']):
            raise NotImplementedError('Implemente "speek"')
        return cls
    
    def __call__(cls, *a, **k):
        print('Metaclass Call  ')
        instance_ = super().__call__(*a, **k)
        print(instance_.__dict__)
        if 'name' not in instance_.__dict__:
            raise NotImplementedError('Implemente o attr "name"')
        return instance_
    
    # se eu quiser obrigar alguém a definir um método:
    


# object, metaclass=type -> já é padrão
class People(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('My New')
        instance_ = super().__new__(cls)
        return instance_
    
    def __init__(self, name):
        print('My Init')
        self.name = name

    def speek(self):
        print('me obrigaram a implementar esse método')

p1 = People('Vini')
print(p1)
print(p1.attr)
