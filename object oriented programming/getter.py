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

    # def get_color(self): #com isso, o self.color é protegido e pode fazer alterações no código, unica coisa que vai passar para quem está trabalhando com vc -> get_color()
    #     return self.color 

    @property
    def get_color(self):
        return self.color_atualization
###################################
# código cliente

p1 = Pen('blue')
print(p1.get_color)