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

'''cores = ["amarelo","azul","branco","preto","verde"]
print(cores)
cores = ["amarelo","azul","branco","preto","verde"]
print(cores[2])
cores = ["amarelo","azul","branco","preto","verde"]
cores[0]="vermelho"
print(cores)
cores = ['vermelho', 'azul', 'branco', 'preto', 'verde']
cores.append("amarelo")
print(cores)
cores=['vermelho', 'azul', 'branco', 'preto', 'verde', 'amarelo']
cores.insert(2,"roxo")
print(cores)
cores=['vermelho', 'azul', 'roxo', 'branco', 'preto', 'verde', 'amarelo']
cores.pop()
print(cores)
cores=['vermelho', 'azul', 'roxo', 'branco', 'preto', 'verde']
tamanho=len(cores)
print(tamanho)

#Considera a lista:
#cores=["amarelo", "azul", "branco", "preto", "verde"]
#Cria um programa, em python, que:
#a: Faz o print de toda a lista:
#b Faz o print do indice 2 da lista
#c Altera o índice 0 da lista para "vermelho"
#d Faz o print de toda a lista
#e Acrescenta no final da lista a cor "amarelo"
#f Faz o print de toda a lista
#g Acrescenta no indice 2 a cor "roxo"
#h Faz o print de toda a lista
#i Apaga o último elemento da lista
#j Faz o print de toda a lista
#k Faz o print do tamanho da lista