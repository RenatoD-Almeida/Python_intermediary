class Felino:
    def __init__(self, tipo = "<Não informado>", nome = "<Não informado>", andar = False, comer = False):
        self.nome = nome
        self.tipo_animal = tipo
        self.andando = andar
        self.comendo = comer

    def status(self):
        print(f'Nome: {self.nome}')
        print(f'tipo: {self.tipo_animal}')
        print(f'Andando') if self.andando else print("Parado")
        print(f'Se alimentando') if self.comendo else print("Não está se alimentando")

    def set_andar(self):
        if self.andando:
            self.andando = False
        else:
            self.andando = True

    def set_comer(self):
        if self.andando:
            print("Não pode se alimentar andando")
        else:
            if self.comendo:
                self.comendo = False
            else:
                self.comendo = True


nome = input("Digite o nome do seu felino: ")
tipo = input("Digite o tipo de felino: ")

teste = Felino(tipo, nome)
teste.status()
print("+" * 10)
teste.set_andar()
teste.set_comer()
teste.status()
print("+" * 10)
teste.set_andar()
teste.status()
print("+" * 10)
teste.set_comer()
teste.status()


