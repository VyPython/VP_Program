# 4 Métodos de Escrita de Ficheiros
# xv. append() - Acrescentar o conteúdo ao ficheiro, adiciona no final do ficheiro sem sobrescrever

with open("c:\\nexemplo.txt", "a") as ficheiro:
    ficheiro.write("\nEsta é a nova linha adicionada.")
    