# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html

from datetime import datetime

fmt = '%d/%m/%Y'
# date = datetime('2024, 10, 27')
date = datetime.strptime('2024-10-27', '%Y-%m-%d')
print(date)
print(date.strftime(fmt))
