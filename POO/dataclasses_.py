# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass, asdict, astuple

# frozen = True -> não deixa setar nada na classe


@dataclass(frozen=True, order=True)
class People:
    name_: str
    age: int

    def __post_init__(self):
        print('venho dps do init')

    @property
    def name(self) -> str:
        return self.name_

    # @name.setter
    # def name(self, value) -> str:
    #     self.name_ = value
    #     return self.name_


if __name__ == '__main__':
    p1 = People('Vini', 20)
    # print(p1)
    # p1.name = 'vini mesmo'
    # print(p1)
    # list_ = [People('B', 10), People('A', 10), People('C', 10)]
    # ordened = sorted(list_, reverse=True, key=lambda p: p.name)
    # print(ordened)
    print(astuple(p1))
    print(asdict(p1))
