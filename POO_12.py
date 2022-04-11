class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} {self.nome} está falando...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} está comprando...')

    """OverWrite falar"""
    def falar(self):
        print("Estou em cliente")


class ClienteVIP(Cliente):
    """Construtor"""
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    '''OverWrite falar'''
    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f"{self.nome} {self.sobrenome} tem {self.idade} anos de idade")


print()
p1 = ClienteVIP("Renato", 22, "Almeida")
p1.falar()
print()
p2 = Cliente("Letícia", 22)
p2.falar()
print()
p3 = Pessoa("Joane", 40)
p3.falar()
