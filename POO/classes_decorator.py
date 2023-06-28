class Multi:
    def __init__(self, multiply):
        self._multiply = multiply
    
    def __call__(self, func):
        def intern(*args, **kwds):
            value = func(*args, **kwds)
            return value * self._multiply
        return intern

@Multi(20)
def sum_(x, y):
    return x + y

two_and_two =sum_(2, 2)
print(two_and_two)