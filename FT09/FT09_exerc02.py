# criar dicionário
viatura = {
    "tipo": "Autocarro",
    "marca": "Scania",
    "ano": 2021
}
#vários prints apenas para verificação 
print (viatura)

# acrescentar uma nova chave e respetivo
viatura.update({"lugares": 65})

print (viatura)

# eliminar a chave ano
viatura.pop("ano")

print(viatura)

# atualizar o número de lugares para 100
viatura.update({"lugares":100})
print(viatura)

'''
print("a - Cria um dicionário e efetua o respetivo print")
print("b - Acrescentes dois novos elementos ao dicionário")
print("c - Removes um dos elementos da lista")
print("d - Efetues uma operação, à escolha, sobre os dados no dicionário")
disciplinas = {"matematica":15, "ingles":16, "historia":16}
while True:
    user = input("Escolha uma opção:")
    match user:
        case "a":
            print(disciplinas)
        case "b":
            disciplinas.update({"portugues":15})
            disciplinas.update({"geografia":15})
            print(disciplinas)
        case "c":
            del disciplinas["matematica"]
            print(disciplinas)
        case "d":
            disciplinas.popitem()
            print("Removi o último conjunto chave:valor")
            print(disciplinas)
        case _:
            print("Escolha uma opção entre a e d")