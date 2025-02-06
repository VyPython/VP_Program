produto=input("Digite o nome do produto:\n---->\t")
preco=float(input("Digite o preço do produto:\n---->\t"))
match produto:
    case "smartphone":
        desconto = 0.1
    case "tablet":
        desconto = 0.15
    case "laptop":
        desconto = 0.2
    case _:
        desconto = 0.0
preco_final = preco - (preco * desconto)
print(f"O preço final do {produto} é {preco_final:.2f}€")

'''#Seleccionar o produto e aplicar o desconto
codigo_produto=int(input("introduza o código do produto(Smartphone=1, Tablet=2, laptop=3, Outro=4)"))
preco=float(input("introduza o preço do produto:"))
match codigo_produto:
    case (1):
        preco_final=preco*0.90
        print(f"O preço final é: {preco_final}")
    case (2):
        preco_final=preco*0.85
        print(f"O preço final é: {preco_final}")
    case (3):
        preco_final=preco*0.80
        print(f"O preço final é: {preco_final}")
    case (4):
        preco_final=preco
        print(f"O preço final é: {preco_final}")
    case _:
         print("código inválido")'''