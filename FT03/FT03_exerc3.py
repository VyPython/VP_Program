'''Escreve um programa que solicite um número inteiro ao utilizador e verifique se o 
mesmo é par ou ímpar. A mensagem no ecrã deverá ter o seguinte formato;
"O número [número] é [par/ímpar]"'''

# Solicitar um número inteiro ao utilizador
numero = int(input('Digite um número inteiro: '))
if numero % 2 == 0:
    print(f'O número {numero} é par.')
else:
    print(f'O número {numero} é ímpar.')

