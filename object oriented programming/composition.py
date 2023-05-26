# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Custumer:
    def __init__(self, name):
        self.name = name
        self.adress = []

    def insert_adress(self, street, number):
        self.adress.append(Adress(street, number))

    def list_adress(self,):
        for adress in self.adress:
            print(adress.street, adress.number)

class Adress:
    def __init__(self, street, number):
        self.street = street
        self.number = number

c1 = Custumer('maria')
c1.insert_adress('av. paulista', 78) 
c1.insert_adress('av. brasil', 52) 

print(c1.adress[0].street)
print(c1.adress[1].street)
print()
c1.list_adress()

