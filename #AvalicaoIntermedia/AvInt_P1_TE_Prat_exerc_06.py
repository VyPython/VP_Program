# 6)
'''Elabora uma script em python que peça ao utilizador dois números e devolva
a divisão do primeiro número introduzido pelo seguinte. Trate erros como
divisão por zero e valores inválidos'''


while True:
    try:
        num1 = float(input("Digite o primeiro número: ")) #inserção dos números e converte para décimal
        num2 = float(input("Digite o segundo número: "))

        if num2 == 0: # validação do segundo número porque a divisão por zero não é permitida
            print("Erro: A divisão por zero não é permitida. Tente novamente.")
            continue  # Repete o loop para pedir novos valores

        resultado = num1 / num2
        print(f"O resultado da divisão de {num1} por {num2} é {resultado:.2f}") #apresenta dados com 2 casas décimais
        break  # Sai do loop após uma entrada válida

    except ValueError:
        print("Erro: Por favor, insira apenas números válidos.") #tratamento das exceções de números inválidos