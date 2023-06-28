# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".
from typing import Any


class CallMe:
    def __init__(self, phone):
        self.phone = phone


    def __call__(self, name):
        print(f'{name} are call in {self.phone}')

c1 = CallMe('123456789')
# callable -> executando com parenteses:
c1('Vini')