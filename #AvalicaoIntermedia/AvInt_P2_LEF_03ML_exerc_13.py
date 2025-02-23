# 3 Métodos de Leitura de Ficheiros
# xiii. readlines() - Retorna todas as linhas como uma lista - cada linha é um elemento

with open("c:\\exemplo.txt", "r") as ficheiro:
    linhas = ficheiro.readlines()
    for linha in linhas:
        print(linha.strip())