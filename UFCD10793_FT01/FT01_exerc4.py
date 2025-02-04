r=input("insere o raio da circunferência:\n")  #valor a inserir pelo utilizador
r=int(r)                                       #conversão do valor inserido para inteiro
PI=3.14159                                     #valor de pi
V= round (4/3*PI*r**3,2)                                #cálculo do volume da esfera com base no valor do raio inserido, round para arredondar o resultado
print("O volume da esfera de raio,",r, "é",V)  #impressão do resultado
''' Escreve um programa que calcule o volume de uma esfera. O valor do raio deverá ser 
introduzido pelo utilizador (deverá ser criado o ficheiro ex04.py).
import math
pi = math.pi
raio = input ("Introduza um valor para o raio:\n---->\t")
raio = float(raio)
volume = round (4/3*pi*raio**3, 2)
output = f"o volume da esfera com raio {raio} é {volume}" #formated stringd
print (output)'''