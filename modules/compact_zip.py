import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# paths
PATH_SEED = Path(__file__).parent
PATH_ZIP_DIR = PATH_SEED / 'zip_dir'
PATH_ZIPPED = PATH_SEED / 'zipped.zip'
PATH_UNZIPPED = PATH_SEED / 'unzipped'


# Cria diretório
PATH_ZIP_DIR.mkdir(exist_ok=True)

# cria arquivos


def make_file(amount: int, zip_dir: Path):
    for i in range(amount):
        txt = 'file_%s' % i
        with open(zip_dir / f'{txt}.txt', 'w') as file:
            file.write(txt)


make_file(3, PATH_ZIP_DIR)

# compacta os arquivos para um zip
with ZipFile(PATH_ZIPPED, 'w') as zip:
    for root, dirs, files in os.walk(PATH_ZIP_DIR):
        for file in files:
            # dessa maneira o python compacta apenas os arquivos e não
            # o diretório como um todo:
            zip.write(os.path.join(root, file), file)

# lê arquivos zip
with ZipFile(PATH_ZIPPED, 'r') as zip:
    for file in zip.namelist():
        print(file)

# descompactando arquivo zip
with ZipFile(PATH_ZIPPED, 'r') as zip:
    zip.extractall(PATH_UNZIPPED)
