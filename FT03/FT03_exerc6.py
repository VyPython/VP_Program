'''Escreve um programa que receba três números reais e indique qual o maior dos três 
números'''

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))
if num1 > num2 and num1 > num3:
    print('O maior número é o primeiro número: ', num1)
elif num2 > num1 and num2 > num3:
    print('O maior número é o segundo número: ', num2)
else:
    print('O maior número é o terceiro número: ', num3)

# Solicita três números reais ao utilizador
'''numero1 = float(input("Por favor, insira o primeiro número real: "))
numero2 = float(input("Por favor, insira o segundo número real: "))
numero3 = float(input("Por favor, insira o terceiro número real: "))
#1 Encontra o maior número entre os três
maior = numero1   #maior é definido como numero1. ponto de partida para fazer a comparação.
#2 o código verifica se numero2 ou numero3 são maiores que o valor atual de maior. Se for o caso, maior é atualizado para o novo valor mais alto. 
if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero3
# Imprime o maior número
print(f"O maior número é {maior}.")'''

'''max = max(num1, num2, num3)
print(f'O maior número é: {max}')'''