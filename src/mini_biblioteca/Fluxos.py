from mini_biblioteca.Emprestimos import Emprestimo
from mini_biblioteca.Livros import Livro
from mini_biblioteca.Usuarios import Usuario

import uuid
import random
import json
import os

class Fluxos():
    """ 
    regras
        cria 1 Usuario
        cria 1 Livro
        cria 1 Emprestimo
        devolve o livro
        imprime 2 ou 3 linhas mostrando o estado
    """

    def criar_usuario(self):

        nome = input("nome do usuario: ")
        id_usuario = str(uuid.uuid4()) 
        self.user = Usuario(nome, id_usuario)


        # Vou fazer um json para persistir os nomes e id.
        # Não estou a me procupar com segurança nesse exemplo específico.

        dados_python = {
            "id": self.user.id_usuario,
            "nome": self.user.nome
        }

        with open('usuarios.json', 'a', encoding='utf-8') as arquivo_json:
            json.dump(dados_python, arquivo_json, indent=4, ensure_ascii=False ) #utf-8

        print(f"Usuario '{self.user.nome}' cadastrado com sucesso!")


    def criar_livro(self):

        titulo = input("Título do livro: ")
        autor = input("Autor do livro :")

        
        # Utilizarei o formato ISBN, os numeros gerados não são reais, em verdade, são pseudo aleatórios.
        EAN_PREFIX = "978"
        registration_group = random.randrange(1, 99)
        registrant = random.randrange(1, 99999)
        publication = random.randrange(1, 99)
        check_digit = random.randrange(1, 9)
        # numero gerado é Pseudo aleatório, privavelmente não vou fazer verificaçoes, apenas adicionei porque e legal <uwu>

        codigo = f"{EAN_PREFIX}-{registration_group}-{registrant}-{publication}-{check_digit}"
        
        self.livro = Livro(titulo, autor, codigo)

        dados_python = {
            "ispn": self.livro.codigo,
            "titulo": self.livro.titulo,
            "autor": self.livro.autor
        }

        with open('livros.json', 'a', encoding='utf-8') as arquivo_json:
            json.dump(dados_python, arquivo_json, indent=4, ensure_ascii=False ) #utf-8

            print(f"Livro '{self.livro.titulo}' cadastrado com sucesso!")

    from mini_biblioteca.Emprestimos import Emprestimo

    def criar_emprestimo(self):
        titulo_busca = input("Digite o TÍTULO do livro para empréstimo: ").strip().lower()

        caminho_livros = os.path.join("database", "livros.json")

        livros_atualizados = []
        livro_encontrado = None

        with open(caminho_livros, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                livro = json.loads(linha)

                if livro.get("titulo", "").strip().lower() == titulo_busca:
                    livro_encontrado = livro

                    if not livro.get("disponivel", True):
                        print("Livro indisponível para empréstimo.")
                        return

                    # Marca como indisponível
                    livro["disponivel"] = False

                livros_atualizados.append(livro)

        if not livro_encontrado:
            print("Livro não encontrado.")
            return

        with open(caminho_livros, "w", encoding="utf-8") as arquivo:
            for livro in livros_atualizados:
                json.dump(livro, arquivo, ensure_ascii=False)
                arquivo.write("\n")

        self.emprestimo = Emprestimo(
            livro=self.livro,
            usuario=self.user
        )

        print(f"Emprestimo criado com sucesso para o livro '{livro_encontrado['titulo']}'!")


