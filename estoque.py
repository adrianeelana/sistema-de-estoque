
import sqlite3
from produto import Produto


class Estoque:
    def __init__(self):
        self.banco = sqlite3.connect("estoque.db")

        with open("banco.sql", "r", encoding="utf-8") as arquivo:
            self.banco.executescript(arquivo.read())

    # CREATE - Cadastrar
    def cadastrar(self, nome, preco, quantidade):
        cursor = self.banco.cursor()

        cursor.execute(
            "INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)",
            (nome, preco, quantidade)
        )

        self.banco.commit()
        print("Produto cadastrado!")

    # READ - Listar
    def listar(self):
        cursor = self.banco.cursor()
        cursor.execute("SELECT * FROM produtos")

        produtos = cursor.fetchall()

        if not produtos:
            print("Nenhum produto cadastrado.")
            return

        for p in produtos:
            produto = Produto(p[0], p[1], p[2], p[3])
            produto.mostrar()
            print("-------------------")

    # UPDATE - Atualizar
    def atualizar(self, id, nome, preco, quantidade):
        cursor = self.banco.cursor()

        cursor.execute(
            "UPDATE produtos SET nome = ?, preco = ?, quantidade = ? WHERE id = ?",
            (nome, preco, quantidade, id)
        )

        self.banco.commit()

        if cursor.rowcount > 0:
            print("Produto atualizado!")
        else:
            print("Produto não encontrado.")

    # DELETE - Excluir
    def excluir(self, id):
        cursor = self.banco.cursor()

        cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
        self.banco.commit()

        if cursor.rowcount > 0:
            print("Produto excluído!")
        else:
            print("Produto não encontrado.")

    def fechar(self):
        self.banco.close()
