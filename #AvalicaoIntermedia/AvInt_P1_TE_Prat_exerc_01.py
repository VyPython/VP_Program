# 1) Reproduz o seguinte código.
'''Escreva um programa que pede ao utilizador um número inteiro e trata erros de entrada.'''

try:
    numero = int(input("Digite um número inteiro: "))
    print("Número inserido:", numero)
except ValueError:
    print("Erro: O valor dever ser um número inteiro.")
