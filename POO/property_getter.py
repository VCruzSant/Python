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

class Pen:
    def __init__(self, color):
        self.color_paint = color

    # getter normal:
    # def get_color(self):
    #     print('get color')
    #     return self.color_paint

    #getter pythonico
    @property
    def color(self):
        print('property')
        return self.color_paint

#############


# SITUAÇÂO: muitas pessoas executam o comando a baixo, pegando meu código
# código cliente:
p1 = Pen('azul')

# sem o getter:
# print(pen.color)
# print(pen.color)
# print(pen.color)
# print(pen.color)

#____________________

#com o getter:
# print(pen.get_color())
# print(pen.get_color())
# print(pen.get_color())
# print(pen.get_color())

#____________________
#chamando @property
print(p1.color)

