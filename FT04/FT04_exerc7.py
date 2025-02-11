'''Elabora um programa para calcular a soma dos N primeiros números naturais (1+2+3+...+N)
em que N é um número introduzido pelo utilizador (NOTA: este programa poderia ser feito 
utilizando a fórmula da progressão aritmética, S = (1+N) * N/2, mas faz de conta que não 
sabíamos a fórmula)'''

N = int(input('Introduza um número inteiro positivo: '))    # Número introduzido pelo utilizador  
soma = 0   
for i in range(1, N+1):   
    soma = soma + i
print(f'A soma dos {N} primeiros números naturais é {soma}')   # Imprime a soma dos N primeiros números naturais
# End of code
