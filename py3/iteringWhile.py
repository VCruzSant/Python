frase = 'wwwbb'

i = 0
qntd_apareceu_mais = 0
letra_apareceu_mais = ''


while i < len(frase):
    letra_atual = frase[i]
    qntd_atual = frase.count(letra_atual)

    if letra_atual == ' ':
        i+= 1
        continue


    if qntd_atual > qntd_apareceu_mais:
        qntd_apareceu_mais = qntd_atual
        letra_apareceu_mais = letra_atual

    i += 1

print(f'a letra que apareceu mais foi: "{letra_apareceu_mais}" que apareceu {qntd_apareceu_mais}x')