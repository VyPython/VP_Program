# Parte III – SQLite em Python
# 3 - Inserir Dados na Tabela
import sqlite3
import os

conexao = sqlite3.connect('c:\\universidade.db') # Cria a Base de Dados
cursor = conexao.cursor() # Cria o Cursor para interagir com a BD


# Inserir alunos na tabela
#cursor.execute("INSERT INTO Alunos (nome, idade, curso) VALUES (?, ?, ?)", ("João", 20, "Informática"))
cursor.execute("INSERT INTO Alunos (nome, idade, curso) VALUES (?, ?, ?)", ("Maria", 22, "Matemática"))
cursor.execute("INSERT INTO Alunos (nome, idade, curso) VALUES (?, ?, ?)", ("Carlos", 21, "Física"))
cursor.execute("INSERT INTO Alunos (nome, idade, curso) VALUES (?, ?, ?)", ("Ana", 23, "Química"))

conexao.commit() # Grava as Alterações
conexao.close() # Fecha a Conexão
print("Dados inseridos com Sucesso!")
