from pathlib import Path
from shutil import rmtree

# até a pasta do projeto
PATH_PRJ = Path()
print(PATH_PRJ.absolute())

# vai até o arquivo final
PATH_FILE = Path(__file__)
print(PATH_FILE)

# o dir do arquivo
print(PATH_FILE.parent)

# mãe da pasta modules que é onde está o pathlib
print(PATH_FILE.parent.parent)

# criado um caminho de uma nova pasta
ideas = PATH_FILE.parent / 'ideas'

# criado um caminho de um novo arquivo
idea_file = ideas / 'idea.txt'

print(ideas)
print(idea_file)

# exemplo, meu softawe tem opção de salvar as configurações mas eu não dei
# opção para ele escolher então eu salvo na home dele
file_config = Path.home() / 'configsoft.txt'

# para criar o arquivo:
file_config.touch()
print(file_config)
# escrevendo algo no arquivo:
file_config.write_text('Olá Mundo')
# lendo o que tem no arquivo:
print(file_config.read_text())
# deletando o arquivo:
file_config.unlink()

with open(file_config, 'a+', encoding='utf8') as file:
    file.write('uma linha \r\n')
    file.write('outra linha')

print(file_config.read_text())

# criando uma pasta
path_foo = Path.home() / 'path_example_foo'
path_foo.mkdir(exist_ok=True)
sub_foo = path_foo / 'sub_path_foo'
sub_foo.mkdir(exist_ok=True)
sub_foo_file = sub_foo / 'foo.txt'
sub_foo_file.touch()
sub_foo_file.write_text('hellow word')
print(sub_foo_file.read_text())

# para apagar pastas
rmtree(path_foo)
