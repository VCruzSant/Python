def decor_factory(a=None, b=None, c=None):
    def exec_closure(f):
        def inner(*args):
            print("decorando...")
            for s in args:
                validating(s)
            result = f(*args)
            print(f"seu resultado é {result}")
            return result

        return inner

    return exec_closure


decorator = decor_factory()


def validating(s):
    if not isinstance(s, str):
        raise TypeError("apenas letras são validas")


@decor_factory(1, 2, 3)
def letter(string):
    print(letter.__name__)
    return len(string)


fras = letter("vinicius")
print(fras)


inverter = decorator(lambda string: string[::-1])
print(inverter("isso aqui"))
