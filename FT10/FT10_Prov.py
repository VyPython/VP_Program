prov="""o pior cego é aquele que não quer ver."""

prov=prov.capitalize() #imprimir texto com a primeira letra em maiuscula
print(prov)

palavras=prov.split(" ") #imprimir texto separado por palavras
print(palavras)

count=0
for x in palavras:
    if x=="que":
        count+=1
print(count)

prov=prov.replace("quer ver","compra um cão") #imprimir texto com a palavra substituida
print(prov)