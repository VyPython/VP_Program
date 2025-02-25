txt="""Python é uma linguagem de programação
de alto nível, interpretada de script, imperativa, orientada a objetos,
funcional, de tipagem dinâmica e forte."""

txt = txt.upper()
print(txt)

# b. Verifica se uma palavra fornecida pelo usuário está no texto
palavra = input("\nDigite uma palavra para buscar no texto: ")
if palavra.lower() in txt.lower():
    print(f"A palavra '{palavra}' está no texto.")
else:
    print(f"A palavra '{palavra}' não foi encontrada no texto.")

# c. Conta o número de vezes que a letra 'O' ocorre no texto (case insensitive)
contagem_o = txt.lower().count('o')
print(f"\nA letra 'O' ocorre {contagem_o} vezes no texto.")

# d. Substitui todas as ocorrências da letra 'P' por '_'
txt_modificado = txt.replace('P', '_').replace('p', '_')
print("\nTexto após substituição da letra 'P' por '_':")
print(txt_modificado)