from smartphone  import Smartphone

telefone = Smartphone("Sansung")

print(telefone.esta_ligado())
telefone.conectar()
telefone.ligar()
telefone.ligar()
telefone.conectar()
telefone.conectar()
telefone.desconectar()
telefone.desligar()
telefone.conectar()

print(telefone.esta_conectado())

