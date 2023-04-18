
import re #regular expretion
import sys

cpf_enviado = input('Digite seu cpf: ')#.replace('.', '').replace('.', '').replace('-', '') ->é passado dois argumentos: vai substituir um por outro, no caso, vai ser substituido por nada
cpf_enviado = re.sub(
    r'[^0-9]', #tudo o que não estiver entre zero e nove
    '', #vai ser substituido por isso
    cpf_enviado
)

enviou_sequencia = cpf_enviado == cpf_enviado[0] * len(cpf_enviado)
if enviou_sequencia:
    print('Enviou sequencia')
    sys.exit()

if len(cpf_enviado) != 11:
    print('Quantidade de digitos insuficientes')
    sys.exit()

nove_digitos = cpf_enviado[:9]
contador_1 = 10

resultado_1 = 0
for digitos in nove_digitos:
    resultado_1 += int(digitos) * contador_1
    contador_1 -= 1

digito_1 = (resultado_1 * 10) % 11
digito_1 = digito_1 if digito_1 <=9 else 0


dez_digitos = nove_digitos + str(digito_1)
contador_2 = 11

resultado_2 = 0
for digitos_2 in dez_digitos:
    resultado_2 += int(digitos_2) * contador_2
    contador_2 -= 1

digito_2 = (resultado_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_calculado = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado == cpf_calculado:
    print(f'Seu cpf {cpf_enviado} é valido')

else:
    print('Seu cpf não é valido')

