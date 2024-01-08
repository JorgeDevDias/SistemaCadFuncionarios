import tkinter as tk
from tkinter import ttk
import openpyxl as xl

#Funcoes
def inserir_dados():
  pass

def tema_selecionado():
  pass



#Iniciano a janela
root = tk.Tk()
root.title("Sistema de Cadastro Funcionários")

#Configuração do Tema
estilo = ttk.Style(root)
root.tk.call("source", "forest-light.tcl")
root.tk.call("source", "forest-dark.tcl")
estilo.theme_use("forest-dark")

#Frame principal
frame_principal = ttk.Frame(root)
frame_principal.pack()

frame_cadastro = ttk.LabelFrame(frame_principal, text="Cadastro")
frame_cadastro.grid(row=0, column=0, padx=20, pady=10)

#Campos de cadastro
nome_entry = ttk.Entry(frame_cadastro)
nome_entry.insert(0,"Nome...")
nome_entry.bind("<FocusIn>", lambda e: nome_entry.delete("0","end"))
nome_entry.grid(row=0,column=0, padx=5, pady=(10,5), sticky='ew')

idade_spinbox = ttk.Spinbox(frame_cadastro, from_=18, to=70)
idade_spinbox.insert(0,"Idade")
idade_spinbox.grid(row=1,column=0, padx=5, pady=5, sticky='ew')

lista_status = ['Ativo','Afastado']
status_col = ttk.Combobox(frame_cadastro,values=lista_status)
status_col.current(0)
status_col.grid(row=2,column=0, padx=5, pady=5, sticky='ew')

ferias = tk.BooleanVar()
check_ferias = ttk.Checkbutton(frame_cadastro, text="Férias", variable=ferias)
check_ferias.grid(row=3,column=0, padx=5, pady=5, sticky='nsew')

btn_cadastrar = ttk.Button(frame_cadastro,text="Inser dados".upper(), command=inserir_dados)
btn_cadastrar.grid(row=4,column=0, padx=5, pady=5, sticky='nsew')

separador = ttk.Separator(frame_cadastro)
separador.grid(row=5,column=0, padx=5, pady=10)

tema = ttk.Checkbutton(frame_cadastro, text="Tema", style='Switch', command=tema_selecionado)
tema.grid(row=6,column=0, padx=5, pady=10, sticky='nsew')

#Rodanddo a aplicação
root.mainloop()