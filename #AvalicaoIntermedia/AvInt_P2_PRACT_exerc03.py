# PRÁTICA - RESOLVE OS SEGUINTES EXERCÍCIOS
#Reproduz o seguinte Código que tem como objetivo:

# 3 - Criar um programa que escreva três linhas num ficheiro novo.

with open("c:\\novo_ficheiro.txt", "w") as ficheiro:
    ficheiro.write("Linha 1\n")
    ficheiro.write("Linha 2\n")
    ficheiro.write("Linha 3\n")
