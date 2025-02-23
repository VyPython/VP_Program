# 3 Métodos de Leitura de Ficheiros
# xi) read() - lê o ficheiro todo

with open("c:\\exemplo.txt", "r") as ficheiro:
    conteudo = ficheiro.read()
    print(conteudo)