# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import os
import dotenv
import pymysql
import pymysql.cursors

dotenv.load_dotenv()

TABLE_NAME = 'customers'

con = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    cursorclass=pymysql.cursors.DictCursor
)
cursor = con.cursor()

# SQL:

# C:

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
    'id INT NOT NULL AUTO_INCREMENT, '
    'name VARCHAR(50) NOT NULL, '
    'age INT NOT NULL, '
    'PRIMARY KEY (id)'
    ') '
)
# WARNING: esse comando limpa a tabela
# Em ambiente de testes tudo bem, NUNCA fazer isso em produção
cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
con.commit()

# Inserindo valores por tupla:
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, age) '
    'VALUES ("%s", %s) '
)
# Tupla -> não posso editar, Lista -> posso editar
data_tuple = ('Sant', 20)
cursor.execute(sql, data_tuple)
con.commit()

# Inserindo valores por dict
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, age) '
    'VALUES ("%(name)s", %(age)s) '
)
data_dict = {
    "name": "Vini",
    "age": 20
}
cursor.execute(sql, data_dict)
con.commit()

# Inserindo valores por dict em executemany(tem que ser iteráveis):
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, age) '
    'VALUES ("%(name)s", %(age)s) '
)
data_dict_many = (
    {"name": "Cruz", "age": 29},
    {"name": "Example", "age": 19},
    {"name": "Rich", "age": 23}
)
cursor.executemany(sql, data_dict_many)
con.commit()

# Inserindo valores por tuple em executemany(tem que ser iteráveis):
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, age) '
    'VALUES ("%s", %s) '
)
data_tuple_many = (
    ("IA", 5),
    ("Alchemy", 7),
    ("IoT", 50)
)
cursor.executemany(sql, data_tuple_many)
con.commit()


# R:

# Selecionando tudo dentro da table:
sql = (
    f'SELECT * FROM {TABLE_NAME} '
)

cursor.execute(sql)
for row in cursor.fetchall():
    print(row)
print('-----------')

# Selecionando tudo relacionado a um id específico:
column = 'id'
sql = (
    f'SELECT * FROM {TABLE_NAME} '
    f'WHERE {column} = (%s)'
)
id_ = int(input('Digite um id: '))
cursor.execute(sql, id_)
# fetchone pq é uma única linha,
# se eu desse fetchall, ele retornaria uma tupla dentro de tupla
print(cursor.fetchone())
print('-----------')

# U:

sql = (
    f'UPDATE {TABLE_NAME} '
    'SET name = %s, age = %s '
    'WHERE id = %s'
)
cursor.execute(sql, ('Linuz', 18, 2))
con.commit()

sql = (
    f'SELECT * FROM {TABLE_NAME} '
)
cursor.execute(sql)
for row in cursor.fetchall():
    print(row)
print('-----------')

# D:
sql = (
    f'DELETE FROM {TABLE_NAME} '
    'WHERE id = %s'
)
cursor.execute(sql, 3)
con.commit()

sql = (
    f'SELECT * FROM {TABLE_NAME} '
)
cursor.execute(sql)
for row in cursor.fetchall():
    print(row)
print('-----------')

# scrol:
# cursor.scroll(-2) -> padrão relativo
# for row in cursor.fetchall():
#     print(row)

# cursor.scroll(0, 'absolute')
# for row in cursor.fetchall():
#     print(row)

# Scroll com SSDictCursor
# print('fetchall_unbuffered: ')
# sql = (
#     f'SELECT * FROM {TABLE_NAME} '
# )
# cursor.execute(sql)
# for row in cursor.fetchall_unbuffered():
#     print(row)

# rows
sql = (
    f'SELECT * FROM {TABLE_NAME} '
)
resultFromSelect = cursor.execute(sql)
for row in cursor.fetchall():
    print(row)
print('resultFromSelect: ', resultFromSelect)
print('rowCount: ', cursor.rowcount)
print('-----------')

cursor.close()
con.close()
