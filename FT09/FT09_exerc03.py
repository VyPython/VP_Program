import copy

# a. Instanciar o dicionário
Computadores_1 = {
    "Marca": "Asus",
    "Ecra": "14Pol",
    "RAM": [4, 8, 12]
}

# b. Acrescentar chave "Disco"
Computadores_1["Disco"] = ["128G", "256G"]

# c. Verificar valor de RAM, solicitar ao utilizador para digitar um valor com verificação 
while True:
    try:
        ram_input = int(input("Introduza um valor de RAM para verificar: "))
        if ram_input in Computadores_1["RAM"]:
                    print(f"O valor de RAM {ram_input}GB está presente na lista.")
        else:
                    print(f"O valor de RAM {ram_input}GB não está presente na lista.")
        break
    except ValueError:
            print ("Erro: Digite um número inteiro válido.")


# d. Acrescentar 16GB de RAM

if 16 not in Computadores_1["RAM"]:
        Computadores_1["RAM"].append(16)


# e. Copiar dicionário usando deepcopy
Computadores_2 = copy.deepcopy(Computadores_1)

# f. Modificar Computadores_2
Computadores_2["Marca"] = "Lenovo"
Computadores_2["RAM"] = [4, 8]
print("Computadores_2:", Computadores_2)

# g. Criar nova cópia profunda e modificar
Computadores_3 = copy.deepcopy(Computadores_1)
Computadores_3["Marca"] = "HP"
Computadores_3["Disco"] = ["256G"]
print("Computadores_3:", Computadores_3)

# h. Criar lista de dicionários
lista_computadores = [Computadores_1, Computadores_2, Computadores_3]

# i. Imprimir marcas com "128G" de Disco
print("Marcas com '128G' de Disco:")
for computador in lista_computadores:
    if "Disco" in computador and "128G" in computador["Disco"]:
        print(computador["Marca"])

# j. Imprimir marcas com 8GB e 12GB de RAM
print("Marcas com 8GB e 12GB de RAM:")
for computador in lista_computadores:
    if all(ram in computador["RAM"] for ram in [8, 12]):
        print(computador["Marca"])