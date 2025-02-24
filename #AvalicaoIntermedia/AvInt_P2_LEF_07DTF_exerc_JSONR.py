# 7. Trabalhar com Diferentes Tipos de Ficheiros
# ficheiros json




import json

# ler um ficheiro JSON

ficheiro_caminho = "c:\\dados.json"  # Caminho do ficheiro

with open(ficheiro_caminho, "r", encoding="utf-8") as ficheiro:
    dados = json.load(ficheiro)
print(dados)
print(f"Nome: {dados['nome']}")  # Aceder a um campo específico