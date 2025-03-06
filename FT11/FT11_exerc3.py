import main_funcoes as mf # Importa o módulo main_funcoes.py


print(mf.soma_media([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) 
# Chama a função soma_media do módulo main_funcoes


'''ex3: 
def numeros(dados):
    import statistics
    user = list(map(int, dados.split()))
    soma = sum(user)
    conta_numeros = len(user)
    media = statistics.mean(user)
    return soma, conta_numeros, media
import minhasfunc
dados = input("Escreve uma quantidade de números, divididos por espaço: ")
soma, conta_numeros, media = minhasfunc.numeros(dados)
print(f"A soma de todos os números é {soma}; a lista tem {conta_numeros} números e a média é {media}")


import minhasfunc
dados = input("Escreve uma quantidade de números, divididos por espaço: ")
soma, conta_numeros, media = minhasfunc.numeros(dados)
print(f"A soma de todos os números é {soma}; a lista tem {conta_numeros} números e a média é {media}")


def areaeperimetoquadrado(lado):
    area = lado*lado
    perimetro = 4*lado
    return area, perimetro
from  minhasfunc import areaeperimetoquadrado
l1 = float(input("Introduza o valor do lado"))
    
a1, p1 = areaeperimetoquadrado(l1)
print("area = ", a1, " perimetro =",p1)
def dadoslista(valores):
    soma = sum(valores)
    compr = len(valores)
    media = sum(valores)/len(valores)
    return soma, compr, media
    
    
    import minhasfunc

valores = [8,9,10]

res = minhasfunc.dadoslista(valores)
print("Sum: ", res[0])
print("Number of items: ", res[1])
print("Average: ", res[2])


    '''