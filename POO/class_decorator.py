def adiciona_repr(cls):
    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict!r})'
        return class_repr
    cls.__repr__ = meu_repr
    return cls

def speek_name(metod):
    def intern(self, *args, **kwargs):
        result = metod(self, *args, **kwargs)
        if 'earth' in result:
            return 'you are in home'
        return result
    return intern

# class MyReprMixin:
#     def __repr__(self):
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name}({class_dict!r})'
#         return class_repr

# class Team(MyReprMixin):
    
@adiciona_repr
class Team:
    def __init__(self, name) -> None:
        self.name = name

@adiciona_repr
class Planet:
    def __init__(self, name) -> None:
        self.name = name
    
    @speek_name
    def speek_planet(self):
        return f'my name is {self.name}'
    

braz = Team('corinthians')
earth = Planet('earth')

print(braz)
print(earth.speek_planet())