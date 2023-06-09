import os

palavra_secreta = "nicolly"
letras_acertadas = ""  # variavel que salva as letras acertadas
num_tentativas = 0

while True:
    letra_digitada = input("Digite uma letra: ")
    num_tentativas += 1
    numbs = "123456789"

    if len(letra_digitada) > 1:  # lógica de apenas uma letra
        print("Digite apenas uma letra")
        continue

    elif letra_digitada == "":
        print("Você não digitou uma letra")
        continue

    elif letra_digitada in numbs:
        print("digite apenas letras")
        continue

    if letra_digitada in palavra_secreta:  # lógica que salva as letras acertadas
        letras_acertadas += letra_digitada

    palavra_formada = ""
    for letra_secreta in palavra_secreta:  # itera sobre palavra secreta
        if (
            letra_secreta in letras_acertadas
        ):  # se a letra secreta estiver na letra acertada
            palavra_formada += (
                letra_secreta  # a palavra formada recebe essa letra acertada
            )
        else:
            palavra_formada += "*"

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system("cls")
        print(f"VOCÊ ACERTOU: {palavra_secreta}!")
        print(f"tentativas: {num_tentativas}")
        letras_acertadas = ""
