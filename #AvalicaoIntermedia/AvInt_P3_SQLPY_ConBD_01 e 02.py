# Parte III – SQLite em Python
# 1 - Criar uma Base de Dados SQLite3 em Python e 2 - Criar uma Tabela em SQLite3
import sqlite3
import os

conexao = sqlite3.connect('c:\\universidade.db') # Cria a Base de Dados
cursor = conexao.cursor() # Cria o Cursor para interagir com a BD
print("Base de Dados Criada com Sucesso!")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idade INTEGER,
    curso TEXT
)
""") # Cria a Tabela Alunos

print("Tabela Alunos Criada com Sucesso!")

conexao.commit() # Grava as Alterações
conexao.close() # Fecha a Conexão
