class Pen:
    def __init__(self, color):
        #private protected
        self._color = color
        self._color_tamp = None


    @property
    def color(self):
        print('do property:')
        return self._color
    
    @color.setter
    def color(self, value):
        print('estou no setter', value)
        self._color = value

    @property
    def color_tamp(self):
        print('estou no getter')
        return self._color_tamp
    
    @color_tamp.setter
    def color_tamp(self, value):
        print('estou no setter')
        self._color_tamp = value
# ____________________
# código cliente:

p1 = Pen('blue')
p1.color = 'red'
print(p1.color)

p1.color_tamp = 'black'
print(p1.color_tamp)


    
