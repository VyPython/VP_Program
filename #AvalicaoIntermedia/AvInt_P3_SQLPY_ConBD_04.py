# Parte III – SQLite em Python
# 4 - Ler Dados da Base de Dados
import sqlite3
import os

conexao = sqlite3.connect('c:\\universidade.db') # Cria a Base de Dados
cursor = conexao.cursor() # Cria o Cursor para interagir com a BD


# selecionar todos os alunos na tabela
cursor.execute("SELECT * FROM Alunos")
alunos = cursor.fetchall()
for aluno in alunos:
    print(aluno)
    
conexao.close() # Fecha a Conexão

