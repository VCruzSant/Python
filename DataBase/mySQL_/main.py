# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import os
import dotenv
import pymysql

dotenv.load_dotenv()

TABLE_NAME = 'customers'

con = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE']
)
cursor = con.cursor()

# SQL:
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

sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, age) '
    'VALUES ("%s", %s) '
)
# Tupla -> não posso editar, Lista -> posso editar
data = ('Sant', 20)
cursor.execute(sql, data)
con.commit()


cursor.close()
con.close()
