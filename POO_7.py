if __name__ == '__main__':
    # Setter = configura um valor (=)
    # Getter = retorna o valor (obtem)

    class Pessoa:
        def __init__(self, nome: str, idade: int):
            self.nome = nome
            self.idade = idade
            self._peso = 79

        @property
        def peso(self):
            return self._peso

        @peso.setter
        def peso(self, value):
            self._peso = value

    p1 = Pessoa("Renato", 22)
    p1.peso = 20
    print(p1.peso)
