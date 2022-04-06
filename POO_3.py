class Pessoa:
    def __init__(self, nome, idade, peso):
        """ Constrói o objeto"""
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.tipo = "Humano"

    def status(self):
        """ Retorna as informações para prova real"""
        return f'Nome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}\nTipo:{self.tipo}'


class Animal:
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.tipo = "Animal"

    def status(self):
        """ Retorna as informações para prova real"""
        return f'Nome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}\nTipo: {self.tipo}'


def cadastrar(classe):
    """ Instancia um objeto de uma maneira alterantiva """
    nome = input("NOME: ")
    idade = int(input("IDADE: "))
    peso = float(input("peso: "))
    return classe(nome, idade, peso)


p1 = cadastrar(Pessoa)
print(p1.status())
print(" - " * 10)
p2 = cadastrar(Animal)
print(p2.status())
