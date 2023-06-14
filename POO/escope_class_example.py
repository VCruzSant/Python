# Escopo da classe e de métodos

class Animal:
    def __init__(self, name):
        self.name = name

    def action(self, action, target):
        print(f'{self.name} está {action} a {target}')

a1 = Animal('lion')
a1.action('comendo', 'gazela')

    