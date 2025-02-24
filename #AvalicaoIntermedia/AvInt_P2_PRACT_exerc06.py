# PRÁTICA - RESOLVE OS SEGUINTES EXERCÍCIOS
#Reproduz o seguinte Código que tem como objetivo:

# 6 - Cria ou faz download de um ficheiro CSV. De seguida cria um programa que leia o ficheiro CSV e mostre cada linha do mesmo
import csv
import os

if os.path.exists("c:\\test.csv"):
    with open('c:\\test.csv', newline='', encoding='utf-8') as ficheiro:
        leitor = csv.reader(ficheiro)
        for linha in leitor:
            print(linha)
else:
    print("Erro: O ficheiro não foi encontrado.")