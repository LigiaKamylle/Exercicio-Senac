class  Produto:
    def __init__(self, nome, preço, país_origem) -> None:
        self.nome = nome
        self.preço = preço
        self.país_origem = país_origem

    def exibir(self, indice = 0):
        print(f"{indice} === Nome: {self.nome} - Preço {self.preço}")        

produto_um = Produto("pizza", 25, "Itália")
produto_dois = Produto("Torta", 5, "Grécia")

produtos = [produto_um, produto_dois]

for produto in produtos:
    indice = produtos.index(produto)
    produto.exibir(indice)

indice_selecionado = int(input("Selecione o produto: "))
if indice_selecionado > len(produtos):
    print("Produto inexistente")
else: 
    produto = produtos[indice_selecionado]   
    quantidade = int(input("Informe a quantidade: "))
    print(f"O valor total é: {quantidade * produto.preço}")
