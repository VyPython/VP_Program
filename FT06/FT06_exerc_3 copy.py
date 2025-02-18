idades=[25,15,19,22,37,78,46,2,67]

idades.sort()
print(f"lista ordenada de idades: {idades}")
menores_de_idade = len([idade for idade in idades if idade < 18])
print(f"Quantidade de pessoas menores de idade: {menores_de_idade}")

idades.sort(reverse=True)
print(f"Lista de idades por ordem decrescente: {idades}")

idade_a_verificar = int(input("Digita a tua idade: "))

if idade_a_verificar in idades:
    print("A idade está na lista")
else:
    print("Na lista, não existe ninguém com a tua idade")
    
    '''idades = [25, 15, 19, 22, 37, 78, 46, 2, 67]
#Soma de idades menores de 18 anos
print("Pessoas menores de idade: " , sum(1 for idade in idades if idade < 18))
#Ordenar idades de forma decrescente
idades.sort(reverse=True)
print(idades)
#Procurar uma idade na lista
idade = int(input("Insira a idade que deseja procurar: "))
if idade in idades:
    print(f"A idade {idade} está na lista.")
else:
    print(f"Não existe ninguém com {idade} na lista.")