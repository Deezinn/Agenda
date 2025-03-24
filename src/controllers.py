from datetime import datetime
from services import AgendaService
from models import AgendaModels

class AgendaController:
    def __init__(self):
        self.service = AgendaService()

    def adicionar_contato(self):

        nome = input("Digite o nome do contato: ")
        telefone = input(f"Digite o número desse contato {nome}: ")
        email = input(f"Digite o e-mail desse contato {nome}: ")
        created_at = datetime.now().date()
        updated_at = None

        try:
            print(self.service.adicionar_contato(nome,telefone,email,created_at,updated_at))
        except ValueError as e:
            print(f"Erro: {e}")

    def visualizar_contatos(self):
        contatos = self.service.listar_contatos()
        if not contatos:
            print("Não há contatos cadastrados!")
        else:
            for contato in contatos:
                print(contato)

    # def editar_contato(self):

    # def marcar_contato_favorito(self):

    # def listar_contatos_favoritos(self):

    # def apagar_contato(self):

count = 0
agenda = AgendaController()

while True:
    agenda.adicionar_contato()
    print(agenda.visualizar_contatos())
    count+= 1
    if count > 3:
        break
