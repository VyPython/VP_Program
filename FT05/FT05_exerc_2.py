'''Crie um programa para controlar listas, com as seguintes funções:
• Adicionar elemento no início;
• Adicionar elemento no fim;
• Remover elemento;
• Tamanho da lista;
• Imprimir elementos da lista;
• Esvaziar lista


or x in nums:

    if type(x)==int:

        c_int=c_int+1

        continue

    if type(x)==float:

        c_float=c_float+1

        continue

    if type(x)==str:

        c_str=c_str+1

        continue

    if type(x)==bool:

        c_bool=c_bool+1'''

'''lista=[]
def adicionar_inicio(lista, elemento):
    lista.insert(0, elemento)
    
def adicionar_fim(lista, elemento):
    lista.append(elemento)

lista.remove(0)

lista.len()'''

lista=[1,2,3,4,5,6,7,8,9,10,11,12]

lista.insert(0,8)

print(lista) #Adicionar elemento no início;

lista.append(8)

print(lista) #Adicionar elemento no fim;

lista.remove(8)

print(lista) #Remover elemento;

print(len(lista)) #Tamanho da lista;

print(sum(lista)) #Imprimir elementos da lista;

lista.clear()

print(lista) #Esvaziar lista