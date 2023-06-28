class Multi:
    def __init__(self, multiplyer):
        self._multiplyer = multiplyer

    def __call__(self, func):
        def intern(*args, **kwargs):
            func_sum = func(*args, **kwargs)
            return func_sum * self._multiplyer
        return intern
    
@Multi(10)
def sum_(x, y):
    return x + y

two_and_two = sum_(2, 2)
print(two_and_two)