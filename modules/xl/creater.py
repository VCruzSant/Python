# openpyxl para arquivos Excel xlsx, xlsm, xltx e xltm (instalação)
# Com essa biblioteca será possível ler e escrever dados em células
# específicas, formatar células, inserir gráficos,
# criar fórmulas, adicionar imagens e outros elementos gráficos às suas
# planilhas. Ela é útil para automatizar tarefas envolvendo planilhas do
# Excel, como a criação de relatórios e análise de dados e/ou facilitando a
# manipulação de grandes quantidades de informações.
# Instalação necessária: pip install openpyxl
# Documentação: https://openpyxl.readthedocs.io/en/stable/
from pathlib import Path

from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

ROOT_FOLDER = Path(__file__).parent
WORKBOOK_PATH = ROOT_FOLDER / 'workbook.xlsx'

# configurando a classe que edita planilhas
workbook = Workbook()

# criando uma página pra planilha:
sheet_name = 'My Sheet'
workbook.create_sheet(sheet_name, 0)

# dizendo pro python que quero mexer na planilha que eu selecionei
worksheet: Worksheet = workbook.active  # type: ignore

# printando os nomes das páginas de planilhas existentes:
print(workbook.sheetnames)

# remover uma planilha:
workbook.remove(workbook['Sheet'])
print(workbook.sheetnames)


# criando cabeçalhos
worksheet.cell(1, 1, 'Name')
worksheet.cell(1, 2, 'Age')
worksheet.cell(1, 3, 'Note')

students = [
    # name      age   note
    ['João',    14,   5.5],
    ['Maria',   13,   9.7],
    ['Luiz',    15,   8.8],
    ['Alberto', 16,   10],
]

# # começa em 2 pq a linha 1 é do cabeçalho:
# for i, student_row in enumerate(students, start=2):
#     for j, student_column in enumerate(student_row, start=1):
#         # como i e j são a númeração, só passo o conteudo
#         worksheet.cell(i, j, student_column)

# método mais fácil:
for student in students:
    worksheet.append(student)

# salvando a planilha configurada no caminho desejado
workbook.save(WORKBOOK_PATH)
