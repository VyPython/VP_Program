# Parte III – SQLite em Python
# PRÁTICA
# 5. Eliminar dados


import sqlite3

conn = sqlite3.connect('c:\\empresa.db')
cursor = conn.cursor() # Cria o Cursor para interagir com a BD


# eliminar um funcionários
#cursor.execute("DELETE FROM funcionarios WHERE nome ='Marina Costa'")
cursor.execute("DELETE FROM funcionarios WHERE salario < ?", (3000,))

conn.commit() # Grava as Alterações

cursor.execute("SELECT * FROM funcionarios")
for linha in cursor.fetchall():
    print(linha)
    
conn.close() # Fecha a Conexão

