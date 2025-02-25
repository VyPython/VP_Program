# Parte III – SQLite em Python
# PRÁTICA
# 2. inserir dados


import sqlite3

conn = sqlite3.connect('c:\\empresa.db')
cursor = conn.cursor() # Cria o Cursor para interagir com a BD


# inserir funcionários
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Carla Antunes', 'Assistente', 1500)")
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Sérgio Costa', 'Progamador Jr', 1900)")

conn.commit() # Grava as Alterações

cursor.execute("SELECT * FROM funcionarios")
for linha in cursor.fetchall():
    print(linha)
    
conn.close() # Fecha a Conexão

