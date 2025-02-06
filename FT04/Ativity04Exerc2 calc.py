num1=int(input("Digita o primeiro número:\n---->\t"))
num2=int(input("Digita o segundo número:\n---->\t"))

operacao = input("Seleciona a operação a realizar (+, -, *, /):\n---->\t")

match operacao:
    case "+":
        resultado = num1 + num2
    case "-":
        resultado = num1 - num2
    case "*":
        resultado = num1 * num2
    case "/":
        if num2 == 0:
            resultado = "Divisão por zero não é permitida"
        else:
            resultado = num1 // num2
    case _:
        resultado = "Operação inválida"

print("Resultado:", resultado)
