from mini_biblioteca.Livros import Livro
from mini_biblioteca.Usuarios import Usuario

class Emprestimo():

    livro: Livro
    usuario: Usuario
    ativo: bool = True #(default=true)

    def __init__(self, livro: Livro, usuario: Usuario, ativo: bool = True):
        self.livro = livro
        self.usuario = usuario
        self.ativo = ativo
