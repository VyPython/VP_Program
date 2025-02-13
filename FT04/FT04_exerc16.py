'''Escreva um programa que peça ao utilizador números entre 0-10. Se o utilizador inserir um número
fora desse intervalo o programa deverá finalizar com uma mensagem personalizada'''
while True:
    try:
        num = int(input("Insira um número entre 0 e 10: "))
        if 0 <= num <= 10:
            print(f"Você inseriu o número {num}.")
        else:
            print("Número fora do intervalo permitido. Programa finalizado.")
            break
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")