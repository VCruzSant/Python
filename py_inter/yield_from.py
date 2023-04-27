def gen1():
    yield 1
    yield 2
    

def gen2():
    yield from gen1()
    yield 3
    yield 4

ge = gen2()
for numb in ge:
    print(numb)