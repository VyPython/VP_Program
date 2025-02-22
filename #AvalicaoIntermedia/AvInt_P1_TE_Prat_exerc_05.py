# 5)
'''Elabora uma script em python que peça ao utilizador um número e some todos
os números de 1 até esse mesmo número. 
Deves utilizar o tratamento de erros.'''


while True:
    try:
        numero = int(input("Digite um número inteiro positivo: "))
        if numero < 1: #garante que o número é maior ou igual a 1
            print("Por favor, insira um número maior ou igual a 1.")
            continue  # Repete o loop se o número for inválido

        soma = sum(range(1, numero + 1)) #soma de 1 até ao número digitado com a opção range
        print(f"A soma dos números de 1 até {numero} é {soma}.")
        break  # Sai do loop quando a entrada for válida
    except ValueError:
        print("Erro: Por favor, insira um número inteiro válido.") #tratamento de erros de digitos não inteiros