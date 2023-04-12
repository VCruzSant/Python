names = ['vinicius', 'cruz', 'santiago']
name1, name2, name3 = names
print(name3)

print('-' * 10)

value1, value2, value3, = [1, 2, 3]
print(value1)

obj, *_ = ['toy', 'bike', 'pc', 'mouse'] #apenas o primeiro valor é atribuido a uma variavel, o resto é atribuido a outro variavel (valor -> mesmo pacote | empacotamento)
print(obj) #apenas o primeiro obj
print(_, '|', *_) #se colocar a variavel pacote sem '*' -> os valores vem em [], se tiver '*', os valores vem sem [] 
#boas praticas -> colocar variável não utilizada em '_'

_, numbs, *_ = [20, 30, 50] #para pegar um valor no meio da lista
print(numbs) 