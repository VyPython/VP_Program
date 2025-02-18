# i. Exemplo de ValueError:

try:
    idade=int(input("Digite a sua idade: "))
except ValueError:
    print ("Erro: Digite um número inteiro válido.")
