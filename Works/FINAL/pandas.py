FILE_PATH = "C:\\Historico\\DadosSelecao.csv"
def load_data():
    try:
        return pd.read_csv(FILE_PATH, encoding="ISO-8859-1")
    except FileNotFoundError:
        return pd.DataFrame(columns=["Jogo", "Data", "Local", "Adversário", "GM", "GS", "Competição", "Técnico", "Marcadores Golos", "Golos marcados", "Tipo Golo", "Estreias"])

def save_data(df):
    df.to_csv(FILE_PATH, index=False, encoding="ISO-8859-1")
    
    
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

    