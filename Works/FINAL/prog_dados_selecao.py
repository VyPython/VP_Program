import tkinter as tk
from tkinter import ttk, messagebox
#import pandas as pd
from func_pandas import load_data, save_data
#myfunc as mf

# Criar a interface gráfica
root = tk.Tk()
root.title("Gerenciador de Jogos")
root.geometry("900x600")
root.configure(bg="#f0f0f0")


def show_data(filtered_data=None):
    for row in tree.get_children():
        tree.delete(row)
    df_to_show = filtered_data if filtered_data is not None else data
    for index, row in df_to_show.iterrows():
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

def filter_data():
    filter_text = filter_entry.get().strip().lower()
    if not filter_text:
        show_data()
        return
    filtered = data[data.apply(lambda row: filter_text in row.astype(str).str.lower().to_list(), axis=1)]
    show_data(filtered)

data = load_data()

tree = ttk.Treeview(root, columns=list(data.columns), show="headings")
for col in data.columns:
    tree.heading(col, text=col)
    tree.column(col, width=80)
tree.pack(expand=True, fill="both", padx=10, pady=10)

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)
entries = [tk.Entry(frame) for _ in data.columns]
for i, col in enumerate(data.columns):
    tk.Label(frame, text=col, bg="#f0f0f0").grid(row=0, column=i, padx=5, pady=5)
    entries[i].grid(row=1, column=i, padx=5, pady=5)

btn_add = tk.Button(root, text="Adicionar Jogo", command=add_game, bg="#4CAF50", fg="white")
btn_add.pack(pady=5)

filter_frame = tk.Frame(root, bg="#f0f0f0")
filter_frame.pack(pady=5)
tk.Label(filter_frame, text="Filtrar:", bg="#f0f0f0").pack(side=tk.LEFT, padx=5)
filter_entry = tk.Entry(filter_frame)
filter_entry.pack(side=tk.LEFT, padx=5)
btn_filter = tk.Button(filter_frame, text="Aplicar Filtro", command=filter_data, bg="#2196F3", fg="white")
btn_filter.pack(side=tk.LEFT, padx=5)

show_data()
root.mainloop()