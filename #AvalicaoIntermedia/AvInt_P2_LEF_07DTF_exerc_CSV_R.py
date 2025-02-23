# 7. Trabalhar com Diferentes Tipos de Ficheiros
# Leitura de um ficheiro CSV

'''csv.reader() converte cada linha do ficheiro CSV numa lista de valores.
newline='' evita problemas com quebras de linha extras.
encoding="utf-8" garante compatibilidade com caracteres especiais.'''


import csv
with open("c:\\dados.csv", newline='', encoding="utf-8") as ficheiro:
    leitor = csv.reader(ficheiro)
    for linha in leitor:
        print(linha)