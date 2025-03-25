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
            print(self.service.adicionar_contato(nome, telefone, email, favorito, created_at, updated_at))
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
            nome = input("Digite o contato a ser editado: ")
            opcoes = input("Digite a opção para modificar, [1] nome, [2] telefone, [3] E-mail: ")
            if opcoes == '1' or opcoes == '2' or opcoes == '3':
                if opcoes == '1':
                    novo_nome = input("Digite o novo nome:")
                    self.service.editar_contato(nome,novo_nome,None,None, datetime.now().date())
                if opcoes == '2':
                    novo_telefone = input("Digite o novo telefone:")
                    self.service.editar_contato(nome,None,novo_telefone,None, datetime.now().date())
                if opcoes == '3':
                    novo_email = input("Digite o novo email:")
                    self.service.editar_contato(nome,None,None,novo_email, datetime.now().date())
            else:
                print('Opções invalidas!')

    def marcar_contato_favorito(self):
        contatos = self.service.listar_contatos()
        if not contatos:
            print("Não há contatos cadastrados!")
        else:
            nome = input("Digite o contato a ser favorito: ")
            self.service.marcar_contato_favorito(nome,favorito=True)

    def listar_contatos_favoritos(self):
        contatos = self.service.listar_contatos()
        if not contatos:
            print("Não há contatos cadastrados!")
        else:
            self.service.listar_contatos_favoritos()

    def deletar_contato(self):
        contatos = self.service.listar_contatos()
        if not contatos:
            print("Não há contatos cadastrados!")
        else:
            nome_a_deletar = input("Digite o nome do contato que queira deletar: ")
            self.service.deletar_contato(nome_a_deletar)

agenda = AgendaController()
count = 0
while True:
    agenda.adicionar_contato()
    agenda.marcar_contato_favorito()
    count += 1
    if count >= 1:
        break

agenda.listar_contatos_favoritos()
agenda.deletar_contato()
agenda.visualizar_contatos()
