# Parte III – SQLite em Python
# 5 - Atualizar e Apagar Dados
import sqlite3
import os

conexao = sqlite3.connect('c:\\universidade.db') # Cria a Base de Dados
cursor = conexao.cursor() # Cria o Cursor para interagir com a BD


# selecionar todos os alunos na tabela
#cursor.execute("UPDATE Alunos SET idade = ? WHERE nome = ?", (24, "João"))
cursor.execute("DELETE FROM Alunos WHERE nome = ?", ("João",))
conexao.commit() # Grava as Alterações
conexao.close() # Fecha a Conexão

print("Aluno eliminado com Sucesso!")