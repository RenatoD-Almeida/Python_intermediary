from random import randint

numero = str(randint(100000000, 999999999))
index_reverso = 10
total = 0

for index in range(len(numero)):
    total += int(numero[index]) * index_reverso
    index_reverso -= 1

verifica = 11 - (total % 11)

if verifica > 9:
    numero += "0"
else:
    numero += str(verifica)

total = 0
for index in range(len(numero)):
    total += int(numero[index]) * index_reverso
    index_reverso -= 1

verifica = 11 - (total % 11)

if verifica > 9:
    numero += "0"
else:
    numero += str(verifica)

print(numero)




