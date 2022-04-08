class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, value):
        """Setter da ferramenta"""
        self.__ferramenta = value


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    def escrever(self):
        print("Caneta está escrevendo")

    @property
    def marca(self):
        return self.__marca


class MarquinaDeEscrever:
    def __init__(self):
        pass

    def escrever(self):
        print("Maquina está escrevendo")


escritor = Escritor("Renato")
caneta = Caneta("Bic")
maquina = MarquinaDeEscrever()

print(escritor.nome)

escritor.ferramenta = caneta

escritor.ferramenta.escrever()

