# Parte III – SQLite em Python
# PRÁTICA
# 3. Consultar dados


import sqlite3

conn = sqlite3.connect('c:\\empresa.db')        # Conecta com a BD
cursor = conn.cursor()                          # Cria o Cursor para interagir com a BD

cursor.execute("SELECT * FROM funcionarios")    #consultar todos os dados da tabela funcionarios
for linha in cursor.fetchall():                 #percorre todas as linhas
    print(linha)                                #imprime cada linha
    
conn.close()                                    # Fecha a Conexão

