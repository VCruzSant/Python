# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime
from pytz import timezone
# date = datetime(2023, 7, 3)

date_ = '2023-07-03 21:15:32'
date_frmt = '%Y-%m-%d %H:%M:%S'

date = datetime.strptime(date_, date_frmt)
date_zone = datetime(2023, 7, 3, tzinfo=timezone('Asia/Singapore'))

date_now = datetime.now()

print(date)
print(datetime.now(timezone('Asia/Singapore')))
print(date_zone)

print(date_now.timestamp())
print(datetime.fromtimestamp(1688431544.838016))
