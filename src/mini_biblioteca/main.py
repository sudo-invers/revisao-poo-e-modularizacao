from mini_biblioteca.Fluxos import Fluxos

def main():
    fluxo = Fluxos()

    while True:

        # TODO: Criar tela de login no futuro talvez

        print("\n===== MINI BIBLIOTECA =====")
        print("1 - Criar usuário")
        print("2 - Criar livro")
        print("3 - Criar empréstimo")
        print("4 - Devolver livro")
        print("5 - Mostrar estado atual")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            fluxo.criar_usuario()

        elif opcao == "2":
            fluxo.criar_livro()

        elif opcao == "3":
            if not hasattr(fluxo, "user") or fluxo.user is None:
                print("❌ Crie um usuário antes de fazer um empréstimo.")
            elif not hasattr(fluxo, "livro") or fluxo.livro is None:
                print("❌ Crie um livro antes de fazer um empréstimo.")
            else:
                fluxo.criar_emprestimo()

        elif opcao == "4":
            # Professor, me perdoe, quero dormir...
            print("WIP...")
        elif opcao == "5":
            print("\nESTADO ATUAL")
            if hasattr(fluxo, "user") and fluxo.user:
                print(f"Usuário: {fluxo.user.nome}")
            else:
                print("Usuário: não criado")

            if hasattr(fluxo, "livro") and fluxo.livro:
                print(f"Livro: {fluxo.livro.titulo} | Disponível: {fluxo.livro.disponivel}")
            else:
                print("Livro: não criado")

            if hasattr(fluxo, "emprestimo") and fluxo.emprestimo:
                print(f"Empréstimo ativo: {fluxo.emprestimo.ativo}")
            else:
                print("Empréstimo: não criado")

        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

