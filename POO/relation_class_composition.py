# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Customer:
    def __init__(self, name):
        self.name = name
        self.adress = []

    def insert_adress(self, street, number):
        # Composição no append
        self.adress.append(Adress(street, number))

    def list_adress(self):
        for adress in self.adress:
            print(adress.street, adress.number)


class Adress:
    def __init__(self, street, number):
        self.street = street
        self.number = number

c1 = Customer('Vinicius')
c1.insert_adress('Av. Brasil', 12)
c1.insert_adress('Av. Paulista', 6)

c1.list_adress()