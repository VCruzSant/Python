# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Por convenção, colocar Error no final do nome da classe
class MyError(Exception):
    ...

class OtherError(Exception):
    ...

def up_raise():
    exception_ = MyError('a', 'b')
    exception_.add_note('vc errou nisso sla, tenta ai')
    raise exception_

try:
    up_raise()
except MyError as error:
    print(error.__class__.__name__)
    print(error)
    exception_ = OtherError('vou lançar dnv')
    raise exception_ from error
