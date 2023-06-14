# Escopo da classe e de métodos

class Animal:
    def __init__(self, name):
        self.name = name

        vari = 'value'
        print(vari)

    def action(self, other):
        print(self.name, 'está caçando', other)

a1 = Animal('Lion')
print(a1.name)
a1.action('gazel')