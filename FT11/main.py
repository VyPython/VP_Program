def main():
    print("Execução da função main")

main()

# O que acontece se executarmos o código acima?
#
# A) O código executa normalmente e imprime "Execução da função main".


def função2():
    print("Execução da função 2")

def função1():
    print("Execução da função 1")

def main():
    função1() 
    função2()


main()
# Execução da função 1 
# Execução da função 2