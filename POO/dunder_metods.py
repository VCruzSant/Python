# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str

class Point:
    def __init__(self, x, y, z='String'):
        self.x = x 
        self.y = y
        self.z = z

    def __repr__(self):
        # retorna o que a class é, podendo também definir seus objetos 
        # Estou passando para os desenvolvedores como essa classe é, podendo recria-la
        # class_name = self.__class__.__name__ 
        # mesma coisa do exemplo abaixo:
        class_name = type(self).__name__
        # ao colocar !r numa string, o python acrescenta '' automaticamente 
        return f'{class_name}(x={self.x!r}, y={self.y!r}) z = {self.z!r}'

    def __str__(self):
        # representação em string do meu obj
        return f'({self.x}, {self.y})'
    
    def __add__(self, other):
         new_x = self.x + other.x
         new_y = self.y + other.y
         return Point(new_x, new_y)
    
    def __gt__(self, other):
         result_self = self.x + self.y
         result_other = other.x + other.y
         return result_self > result_other

    
p1 = Point(1, 2)
p2 = Point(3, 4)

# Ele retorna string de pereferencia 
print(p1)
print(p2)
print()
# forçando ele retornar o repr
print(repr(p1))
print(repr(p2))
print()
# repr em str
print(f'{p1!r}')
print(f'{p2!r}')
print()
# outra maneira de chamar os obj em str
print(f'{p1!s}')
print(f'{p2!s}')

p3 = p1 + p2
print('somando...')
print(p3)

print('apenas comparando, n tem nada a ver com a soma anterior')
print(p1 > p2)
print(p2 > p1)