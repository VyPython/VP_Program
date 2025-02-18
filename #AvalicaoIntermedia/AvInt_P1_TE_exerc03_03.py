
# iii. Exemplo de FileNotFoundError:

try:
    with open("arquivo_inexistente.txt", "r") as file:
        conteudo = file.read()
except FileNotFoundError:

    print ("Erro: o ficheiro não foi encontrado.")
