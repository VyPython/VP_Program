# PRÁTICA - RESOLVE OS SEGUINTES EXERCÍCIOS
#Reproduz o seguinte Código que tem como objetivo:

# 4 - Modificar o programa anterior para acrescentar mais uma linha ao ficheiro.

with open("c:\\novo_ficheiro.txt", "a") as ficheiro:
    ficheiro.write("Linha adicional\n")

'''with open("c:\\novo_ficheiro.txt", "r") as ficheiro:
    print(ficheiro.read())'''  