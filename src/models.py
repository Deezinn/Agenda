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

    def editar_contato(self, nome, novo_nome=None, novo_telefone=None, novo_email=None, novo_update=None):
        for contato in self.contatos:
            if contato.nome == nome:
                if novo_nome is not None:
                    contato.nome = novo_nome
                if novo_telefone is not None:
                    contato.telefone = novo_telefone
                if novo_email is not None:
                    contato.email = novo_email
                if novo_update is not None:
                    contato.updated_at = novo_update
                return "Contato alterado com sucesso!"
            return "Não encontramos esse contato."

    def marcar_contato_favorito(self, nome, favorito):
        for contato in self.contatos:
            if contato.nome == nome:
                contato.favorito = favorito
                return "Contato marcado como favorito"
            return "Contato não encontrado"

    def listar_contatos_favoritos(self):
        for contato in self.contatos:
            if contato.favorito:
                print(contato)
                return contato
            else:
                print("Não existe contato como favorito!")
                return contato

    def deletar_contato(self,nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.clear()

