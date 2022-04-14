class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            print(f'{self._nome} já está ligado')
            return
        print("Agora o {} está ligado".format(self._nome))
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            print(f'{self._nome} já está desligado')
            return

        print("Agora o {} está desligado".format(self._nome))
        self._ligado = False

    def esta_ligado(self):
        return f'{self._nome} está Ligado' if self._ligado else f'{self._nome} está desligado'