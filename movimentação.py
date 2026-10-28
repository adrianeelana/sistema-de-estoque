
import sqlite3


class Movimentacao:
    def __init__(self):
        self.banco = sqlite3.connect("estoque.db")

    def movimentar(self, id, quantidade, tipo):
        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            return

        cursor = self.banco.cursor()

        cursor.execute(
            "SELECT quantidade FROM produtos WHERE id = ?", (id,)
        )
        produto = cursor.fetchone()

        if produto is None:
            print("Produto não encontrado.")
            return

        atual = produto[0]

        if tipo == "entrada":
            nova_quantidade = atual + quantidade

        elif tipo == "saida":
            if quantidade > atual:
                print("Estoque insuficiente!")
                return

            nova_quantidade = atual - quantidade

        else:
            print("Tipo de movimentação inválido.")
            return

        cursor.execute(
            "UPDATE produtos SET quantidade = ? WHERE id = ?",
            (nova_quantidade, id)
        )

        self.banco.commit()
        print("Movimentação realizada!")

    def fechar(self):
        self.banco.close()
