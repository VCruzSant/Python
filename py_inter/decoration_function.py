# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
#@sintax_sugar ->decorador 

def make_func(func):

    def intern(*args, **kwargs):
        print('Decorando a função')
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        print(f'seu resultado é {result}')
        print('Função decorada')
        return result
    return intern

@make_func
def invert_string(string):
    print(f'agora a função é {invert_string.__name__}')
    return string[::-1]



def is_string(param):
    if not isinstance(param, str):
        raise TypeError('deve ser uma string')


# check_invert = make_func(invert_string)
inverted = invert_string('SantiagO')
print(inverted)