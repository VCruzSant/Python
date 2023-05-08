def decor_factory(a=None, b=None, c=None):
    def function_factory(func):
        print("decoradora")

        def inner(*args, **kwargs):
            print("aninhada")
            ret = func(*args, **kwargs)
            return ret

        return inner

    return function_factory


@decor_factory(1, 2, 3)
def sumx(x, y):
    return x + y


numbs = sumx(10, 5)
print(numbs)


decorator = decor_factory()
multiple = decorator(lambda x, y: x * y)
print(multiple(4, 4))
