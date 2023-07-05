# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo

import calendar

# print(calendar.calendar(2023))
# print(calendar.month(2023, 7))
# print(calendar.monthrange(2023, 7))
# print(list(calendar.day_name))

# first_day_wk, last_day_numb = calendar.monthrange(2023, 7)

# print(calendar.day_name[first_day_wk])

# print(calendar.monthcalendar(2023, 7))
for w in calendar.monthcalendar(2023, 7):
    print(list(enumerate(w)))
    # for d in w:
#         print(d)
