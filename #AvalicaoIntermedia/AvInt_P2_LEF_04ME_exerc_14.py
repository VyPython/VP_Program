# 4 Métodos de Escrita de Ficheiros
# xiv. write() - Escrever num ficheiro - sobrescreve o conteúdo

with open("c:\\nexemplo.txt", "w") as ficheiro:
    ficheiro.write("Esta é a nova primeira linha.\n")
    ficheiro.write("Segunda linha do ficheiro.")