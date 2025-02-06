'''Escreve um programa que receba dois números reais e indique qual o maior dos dois 
números. Considera a possibilidade de o utilizador indicar dois números iguais'''

# Solicitar dois números reais ao utilizador   
numero1 = float(input('Digite o primeiro número real: '))
numero2 = float(input('Digite o segundo número real: '))
if numero1 > numero2:
    print(f'O número {numero1} é maior que o número {numero2}.')
elif numero1 == numero2:
    print(f'O número {numero1} é igual ao número {numero2}.',)
else:
    print(f'O número {numero2} é maior que o número {numero1}.')
    
#,round(numero1,numero2,2