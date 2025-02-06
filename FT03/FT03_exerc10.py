'''Implemente uma calculadora simples com as operações aritméticas básicas. O utilizador
deverá especificar a operação desejada (+,-,*,/) e, em seguida, inserir dois valores. 
Caso, o utilizador escolha divisão e insira como valor do denominar 0 mostra uma 
mensagem personalizada. Para os restantes casos, mostra no ecrã o resultado da 
operação desejada'''

operacao = input('Digite a operação desejada (+,-,*,/): ')
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
if operacao == '+':
    print('O resultado da soma é: ', valor1 + valor2)
elif operacao == '-':
    print('O resultado da subtração é: ', valor1 - valor2)
elif operacao == '*':
    print('O resultado da multiplicação é: ', valor1 * valor2)  
elif operacao == '/':
    if valor2 == 0:
        print('Não é possível dividir por zero')
    else:
        print('O resultado da divisão é: ', valor1 / valor2)
