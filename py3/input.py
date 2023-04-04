name = input('Qual seu nome? ') #atribuindo uma variavél ao input para salvar uma inf na memória
print (f'seu nome é: {name=}') #nome da varivável com '=' mostra o nome da variavel e o valor que foi atribuido a ela



numb1 = input('Digite um número: ')
numb2 = input('Digite outro número: ')

flonumb1 = float(numb1)#coerção
flonumb2 = float(numb2)

rnumb = flonumb1 + flonumb2 #soma os números ja convertidos pela coerção

print(f'A soma desses números é {rnumb}')#apresenta o resultado
