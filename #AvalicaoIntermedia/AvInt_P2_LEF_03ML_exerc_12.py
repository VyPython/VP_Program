# 3 Métodos de Leitura de Ficheiros
# xii) readline() - Lê linha a linha, evita ocupação da memmória

with open("c:\\exemplo.txt", "r") as ficheiro:
    linha = ficheiro.readline()
    while linha:
        print(linha, end="")
        linha = ficheiro.readline()