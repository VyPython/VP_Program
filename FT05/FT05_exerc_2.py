'''Crie um programa para controlar listas, com as seguintes funções:
• Adicionar elemento no início;
• Adicionar elemento no fim;
• Remover elemento;
• Tamanho da lista;
• Imprimir elementos da lista;
• Esvaziar lista'''


def adicionar_inicio(lista, elemento):
    lista.insert(0, elemento)
    
def adicionar_fim(lista, elemento):
    lista.append(elemento)