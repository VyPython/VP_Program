status = 404
match status:
    case 400:
        print("Bad Request")
    case 404:  
        print("Not Found")
    case 418:
        print("Internal Server Error")
    case _:
        print("Erro desconhecido")
# match status:
nota=int(input('Digite a nota: '))
match nota:
    case 0:
        print("Muito insuficiente")
    case 1,2:
        print("Insuficiente")
    case 3: 
        print("Suficiente")
    case 4:
        print("Bom")
    case 5:
        print("Muito Bom")
    case _:
        print("Nota inválida")