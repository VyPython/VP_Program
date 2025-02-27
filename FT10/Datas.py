Datas="12ago2021,02set2020,20jan2022,11out2019,09mar2020,10dez2022"
list_datas = Datas.split(",")
print("\n Lista completa de datas:")
print (" - ", list_datas)

print("\n Datas para o ano de 2020:")
for x in list_datas:
    if "2020" in x:
        print(" ", x)

dias = sorted([int(x[:2]) for x in list_datas])
print("\n Dias ordenados de forma crescente:", dias)


txt = """" Python é uma linguagem de programação 
de alto nível, interpretada, de script, imperativa, orientada a objetos, 
funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991. 
Atualmente possui um modelo de desenvolvimento comunitário, aberto e 
gerenciado pela organização sem fins lucrativos Python Software Foundation. 
Apresenta uma sintaxe elegante, tipagem dinâmica e uma gestão de memória automática, 
sendo por isso uma das linguagens mais utilizadas para o ensino de programação e 
para a prototipagem de software."""

txt = txt.upper()
print(txt)

palav = input("Digite a palavra que deseja contar: ")
cont = txt.count(palav.upper())
print("A palavra", palav, "aparece", cont, "vezes no texto.")

letra = input("Digite a letra que deseja contar: ")
contl = txt.count(letra.upper())
print("A letra", letra, "aparece", contl, "vezes no texto.")    # Conta a quantidade de vezes que a letra aparece no texto

# substitui a palavra Python por Java
txt = txt.replace("PYTHON", "JAVA") 
print(txt)
txt = txt.replace("P", "_")
print(txt)