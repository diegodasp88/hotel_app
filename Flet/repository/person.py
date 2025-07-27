class Person:
    def __init__(self, nome: str, telefone: str, email: str):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email

    # GETTERS and SETTERS
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str):
        if novo_nome:
            self.__nome = novo_nome

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, novo_telefone: str):
        if novo_telefone:
            self.__telefone = novo_telefone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, novo_email: str):
        if novo_email:
            self.__email = novo_email


class Client(Person):
    def __init__(self, id: int, nome: str, telefone: str, email: str):
        super().__init__(nome, telefone, email)
        self.__id = id

    @property
    def id(self):
        return self.__id
    
    def to_dict(self):
        """Método para transformar os dados dos clientes em dicionário para salvar no bd."""
        return {
            "id": int(self.id),
            "nome": self.nome,
            "telefone": self.telefone,
            "email": self.email
        }
