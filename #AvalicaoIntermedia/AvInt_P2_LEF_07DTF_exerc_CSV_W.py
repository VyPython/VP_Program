# 7. Trabalhar com Diferentes Tipos de Ficheiros
# Escrita num ficheiro CSV – O código seguinte cria um ficheiro CSV com duas colunas (Nome, Idade).

'''writerows() escreve múltiplas linhas de uma vez.
Se o ficheiro já existir, será sobrescrito.'''


import csv
data = [["Nome", "Idade"], ["João", 25], ["Ana", 30]]
with open("c:\\data.csv", "w", newline='', encoding="utf-8") as ficheiro:
    escritor = csv.writer(ficheiro)
    escritor.writerows(data)