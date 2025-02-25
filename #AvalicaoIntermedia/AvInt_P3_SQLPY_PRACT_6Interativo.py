# Parte III – SQLite em Python
# PRÁTICA
# 5. Eliminar dados


import sqlite3

def menu():
    print("\nMENU DE GESTÃO DE FUNCIONÁRIOS")
    print('1 - Adicionar Funcionário')
    print('2 - Listar Funcionário')
    print('3 - Atualizar Funcionário')
    print('4 - Eliminar Funcionário')   
    print('5 - Sair')
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
            nome = input('Nome: ')
            cargo = input('Cargo: ')
            salario = float(input('Salário: '))
            cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)", (nome, cargo, salario))
    elif opcao == '2':
            cursor.execute("SELECT * FROM funcionarios")
            for funcionario in cursor.fetchall():
                print(funcionario)
    elif opcao == '3':
            nome = input('Nome do funcionário: ')
            novo_salario = float(input('Novo salário: '))
            cursor.execute("UPDATE funcionarios SET salario = ? WHERE nome = ?", (novo_salario, nome))
    elif opcao == '4': 
            nome = input('Nome do funcionário a eliminar: ')
            cursor.execute("DELETE FROM funcionarios WHERE nome = ?", (nome,))
    elif opcao == '5': 
            conn.commit()
            conn.close()
            print('Até à próxima!')
    else:
        print('Opção inválida! Tente de novo.')

conn = sqlite3.connect('c:\\empresa.db')
cursor = conn.cursor() # Cria o Cursor para interagir com a BD
menu() # Chama a função menu