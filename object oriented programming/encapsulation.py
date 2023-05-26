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
        self.public = 'isso é publico -> usado em qualquer lugar'
        self._protected = 'isso é protegido -> usado dentro de classes e subclasses somente'
        self.__private = 'isso é protegido -> somente dentro de classes'


    def public_method(self):
        print(self.__private)
        return self.public
    
    def _protected_method(self):
        return self._protected
    
f = Foo()
print(f.public_method())