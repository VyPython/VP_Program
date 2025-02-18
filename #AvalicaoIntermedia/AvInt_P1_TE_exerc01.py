#1. Exemplo simples:

try:
    num = int(input("Digita um número: "))
    print("o dobro do número é:", num * 2)
except ValueError:
    print("Erro: Digita apenas números interios.")