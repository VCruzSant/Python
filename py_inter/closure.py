'''Closure -> usado para não repetir chamadas de funções toda hora'''

def make_saludation(salu):
    def salute(name):
        return f'{salu}, {name}!'
    return salute

say_day = make_saludation('bom dia')
say_night = make_saludation('boa noite')

names = ['vini', 'cruz', 'santiago']

for name in names:
    print(say_day(name))
    print(say_night(name))

