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
        # aplicar validações futuramente

    def listar_contatos(self):
        return self.model.listar_contatos()
        # aplicar validações futuramente

    def editar_contato(self, nome, novo_nome=None, novo_telefone=None, novo_email=None, novo_update=None):
        # aplicar validações futuramente
       return self.model.editar_contato(nome, novo_nome, novo_telefone, novo_email, novo_update)

    def marcar_contato_favorito(self,nome, favorito):
        # aplicar validações futuramente
        return self.model.marcar_contato_favorito(nome,favorito)

    def listar_contatos_favoritos(self):
        # aplicar validações futuramente
        return self.model.listar_contatos_favoritos()

    def deletar_contato(self,nome):
        # aplicar validações futuramente
        return self.model.deletar_contato(nome)



