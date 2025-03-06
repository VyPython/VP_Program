import main_funcoes as mf # Importa o módulo main_funcoes.py

input_mes = int(input("Digite o número do mês: ")) # Solicita o número do mês ao usuário

res = mf.mes_extenso(input_mes) # Chama a função mes_extenso do módulo main_funcoes

print(f"O mês {input_mes} é {mf.mes_extenso(input_mes)}") # Imprime o mês por extenso
