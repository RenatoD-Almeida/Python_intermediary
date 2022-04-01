class Felino:
    def __init__(self, tipo = "<Não informado>", nome = "<Não informado>", andar = False):
        self.nome = nome
        self.tipo_animal = tipo
        self.andando = andar

    def status(self):
        print(f'Nome: {self.nome}')
        print(f'tipo: {self.tipo_animal}')
        print(f'Andando') if self.andando else print("Parado")

    def set_andar(self):
        if self.andando:
            self.andando = False
        else:
            self.andando = True


nome = input("Digite o nome do seu felino: ")
tipo = input("Digite o tipo de felino: ")

teste = Felino(tipo, nome)
teste.status()
print("+" * 10)
teste.set_andar()
teste.status()
print("+" * 10)
teste.set_andar()
teste.status()

