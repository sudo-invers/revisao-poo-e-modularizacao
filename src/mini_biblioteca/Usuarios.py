class Usuario():
    def __init__(self, nome: str, id_usuario: str): # No caso, o id sera uma string de UUID
        self.nome = nome
        self.id_usuario = id_usuario

    @property
    def nome(self):
        """The nome property."""
        return self._nome
    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def id_usuario(self):
        """The id_usuario property."""
        return self._id_usuario
    @id_usuario.setter
    def id_usuario(self, value):
        self._id_usuario = value
