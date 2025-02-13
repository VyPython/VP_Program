'''Escreva um programa que peça ao utilizador 20 números reais e no final mostre a soma e a média'''

numeros = []
for _ in range(20):
    numero = float(input("Digite um número real: "))
    numeros.append(numero)

soma = sum(numeros)
media = soma / len(numeros)

print(f"Soma: {soma}")
print(f"Média: {media}")