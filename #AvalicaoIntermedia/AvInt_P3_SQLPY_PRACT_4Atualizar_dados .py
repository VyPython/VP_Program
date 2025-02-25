# Parte III – SQLite em Python
# PRÁTICA
# 4. Atualizar dados


import sqlite3

conn = sqlite3.connect('c:\\empresa.db')
cursor = conn.cursor() # Cria o Cursor para interagir com a BD


# atualizar funcionários
cursor.execute("UPDATE funcionarios SET salario = 3000.00 WHERE nome ='Pedro Santos'")

conn.commit() # Grava as Alterações

cursor.execute("SELECT * FROM funcionarios")
for linha in cursor.fetchall():
    print(linha)
    
conn.close() # Fecha a Conexão

