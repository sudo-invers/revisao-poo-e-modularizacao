class Livro:
    def __init__(self, titulo: str, autor: str, codigo: str, disponivel: bool = True):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo  # (unico)
        self.disponivel = disponivel # (default=true)

    @property
    def titulo(self):
        """The titulo property."""
        return self._titulo
    @titulo.setter
    def titulo(self, value):
        self._titulo = value
    
    @property
    def autor(self):
        """The autor property."""
        return self.autor._autor
    @autor.setter
    def autor(self, value):
        self._autor = value

    @property
    def codigo(self):
        """The codigo property."""
        return self._codigo
    @codigo.setter
    def codigo(self, value):
        self._codigo = value

    @property
    def disponivel(self):
        """The disponivel property."""
        return self._disponivel
    @disponivel.setter
    def disponivel(self, value):
        self._disponivel = value
