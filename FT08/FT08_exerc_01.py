'''1. Escreva um programa que, dada uma sequência de números inteiros
(todos fornecidos na mesma linha, separados por espaços), imprima
a média desses números.'''


# Lê a entrada digitada e divide os números
numeros = list(map(int, input("Digite os números separados por espaço: ").split()))

# Calcula a média
media = sum(numeros) / len(numeros) if numeros else 0

# Exibe o resultado
print(f"A média é: {media:.2f}")




# Solução alternativa
texto = input("Digite uma sequencia de números separados por espaço: ")
numeros = texto.split()
soma = 0
for n in numeros:
    soma += int(n)
media = soma / len(numeros)
print(f"A média é: {media:.2f}")