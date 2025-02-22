import sys

# 5)
'''Elabora uma script em python que peça ao utilizador um número e some todos
os números de 1 até esse mesmo número. 
Deves utilizar o tratamento de erros.'''
'''def soma_numeros(n):
    return sum(range(1, n + 1))

try:
    numero = int(input ("Digite um número: ")) # numero a digitar pelo user
    #print("Número inserido é: ", numero)
    for x in range(, numero)
    soma = x + numero if numero  
    
except ValueError:
    print("Erro: O número inserido não é válido")'''
    
'''def obter_numero():
    while True:
        try:
            numero = int(input("Por favor, insira um número inteiro positivo: "))
            if numero <= 0:
                print("O número deve ser maior que zero. Tente novamente.")
            else:
                return numero
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar um número inteiro.")

def calcular_soma(numero):
    return sum(range(1, numero + 1))

def main():
    numero = obter_numero()
    soma = calcular_soma(numero)
    print(f"A soma de todos os números de 1 até {numero} é {soma}.")

if __name__ == "__main__":
    main()'''


'''Função obter_numero: Solicita ao utilizador que insira um número. Utiliza um loop while para continuar pedindo a entrada até que o utilizador forneça um número inteiro positivo. Se o utilizador inserir um valor que não seja um número inteiro, é gerada uma exceção ValueError, e uma mensagem de erro é exibida.

Função calcular_soma: Recebe um número inteiro e retorna a soma de todos os números de 1 até esse número, utilizando a função sum e a função range para gerar a sequência de números.

Função main: Coordena a execução do script. Chama a função obter_numero para obter um número válido do utilizador, em seguida, chama calcular_soma para calcular a soma e, por fim, exibe o resultado.

Bloco if __name__ == "__main__": Garante que a função main seja executada apenas quando o script é executado diretamente, e não quando é importado como um módulo em outro script.0'''


while True:
    try:
        numero = int(input("Digite um número inteiro positivo: "))
        if numero < 1:
            print("Por favor, insira um número maior ou igual a 1.")
            continue  # Repete o loop se o número for inválido

        soma = sum(range(1, numero + 1))
        print(f"A soma dos números de 1 até {numero} é {soma}.")
        break  # Sai do loop após uma entrada válida
    except ValueError:
        print("Erro: Por favor, insira um número inteiro válido.")