# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código


# meu código 
class Pen():
    def __init__(self, color):
        self.color_atualization = color 
        self._color = self.color_atualization
        self._color_tamp = None

    # def get_color(self): #com isso, o self.color é protegido e pode fazer alterações no código, unica coisa que vai passar para quem está trabalhando com vc -> get_color()
    #     return self.color 

    @property
    def color(self): # mesma coisa do exemplo acima de um jeito pythonico, só passar o get_color pro cliente
        return self._color
    
    @color.setter
    def color(self, value):
        print('estou no setter da cor da caneta')
        self._color = value

    @property
    def color_tamp(self):
        return self._color_tamp
    
    @color_tamp.setter
    def color_tamp(self, value):
        print('estou no setter da cor da tampa')
        self._color_tamp = value
###################################
# código cliente

p1 = Pen('blue')
p1.color = 'red'
p1.color_tamp = 'black'
print(p1.color)
print(p1.color_tamp)

