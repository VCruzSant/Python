# Enum -> grupos de um tipo
# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value
import enum

# Directions = enum.Enum('Direction', ['LEFT', 'RIGHT', 'UP', 'DOWN'])
# Para facilitar a tipagem:
class Directions(enum.Enum):
    # LEFT = 1
    # Como fazer automatico:
    LEFT = enum.auto()
    RIGHT = 2
    UP = 3
    DOWN = 4

print(Directions(1))

def move(direction: Directions):
    if not isinstance(direction, Directions):
        raise ValueError('invalid direction')
    print(f'moving in {direction}')

move(Directions.LEFT)
move(Directions.RIGHT)
move(Directions.UP)
move(Directions.DOWN)
# move('lado')