notas=[11.2, 15, 8.7, 17.2, 7.9 ]
print(len(notas))
notas.append(float(10.9))
print(len(notas))
print(f'mínimo: {min(notas)}')

def average(notas):
    return sum(notas) / len(notas)

print(f'média: {average(notas)}')

# from statistics import mean
# from numpy import average
'''from statistics import mean
from numpy import average
notas=[11.2, 15, 8.7, 17.2, 7.9 ]
notas.append(10.9)
print(f"A lista inclui os seguintes elementos{notas}")
print(f"O número de elementos na lista é é {len(notas)}")
print(f"A nota mínima é {min(notas)}")
print(f"A média das notas é {mean(notas)}")
print(f"A média das notas é {average(notas)}")'''

'''notas=[11.2, 15, 8.7, 17.2, 7.9 ]
Cria um programa, em python, que:
a. Acrescenta o valor 10.9 no final da lista e faz o print de toda a lista
b. Faz o print do tamanho da lista
c. Faz o print do valor mínimo da lista
d. Faz a média dos valores da lista
notas=[11.2, 15, 8.7, 17.2, 7.9 ]
notas.insert(5,10.9)
print(notas)
print(len(notas))
print(min(notas))
print (sum(notas) / 6)'''