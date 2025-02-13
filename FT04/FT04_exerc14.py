'''Elabora um programa que pede ao utilizador para inserir dois números inteiros. O programa deve
escrever todos os números inteiros entre os dois limites por ordem crescente. Utiliza o ciclo for'''

# Solicita ao utilizador para inserir dois números inteiros
num1 = int(input("Insira o primeiro número inteiro: "))
num2 = int(input("Insira o segundo número inteiro: "))

# Determina o menor e o maior número
if num1 > num2:
    num1, num2 = num2, num1

# Escreve todos os números inteiros entre os dois limites por ordem crescente
for i in range(num1, num2 + 1):
    print(i)