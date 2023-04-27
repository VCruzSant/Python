def generator(n=0, max=10):
    while True:
        print(n)
        yield n
        n += 1
        input("mais um?")

        if n > max:
            return 'finish'


gene = generator(n=0, max =10)
contin = input("Start? ")

if contin:
    for n in gene:
        next(gene)