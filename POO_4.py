if __name__ == '__main__':
    from datetime import date


    class Pessoa:
        ano_atual = date.today().year

        def __init__(self, nome, idade, peso):
            self.nome = nome
            self.idade = idade
            self.peso = peso

        @classmethod
        def por_ano_nascimento(cls, nome, ano_nascimento, peso = "<Não informado>"):
            idade = cls.ano_atual - ano_nascimento
            return cls(nome, idade, peso)


p1 = Pessoa.por_ano_nascimento("Renato", 2000)

print(p1.idade)