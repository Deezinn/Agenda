from models import Contato, AgendaModels

class AgendaService:
    def __init__(self):
        self.model = AgendaModels()

    def adicionar_contato(self, nome, telefone, email, favorito,created_at, updated_at):
        if not nome or not telefone:
            raise ValueError("Nome e telefone são obrigatórios!")
        contato = Contato(nome, telefone, email, favorito, created_at, updated_at)
        self.model.adicionar_contato(contato)
        return f"contato {nome} adicionado com sucesso."

    def listar_contatos(self):
        return self.model.listar_contatos()

    def editar_contato(self):
       return self.model.editar_contato(nome, novo_telefone, novo_email, novo_favorito):
