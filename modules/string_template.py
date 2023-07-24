# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
from datetime import datetime
from string import Template
from pathlib import Path
import locale

PATH_TEMPLATE = Path(__file__).parent / 'template.txt'


locale.setlocale(locale.LC_ALL, '')


def convert_to_br(number: float) -> str:
    brl = locale.currency(val=number, grouping=True)
    return brl


date_ = datetime(2023, 6, 7)

data = dict(
    name='Vini',
    value=convert_to_br(1_234_456),
    date=date_.strftime('%d/%m/%Y'),
    company='V. S.',
    # tel='+55 (11) 1111-1111'
)

with open(PATH_TEMPLATE, 'r', encoding='utf8') as file:
    text = file.read()
    template_ = Template(text)
    # print(template_.substitute(data))

    # quando eu não tiver todas as variáveis do template:
    print(template_.safe_substitute(data))
