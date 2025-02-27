'''# Escreve uma função em Python que, dados a medida do comprimento dos três
lados de um triângulo diga se o mesmo é equilátero, isósceles ou escaleno.'''

# Função que verifica o tipo de triângulo
def tipo_triangulo(a, b, c):
    if a == b and b == c:
        return 'Equilátero'
    elif a == b or a == c or b == c:
        return 'Isósceles'
    else:
        return 'Escaleno'  

''' Escreve uma função em Python que, dados a medida do comprimento do lado de
um quadrado imprima os valores do seu perímero e da sua área (area=lado x 
lado; perimetro = 4 x lado).'''

# Função que calcula o perímetro e a área de um quadrado
def perimetro_area_quadrado(lado):
    perimetro = 4 * lado
    area = lado * lado
    return f'Perímetro: {perimetro} Área: {area}'


''' Escreve uma função em Python que dada uma lista de números imprime a soma
dos valores dessa lista, o número de elementos da lista e a media desses 
valores.'''
# Função que calcula a soma, a quantidade de elementos e a média de uma lista
def soma_media(lista):
    soma = sum(lista)
    quantidade = len(lista)
    media = soma / quantidade
    return f'Soma: {soma} Quantidade: {quantidade} Média: {media}'
