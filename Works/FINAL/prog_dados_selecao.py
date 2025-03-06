import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd



# Carregar os dados do CSV
FILE_PATH = "C:\\Historico\\DadosSelecao.csv"
def load_data():
    try:
        return pd.read_csv(FILE_PATH, encoding="ISO-8859-1")
    except FileNotFoundError:
        return pd.DataFrame(columns=["Jogo", "Data", "Local", "Adversário", "GM", "GS", "Competição", "Técnico", "Marcadores Golos", "Golos marcados", "Tipo Golo", "Estreias"])

def save_data(df):
    df.to_csv(FILE_PATH, index=False, encoding="ISO-8859-1")

# Criar a interface gráfica
root = tk.Tk()
root.title("Gerenciador de Jogos")
root.geometry("800x500")

data = load_data()
'''
def show_data():
    for row in tree.get_children():
        tree.delete(row)
    for index, row in data.iterrows():
        tree.insert("", "end", values=list(row))

def add_game():
    new_game = [entry.get() for entry in entries]
    if "" in new_game:
        messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos!")
        return
    global data
    data = data.append(pd.Series(new_game, index=data.columns), ignore_index=True)
    save_data(data)
    show_data()
    for entry in entries:
        entry.delete(0, tk.END)

tree = ttk.Treeview(root, columns=list(data.columns), show="headings")
for col in data.columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)
tree.pack(expand=True, fill="both")

frame = tk.Frame(root)
frame.pack()
entries = [tk.Entry(frame) for _ in data.columns]
for i, col in enumerate(data.columns):
    tk.Label(frame, text=col).grid(row=0, column=i)
    entries[i].grid(row=1, column=i)

btn_add = tk.Button(root, text="Adicionar Jogo", command=add_game)
btn_add.pack()

show_data()
root.mainloop() '''