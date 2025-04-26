import json

class Usuario:
    def __init__(self, nome_usuario, senha, saldo=0, transacoes=None):
        self.nome_usuario = nome_usuario
        self.senha = senha
        self.saldo = saldo
        self.transacoes = transacoes if transacoes else []

    def to_dict(self):
        return {
            "nome_usuario": self.nome_usuario,
            "senha": self.senha,
            "saldo": self.saldo,
            "transacoes": self.transacoes
        }

    @staticmethod
    def from_dict(dado):
        return Usuario(dado["nome_usuario"], dado["senha"], dado["saldo"], dado["transacoes"])

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append(f"Depósito de R${valor:.2f}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.transacoes.append(f"Saque de R${valor:.2f}")
        else:
            print("Saldo insuficiente.")

class Banco:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.usuarios = []
        self.carregar()

    def cadastrar_usuario(self, nome_usuario, senha):
        if any(u.nome_usuario == nome_usuario for u in self.usuarios):
            print("Usuário já existe.")
        else:
            usuario = Usuario(nome_usuario, senha)
            self.usuarios.append(usuario)
            self.salvar()

    def autenticar(self, nome_usuario, senha):
        for usuario in self.usuarios:
            if usuario.nome_usuario == nome_usuario and usuario.senha == senha:
                return usuario
        print("Nome de usuário ou senha incorretos.")
        return None

    def salvar(self):
        with open(self.arquivo, "w") as f:
            json.dump([u.to_dict() for u in self.usuarios], f, indent=4)

    def carregar(self):
        try:
            with open(self.arquivo, "r") as f:
                dados = json.load(f)
                self.usuarios = [Usuario.from_dict(d) for d in dados]
        except FileNotFoundError:
            self.usuarios = []

def menu():
    banco = Banco("usuarios.json")
    while True:
        print("\n1. Cadastrar\n2. Login\n3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nome = input("Nome de usuário: ")
            senha = input("Senha: ")
            banco.cadastrar_usuario(nome, senha)
        elif opcao == "2":
            nome = input("Nome de usuário: ")
            senha = input("Senha: ")
            usuario = banco.autenticar(nome, senha)
            if usuario:
                menu_usuario(usuario, banco)
        elif opcao == "3":
            break
        else:
            print("Opção inválida.")

def menu_usuario(usuario, banco):
    while True:
        print(f"\nUsuário: {usuario.nome_usuario} | Saldo: R${usuario.saldo:.2f}")
        print("1. Depositar\n2. Sacar\n3. Extrato\n4. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            valor = float(input("Valor para depósito: "))
            usuario.depositar(valor)
            banco.salvar()
        elif opcao == "2":
            valor = float(input("Valor para saque: "))
            usuario.sacar(valor)
            banco.salvar()
        elif opcao == "3":
            print("\nExtrato de Transações:")
            for t in usuario.transacoes:
                print("-", t)
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
