# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
from pathlib import Path
import csv

PATH_CSV = Path(__file__).parent / 'csv_ex2.csv'

customer_list = [
    {'Name': 'Vini', 'Adress': 'Av 1, 22'},
    {'Name': 'Cruz', 'Adress': 'R. 2, "1"'},
    {'Name': 'Sant', 'Adress': 'Av B, 3A'},

]
with open(PATH_CSV, 'w', encoding='utf8', newline='') as file:
    # reader = csv.writer(file)
    # name_colum = customer_list[0].keys()
    # reader.writerow(name_colum)

    # for customer in customer_list:
    #     name_line = customer.values()
    #     reader.writerow(name_line)

    name_colum = customer_list[0].keys()
    reader = csv.DictWriter(
        file,
        fieldnames=name_colum
    )
    reader.writeheader()

    for customer in customer_list:
        reader.writerow(customer)
