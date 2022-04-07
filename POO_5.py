if __name__ == '__main__':
    from random import randint


    class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

        @staticmethod
        def gera_id():
            rand = randint(10000, 19999)
            return rand

p1 = Pessoa("Renato", 22)
print(p1.gera_id())