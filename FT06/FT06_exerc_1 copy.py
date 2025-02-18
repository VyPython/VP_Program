cores=["amarelo", "azul", "branco", "preto", "verde"]

while True:
    print("\n a. Faz o print da lista toda")
    print("b. Faz o print do indíce 2 da lista")
    
    opcao = input("Escolha uma opção: ")
    
    match opcao:
        case "a.":
        print(f'Lista de cores: {cores}')
        
        case "b."
        print(f'A cor no índice 2 é: {cores[2]}')      

'''print(f'Lista de cores atualizada: {cores}')'''

'''cores[0] = "vermelho"
print(f'Lista de cores após alteração: {cores}')
'''print(f'Lista de cores: {cores}')'''
cores.append("amarelo")
print(f'Lista de cores: {cores}')
cores[2]= "roxo"
print(f'Lista de cores: {cores}')
cores.remove("amarelo")
print(f'Lista de cores: {cores}')
print(len(cores))