''' a=input("digite o valor de a: ")

if int(a) > 20:
    print(a/2)
else:
    print ("o valor de a é menor que 20")'''
    
    '''Escreve um programa que solicite um número inteiro ao utilizador e caso o mesmo seja maior que 20, 
devolva o resultado da sua divisão por 2.'''

num = int(input("Digite um número: "))
if num > 20:
        print(f"O resultado da divisão de {num} por 2 é {num / 2}")
else:
        print("O número digitado é menor ou igual a 20")

numero1 = float(input("Número:"))
numero2 = float(input("Número:"))
if numero1 == numero2:
    print("Os números são iguais")
else:
    print("Os números são diferentes")
