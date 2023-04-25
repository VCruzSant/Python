# Exercício - sistema de perguntas e respostas

quest = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

print(len(quest))




qnt_acertos = 0
for ques in quest:
    print('Pergunta:', ques['Pergunta'])
    print()



    for i, opt in enumerate(ques['Opções']):
        print(f'{i})', opt)
    print()

    resp_1 = input('Escolha uma laternativa: ')
    print()



    acertou = False
    resp_1_int  = None


    qtd_opt = len(ques['Opções'])



    if resp_1.isdigit():
        resp_1_int = int(resp_1)



    if resp_1_int is not None:
        if resp_1_int >= 0 and resp_1_int <=  qtd_opt:
            if ques['Opções'][resp_1_int] == ques['Resposta']:
                acertou = True


    
    if acertou:
        qnt_acertos += 1
        print('Acertou ✅')
        print()
    else:
        print('Errou ❌')
        print()

print(f'você acertou {qnt_acertos}')
print(f'de {len(quest)} perguntas')



