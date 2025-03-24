class Contato:
    def __init__(self, nome, telefone, email, created_at, updated_at):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.create_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return f"Nome: {self.nome}, Telefone {self.telefone}, Email: {self.email} foi criado em: {self.create_at}"


class AgendaModels:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self,contato):
        self.contatos.append(contato)

    def listar_contatos(self):
        return self.contatos
