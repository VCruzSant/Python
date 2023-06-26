class Foo:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}({self.x!r}, {self.y!r}, {self.z!r})'
    
    def __str__(self):
        return f'x = {self.x}, y = {self.y}, z = {self.z!s}'
    
    def __add__(self, other):
        sum_x = self.x + other.x
        sum_y = self.y + other.y
        return sum_x, sum_y
    
    def __gt__(self, other):
        self_result = self.x + self.y
        other_result = other.x + other.y
        return (self_result > other_result)
    
f1 = Foo(10, 20)
f2 = Foo(30, 40)

print(f1)
print(f2)
print()
print(f'{f1!r}')
print(f'{f2!r}')
print()
print(f'{f1!s}')
print(f'{f2!s}')
print(f1 + f2)
print(f1 > f2)
print(f2 > f1)