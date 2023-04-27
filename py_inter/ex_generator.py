def generator(n=0):
    while True:
        print(n)
        yield n
        n += 1
        input("mais um?")


gene = generator(n=0)
contin = input("Start? ")

if contin:
    for n in gene:
        next(gene)
