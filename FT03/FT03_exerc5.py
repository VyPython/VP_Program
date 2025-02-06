''' Escreva um programa que verifique se um determinado número introduzido pelo 
utilizador é nulo, positivo ou negativo'''
# Solicitar um número inteiro ao utilizador
numero = int(input('Digite um número inteiro: '))
if numero == 0:
    print(f'O número {numero} é nulo.')
elif numero > 0:
    print(f'O número {numero} é positivo.')
else:
    print(f'O número {numero} é negativo.')
    

''' numero = float(input("Introduza um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é nulo.")'''