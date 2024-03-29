import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

# Estabelecendo uma conexão com o DB
con = sqlite3.connect(DB_FILE)
# agente que gerencia edições dentro do DB
cursor = con.cursor()

# SQL

# CUIDADO: Delete sem where
# Zerar tabela para inicio limpo:
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

# Apagando sequencia do ID
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)

# criando uma table
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
con.commit()

# Registrando valores

# CUIDADO: SQL injection
# cursor.execute(
#     f'INSERT INTO {TABLE_NAME} (name, weight)'
#     'VALUES ("Vini Sant", 79.9)'
# )

# Maneira correta com bindings:
sql = (
    f'INSERT INTO {TABLE_NAME} (name, weight) '
    'VALUES '
    '(:name, :weight)'
)

# executa um só comando:
# cursor.execute(sql, ['vini sant', 79.9])

# executa um comando com vários valores, lista ou tuplas de valores:
# cursor.executemany(
#     sql,
#     [
#         ['vini sant', 79.9], ['Cruz Vini', 79.9]
#     ]
# )

cursor.executemany(
    sql,
    [
        {'name': 'Vini', 'weight': 80}, {'name': 'Sant', 'weight': 80}
    ]
)

cursor.execute(
    f'DELETE FROM {TABLE_NAME} '
    'WHERE id = "2"'
)
con.commit()

cursor.execute(
    f'UPDATE {TABLE_NAME} '
    'SET name = "Mudei o Nome"'
    'WHERE id = "1"'
)
con.commit()

cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
)

# cursor.fetchall() -> Extrair dados para o Python
for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

cursor.close()
con.close()
