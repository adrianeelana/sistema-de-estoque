
from estoque import Estoque
from movimentacao import Movimentacao


estoque = Estoque()
movimentacao = Movimentacao()

while True:
    print("""
===== SISTEMA DE ESTOQUE =====

1 - Cadastrar produto
2 - Listar produtos
3 - Atualizar produto
4 - Excluir produto
5 - Entrada de produtos
6 - Saída de produtos
0 - Sair
""")

    opcao = input("Escolha uma opção: ")

    try:
        if opcao == "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço: R$ "))
            quantidade = int(input("Quantidade: "))

            if not nome.strip() or preco < 0 or quantidade < 0:
                print("Dados inválidos!")
            else:
                estoque.cadastrar(nome, preco, quantidade)

        elif opcao == "2":
            estoque.listar()

        elif opcao == "3":
            id = int(input("ID do produto: "))
            nome = input("Novo nome: ")
            preco = float(input("Novo preço: R$ "))
            quantidade = int(input("Nova quantidade: "))

            if not nome.strip() or preco < 0 or quantidade < 0:
                print("Dados inválidos!")
            else:
                estoque.atualizar(id, nome, preco, quantidade)

        elif opcao == "4":
            id = int(input("ID do produto: "))
            estoque.excluir(id)

        elif opcao == "5":
            id = int(input("ID do produto: "))
            quantidade = int(input("Quantidade recebida: "))
            movimentacao.movimentar(id, quantidade, "entrada")

        elif opcao == "6":
            id = int(input("ID do produto: "))
            quantidade = int(input("Quantidade retirada: "))
            movimentacao.movimentar(id, quantidade, "saida")

        elif opcao == "0":
            print("Sistema encerrado!")
            break

        else:
            print("Opção inválida!")

    except ValueError:
        print("Digite um valor válido!")

estoque.fechar()
movimentacao.fechar()
