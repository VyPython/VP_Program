'''Escreve um programa que solicite ao utilizador um número e escreva em simultâneo a sequência
crescente e decrescente entre 1 e esse número'''

def sequencias(numero):
    crescente = list(range(1, numero + 1))
    decrescente = list(range(numero, 0, -1))
    for c, d in zip(crescente, decrescente):
        print(f"{c} - {d}")

numero = int(input("Digite um número: "))
sequencias(numero)