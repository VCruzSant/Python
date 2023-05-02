#try, excpet, else & finally.
try:
    print('abri arquivo')
    print()
    a = 1/0

except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('tentou dividir por 0')
    print()
else: #vai ser executado caso não haja nenhum erro
    print('não deu erro')

finally: #semre vai ser executado, independente se houver erro 
    print('fechei o arquivo')