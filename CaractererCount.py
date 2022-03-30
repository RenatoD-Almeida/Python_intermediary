print("Inglês".center(10, "="))
msg = input("Enter with something: ")
counter = dict()

for c in msg:
    counter.setdefault(c, 0)
    counter[c] += 1

for k, v in counter.items():
    print(f'{k}: {v} vezes')


print("\n\nPortuguês".center(10, "="))

mensagem = input("Digite algo: ")
contador = dict()

for letra in mensagem:
    contador.setdefault(letra, 0)
    contador[letra] += 1

for k, v in contador.items():
    print(f'{k} = {v} vezes')