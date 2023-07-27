import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# paths

PATH_SEED = Path(__file__).parent
PATH_ZIP_DIR = PATH_SEED / 'zip_dir'
PATH_ZIPPED = PATH_SEED / 'zipped.zip'
PATH_UNZIPPED = PATH_SEED / 'unzipped'

# delete path

# Cria diretório
PATH_ZIP_DIR.mkdir(exist_ok=True)


def make_file(amount: int, zip_dir: Path):
    for i in range(amount):
        txt = 'file_%s' % i
        with open(zip_dir / f'{txt}.txt', 'w') as file:
            file.write(txt)


make_file(3, PATH_ZIP_DIR)
