# 7. Trabalhar com Diferentes Tipos de Ficheiros
# ficheiros json




import json
dados = {
    "nome": "João",
    "idade": 25, 
    "cidade": "Lisboa"
}
# Escrever para um ficheiro JSON
#
'''with open("c:\\dados.json", "w", encoding="utf-8") as ficheiro:
    json.dump(dados, ficheiro, ident=4) # ident=4 para indentar o JSON com 4 espaços de foma legível'''


# Escrever para um ficheiro JSON
ficheiro_caminho = "c:\\dados.json"  # Caminho do ficheiro

try:
    with open(ficheiro_caminho, "w", encoding="utf-8") as ficheiro:
        json.dump(dados, ficheiro, indent=4, ensure_ascii=False)  # Corrigido para json.dump()
    print(f"Dados guardados com sucesso em {ficheiro_caminho}")

except Exception as e:
    print(f"Erro ao guardar o ficheiro JSON: {e}")