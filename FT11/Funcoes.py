def imprime_mensagem():
    print("Olá, mundo da programação!")

imprime_mensagem()

#imprime_msg()
#NameError: name 'imprime_msg' is not defined
# O erro ocorre porque a função imprime_msg() não foi definida no arquivo Funcoes.py,
# mas sim no arquivo Datas.py. Para corrigir o erro, é necessário importar 
# a função imprime_msg() do arquivo Datas.py.

def imprime_msg():
    print("Minha primeira função em Python!")

imprime_msg()

def imprime_mensagem():
    print("Olá, mundo da programação! Minha primeira função em Python!")

imprime_mensagem()

def minha_funcao():
    print("A função foi chamada!")
#inicio do programa
print("Inicio do programa")
minha_funcao() #chamada da função
print("Fim do programa")

def add(num1, num2):
    print("num1:", num1)
    print("num2:", num2)
    addition = num1 + num2
    return addition

res = add(10, 20)
print("Resultado da soma:", res)

def imprime_msgem():
    msgem = "Variável local"
    print(msgem)

imprime_msgem()
#Variável local
#print(msgem)
#NameError: name 'mensagem' is not defined
# O erro ocorre porque a variável mensagem foi definida dentro da função imprime_mensagem(),
# ou seja, é uma variável local. Portanto, ela não é acessível fora da função.
# Para corrigir o erro, é necessário definir a variável mensagem fora da função.

def curso_func(name, course_name):
    print("olá", name, "bem vindo")
    print("nome do curso", course_name)
    
curso_func('Transformer', 'Python')

# function
def calculator(a, b): 
    add = a + b
    # return the addition
    return add
# call function
# take return value in variable
res = calculator(20, 5) 
print("Addition :", res)


def par_impar(n):
    if n % 2 == 0:
        print('Número Par')
    else:
        print('Número Impar') 

par_impar(19) #chamada pelo nome

def minha_funcao(*kids):
    #recebe e trata como uma lista
    print("filho mais novo: " + kids[2]) #acessa o terceiro elemento da lista

minha_funcao("Emil", "Tobias", "Linus") #chamada da função

def minha_funcao1(child3, child2, child1):
    #recebe e trata como uma lista
    print("filho mais velho: " + child1) #acessa o terceiro elemento da lista

minha_funcao1(child1="Emil", child2="Tobias", child3="Linus") #chamada da função

def minha_funcao2(**kid):
    print("Seu último nome é " + kid["lname"])

minha_funcao2(fname = "Tobias", lname = "Refsnes")

def minha_funcao3(pais = "Brasil"):
    print("Eu sou de " + pais)

minha_funcao3("Suécia")
minha_funcao3()

def minha_funcao4(food):
    for x in food:
        print(x)    

frutas = ["maçã", "banana", "uva"]
minha_funcao4(frutas)

def minha_funcao5(x):
    return 5 * x

print(minha_funcao5(3))
print(minha_funcao5(5))
print(minha_funcao5(9))

def minha_funcao6():
    idade=35
    nome="João"
    return idade, nome

var_1, var_2 = minha_funcao6()
print(var_1, var_2)