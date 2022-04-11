class Bando_De_Dados:
    def __init__(self):
        self.bd = []

    def cadastrar(self, item):
        self.bd.append([item.nome, item.idade])

    def listar(self):
        print(self.bd)


class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


banco_dados = Bando_De_Dados()
# p1 = Cliente("Renato", 22)
banco_dados.cadastrar(Cliente("Renato", 22))
banco_dados.cadastrar(Cliente("Paulo", 25))
banco_dados.cadastrar(Cliente(input("Digite seu nome:"),
                              int(input("Digite sua idade: "))))

banco_dados.listar()