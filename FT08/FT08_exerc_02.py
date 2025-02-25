'''2 -  Escreva um programa que, dada uma String representando um texto, 
imprima o número depalavras existentes. Observação: você deve 
remover os sinais de pontuação (“.”, “,”, “:”, “;”, “!” e “?”) antes 
de realizar a contagem das palavras.'''

import string

# Lê a string do usuário
texto = input("Digite um texto: ")

# Remove sinais de pontuação
for caractere in ".,:;!?":
    texto = texto.replace(caractere, "")
    
print(texto)

# Divide o texto em palavras
palavras = texto.split()

# Exibe a contagem de palavras
print(f"Número de palavras: {len(palavras)}")



#solução alternativa
texto = input("Digite um texto: ")  # Lê o texto
for c in string.punctuation:  # Remove pontuação
    texto = texto.replace(c, "") 
palavras = texto.split()  # Divide o texto em palavras
print(texto)  # Exibe o texto sem pontuação
print(f"O texto tem {len(palavras)} palavras.")  # Exibe o resultado