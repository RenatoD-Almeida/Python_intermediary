class Gato:
    """ Classe para trabalhar com gatinhos """
    tipo_animal = "felino"  # variável de escopo global (acessível em todo lugar da classe)

    def __init__(self, nome: str, peso: float):
        """ Constrói a classe depois dela ser instanciada (método sempre iniciado) """
        self.nome = nome
        self.peso = peso

    def status(self):
        """ Retorna as informações do objeto instanciado """
        return f'Seu gatito se chama {self.nome} e tem {self.peso} kg\n{self._dietaEspecial()}'

    def _dietaEspecial(self) -> str:
        """ Método privado, por isso começa com _ """
        self.msg = "Tudo bem com o/a {}".format(self.nome)
        if self.peso < 3.5:
            self.msg = "{} precisa se alimentar melhor".format(self.nome)
        if self.peso > 5:
            self.msg = "{} gordinho/a".format(self.nome)
        return self.msg


Kiki = Gato("kiki", 2.5)
print(Kiki.status())

