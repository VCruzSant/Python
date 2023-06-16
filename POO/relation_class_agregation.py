# Um objeto PRECISA/TEM de outro objeto para FAZER determinada ação
# Eles podem "viver" separadamente
# EX: carro e roda, carro liga sem a roda mas n funciona mt bem, roda gira mas n serve pra mt coisa sem o carro

class CarShopping:
    def __init__(self):
        # data base -> produtos
        self._products = []

    def insert_product(self, *products):
        # for p in products:
        #     self._products.append(p)
        # self._products += products
        self._products.extend(products)

    def total_price(self):
        # soma os valores(preços) da data base
        sumed = sum([p.price for p in self._products])
        return print(sumed)
    
    def list_product(self):
        # imprime minha data base de produtos
        for product in self._products:
            print(product.name, product.price)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

c1 = CarShopping()

#desempacotamento:
p1, p2 = Product('pen Faber', 1.2), Product('pen Bic', 1)
c1.insert_product(p1, p2)
c1.total_price()
c1.list_product()