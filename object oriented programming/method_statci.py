# @staticmethod (métodos estáticos) são inúteis em Python =)
# Métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua
# classe.

class Classe:
    @staticmethod
    def func_in_class(*args, **kwargs):
        print('func da classe', args, kwargs)

c1 = Classe()
c1.func_in_class(1, 2, 3)
Classe.func_in_class(named=1)