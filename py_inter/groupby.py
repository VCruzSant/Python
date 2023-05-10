# groupby -> agrupando valores

from itertools import groupby

student = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def order(student):
    return student['nota']


grouped_student = sorted(student, key=order) #ordenando para o groupby agrupar
groups_point = groupby(grouped_student, key=order) #agrupando pela key nota





for key, group in groups_point: #grupo completo, ainda em lista
    print(key)
    for student in group: #apenas o dict de cada aluno
        print(student)
