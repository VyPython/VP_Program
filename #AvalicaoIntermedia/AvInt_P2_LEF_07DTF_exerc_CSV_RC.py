# 7. Trabalhar com Diferentes Tipos de Ficheiros
# Ler um ficheiro CSV com cabeçalhos e converter para dicionário

'''csv.DictReader( ) cria um dicionário onde as chaves são os nomes das colunas.
Facilita a extração de dados sem precisar de índices numéricos.'''


import csv
with open("c:\\dados.csv", newline='', encoding="utf-8") as ficheiro:
    leitor = csv.DictReader(ficheiro) # Converte cada linha num dicionário
    for linha in leitor:
        print(linha["Nome"], "-", linha["Idade"])