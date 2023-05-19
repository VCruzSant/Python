import os

# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

path_created = 'C:\\Games\\locals_created\\'
path_created += 'locals_created.txt'

# file = open(path_created, 'w')

# file.close() #sempre que for abrir um arquivo já fecha para evitar dor de cabeça

with open(path_created, 'w+', encoding='utf8') as file:
    file.write('hellow word\r\n')
    file.write('ai ai ai ai ai\n')
    file.write('sla \r\n')
    file.writelines(
        ('outra linha do witrelines \n', 'mais uma linha ateção do writelines\n')
    )
    file.seek(0, 0) #move o 'cursor' do python para o topo do arquivo dnv
    print(file.read()) # e assim ele pode ler o que tem

# os.unlink(path_created) #-> excluindo
# os.rename(path_created, 'renamed_created.txt')

