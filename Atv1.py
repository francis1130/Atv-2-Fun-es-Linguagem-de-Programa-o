import json
from datetime import datetime

class Tarefa:
    def __init__(self, descricao, prazo, concluida=False):
        self.descricao = descricao
        self.prazo = datetime.strptime(prazo, "%Y-%m-%d")
        self.concluida = concluida

    def to_dict(self):
        return {
            "descricao": self.descricao,
            "prazo": self.prazo.strftime("%Y-%m-%d"),
            "concluida": self.concluida
        }

    @staticmethod
    def from_dict(dado):
        return Tarefa(dado["descricao"], dado["prazo"], dado["concluida"])

class GerenciadorTarefas:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.tarefas = []
        self.carregar()

    def adicionar_tarefa(self, descricao, prazo):
        tarefa = Tarefa(descricao, prazo)
        self.tarefas.append(tarefa)
        self.salvar()

    def listar_tarefas(self):
        tarefas_ordenadas = sorted(self.tarefas, key=lambda t: t.prazo)
        for idx, tarefa in enumerate(tarefas_ordenadas, 1):
            status = "Concluída" if tarefa.concluida else "Pendente"
            print(f"{idx}. {tarefa.descricao} - Prazo: {tarefa.prazo.date()} - {status}")

    def marcar_concluida(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].concluida = True
            self.salvar()

    def salvar(self):
        with open(self.arquivo, "w") as f:
            json.dump([tarefa.to_dict() for tarefa in self.tarefas], f, indent=4)

    def carregar(self):
        try:
            with open(self.arquivo, "r") as f:
                dados = json.load(f)
                self.tarefas = [Tarefa.from_dict(d) for d in dados]
        except FileNotFoundError:
            self.tarefas = []

def menu():
    gerenciador = GerenciadorTarefas("tarefas.json")
    while True:
        print("\n1. Adicionar Tarefa\n2. Listar Tarefas\n3. Marcar Tarefa como Concluída\n4. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            descricao = input("Descrição: ")
            prazo = input("Prazo (AAAA-MM-DD): ")
            gerenciador.adicionar_tarefa(descricao, prazo)
        elif opcao == "2":
            gerenciador.listar_tarefas()
        elif opcao == "3":
            gerenciador.listar_tarefas()
            indice = int(input("Número da tarefa para marcar como concluída: ")) - 1
            gerenciador.marcar_concluida(indice)
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
