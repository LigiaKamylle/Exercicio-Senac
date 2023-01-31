class  Produto:
    def __init__(self, nome, preço, país_origem) -> None:
        self.nome = nome
        self.preço = preço
        self.país_origem = país_origem
        

quantidade = int(input("Informe a quantidade: "))
print(quantidade)
