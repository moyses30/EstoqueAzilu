import tkinter as tk
from pandas.core.interchange import column
from prompt_toolkit.layout import menus

janela = tk.Tk()
janela.title('Estoque azilu ')

#janela.rowconfigure(0,weight=1)
# fg muda a cor da letra bg muda o fundo, width Altura, height = lagura
#coloumnspan ocupa mais de um coluna
# stick = NSEW aumenta a caixa para todos os ladow

nome_produto_texto=  tk.Label(text = "Nome do Produto",fg ='red', bg ='green',width=30,height=2)
nome_produto_texto.grid(row=0,column=0)

nome_produto = tk.Entry()
nome_produto.grid(row=1,column=1)
# fg muda a cor da letra bg muda o fundo, width Altura
valor_produto=tk.Label(text = "Valor do Produto" , fg ='red', bg ='blue',width=30,height=2).grid(row=1, column=0,columnspan=1,sticky="NSEW") # fg muda a cor da letra bg muda o fundo, width Altura
valor_produto.grid(row=1, column=0,columnspan=1,sticky="NSEW")

valor_produto = tk.Entry().grid(row=0,column=1)


quantidade_texto=  tk.Label(text = "Quantidade",fg ='red', bg ='orange',width=30,height=2).grid(row=3,column=0)
quantidade= tk.Entry().grid(row=3,column=1)


def adicionar_produto ():
    print('produto adicionado com sucesso')

botao_adicionar= tk.Button(text="Adiconar produto",command=adicionar_produto)
botao_adicionar.grid(row=4, column=1)

def deletar_produto():
    print(f'{nome_produto},foi deletado com sucesso ')

botao_deletar= tk.Button(text="Deletar produto", command=deletar_produto)
botao_deletar.grid(row=4, column=2)

def registrar_uso ():
    print('Produto registrado')
botao_registar_uso= tk.Button(text="Registrar uso ", command=registrar_uso)
botao_registar_uso.grid(row=4, column=3)

def procurar_produto():

    print(nome_produto.get())

botao_procurar_produto= tk.Button(text="Procurar Produto", command=procurar_produto)
botao_procurar_produto.grid(row=4, column=4)

janela.mainloop()