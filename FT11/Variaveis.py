mensagem = "Variável global"    # Variável global

def imprime_mensagem():
    print(mensagem)    # Acessando a variável global

imprime_mensagem()

a = 1
def imprime(): 
    a = 5
    print (a) 
imprime() 
# 5
print (a) 


a = 1
def incrementa():
    global a
    a = a + 1
    print (a) 

incrementa()
# UnboundLocalError: local variable 'a' referenced before assignment

a  = 1
def incrementa(): 
    a = 12
    a = a + 1
    print (a) 
incrementa() 
# 13
print (a) 
# 1

def imprime_mensagem(mensagem):
    print(mensagem)
bomdia = "Bom dia" 
imprime_mensagem(bomdia) 

#total é utilizado como variável local
def soma(a, b):
    total = a + b
    print("Total soma =", total)
#programa principal
total=10
soma(5, 3)
print("Total programa principal =", total)

#total é utilizado como variável global
def soma(a, b):
    global total #define total como variável global
    total = a + b
    print("Total soma =", total)
#programa principal
total=10   
soma(5, 3)
print("Total programa principal =", total)