import main_funcoes as mf # Importa o módulo main_funcoes.py

#lista = [3, 4, 5, 6, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6] # Define a lista

lista = input("Digite a lista: ").split() # Solicita a lista ao usuário
lista = [int(i) for i in lista] # Converte os elementos da lista para inteiros

res = mf.remover_repetidos(lista) # Chama a função remover_repetidos do módulo main_funcoes
res.sort() # Ordena a lista sem elementos repetidos
print(res) # Imprime o resultado

