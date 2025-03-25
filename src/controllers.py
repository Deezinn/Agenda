from datetime import datetime
from services import AgendaService

class AgendaController:
    def __init__(self):
        self.service = AgendaService()

    def adicionar_contato(self):
        nome = input("Digite o nome do contato: ")
        telefone = input(f"Digite o número desse contato {nome}: ")
        email = input(f"Digite o e-mail desse contato {nome}: ")
        favorito = False
        created_at = datetime.now().date()
        updated_at = None

        try:
            print(self.service.adicionar_contato(nome,telefone,email,favorito,created_at,updated_at))
        except ValueError as e:
            print(f"Erro: {e}")

    def visualizar_contatos(self):
        contatos = self.service.listar_contatos()
        if not contatos:
            print("Não há contatos cadastrados!")
        else:
            for contato in contatos:
               print(contato)

    def editar_contato(self):
        contatos = self.service.listar_contatos()
        if not contatos:
            print("Não há contatos cadastrados!")
        else:
            for contato in contatos:
                contato_a_mudar = input("Digite qual contato queira mudar: ")
                







                else:
                    print('Você digitou algo errado')

    def marcar_contato_favorito(self):
        contatos = self.service.listar_contatos()
        if not contatos:
            print("Não há contatos cadastrados!")
        else:
            for contato in contatos:
                contato_a_favoritar = input("Digite o contato que queira favoritar: ")
                if contato.nome == contato_a_favoritar:
                    contato.favorito = True
                    print("Pronto, foi marcado com uma estrelinha")

    def listar_contatos_favoritos(self):
        contatos = self.service.listar_contatos()
        if not contatos:
            print("Não há contatos cadastrados!")
        else:
            for contato in contatos:
                if contato.favorito == True:
                    print(contato)

    def apagar_contato(self):
        contatos = self.service.listar_contatos()
        if not contatos:
            print("Não há contatos cadastrados!")
        else:
            for contato in contatos:
                contato_a_deletar = input("Digite o contato que deseja deletar: ")
                if contato.nome == contato_a_deletar:


agenda = AgendaController()
count = 0
while True:
    agenda.adicionar_contato()
    agenda.visualizar_contatos()
    count+= 1
    agenda.editar_contato()
    if count >= 2:
        break
agenda.visualizar_contatos()
