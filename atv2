import json

class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def to_dict(self):
        return {
            "nome": self.nome,
            "quantidade": self.quantidade,
            "preco": self.preco
        }

    @staticmethod
    def from_dict(dado):
        return Produto(dado["nome"], dado["quantidade"], dado["preco"])

class ControleEstoque:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.produtos = []
        self.carregar()

    def adicionar_produto(self, nome, quantidade, preco):
        produto = Produto(nome, quantidade, preco)
        self.produtos.append(produto)
        self.salvar()

    def exibir_produtos(self):
        total = 0
        for idx, produto in enumerate(self.produtos, 1):
            subtotal = produto.quantidade * produto.preco
            total += subtotal
            print(f"{idx}. {produto.nome} - Quantidade: {produto.quantidade} - Preço: R${produto.preco:.2f} - Subtotal: R${subtotal:.2f}")
        print(f"\nValor total do estoque: R${total:.2f}")

    def salvar(self):
        with open(self.arquivo, "w") as f:
            json.dump([produto.to_dict() for produto in self.produtos], f, indent=4)

    def carregar(self):
        try:
            with open(self.arquivo, "r") as f:
                dados = json.load(f)
                self.produtos = [Produto.from_dict(d) for d in dados]
        except FileNotFoundError:
            self.produtos = []

def menu():
    estoque = ControleEstoque("estoque.json")
    while True:
        print("\n1. Adicionar Produto\n2. Exibir Produtos\n3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            estoque.adicionar_produto(nome, quantidade, preco)
        elif opcao == "2":
            estoque.exibir_produtos()
        elif opcao == "3":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
