# 2) Reproduz o seguinte código.
'''Peça dois números ao utilizador e trate a divisão por zero.'''

try:
    a = int(input("Digite numerador: "))
    b = int(input("Digite o denominador: "))
    
    print("Resultado da divisão:", a / b)
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except ValueError:
    print("Erro: Apenas números inteiros são permitidos")
