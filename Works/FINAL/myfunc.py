
import pandas as pd


# Criar um DataFrame simples baseado num no ficheiro CSV

FILE_PATH="C:\\historico\\dadosseleccao.csv" # Caminho do ficheiro CSV

def load_data(): # Função para carregar o ficheiro CSV
    try:
        return pd.read_csv("dadosseleccao.csv", encoding="ISO-8859-1") # Ler o ficheiro CSV
    except FileNotFoundError: # Se o ficheiro não for encontrado
        return pd.DataFrame(columns=["Jogo", "Data", "Local", "Adversário", "GM", "GS", "Competição", "Técnico", "Marcadores Golos", "Golos marcados", "Tipo Golo", "Estreias"]) # Criar um DataFrame vazio com as colunas necessárias

#mostrar os dados
def show_data():
    df = load_data() # Carregar o DataFrame
    return df # Retornar o DataFrame

print(show_data()) # Mostrar o DataFrame


    
'''# Função para adicionar um novo registo ao DataFrame
def add_data(jogo, data, local, adversario, gm, gs, competicao, tecnico, marcadores_golos, golos_marcados, tipo_golo, estreias):
    df = load_data() # Carregar o DataFrame
    new_data = pd.DataFrame([[jogo, data, local, adversario, gm, gs, competicao, tecnico, marcadores_golos, golos_marcados, tipo_golo, estreias]], columns=["Jogo", "Data", "Local", "Adversário", "GM", "GS", "Competição", "Técnico", "Marcadores Golos", "Golos marcados", "Tipo Golo", "Estreias"]) # Criar um novo DataFrame com o registo a adicionar
    df = df.append(new_data, ignore_index=True) # Adicionar o registo ao DataFrame
    df.to_csv("dadosseleccao.csv", index=False) # Guardar o DataFrame no ficheiro CSV
    return df # Retornar o DataFrame'''


casts = pd.read_csv(FILE_PATH, index_col=None, encoding="ISO-8859-1")

pd.set_option('max_columns', 5, 'max_rows', 10) # Limitar o número de colunas e linhas a mostrar
titles

print(casts) # Mostrar o DataFrame



'''def load_data():
    try:
        return pd.read_csv(FILE_PATH, encoding="ISO-8859-1")
    except FileNotFoundError:
        return pd.DataFrame(columns=["Jogo", "Data", "Local", "Adversário", "GM", "GS", "Competição", "Técnico", "Marcadores Golos", "Golos marcados", "Tipo Golo", "Estreias"])'''

