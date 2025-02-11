'''. Escreve um programa que calcule a soma e o produto dos N primeiros números naturais'''

'''def soma_e_produto(n):
    soma = sum(range(1, n + 1))
    produto = 1
    for i in range(1, n + 1):
        produto *= i
    return soma, produto

n = int(input("Digite um número natural: "))
soma, produto = soma_e_produto(n)
print(f"A soma dos {n} primeiros números naturais é: {soma}")
print(f"O produto dos {n} primeiros números naturais é: {produto}")'''

y=0
z=1
x= input("Introduza um número para calcular a soma: ")
x= int(x)
for i in range(1,x+1):
    y += i
    z *= i
    
print(y)
print(z)
