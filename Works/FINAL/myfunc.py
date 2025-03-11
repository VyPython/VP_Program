
import pandas as pd
print(pd.__version__)

# Criar um DataFrame simples
data = {'Nome': ['Alice', 'Bob', 'Charlie'], 'Idade': [25, 30, 35]}
df = pd.DataFrame(data)

# Exibir o DataFrame
print(df)

'''FILE_PATH="C:\\historico\\dadosseleccao.csv"
read_csv = FILE_PATH
def load_data():
    try:
        return pd.read_csv(FILE_PATH, encoding="ISO-8859-1")
    except FileNotFoundError:
        return pd.DataFrame(columns=["Jogo", "Data", "Local", "Adversário", "GM", "GS", "Competição", "Técnico", "Marcadores Golos", "Golos marcados", "Tipo Golo", "Estreias"])

def save_data(df):
    df.to_csv(FILE_PATH, index=False, encoding="ISO-8859-1")'''
