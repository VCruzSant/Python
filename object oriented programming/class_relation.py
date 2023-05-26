# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.

class Writer:
    def __init__(self, name):
        self.name = name
        self._tool = None

    @property
    def tool(self):
        return self._tool
    
    @tool.setter
    def tool(self, tool):
        self._tool = tool

class WriterTool:
    def __init__(self, name):
        self.name = name

    def write(self):
        return f'{self.name} is writing'
    

w1 = Writer('author')
t1 = WriterTool('pen')
t2 = WriterTool('machine')
w1.tool = t2

print(t1.write())
print(w1.tool.write())
    

