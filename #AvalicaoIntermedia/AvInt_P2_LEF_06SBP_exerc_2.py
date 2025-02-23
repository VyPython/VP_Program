# 6 Segurança e Boas Práticas
# ii. Prevenir falhas com tre-except – garante robustez contra falhas



'''Evitar erros ao tentar abrir ficheiros inexistentes:'''

import os
try:
    with open("c:\\exemplo2.txt", "r") as ficheiro:
        print(ficheiro.read())
except FileNotFoundError:
    print("Erro: O ficheiro não existe.")
except Exception as e:
    print (f"Ocorreu um erro inesperado: {e}")