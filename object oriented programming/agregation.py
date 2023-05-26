# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).

class ShoppingKart:
    def __init__(self):
        self._products = []

    def total(self):
        return sum([p.value for p in self._products])
    
    def insert_products(self, *products):
        for product in products:
            self._products.append(product)
    
    def products_list(self):
        for product in self._products:
            print(product.name, product.value)

class Products:
    def __init__(self, name, value):
        self.name = name
        self.value = value

kart = ShoppingKart()
p1, p2 = Products('cookie', 2.00), Products('milk', 1.50)
kart.insert_products(p1, p2)
kart.products_list()
print(kart.total())
