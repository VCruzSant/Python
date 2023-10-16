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
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (name, weight)'
    'VALUES ("Vini Sant", 79.9)'
)
con.commit()

cursor.close()
con.close()
