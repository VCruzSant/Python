# Escopos da classe e Métodos da classe

class Animal:
    def __init__(self, name):
        self.name = name

    def action(self, prey):
        return f'{self.name} está caçando {prey}' #self. alguma coisa pode ser acessado em qualquer lugar pq é do escopo da classe

lion = Animal('lion')
print(lion.name)
print(lion.action('bull'))