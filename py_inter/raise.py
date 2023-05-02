#raisa - tratando erros (except)
def erro_zero(d):
    if d == 0:
        raise ZeroDivisionError('tentou dividir por zero')

def erro_int_float(x):
    type_x = type(x)
    if not isinstance(x, (int or float)):
        raise TypeError(
            f'não é número. '
            f'{type_x.__name__} que foi enviado'
        )


def divisor(x, d):
    erro_int_float(x)
    erro_int_float(d)
    erro_zero(d)
    return x / d

print(divisor('5', 0))