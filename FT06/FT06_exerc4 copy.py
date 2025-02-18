''' Considera a seguinte lista:
nums=[10, 2.5, 7, 11, 7.9, "Python", True,6, 5.8 , "Listas"]
Efetua um programa em python que:
a. Imprima a quantidade de inteiros, floats, strings e boleanos na lista;
b. Efetua a média de todos os valores inteiros na lista.
c. Crie e retorne uma nova lista só com os valores inteiros'''

nums = [10, 2.5, 7, 11, 7.9, "Python", True, 6, 5.8, "Listas"]

# a. Calcula e Imprime a quantidade de inteiros, floats, strings e boleanos na lista
int_count = sum(isinstance(x, int) and not isinstance(x,bool) for x in nums)
float_count = sum(isinstance(x, float) for x in nums)
str_count = sum(isinstance(x, str) for x in nums)
bool_count = sum(isinstance(x, bool) for x in nums)

print(f"Quantidade de inteiros: {int_count}")
print(f"Quantidade de floats: {float_count}")
print(f"Quantidade de strings: {str_count}")
print(f"Quantidade de booleanos: {bool_count}")

# b. Efetua a média de todos os valores inteiros na lista
int_values = [x for x in nums if isinstance(x, int) and not isinstance(x,bool)]
if int_values:
    int_mean = sum(int_values) / len(int_values)
    print(f"Média dos valores inteiros: {int_mean}")
else:
    print("Não há valores inteiros na lista para calcular a média.")

# c. Crie e retorne uma nova lista só com os valores inteiros
int_list = [x for x in nums if isinstance(x, int)and not isinstance(x,bool)]
print(f"Nova lista com valores inteiros: {int_list}")

'''
nums=[10, 2.5, 7, 11, 7.9, "Python", True,6, 5.8 , "Listas"]

#Alinea a)
c_int=0
c_float=0
c_str=0
c_bool=0
for x in nums:
    if type(x)==int:
        c_int=c_int+1
        continue
    if type(x)==float:
        c_float=c_float+1
        continue
    if type(x)==str:
        c_str=c_str+1
        continue
    if type(x)==bool:
        c_bool=c_bool+1
print("quantidade de inteiros na lista= ", c_int)
print("quantidade de floats na lista= ", c_float)
print("quantidade de Strings na lista= ", c_str)
print("quantidade de Booleanos na lista= ", c_bool)
#Alinea b)
soma=0
count=0
for x in nums:
    if type(x)==int:
        soma = soma +x
        count=count+1
media=soma/count
print("A media dos valores inteiros é: ", media)
#Alinea c)
nova_lista=[]
for x in nums:
    if type(x)==int:
        nova_lista.append(x)

print(nova_lista)

############################################
# Lista inicial
nums = [10, 2.5, 7, 11, 7.9, "Python", True, 6, 5.8, "Listas"]
# a. Conta a quantidade de cada tipo de dado
inteiros = len([x for x in nums if isinstance(x, int) and not isinstance(x, bool)])
floats = sum(1 for x in nums if isinstance(x, float))
strings = sum(1 for x in nums if isinstance(x, str))
booleanos = sum(1 for x in nums if isinstance(x, bool))
print(f"Inteiros: {inteiros}, Floats: {floats}, Strings: {strings}, Booleanos: {booleanos}")
# b. Calcula a média dos inteiros
valores_inteiros = [x for x in nums if isinstance(x, int) and not isinstance(x, bool)]
media = sum(valores_inteiros) / len(valores_inteiros)
print(media)
# c. Cria uma nova lista só com os inteiros
lista_inteiros = [x for x in nums if isinstance(x, int) and not isinstance(x, bool)]
print(lista_inteiros)

idades =[25, 15, 19, "test", 18.8, 37, 78, 46, 2, 67]
numeros = [x for x in idades if type(x) == int]
print(numeros)

####################################
# Lista inicial
nums = [10, 2.5, 7, 11, 7.9, "Python", True, 6, 5.8, "Listas"]
# a. Conta a quantidade de cada tipo de dado
inteiros = len([x for x in nums if type(x)== int])
floats = sum(1 for x in nums if type(x)== float)
strings = sum(1 for x in nums if type(x)== str)
booleanos = sum(1 for x in nums if type(x)== bool)
print(f"Inteiros: {inteiros}, Floats: {floats}, Strings: {strings}, Booleanos: {booleanos}")
# b. Calcula a média dos inteiros
valores_inteiros = [x for x in nums if type(x)== int]
media = sum(valores_inteiros) / len(valores_inteiros)
print(media)
# c. Cria uma nova lista só com os inteiros
lista_inteiros = [x for x in nums if type(x)== int]
print(lista_inteiros)