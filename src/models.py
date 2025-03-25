class Contato:
    def __init__(self, nome, telefone, email,favorito,created_at, updated_at):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.favorito = favorito
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
         return f"Nome: {self.nome}, Telefone {self.telefone}, Email: {self.email}, é favorito? {self.favorito}, foi criado em: {self.created_at} e foi atualizado em: {self.updated_at}"


class AgendaModels:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self,contato_a_adicionar):
        self.contatos.append(contato_a_adicionar)


    def listar_contatos(self):
        return self.contatos

    def editar_contato(self, nome, novo_telefone=None, novo_email=None, novo_favorito=None):
        for contato in self.contatos:
            if contato.nome == nome:
                if novo_telefone:
                    contato.telefone = novo_telefone
                if novo_email:
                    contato.email = novo_email
                if novo_favorito is not None:
                    contato.favorito = novo_favorito
                contato.updated_at = datetime.now.date()
                return f"Contato {nome} foi editado com sucesso!"
        return f"contato {nome} não encontrado"


