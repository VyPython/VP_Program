import main_funcoes as mf # Importa o módulo main_funcoes.py

a = input('Digite o valor do lado a: ')
b = input('Digite o valor do lado b: ')
c = input('Digite o valor do lado c: ')

# Converte os valores para float
a = float(a)
b = float(b)
c = float(c)

# Chama a função tipo_triangulo do módulo main_funcoes
print(mf.tipo_triangulo(a, b, c))

res = mf.tipo_triangulo(a, b, c)
print(res)