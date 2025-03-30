from controllers import AgendaController
class Menu:
    def __init__(self):
        self.agenda = AgendaController()

    def menu(self):
        print("-------------------------")
        print("         Agenda")
        print("-------------------------")
        print("Digite as opções abaixo: ")
        print("[1] para adicionar Contato.")
        print("[2] para visualizar Contatos.")
        print("[3] editar contato.")
        print("[4] marcar como favorito.")
        print("[5] listar contatos favoritos.")
        print("[6] deletar contato.")
        print("[7] sair")

    def opcoes(self):
        self.menu()
        while True:
            escolha = input("\nDigite sua opção:")
            match escolha:

                case "1":
                    self.agenda.adicionar_contato()
                case "2":
                    self.agenda.visualizar_contatos()
                case "3":
                    self.agenda.editar_contato()
                case "4":
                    self.agenda.marcar_contato_favorito()
                case "5":
                    self.agenda.listar_contatos_favoritos()
                case "6":
                    self.agenda.deletar_contato()
                case "7":
                    print("Saindo...")
                    break
                case _:
                    print("Escolha incorreta.")
