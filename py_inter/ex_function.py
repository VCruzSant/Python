def multi(*args):
    total = 1
    for numbs in args:
        total *= numbs
    return total

numbs_multi = multi(5, 5)


def par(x):
    is_par = x % 2 == 0
    if is_par is True:
        return "é par"
    return 'é impar'

resolvido = par(multi(numbs_multi))
print(numbs_multi, resolvido)



