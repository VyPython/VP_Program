# PRÁTICA - RESOLVE OS SEGUINTES EXERCÍCIOS
#Reproduz o seguinte Código que tem como objetivo:

# 2 - Modificar o exercício anterior para exibir o conteúdo linha por linha.

with open("c:\\exemplo.txt", "r") as ficheiro:
    for linha in ficheiro:
        print(linha.strip())

