"""
try -> tente executar o código
except -> se ocorrer erro no try, tente isso
"""

numstr = input("Digite um número: ")

'''if numstr.isdigit():
    numflo = float(numstr)
    print(f"o dobro de {numstr} é: {numflo * 20}")

else:
    print("não é um número valido")
'''
try:
    numflo = float(numstr)
    print(f"o dobro de {numstr} é: {numflo * 2}")

except:
    print("não é um número valido")

#try e except não é usado assim, usei assim para entender o funcionamento.