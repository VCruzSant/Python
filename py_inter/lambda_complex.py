def execu(funct, *args):
    return funct(*args)

# def sum(x, y):
#     return x + y

print(
    execu(
        lambda x,y: x + y, 5, 5 #mesma coisa que a função sum
    )
)

adicion = execu(lambda *args: sum(args), 1, 2, 3, 4, 5)
print(adicion)


inf = input('digite um numb: ')
inf_int = int(inf)
multi = execu(lambda x: x * x, inf_int)
print(multi)
