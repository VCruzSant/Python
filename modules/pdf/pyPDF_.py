# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

ROOT_PATH = Path(__file__).parent
ORIGINALS_FOLDER = ROOT_PATH / 'pdf_original'
NEW_FOLDER = ROOT_PATH / 'new_files'

BACEN_REPORT = ORIGINALS_FOLDER / 'R20230908.pdf'
NEW_FOLDER.mkdir(exist_ok=True)

# configurando o leitor do pdf
reader = PdfReader(BACEN_REPORT)

# # pedindo pro len contar quantas paginas tem
# print(len(reader.pages))

# # printando o que tem nas páginas
# for page in reader.pages:
#     print(page)

# identificando a pagina 1
page1 = reader.pages[0]

# printando o texto da pagina 1:
# print(page1.extract_text())

# # printando as imagens da página 1:
# print(page1.images)

# manipulando a imagem selecionada
# wb(write bytes) por causa que a imagem é em bytes
with open(NEW_FOLDER / page1.images[0].name, 'wb') as image:
    # Criando o arquivo da imagem:
    image.write(page1.images[0].data)


# criando um pdf de uma página somente:
# writer = PdfWriter()
# writer.add_page(page1)


# with open(NEW_FOLDER / 'page0.pdf', 'wb') as fp:
#     writer.write(fp)  # type: ignore


# criando um pdf com todas as páginas:
# criando um arquivo e abrindo no modo de escrita write bytes:
# with open(NEW_FOLDER / 'new_pdf.pdf', 'wb') as fp:
# para cada página nas páginas lidas:
# for page in reader.pages:
# adicione a página:
# writer.add_page(page)
# crie o pdf
# writer.write(fp)


# Criando um pdf para cada pagina:
# para cada página lida, númere:
for i, page in enumerate(reader.pages):
    # configurando o writer:
    writer = PdfWriter()
    # criando e escrevendo o novo arquivo:
    with open(NEW_FOLDER / f'page{i}.pdf', 'wb') as fp:
        # adicionando uma página
        writer.add_page(page)
        # escrevendo no arquivo:
        writer.write(fp)


files = [
    NEW_FOLDER / 'page1.pdf',
    NEW_FOLDER / 'page0.pdf',
]

merger = PdfMerger()
for file in files:
    merger.append(file)

with open(NEW_FOLDER / 'merged.pdf', 'wb') as fp:
    merger.write(fp)
