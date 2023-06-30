# namedtuples - tuplas imutáveis com nomes para valores
# Usamos namedtuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou registros de
# bases de dados, etc.
# As namedtuples são imutáveis assim como as tuplas.
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NamedTuple
# https://brasilescola.uol.com.br/curiosidades/baralho.htm
# from collections import namedtuple

# from collections import namedtuple

# Card = namedtuple('Card', ['value', 'naipe'], defaults=['VALUE', 'NAIPE'])

from typing import NamedTuple


class Card(NamedTuple):
    value: str = 'value'
    naipe: str = 'naipe'


as_sword = Card('A', '♠')
print(as_sword)
print(as_sword.value)
print(as_sword.naipe)
print()
print(as_sword._fields)
