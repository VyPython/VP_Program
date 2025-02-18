idades=[25,15,19,22,37,78,46,2,67]

idades.sort()
menores_de_idade = len([idade for idade in idades if idade < 18])
print(f"Quantidade de pessoas menores de idade: {menores_de_idade}")

idades.sort(reverse=True)
print(f"Lista de idades por ordem decrescente: {idades}")

idade_a_verificar = int(input("Digita a tua idade: "))

if idade_a_verificar in idades:
    print("A idade está na lista")
else:
    print("Na lista, não existe ninguém com a tua idade")