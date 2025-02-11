'''Fazer um programa para ler quatro números inteiros e positivos, calcular e devolver a sua
média. usando o ciclo while'''

'''num1=int(input("Introduza o primeiro número:"))
num2=int(input("Introduza o segundo número:"))
num3=int(input("Introduza o terceiro número:"))
num4=int(input("Introduza o quarto número:"))

media=(num1+num2+num3+num4)/4
print("A média dos números é:",media)   '''

contador=1
soma=0 
media=0
while contador<=4:  #contador=1,2,3,4
    num=int(input("Introduza um número:"))
    contador+=1 #contador=2,3,4,5   
    soma+=num
    media+=num
media=media/4
print("A média dos números é:",media)  #media=soma/4
print("A soma dos números é:",soma)  #soma=num1+num2+num3+num4

