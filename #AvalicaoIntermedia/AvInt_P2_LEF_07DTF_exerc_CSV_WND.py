# 7. Trabalhar com Diferentes Tipos de Ficheiros
# Acrescentar dados a um ficheiro CSV existente

'''O modo "a" permite acrescentar conteúdo sem apagar os dados existentes.'''


import csv
new_data = [
    ["Carlos", 35, "Braga"],
    ["Ana", 40, "Faro"]
]

with open("c:\\data.csv", "a", newline='', encoding="utf-8") as ficheiro:
    escritor = csv.writer(ficheiro)
    escritor.writerows(new_data)