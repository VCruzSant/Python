# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
date_init = datetime.strptime('10/10/2010 10:10:10', fmt)
date_end = datetime.strptime('20/10/2020 20:20:20', fmt)

delta = date_end - date_init

delt_time = timedelta(days=27, hours=10)
relative = relativedelta(date_init, date_end)

# print(delta.days, delta.seconds)
print(date_end - delt_time)

print(date_end + relativedelta(seconds=60))

print(relative.days, relative.hours)
