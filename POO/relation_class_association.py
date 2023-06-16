# associação: uma classe USA outra, escritor usa sua ferramenta
class Writer:
    def __init__(self, name):
        self.name = name
        self._tool = None
    
    #getter
    @property
    def tool(self):
        return self._tool
    
    #setter
    @tool.setter
    def tool(self, tool):
        self._tool = tool


class WriterTool:
    def __init__(self, name_tool):
        self.name_tool = name_tool

    def write(self):
        return f'{self.name_tool} está escrevendo'
    

w1 = Writer('Sant')
w2 = Writer('Vini')
t1 = WriterTool('pen Faber-Castell')
t2 = WriterTool('machine write')

# association:
w1.tool = t1
w2.tool = t2

print(t1.write())

# pode ser também:
print(w1.tool.write())
print(w2.tool.write())