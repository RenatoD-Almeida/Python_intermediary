class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def status(self):
        print(f'nome: {self.nome}')
        print(f'idade: {self.idade}')
        print("= " * 7)

    def falar(self, msg):
        return f'{self.nome} está falando: \'{msg}\''


class Cliente(Pessoa):
    ...


class Aluno(Pessoa):
    ...


c1 = Cliente("Renato", 22)
c1.status()
print(c1.falar("Oiee"))

a1 = Aluno("José", 45)
a1.status()
print(a1.falar("Tchauuu"))
