# 7. Trabalhar com Diferentes Tipos de Ficheiros
# Escrever ficheiros CSV formatados com DictWriter

'''DictWriter() permite escrever ficheiros CSV diretamente a partir de dicionários.
writeheader() escreve os cabeçalhos no ficheiro automaticamente.'''


import csv
dados = [
{"Nome": "João", "Idade": 25, "Cidade": "Lisboa"},
{"Nome": "Maria", "Idade": 30, "Cidade": "Porto"}
]

with open("c:\\dados_formatados.csv", "w", newline='', encoding="utf-8") as ficheiro:
    campos = ["Nome", "Idade", "Cidade"]
    escritor = csv.DictWriter(ficheiro, fieldnames=campos)
    escritor.writeheader() # Escreve os cabeçalhos
    escritor.writerows(dados) # Escreve os dados


# Boas Práticas ao Trabalhar com Ficheiros CSV em Python

'''
1 - Usar with open() para Gerenciamento Automático de Recursos

2 - Definir encoding="utf-8" para Evitar Problemas com Caracteres Especiais

3 -  Usar newline='' ao Abrir o Ficheiro

4 - Verificar se o ficheiro CSV existe antes de tentar abrir

import os

if os.path.exists("c:\\exemplo1.txt"):
    with open("c:\\exemplo1.txt", "r") as ficheiro:
        print(ficheiro.read())
else:
    print("Erro: O ficheiro não foi encontrado.")'''