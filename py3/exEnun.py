number = input("Digite um número inteiro: ")


if number.isdigit():
    intNumb = int(number)

    if (intNumb % 2) == 0:
        print("Seu número é par")

    else:
        print("Seu número é impar")

else:
    print("Digite um número valido")

print("-" * 10)


hour = input("Digite que horas são: ")

try:
    hNumber = float(hour)

    if hNumber >= 0 and hNumber <= 11:
        print("Bom dia")

    elif hNumber >= 12 and hNumber <= 17:
        print("Boa Tarde")

    elif hNumber >= 18 and hNumber <= 23:
        print("Boa noite")


except:
    print("digite uma hora valida")

print('-' * 10)

name = input("Digite seu nome: ")
tname = len(name)

if tname > 1 and tname <= 4:
    print("Seu nome é curto")
elif tname == 5:
    print("Seu nome é normal")
elif tname > 6:
    print("Seu nome é gande")
else:
    print("não entendi seu nome")
