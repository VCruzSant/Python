class Foo:
    def __new__(cls, *args, **kwargs):
        instance_ = super().__new__(cls)
        print('e assim criei Foo()')
        instance_.y = 'eu quis assim'
        return instance_
    
    def __init__(self, x):
        self.x  = x

    def __repr__(self):
        return f'Foo({self.x!r})'
    
f1 = Foo('meu x')
print(f1)
print(f1.x)
print(f1.y)
