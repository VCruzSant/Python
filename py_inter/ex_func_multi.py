def make_multi(multi):
    def multipli(number):
        return multi * number
    return multipli

duplicate = make_multi(2)
triplicate = make_multi(3)
quadruple = make_multi(4)

print(duplicate(2))
print(triplicate(2))
print(quadruple(2))