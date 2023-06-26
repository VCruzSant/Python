# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe

class A:
    def __new__(cls, *args, **kwargs):
        instance_ = super().__new__(cls)
        print('e assim se criou A')
        instance_.y = 'criei pq eu quis'
        return instance_
    

    def __init__(self, x):
        self.x = x
        print('sou init')

    def __repr__(self):
        return 'A()'

a1 = A(123)

# O que o python faz por debaixo dos panos:
# a1 = object.__new__(A)
# a1.__init__()

print(a1.x)
print(a1.y)