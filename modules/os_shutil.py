# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'desktop')
MY_FOLDER = os.path.join(DESKTOP, 'investimento')
NEW_FOLDER = os.path.join(DESKTOP, 'new_foler')

os.makedirs(NEW_FOLDER, exist_ok=True)

for roots, dirs, files in os.walk(MY_FOLDER):
    # print(roots)
    # print(files)

    for dir_ in dirs:
        # para criar os diretórios
        path_new_directory = os.path.join(
            # se fosse direto no new_folder, não pegaria subdiretórios
            roots.replace(MY_FOLDER, NEW_FOLDER), dir_
        )
        print(path_new_directory)
        os.makedirs(NEW_FOLDER, exist_ok=True)

    for file in files:
        path_file = os.path.join(roots, file)
        path_new_file = os.path.join(
            # se fosse direto no new_folder, não pegaria subdiretórios
            roots.replace(MY_FOLDER, NEW_FOLDER), file
        )
        # print(path_file)
        # print(path_new_file)
        shutil.copy(MY_FOLDER, NEW_FOLDER)

# print(HOME)
# print(DESKTOP)
# print(os.path.exists(HOME))
# print(os.listdir(DESKTOP))
