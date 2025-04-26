import json

class Evento:
    def __init__(self, arquivo, linhas=5, colunas=5):
        self.arquivo = arquivo
        self.linhas = linhas
        self.colunas = colunas
        self.assentos = []
        self.carregar()

    def criar_assentos(self):
        self.assentos = [["L" for _ in range(self.colunas)] for _ in range(self.linhas)]

    def exibir_assentos(self):
        print("Mapa de Assentos (L = Livre, X = Reservado)")
        for i, linha in enumerate(self.assentos):
            linha_str = " ".join(linha)
            print(f"{i}: {linha_str}")

    def reservar_assento(self, linha, coluna):
        if self.assentos[linha][coluna] == "L":
            self.assentos[linha][coluna] = "X"
            self.salvar()
        else:
            print("Assento já reservado.")

    def cancelar_reserva(self, linha, coluna):
        if self.assentos[linha][coluna] == "X":
            self.assentos[linha][coluna] = "L"
            self.salvar()
        else:
            print("Assento não está reservado.")

    def salvar(self):
        with open(self.arquivo, "w") as f:
            json.dump(self.assentos, f, indent=4)

    def carregar(self):
        try:
            with open(self.arquivo, "r") as f:
                self.assentos = json.load(f)
        except FileNotFoundError:
            self.criar_assentos()
            self.salvar()

def menu():
    evento = Evento("assentos.json")
    while True:
        print("\n1. Exibir mapa de assentos\n2. Reservar assento\n3. Cancelar reserva\n4. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            evento.exibir_assentos()
        elif opcao == "2":
            evento.exibir_assentos()
            linha = int(input("Linha do assento: "))
            coluna = int(input("Coluna do assento: "))
            evento.reservar_assento(linha, coluna)
        elif opcao == "3":
            evento.exibir_assentos()
            linha = int(input("Linha do assento: "))
            coluna = int(input("Coluna do assento: "))
            evento.cancelar_reserva(linha, coluna)
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
