import sqlite3
from main import DB_FILE, TABLE_NAME


# Estabelecendo uma conexão com o DB
con = sqlite3.connect(DB_FILE)
# agente que gerencia edições dentro do DB
cursor = con.cursor()

# SQL
# Query: selecione todos os dados dentro da tabela
cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
)

# Query: selecione todos os dados dentro da tabela com um limite de 1
cursor.execute(
    f'SELECT * FROM {TABLE_NAME} LIMIT 1'
)

# cursor.fetchall() -> Extrair dados para o Python
for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

print('-')

# Query: selecione todos os dados dentro da tabela onde o ID = 2
cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE id = "2"'
)

# cursor.fetchone() -> Extrair o único dado para o Python
row = cursor.fetchone()
_id, name, weight = row
print(_id, name, weight)

cursor.close()
con.close()
