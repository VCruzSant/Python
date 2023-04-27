# dir, hasattr, getattr
string = 'santiago'
metodo_up = 'upper'#atributo pode ser chamado por uma variavel, porém deve estar entre ''

if hasattr(string, metodo_up) is True: #hasattr -> chega se um OBJ tem um determinado atributo
    print('existe upper')
    print(getattr(string, metodo_up)())#getattr -> pega o atributo 

else:
    print('não existe')
    