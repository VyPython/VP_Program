#"o valor do raio é 4"
'''isto é para mudar de linh
e continiar a escrever'''
raio = 4
print("o valor do raio é" , raio)

#COSNTANTE DEVEM SER ESCRITAS EM LETRAS MAIUSCULAS

#variaveis devem ser escritas em letras minusculas
#separar palavras com underline
#não usar acentos
#não usar caracteres especiais
# variaveis são case sensitive
# variaveis não podem começar com numeros

# int - para numeros inteiros
# str - para strings
# bool - para booleanos True/False
# tuple - semelhante a uma list mas imutavel
# list - para agrupar elementos
# float - para numeros decimais
# dic - para agrupar elementos que serão recuperados por uma chave
# set - para agrupar elementos sem repetição - operaçoces matematicas

#operadores aritmeticos
# + - * / % ** //
#// divisao interia entre operandos - numero inteiro mais proximo
#% divisao inteira entre operandos - resto da divisao
#** exponenciação - 

#==   igual a
#!=   diferente de
#>    maior que
#<    menor que
#>=   maior ou igual a
#<=   menor ou igual a

#operadores logicos
#and - e
#or - ou
#not - não

#operadores de atribuição
# =  atribuição
# += adição
# -= subtração
# *= multiplicação
# /= divisão
# %= resto da divisão

#operadores de identidade
# is - retorna verdadeiro se as variaveis forem o mesmo objeto
# is not - retorna verdadeiro se as variaveis não forem o mesmo objeto

#operadores de associação
# in - retorna verdadeiro se um valor especificado for encontrado numa sequencia
# not in - retorna verdadeiro se um valor especificado não for encontrado numa sequencia

#prioridade de operadores
# () - parenteses
# ** not
# * / // %, and
# + - or
# + -
# == != > < >= <=

x = 5
y = "Olá Mundo!"
z = 3.14
lista = [1,2,3,4,5]
tupla = (1,2,3,4,5)
dicionario = {"nome":"João", "idade":25}
print(x)
print(y)  
x= str(3) #texto
y= int(3) #inteiro
z= float(3) #valor deciaml -  real 
print(x)
print(y)
print(z)
n = "Vitor"
s = 'Pereira'
print(n + " " + s)
print(n + " " + str(3))
print (lista)
a, b, c, = 'Joana', 'Andre', 'Ines' 
print (a, b, c)

x = 10
dobro = x * 2
print(dobro)
print ('o dobro de', x, 'é', dobro)
t = '10'
aux = t+t
print(aux)

print (type(x))


#input("Pressione ENTER para sair")

quatro = 4
dois = 2
numero = 10
numero +=7
print (numero)
#import keyword
#print (keyword.kwlist)
import math
print (math.sqrt(25))
