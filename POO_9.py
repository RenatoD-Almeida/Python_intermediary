class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for v in self.produtos:
            print(v.nome, v.valor)

    def soma_total(self):
        total = 0
        for v in self.produtos:
            total += v.valor
        return total


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


from POO_9 import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 50)
p2 = Produto('Iphone', 9000)
p3 = Produto('Chiclete', 0.5)

carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.lista_produtos()

print(carrinho.soma_total())
