from eletronico import Eletronico
from log import LogMixin


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self.conectado = False

    def conectar(self):
        if not self._ligado:
            info = f'{self._nome} não está ligado para que possa conectar'
            print(info)
            self.log_error(info)
            return

        if self.conectado:
            info = "Já está conectado"
            print(info)
            self.log_error(info)
            return

        info = "Agora o {} está conectado".format(self._nome)
        print(info)
        self.log_info(info)
        self.conectado = True

    def desconectar(self):
        if not self._ligado:
            info = f'{self._nome} não está desconectador pois está desligado'
            print(info)
            self.log_error(info)
            return

        if not self.conectado:
            info = f"{self._nome} não está conectado"
            print(info)
            self.log_error(info)
            return

        info = "Agora o {} está desconectado".format(self._nome)
        print(info)
        self.log_info(info)
        self.conectado = False

    def esta_conectado(self):
        if self.conectado:
            info = f'{self._nome} está conectado'
            self.log_info(info)
            return info
        else:
            info = f'{self._nome} não está conectado'
            self.log_info(info)
            return info
