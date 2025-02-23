# PRÁTICA - RESOLVE OS SEGUINTES EXERCÍCIOS
#Reproduz o seguinte Código que tem como objetivo:

#1 - Criar um programa que leia um ficheiro de texto e exibir o seu conteúdo

with open("c:\\exemplo.txt", "r") as ficheiro:
    conteudo = ficheiro.read()
    print(conteudo)
