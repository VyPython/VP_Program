'''O Índice de Massa Corporal (IMC) é utilizado para medir o peso ideal de uma pessoa. 
Escreve um programa que peça o nome, a idade, o peso e a altura do utilizado e que, 
de seguida, calcule e mostre o resultado do seu IMC e classifique esse resultado de 
acordo com as seguintes condições:
• IMC<17 - Muito abaixo do peso ideal
• 17<=IMC<18,5 - Abaixo do peso
• 18,5<=IMC<25 - Peso normal
• 25<=IMC<30 - Acima do peso
• 30<=IMC<35 - Obesidade I
• 35<=IMC<40 - Obesidade II (severa)
• IMC>=40 - Obesidade III (mórbida)'''


nome = input('Digita o teu nome: ')
idade = int(input('Digita a tua idade: '))
peso = float(input('Digita o teu peso: '))
altura = float(input('Digita a tua altura: '))
imc = round(peso / (altura ** 2),2)
if imc < 17:
    print(nome, ': o teu IMC indica que estás Muito Abaixo do peso ideal')
elif 17 <= imc < 18.5:
    print(nome, ': o teu IMC indica que estás Abaixo do peso ideal')
elif 18.5 <= imc < 25:
    print(nome, ': o teu IMC indica que estás com Peso normal')
elif 25 <= imc < 30:
    print(nome, ': o teu IMC indica que estás Acima do peso')
elif 30 <= imc < 35:
    print(nome, ': o teu IMC indica que estás em Obesidade I')
elif 35 <= imc < 40:
    print(nome, ': o teu IMC indica que estás em Obesidade II (severa)')  
else: print(nome, ': o teu IMC indica que estás em Obesidade III (mórbida)')
