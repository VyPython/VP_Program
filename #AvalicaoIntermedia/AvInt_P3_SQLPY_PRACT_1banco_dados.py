# Parte III – SQLite em Python
# PRÁTICA
# 1. Criar um ficheiro python, banco_dados.py


import sqlite3

conn = sqlite3.connect('c:\\empresa.db') # Cria a Base de Dados
cursor = conn.cursor() # Cria o Cursor para interagir com a BD


# Criar a tabela funcionários
cursor.execute('''
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cargo TEXT NOT NULL,
    salario REAL NOT NULL
    )
''')
conn.commit() # Grava as Alterações
conn.close() # Fecha a Conexão

