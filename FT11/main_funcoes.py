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



'''Escreve uma função em Python que dada uma palavra retorne o número de
vogais nessa palavra.'''

def contar_vogais(palavra):
    # Define as vogais (minúsculas e maiúsculas para cobrir todos os casos)
    vogais = "aeiouAEIOUáéíóúÁÉÍÓÚâêîôûÂÊÎÔÛãẽĩõũÃẼĨÕŨàèìòùÀÈÌÒÙ"
    
    # Inicializa o contador de vogais
    contador = 0
    
    # Itera sobre cada caractere da palavra
    for letra in palavra:
        # Verifica se o caractere é uma vogal
        if letra in vogais:
            contador += 1
    
    # Retorna o total de vogais encontradas
    return contador

'''#Escreve uma função em Python que, dada uma lista de elementos, devolva
#essa mesma lista, mas sem elementos repetidos.'''

def remover_repetidos(lista):
    # Inicializa uma lista vazia para armazenar os elementos únicos
    lista_sem_repetidos = []
    
    # Itera sobre cada elemento da lista
    for elemento in lista:
        # Verifica se o elemento já está na lista de elementos únicos
        if elemento not in lista_sem_repetidos:
            # Se não estiver, adiciona o elemento à lista
            lista_sem_repetidos.append(elemento)
    
    # Retorna a lista sem elementos repetidos
    return lista_sem_repetidos


# Escreve uma função que, dado o número do mês retorne o mesmo, por extenso.
def mes_extenso(mes):
    # Dicionário com os meses do ano
    meses = {
        1: 'Janeiro',
        2: 'Fevereiro',
        3: 'Março',
        4: 'Abril',
        5: 'Maio',
        6: 'Junho',
        7: 'Julho',
        8: 'Agosto',
        9: 'Setembro',
        10: 'Outubro',
        11: 'Novembro',
        12: 'Dezembro'
    }
    
    # Retorna o mês por extenso
    return meses.get(mes, 'Mês inválido')