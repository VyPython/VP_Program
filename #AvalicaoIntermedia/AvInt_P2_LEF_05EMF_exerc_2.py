# 5 Eficiência na Manipulação de Ficheiros
# ii. Uso de mmap para leitura eficiente

'''mmap permite mapear ficheiros diretamente para a memória (altamente eficiente
para ficheiros grandes.'''

import mmap

with open("c:\\grande_ficheiro.txt", "r+b") as f:
    mm = mmap.mmap(f.fileno(), 0)
    print(mm.readline())
    mm.close()
    