class  Produto:
    def __init__(self, nome, preço, país_origem) -> None:
        self.nome = nome
        self.preço = preço
        self.país_origem = país_origem

    def exibir(self):
        print(f"Nome: {self.nome} - Preço {self.preço}")        

produto = Produto("pizza", 25, "Itália")
produto.exibir()
quantidade = int(input("Informe a quantidade: "))

