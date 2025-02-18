notas=[11.2, 15, 8.7, 17.2, 7.9 ]
print(len(notas))
notas.append(float(10.9))
print(len(notas))
print(f'mínimo: {min(notas)}')

def average(notas):
    return sum(notas) / len(notas)

print(f'média: {average(notas)}')

