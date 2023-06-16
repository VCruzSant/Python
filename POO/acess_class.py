# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

class Foo:
    def __init__(self):
        self.public = 'isso é publico'
        self._protected = 'isso é protegido, só use dentro da classe ou subclasse que isso foi criado'
        self.__private = 'isso é privado, só use dentro da classe que foi criado'
    
    def _method_protected(self):
        return print('metodo que só deve ser chamado dentro da classe e subclasse')
    
    def __method_private(self):
        return print('metodo que só deve ser chamado dentro da classe')
    
    def method_public(self):
        print('esse é o método publico que retorna métodos/objetos protegidos')
        print(self._protected)
        print(self.__private)
        return self._method_protected(), self.__method_private()



f = Foo()
print(f.public)
f.method_public()