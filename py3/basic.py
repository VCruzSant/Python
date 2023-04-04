print(123)  # for commentary
ler = '''
    String or documentation
    If y assign to a variable and to print, the console will to read.
    Number int (1, 2, 100, 12134)
    Number float (1.5, 2.8, 5.235)
    phyton is case sensitive
    it isn`t necessary finish line, with ";" for example
'''

print(ler)
print('5' * 5)  # will be printed the number 5, five times

if True:
    pass  # this is indentation

'''
    Arithmetic operators:
    + -> sum or concatenation
    - -> subtraction
    * -> multiplication
    / -> division
    // -> division with result int
    % -> Módulo, resto da divisão
    ** -> potentiation 
'''

print('Divide 10 por 3:', 10/3)
print('Divide 10 por 3 mas só mostra o resultado int:', 10//3)
print('resto da divisão:', 5%2)

'''
    Variáveis:
    Salva alguma informação na memória do computador, python tem tipagem dinâmica.
'''
nome = 'Vini Sant'
idade = 19
altura = 1.8
peso = 75
data = '4/03/2023'

idiceMassaCorporal = peso / (altura**2)
print(nome, 'tem', idade, 'anos e seu IMC é:', idiceMassaCorporal)

print ('Com o ".format" fica: {n} tem {i} anos e seu IMC é: {imc}'.format(n=nome, i=idade, imc=idiceMassaCorporal)) #pode ser substituido por número, no caso nome seria 0, idade 1 e assim vai

print(f'{nome} tem {idade} anos e seu IMC é: {idiceMassaCorporal}')

'''
    Tipos de Dados
    int -> números inteiros
    float ->número reais (quebrados)
    bool -> valor lógico (True, False)
    str -> string ou cadeia de caracteres (texto)
'''

inteiro = 10
real = 10.5
booleano = True
texto = '5.5'

print(inteiro + float(texto)) # convertendo text = '5.5' que está como str para float

print(46, 39, sep='-') #separador

'''
\r\n -> CRLF -> quebra linha
\n ->LF ->unix
'''