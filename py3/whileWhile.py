qnt_line = 5
qnt_colum = 5
line = 1
while line <= qnt_line:
    colum = 1
    while colum <= qnt_colum: #toda vez que linha for menor que a quantidade de linha, ou seja, minha cond for True, 
        print(line, colum) #imprima a linha e coluna 
        colum +=1 #some mais 1
    line += 1# para cada linha 
print('Acabou')