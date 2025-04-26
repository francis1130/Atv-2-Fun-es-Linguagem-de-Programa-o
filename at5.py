import json

class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def to_dict(self):
        return {
            "nome": self.nome,
            "telefone": self.telefone,
            "email": self.email
        }

    @staticmethod
    def from_dict(dado):
        return Contato(dado["nome"], dado["telefone"], dado["email"])

class Agenda:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.contatos = []
        self.carregar()

    def adicionar_contato(self, nome, telefone, email):
        contato = Contato(nome, telefone, email)
        self.contatos.append(contato)
        self.salvar()

    def buscar_contato(self, nome_busca):
        encontrados = [c for c in self.contatos if nome_busca.lower() in c.nome.lower()]
        if encontrados:
            for contato in encontrados:
                print(f"Nome: {contato.nome} | Telefone: {contato.telefone} | Email: {contato.email}")
        else:
            print("Nenhum contato encontrado.")

    def salvar(self):
        with open(self.arquivo, "w") as f:
            json.dump([c.to_dict() for c in self.contatos], f, indent=4)

    def carregar(self):
        try:
            with open(self.arquivo, "r") as f:
                dados = json.load(f)
                self.contatos = [Contato.from_dict(d) for d in dados]
        except FileNotFoundError:
            self.contatos = []

def menu():
    agenda = Agenda("contatos.json")
    while True:
        print("\n1. Adicionar Contato\n2. Buscar Contato\n3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            agenda.adicionar_contato(nome, telefone, email)
        elif opcao == "2":
            nome_busca = input("Nome para buscar: ")
            agenda.buscar_contato(nome_busca)
        elif opcao == "3":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
