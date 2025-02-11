'''Reescreve o programa anterior de forma a apresentar a tabuada de qualquer número
introduzido pelo utilizador'''  

'''x=int(input("Introduza um número:"))
for i in range(1, 11):
    multiplicacao = x * i
    print(f "{x} * {i} = {multiplicacao}")   # 5*i é o resultado da multiplicação de 5 por i
    
    valor = i'''
    
'''i=1
while i<=10:
    print(f"{i} x 5\t {i*5}")
    i=i+1'''
'''
numero = int(input("Digite o número para cálcular a tabuada\n---->\t3"))
for x in range (1,11):
    multiplicacao = numero * x
    print (f"{numero}*{x}={multiplicacao}\n")'''
    
x = input('introduza o valor a multiplicar')
for i in range(1, 11):
    print(int(x), 'x', i, '=', int(x) * i)