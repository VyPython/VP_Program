cores=["amarelo", "azul", "branco", "preto", "verde"]
print(f'Lista de cores: {cores}')

'''print(f'Lista de cores atualizada: {cores}')'''
print(f'A cor no índice 2 é: {cores[2]}')
cores[0] = "vermelho"
print(f'Lista de cores após alteração: {cores}')
'''print(f'Lista de cores: {cores}')'''
cores.append("amarelo")
print(f'Lista de cores: {cores}')
cores[2]= "roxo"
print(f'Lista de cores: {cores}')
cores.remove("amarelo")
print(f'Lista de cores: {cores}')
print(len(cores))