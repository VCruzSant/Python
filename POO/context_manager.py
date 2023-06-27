# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with será
# suprimidas.
#
# Ex:
# with open('context_manager.txt', 'w') as arquivo:
#     ...

class MyOpen:
    def __init__(self, path_file, mode):
        self.path_file = path_file
        self.mode = mode
        self._file = None

    def __enter__(self):
        print('Open')
        # O retorno do enter, vai estar na variavel do with 
        # return 12345
        self._file = open(self.path_file, self.mode, encoding='utf8')
        return self._file
    
    def __exit__(self, class_exception, exception_, traceback_):
        print('Close')
        self._file.close()

        # raise class_exception(*exception_.args).with_traceback(traceback_)
        # print(class_exception)
        # print(exception_)
        # print(traceback_)

        # exception_.add_note('nota do erro')

        raise ConnectionError('erro de conexão')

instance_ = MyOpen('context_manager.txt', 'w')

with instance_ as file:
    file.write('line 1\n')
    file.write('line 2\n', 123)
    file.write('line 3\n')
    print('with', file)