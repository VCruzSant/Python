# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime
from dateutil.relativedelta import relativedelta

t_value = 1_000_000
date_loan = datetime(2020, 12, 20)
delta_yrs = relativedelta(years=5)
date_end = date_loan + delta_yrs

date_insts = []
date_inst = date_loan

while date_inst < date_end:
    date_insts.append(date_inst)
    date_inst += relativedelta(month=+1)

numb_inst = len(date_insts)
value_inst = t_value / numb_inst
for d in date_insts:
    print(d)
