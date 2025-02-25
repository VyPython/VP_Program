txt = "Ufcd  proGRAMação eM phTHON"
print(txt) # imprimir texto

txt=txt.strip() #imprimir texto sem espacamento inicial
print(txt)

print(txt[:13]) #imprimir texto ate a posicao 13

print(txt[-5:]) #imprimir últimos 5 caracteres

txt=txt.upper() #imprimir texto em maiusculas
print(txt)

#formatação de strings

nome = "Maria Silva"
print ("O/A {} gosta muito da {}".format(nome, txt))

print (f"O/A {nome} gosta muito da {txt}")