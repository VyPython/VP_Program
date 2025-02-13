'''Escreve um programa que calcule e escreva o resultado do fatorial de um número inteiro positivo N
sabendo que: n!=1*2*3*…*n'''

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

try:
    N = int(input("Digite um número inteiro positivo: "))
    if N < 0:
        print("Por favor, digite um número inteiro positivo.")
    else:
        resultado = fatorial(N)
        print(f"O fatorial de {N} é {resultado}")
except ValueError:
    print("Por favor, digite um número inteiro válido.")
